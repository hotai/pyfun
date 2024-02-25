# Simple expression evaluator.
# No syntax validation/errors.

from pscript import PScript

pscript = PScript()

text = input("PScript expression (q to quit, ? for help): ")
while text != 'q':
    if text in ['?', 'h', 'help']:
        print("Enter one or more statements separated by semicolons.")
        print("Examples of statements:")
        print("  Variables:   var a = 3")
        print("  Numeric:     (-5 + 20) * 3.5 / 0.5 * -a")
        print("  Boolean:     <expr> and/or [not] <expr>")
        print("  Loops:       while a<10 do var a=a+1")
        print("  Conditional: if <expr> then <statement> elif <expr> then <statement> else <statement>")
        print("  Operators:   + - * / > >= < <= ==")
        text = input("PScript expression (q to quit, ? for help): ")
        continue

    try:
        statements = text.split(";")
        for stmt in statements:
            stmt = stmt.strip()
            if stmt:
                result = pscript.eval(stmt)
                print(f'Evaluated to:     {result}\n')
    except Exception as e:
        print(f"Error evaluating expression '{text}':", e)
    finally:
        text = input("PScript expression (q to quit, ? for help): ")

