from tokens import *

class Lexer:
    __OPERATIONS = ['+', '-', '/', '*', '(', ')', '=']
    __STOPWORDS = [' ', '\t', '\v', '\r', '\n']
    __DECL_OPS = ['var', 'set']
    __BOOL_OPS = ['and', 'or', 'not']
    __COMP_OPS = ['>', '<', '>=', '<=', '==']
    __SPECIAL_CHARS = ['>', '<', '=']
    __CTRL_FLOW_OPS = ['if', 'elif', 'else', 'then', 'while', 'do']

    def __init__(self, expr:str):
        self.expr_str = expr
        self.idx = 0
        self.tokens = []
        self.char = '' if len(self.expr_str) < 1 else self.expr_str[self.idx]
        self.curr_token = None
    
    def tokenize(self):
        while self.idx < len(self.expr_str):
            if self.char.isdigit() or self.char == '.':
                self.curr_token = self.extract_num()
            elif self.char in Lexer.__OPERATIONS and \
                not (self.char == '=' and self.expr_str[self.idx+1] == '='):
                self.curr_token = OpToken(self.char)
                self.move_ptr()
            elif self.char in Lexer.__STOPWORDS:
                self.move_ptr()
                continue
            elif self.char.isalpha():
                word = self.extract_word()
                if word in Lexer.__DECL_OPS:
                    self.curr_token = DeclToken(word)
                elif word in Lexer.__BOOL_OPS:
                    self.curr_token = BoolToken(word)
                elif word in Lexer.__CTRL_FLOW_OPS:
                    self.curr_token = CtrlFlowToken(word)
                else:
                    self.curr_token = VarToken(word)
            elif self.char in Lexer.__SPECIAL_CHARS:
                compareOp = ''
                while self.char in Lexer.__SPECIAL_CHARS and (self.idx < len(self.expr_str)):
                    compareOp += self.char
                    self.move_ptr()
                self.curr_token = CompareToken(compareOp)

            self.tokens.append(self.curr_token)

        return self.tokens

    def extract_num(self):
        number = ''
        isFloat = False
        while (self.char.isdigit() or self.char == '.') and (self.idx < len(self.expr_str)):
            if self.char == '.':
                isFloat = True
            number += self.char
            self.move_ptr()
        
        return IntToken(number) if not isFloat else FloatToken(number)
    
    def extract_word(self):
        word = ''
        while self.char.isalpha() and (self.idx < len(self.expr_str)):
            word += self.char
            self.move_ptr()
        return word

    def move_ptr(self):
        self.idx += 1
        if self.idx < len(self.expr_str):
            self.char = self.expr_str[self.idx]



def _test():
    lexer = Lexer('5 + 3')
    lexer.tokenize()

if __name__ == '__main__':
    _test()
    
