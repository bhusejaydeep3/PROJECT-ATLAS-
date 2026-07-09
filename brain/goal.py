class Goal:
    def __init__(self,original_prompt, task_type,domain,core_topic,
                intent,audience=None,constraints=None):
    
       self.original_prompt = original_prompt
       self.task_type = task_type
       self.domain = domain
       self.core_topic = core_topic
       self.intent = intent
       self.audience = audience
       self.constraints = constraints if constraints else []

    def display(self):
        print("original_prompt:", self.original_prompt)
        print("task_type:", self.task_type)
        print("domain:", self.domain)
        print("core_topic:", self.core_topic)
        print("intent:", self.intent)
        print("audience:", self.audience)
        print("constraints:", self.constraints)