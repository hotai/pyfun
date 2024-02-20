class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def getval(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class OpToken(Token):
    def __init__(self, value):
        super().__init__('OP', value)

class IntToken(Token):
    def __init__(self, value):
        super().__init__('INT', value)

    def getval(self):
        return int(self.value)

class FloatToken(Token):
    def __init__(self, value):
        super().__init__('FLT', value)

    def getval(self):
        return float(self.value)

class DeclToken(Token):
    def __init__(self, value):
        super().__init__('DECL', value)

class VarToken(Token):
    def __init__(self, value):
        super().__init__('VAR', value)

class BoolToken(Token):
    def __init__(self, value):
        super().__init__('BOOL', value)

class CompareToken(Token):
    def __init__(self, value):
        super().__init__('COMP', value)

class CtrlFlowToken(Token):
    def __init__(self, value):
        super().__init__('CTRL', value)
