# 🌾 AgriBot

An AI-powered agricultural assistant that helps farmers with crop disease detection, market price queries, weather forecasts, and voice-based interaction — all through a unified conversational interface.

---

## 📌 Features

- 🧠 **AI Agent** — Intelligent conversational agent built for agricultural queries
- 🖼️ **Image Analysis** — Upload crop/plant images to detect diseases or get visual insights
- 🎙️ **Speech to Text** — Voice input support for hands-free interaction
- 📈 **Mandi Prices** — Real-time or simulated crop market price lookups
- 🌦️ **Weather Forecasts** — Location-based weather information for farming decisions
- ⚡ **FastAPI Backend** — Lightweight, high-performance REST API server

---

## 🗂️ Project Structure

```
AgriBot/
├── app.py                  # FastAPI app entry point
├── requirements.txt        # Python dependencies
├── .gitignore
└── src/
    ├── llm/
    │   ├── __init__.py
    │   └── agri_agent.py   # Core AI agent logic
    ├── speech/
    │   └── speech_to_text.py  # Voice/audio processing
    ├── vision/
    │   ├── __init__.py
    │   └── img_to_text.py  # Image analysis / crop disease detection
    └── tools/
        ├── mandi.py        # Mandi (market) price tool
        └── whether.py      # Weather forecast tool
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/rajashekharkeesari/AgriBot.git
cd AgriBot

# Create and activate a virtual environment
python -m venv agribot
# Windows
agribot\Scripts\activate
# macOS/Linux
source agribot/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

The API will start at `http://127.0.0.1:8000`

You can explore the interactive API docs at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🛠️ Tech Stack

| Component       | Technology          |
|----------------|---------------------|
| Backend         | FastAPI, Uvicorn    |
| AI Agent        | LLM (agri_agent)    |
| Speech Input    | Speech-to-Text      |
| Image Analysis  | Vision / img-to-text|
| Market Prices   | Mandi API / tool    |
| Weather         | Weather API / tool  |
| Language        | Python 3.12         |

---

## 📷 Use Cases

- A farmer uploads a photo of a diseased plant → AgriBot identifies the disease and suggests remedies
- A farmer asks (by voice) "What is the price of tomatoes in Hyderabad?" → AgriBot queries mandi prices
- A farmer asks "Will it rain tomorrow?" → AgriBot returns a weather forecast for their location
- General crop advice, farming tips, and Q&A via text or speech

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Feel free to use and modify it.

---

## 👨‍💻 Author

**Rajashekhar Keesari**  
[GitHub](https://github.com/rajashekharkeesari)
