import os
from openai import OpenAI
import pyttsx3
import threading


class OpenRouterChatBot:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )
        self.conversation_history = []
        self.system_prompt = {
            "role": "system",
            "content": "You are a helpful assistant. Keep responses concise and friendly."
        }
        self.engine = pyttsx3.init()

    def speak(self, text):
        def run_speak():
            self.engine.say(text)
            self.engine.runAndWait()
        
        threading.Thread(target=run_speak).start()
        
    def get_response(self, user_input):
        self.conversation_history.append(self.system_prompt)
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://your-domain.com",
                    "X-Title": "My Chatbot"
                },
                model="openai/gpt-3.5-turbo",
                messages=self.conversation_history
            )
            
            response = completion.choices[0].message.content
            self.speak(response)
            
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
            
        except Exception as e:
            return f"Error: {str(e)}"

    def chat(self):
        print("Dimension Chatbot activated! Type 'exit' to quit.")
        self.conversation_history.append(self.system_prompt)
        
        while True:
            user_input = input("ask anything : ")
            
            if user_input.lower() == 'exit':
                print("thnks for interacting, good day ahead,Bbye!")
                break
                
            response = self.get_response(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    bot = OpenRouterChatBot()
    bot.chat()