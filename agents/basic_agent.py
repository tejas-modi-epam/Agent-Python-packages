class BasicAgent:
    def handle_task(self, task_text):
        if "astronaut" in task_text.lower():
            return "Neil Armstrong was the first astronaut on the moon."
        return "Sorry, I don't know."
