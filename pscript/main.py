# Simple expression evaluator.
# No syntax validation/errors.

from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from vars import Vars

vars = Vars()

text = input("PScript expression (q to quit, ? for help): ")
while text != 'q':
    if text in ['?', 'h', 'help']:
        print("Examples:")
        print("  Conditional: if <expr> then <statement> elif <expr> then <statement> else <statement>")
        print("  Loops:       while <expr> do <statement>")
        print("  Variables:   var a = 3")
        print("  Boolean:     <expr> and/or [not] <expr>")
        print("  Operators:   + - * / > >= < <= ==")
        text = input("PScript expression (q to quit, ? for help): ")
        continue

    try:
        tokenizer = Lexer(text)
        tokens = tokenizer.tokenize()
        print(f'Tokenized string: {tokens}')
        
        parser = Parser(tokens)
        tree = parser.parse()
        print(f'Parsed tree:      {tree}')

        interpreter = Interpreter(tree, vars)
        result = interpreter.interpret()
        print(f'Variables:        {interpreter.vars.getall()}')
        print(f'Evaluated to:     {result}')
    except Exception as e:
        print(f"Error evaluating expression '{text}':", e)
    finally:
        text = input("PScript expression (q to quit, ? for help): ")

