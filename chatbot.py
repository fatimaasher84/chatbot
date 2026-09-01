from openai import OpenAI

class ChatModel:
    def __init__(self, base_url, key):
        self.client = OpenAI(
            base_url=base_url,
            api_key=key,
        )

    def chat_completion(self, model, messages):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response

MODEL = "qwen2.5:0.5b"
BASE_URL = "http://localhost:11434/v1"  # Default local URL for Ollama
chatModel = ChatModel(base_url=BASE_URL, key="fake-key")  # Key is required but not used by Ollama

messages=[{
    "role": "system", "content": "You are a EduBot, an education assistant."
    }]

#greeting message
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
    if message.lower().strip() == "good morning":
        return "Good morning! How can I help you with your studies?"

    if message.lower().strip() == "good afternoon":
        return "Good afternoon! What would you like to learn?"

    if message.lower().strip() == "good evening":
        return "Good evening! How can I help you with your studies?"

    return "Hello! 👋 I'm EduBot. How can I help you with your studies?"

#Guard Rails
def check_guardrails(user_input):
    user_input = user_input.lower().strip()

    # 1. Empty input
    if not user_input:
        return False, "Please enter a question."
 
    # 2. Input length
    if len(user_input) > 1000:
        return False, "Please keep your question under 1000 characters."

    # 2. Forbidden topics
    forbidden_words = [
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

    for word in forbidden_words:
        if word in user_input:
            return False, "Sorry, I can't help with that request."

    # 4. Ask Qwen whether the question is educational
    guardrail_messages = [
        {"role": "system","content": " "},
        {"role": "user","content": user_input}
    ]
    response = chatModel.chat_completion(
        model=MODEL,
        messages=guardrail_messages
    )

    decision = response.choices[0].message.content.strip().upper()

    if decision != "YES":
        return False, (
            "I'm EduBot, an education assistant. "
            "I can only help with education-related questions."
        )

    return True, None

#Goodbye check
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

    return any(phrase in message for phrase in goodbye_phrases)

def goodbye_response(message):
    message = message.lower().strip()

    if "thank" in message:
        return "You're welcome! Keep learning and good luck with your studies!"

    if "that's all" in message or "thats all" in message:
        return "You're all set!  Good luck with your studies. Goodbye!"

    return "Goodbye! It was nice helping you. Keep learning!"

while True:
    user_input = input("User: ").strip()
    if not user_input:
        continue

    #goodbye check
    if is_goodbye(user_input):
        print("EduBot:", goodbye_response(user_input))
        break

    #greeting check
    if is_greeting(user_input):
        print("EduBot:", greeting_response(user_input))
        continue

    #guard rail check
    allowed, message = check_guardrails(user_input)

    if not allowed:
        print("EduBot:", message)
        continue

    # Send allowed question to Qwen
    messages.append({"role": "user", "content": user_input})

    response = chatModel.chat_completion(
        model=MODEL,
        messages=messages
    )

    bot_response = response.choices[0].message.content
    print(f"EduBot: {bot_response}")
    messages.append({"role": "assistant", "content": bot_response})