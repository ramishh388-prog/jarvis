import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Conversation history to maintain context
conversation_history = []

def chat_with_jarvis(user_message: str) -> str:
    """
    Send a message to Jarvis and get a conversational response.
    Maintains conversation history for context-aware responses.
    """
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Prepare messages with system prompt
    messages = [
        {
            "role": "system",
            "content": "You are Jarvis, a helpful, conversational AI assistant. "
                       "Respond naturally and conversationally, like ChatGPT. "
                       "Be thoughtful, clear, friendly, and engaging. "
                       "Use casual language when appropriate and maintain context from previous messages."
        }
    ] + conversation_history
    
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=messages,
        temperature=0.7,  # Conversational warmth
        max_tokens=500
    )
    
    assistant_message = response.choices[0].message.content
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

def main():
    """Interactive chat loop."""
    print("=" * 50)
    print("✨ Jarvis - Conversational AI")
    print("=" * 50)
    print("Hello! I'm Jarvis, your conversational AI assistant.")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("\nJarvis: It was great talking with you! Take care! 👋\n")
                break
            
            if not user_input:
                continue
            
            print("Jarvis: ", end="", flush=True)
            response = chat_with_jarvis(user_input)
            print(response + "\n")
            
        except KeyboardInterrupt:
            print("\n\nJarvis: Goodbye! See you next time! 👋\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")
            continue

if __name__ == "__main__":
    main()
