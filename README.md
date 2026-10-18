# 🌿 Wellness Buddy

A small, private wellness companion that runs fully on your own laptop using an open-source AI model. No API key, no account, no data sent online.

> **Disclaimer:** Wellness Buddy is an AI companion, not a substitute for professional care. It is not a therapist or a doctor and does not give medical advice.

Built for Hacktoberfest 2026 (open-source AI).

## Features

- **Chat** with a supportive companion powered by an open model (`llama3.2:1b` via Ollama)
- **Age modes** (Teen, Adult, Senior) that change the tone of the replies
- **Calm me down:** a guided box-breathing exercise (3 rounds)
- **Crisis safety check:** messages about self-harm or suicide never reach the AI. A fixed, caring message encouraging real-world support is shown instead
- **Two versions:** a web UI (`ui.py`) and a terminal version (`main.py`)

## How to run

1. Install [Ollama](https://ollama.com) and make sure it is running.
2. Download the model:
   ```
   ollama pull llama3.2:1b
   ```
3. Install the Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Start the web app:
   ```
   python -m streamlit run ui.py
   ```
   Or use the terminal version:
   ```
   python main.py
   ```

## Safety design

- The crisis check is a simple keyword list that runs **before** the model is called.
- The system prompt tells the model it is not a therapist, must not diagnose, and must not give medication advice.
- A disclaimer is always visible.

This is a basic prototype. A keyword list can miss things, so it should not be used as a real crisis tool.

## Screenshot

_Add a screenshot of the app here._

## Future work

- Voice input and output
- Daily reminders
- More languages
- More exercises and age groups
- Better crisis detection

## License

MIT
