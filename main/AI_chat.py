import ollama

class AI_ChatBot:
    def __init__(self, base_question):
        self.message_history = [{'role': 'user', 'content': base_question}]

    def ask(self, query):
        query = query.strip()
        self.message_history.append({'role': 'user', 'content': query})
        response = ollama.chat(model='dolphin-llama3', messages=self.message_history)
        answer = response['message']['content']
        self.message_history.append({'role': 'assistant', 'content': answer})
        
        return answer
    
