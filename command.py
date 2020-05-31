import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["yes", "si", "sure", "do it", "yhea", "confirm"]
        self.cancel = ["No", "no", "negative", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("you dont say me your name")
            else:
                self.respond("my name is PYCOMMANDER. how are you")
        if "launch" or "open" in text:
            # the last word in the voice command
            app = text.split(" ", 1)[-1].lower()
            self.respond("Opening " + app)
            subprocess.call(app)


    def respond(self, response):
        print(response)
        subprocess.call("say "+response, shell=True)