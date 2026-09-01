from openai import OpenAI
import re


# =========================
# Configuration
# =========================

MODEL = "qwen2.5:0.5b"
BASE_URL = "http://localhost:11434/v1"


# =========================
# Chat Model
# =========================

class ChatModel:
    def __init__(self, base_url, key):
        self.client = OpenAI(
            base_url=base_url,
            api_key=key
        )

    def chat_completion(self, model, messages):
        return self.client.chat.completions.create(
            model=model,
            messages=messages
        )


chat_model = ChatModel(
    base_url=BASE_URL,
    key="fake-key"
)


# =========================
# Conversation History
# =========================

messages = [
    {
        "role": "system",
        "content": (
            "You are EduBot, an education assistant. "
            "Help users with educational questions, school subjects, "
            "programming, mathematics, science, history, languages, "
            "homework, and learning."
        )
    }
]


# =========================
# Greeting
# =========================

def is_greeting(message):
    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    return message.lower().strip() in greetings


def greeting_response(message):
    message = message.lower().strip()

    if message == "good morning":
        return "Good morning! How can I help you with your studies?"

    if message == "good afternoon":
        return "Good afternoon! What would you like to learn?"

    if message == "good evening":
        return "Good evening! How can I help you with your studies?"

    return "Hello! 👋 I'm EduBot. How can I help you with your studies?"


# =========================
# Goodbye
# =========================

def is_goodbye(message):
    goodbye_phrases = [
        "bye",
        "goodbye",
        "bye bye",
        "see you",
        "see you later",
        "take care",
        "quit",
        "exit",
        "that's all",
        "thats all",
        "i'm done",
        "im done"
    ]

    message = message.lower().strip()

    return any(
        phrase in message
        for phrase in goodbye_phrases
    )


def goodbye_response(message):
    message = message.lower().strip()

    if "thank" in message:
        return "You're welcome! Keep learning and good luck with your studies!"

    if "that's all" in message or "thats all" in message:
        return "You're all set! Good luck with your studies. Goodbye!"

    return "Goodbye! It was nice helping you. Keep learning!"

def is_thanks(message):
    thanks_phrases = [
        "thanks",
        "thank you",
        "thanks a lot",
        "thank you so much",
        "thx",
        "ty"
    ]

    message = message.lower().strip()

    return message in thanks_phrases


def thanks_response():
    return "You're welcome! 😊 Keep learning and good luck with your studies!"

# =========================
# Guardrails
# =========================

FORBIDDEN_WORDS = [
    "hack",
    "hacking",
    "malware",
    "virus",
    "ransomware",
    "weapon",
    "bomb",
    "drugs",
    "porn",
    "sexual",
    "steal",
    "fraud"
]

EDUCATIONAL_KEYWORDS = [
    # General educational phrases
    "what is",
    "what are",
    "who is",
    "who was",
    "tell me about",
    "explain",
    "define",
    "definition",
    "meaning",
    "difference",
    "how does",
    "how do",
    "why",
    "calculate",
    "solve",

    # Science
    "science",
    "physics",
    "chemistry",
    "biology",
    "photosynthesis",
    "cell",
    "atom",
    "molecule",
    "gravity",
    "energy",
    "force",

    # Mathematics
    "math",
    "mathematics",
    "algebra",
    "geometry",
    "trigonometry",
    "calculus",
    "equation",
    "formula",

    # Programming
    "programming",
    "program",
    "coding",
    "code",
    "python",
    "javascript",
    "java",
    "html",
    "css",
    "django",
    "fastapi",
    "sql",
    "database",
    "algorithm",
    "function",
    "variable",
    "loop",

    # School
    "school",
    "student",
    "teacher",
    "homework",
    "assignment",
    "lesson",
    "chapter",
    "subject",
    "exam",
    "test",
    "study",
    "learn",
    "education",

    # English
    "english",
    "grammar",
    "sentence",
    "noun",
    "verb",
    "adjective",
    "pronoun",
    "synonym",
    "antonym",
    "vocabulary",

    # Other subjects
    "history",
    "geography",
    "economics",
    "literature",
    "artificial intelligence",
    "machine learning",
    "computer science"
]
def is_educational_question(user_input):
    user_input = user_input.lower().strip()

    for keyword in EDUCATIONAL_KEYWORDS:
        if keyword in user_input:
            return True

    return False

def check_guardrails(user_input): 
    user_input = user_input.lower().strip()

    # 1. Empty input 
    if not user_input:
        return False,"Please enter a question."
    
    # 2. Input length
    if len(user_input) > 1000:
        return False, "Please keep your question under 1000 characters."

    # 3. Forbidden topics
    for word in FORBIDDEN_WORDS:
         if re.search(rf"\b{re.escape(word)}\b", user_input):
             return False, "Sorry, I can't help with that request."

     # Educational check
    if not is_educational_question(user_input):
        return False, (
            "I'm EduBot, an education assistant. "
            "I can only help with education-related questions."
        )

    return True, None

# =========================
# Main Chat Loop
# =========================

print("EduBot: Hello! 👋 I'm EduBot. Ask me an educational question.")
print("EduBot: Type 'bye' when you want to exit.\n")


while True:

    user_input = input("User: ").strip()

    # Ignore empty input
    if not user_input:
        print("EduBot: Please enter a question.")
        continue

    # =====================
    # Goodbye check
    # =====================

    if is_goodbye(user_input):
        print("EduBot:", goodbye_response(user_input))
        break

    # =====================
    # Greeting check
    # =====================

    if is_greeting(user_input):
        print("EduBot:", greeting_response(user_input))
        continue

    #======================
    # Thanks check
    #======================
    if is_thanks(user_input):
        print("EduBot:", thanks_response())
        continue
    
    # =====================
    # Guardrail check
    # =====================
    
    allowed, guardrail_message = check_guardrails(user_input)
    
    if not allowed:
        print("EduBot:", guardrail_message)
        continue

    # =====================
    # Add user message to conversation history and get response from model
    # =====================

    messages.append({
        "role": "user",
        "content": user_input
    })

    # =====================
    # Send ONE request to Qwen
    # =====================

    try:
        response = chat_model.chat_completion(
            model=MODEL,
            messages=messages
        )

        bot_response = (
            response.choices[0]
            .message.content
            .strip()
        )

        print("EduBot:", bot_response)

        # Save response to conversation history
        messages.append({
            "role": "assistant",
            "content": bot_response
        })

    except Exception as e:
        print(f"EduBot: Sorry, something went wrong")
        print("Error:", e)