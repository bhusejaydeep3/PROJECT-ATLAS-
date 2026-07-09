"""
Project Atlas 
------------------

The central brain of Atlas.

this module is responsible for receving goals,
planning actions , coordinating agents, and managing
the overall workflow.

version: 0.1

"""
from brain.goal import Goal
class Atlas:
    """Main brain of Project Atlas."""

    def __init__(self):
        print("Atlas Brain Initialized")
    
    def start(self):
        print("\nWelcome to Project Atlas")
        
        prompt = input("Please enter your goal: ")
        
        goal = Goal(   original_prompt=prompt,
            task_type="YouTube Video",
            domain="Philosophy",
            core_topic="Nihilism",
            intent="Explain Nietzsche's view")
        goal.display()