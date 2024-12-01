class statemachine:
    def __init__(self):
        self.state=1

    def go_to(self,state):
        self.state=state

program=statemachine()