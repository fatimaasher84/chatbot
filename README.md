## 🤖 EduBot — AI Education Chatbot

EduBot is a local AI-powered education chatbot built with **Python** and **Ollama**. It uses the **Qwen2.5:0.5B** language model to provide educational assistance and answer users' questions.

The chatbot runs locally through Ollama, so you can interact with the AI without depending on a cloud-based API.

## ✨ Features

* 🤖 AI-powered educational chatbot
* 🧠 Powered by **Qwen2.5:0.5B**
* 🖥️ Runs locally using **Ollama**
* 🔒 No external AI API required
* 💬 Interactive question-and-answer experience
* 🎓 Designed for educational assistance
* ⚡ Lightweight model suitable for local systems

## 🛠️ Technologies Used

* **Python**
* **Ollama**
* **Qwen2.5:0.5B**
* **OpenAI-compatible API**

## 📋 Requirements

Before running the project, make sure you have:

* Python 3.10+
* Ollama installed
* Qwen2.5:0.5B model downloaded

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/fatimaasher84/chatbot.git

```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download and install Ollama from the official website.

After installation, verify it:

```bash
ollama --version
```

### 4. Download the Qwen model

```bash
ollama pull qwen2.5:0.5b
```

### 5. Start Ollama

```bash
ollama run qwen2.5:0.5B
```

Ollama will normally run on:

```text
http://localhost:11434
```

## ▶️ Run the Chatbot

Start the Python application:

```bash
python main.py
```

Then start chatting with EduBot.

## 🧠 Model

This project uses:

```text
qwen2.5:0.5b
```

Qwen2.5 is a family of language models developed by Alibaba Cloud. The 0.5B model is a small, lightweight model that is useful for experimenting with local AI applications.

## ⚙️ Configuration

The chatbot connects to Ollama through its local API:

```text
http://localhost:11434/v1
```

The chatbot uses the following system instruction:

```text
You are an EduBot, an education assistant.
```

You can modify the system prompt in the project code to customize the chatbot's behavior.

## 📁 Project Structure

```text
chatbot/
│
├── main.py
├── requirements.txt
└── README.md
 ```

> Your actual project structure may be different depending on how you organize the application.

## 🔐 Privacy

Because the model runs locally through Ollama, your conversations can remain on your own computer rather than being sent to a third-party cloud AI service.
