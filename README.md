EduBot — AI Education Chatbot

EduBot is a local AI-powered education chatbot built with Python and Ollama. It uses the Qwen2.5:0.5B language model to provide educational assistance and answer users' questions.

The chatbot runs locally through Ollama, so you can interact with the AI without depending on a cloud-based API.

✨ Features
🤖 AI-powered educational chatbot
🧠 Powered by Qwen2.5:0.5B
🖥️ Runs locally using Ollama
🔒 No external AI API required
💬 Interactive question-and-answer experience
🎓 Designed for educational assistance
⚡ Lightweight model suitable for local systems

🛠️ Technologies Used
Python
Ollama
Qwen2.5:0.5B
OpenAI-compatible API


Before running the project, make sure you have:
Python 3.10+
Ollama installed
Qwen2.5:0.5B model downloaded


🚀 Installation

1. Clone the repository
git clone https://github.com/your-username/your-repository.git

2. Install Ollama
Download and install Ollama from the official website.
After installation, verify it:
ollama --version

3. Download the Qwen model
ollama pull qwen2.5:0.5b

4. Start Ollama in CMD
ollama run qwen2.5:0.5b
Ollama will normally run on:
http://localhost:11434


▶️ Run the Chatbot

Start the Python application:
python main.py
Then start chatting with EduBot.

🧠 Model

This project uses:
qwen2.5:0.5b

Qwen2.5 is a family of language models developed by Alibaba Cloud. The 0.5B model is a small, lightweight model that is useful for experimenting with local AI applications.

⚙️ Configuration

The chatbot connects to Ollama through its local API:
http://localhost:11434/v1
The chatbot uses the following system instruction:

You are an EduBot, an education assistant.
You can modify the system prompt in the project code to customize the chatbot's behavior.
