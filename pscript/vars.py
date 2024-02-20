class Vars:
    def __init__(self):
        self.vars = {}

    def getval(self, varname):
        return self.vars[varname]
    
    def getall(self):
        return self.vars
    
    def setval(self, varname, value):
        self.vars[varname] = value
