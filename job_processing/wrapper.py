import requests


# TODO: Allow user to specify which model to run pull it if it dosent exist and run it (daemon runs the specified model).
class DoomModel:
    def __init__(self, model_name="llama3:instruct", host="http://localhost:11434"):
        self.name = model_name
        self.api_url = f"{host}/api/chat"
    
    
    def ask(self, prompt, system=None):
        """ Takes prompt and passes it to the ollama returning its output. """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = requests.post(self.api_url, json={
            "model": self.name,
            "messages": messages,
            "stream": False
        })

        if response.status_code == 200:
            data = response.json()
            return data.get("message", {}).get("content", "")
        else:
            raise Exception(f"Ollama error {response.status_code}: {response.text}")
    
        
