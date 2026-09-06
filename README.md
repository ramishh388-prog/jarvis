# Jarvis - Conversational AI

A Python-based conversational AI that talks just like ChatGPT. Built with OpenAI's API for natural, context-aware conversations.

## Features

✨ **Conversational Style** - Responds naturally like ChatGPT
🧠 **Context Awareness** - Maintains conversation history for coherent multi-turn dialogue
⚡ **Fast & Reliable** - Powered by OpenAI's GPT models
🎯 **Easy to Use** - Simple command-line interface

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramishh388-prog/jarvis.git
   cd jarvis
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## Usage

Run the conversational AI:

```bash
python jarvis.py
```

Then start chatting! Jarvis will respond conversationally to your messages.

**Commands:**
- Type normally to chat
- Type `quit`, `exit`, or `bye` to end the conversation

## Example Conversation

```
You: What's your name?
Jarvis: I'm Jarvis, your conversational AI assistant. Nice to meet you!

You: Tell me a joke
Jarvis: Why don't scientists trust atoms? Because they make up everything! 😄

You: quit
Jarvis: It was great talking with you! Take care! 👋
```

## Configuration

Edit `jarvis.py` to customize:
- **Model**: Change `model="gpt-4"` to `"gpt-3.5-turbo"` for faster/cheaper responses
- **Temperature**: Adjust from 0.0 (precise) to 1.0 (creative)
- **Max Tokens**: Limit response length with `max_tokens`
- **System Prompt**: Customize Jarvis's personality in the system message

## Requirements

- `openai>=1.0.0` - OpenAI Python SDK
- `python-dotenv>=1.0.0` - Environment variable management

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.
