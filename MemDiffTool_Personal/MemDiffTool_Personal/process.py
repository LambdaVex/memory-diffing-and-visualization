class Process:

    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.modules = []    

    def add_modules(self, module):
        self.modules.append(module)
