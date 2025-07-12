import requests
import subprocess
import time


class DoomDaemon:
    def __init__(self):
        self.process = None
        
        
    def is_ollama_alive():
        """ Check if ollama is already running in the background. """
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


    def start(self):
        """ Start ollama background process. """
        if self.is_ollama_alive():
            print("Ollama already active.")
            self.spawned = False
            return
        
        print("Summoning Ollama daemon...")
        self.process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        self.spawned = True
        time.sleep(5)  # Give daemon time to awaken
        


    def stop(self):
        """ End ollama background process if started by program. """
        if self.spawned and self.process:
            print("Banishing Ollama daemon...")
            self.process.terminate()
            self.process.wait()
            self.process = None
        else:
            print("Ollama was not summoned by this session. Skipping termination.")