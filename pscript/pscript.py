# Simple expression evaluator.
# No syntax validation/errors.

from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from vars import Vars

vars = Vars()

class PScript:
    def eval(self, input, print_steps=True):
        tokenizer = Lexer(input)
        tokens = tokenizer.tokenize()
        if print_steps:
            print(f'Tokenized string: {tokens}')
        
        parser = Parser(tokens)
        tree = parser.parse()
        if print_steps:
            print(f'Parsed tree:      {tree}')

        interpreter = Interpreter(tree, vars)
        result = interpreter.interpret()
        if print_steps:
            print(f'Variables:        {interpreter.vars.getall()}')
        
        return result
