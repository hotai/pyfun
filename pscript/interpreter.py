from tokens import Token, IntToken, FloatToken, CtrlFlowToken
from vars import Vars

class Interpreter:
    def __init__(self, tree, vars=None):
        self.tree = tree
        self.vars = vars if vars is not None else Vars()

    def interpret(self, tree=None):
        # interpret by doing a postorder traversal of the tree
        # represented by a list and any sublists
        # 2 + 3 * 4 -> [2, +, [3, *, 4]]
        if tree is None:
            tree = self.tree
        
        if not isinstance(tree, list):
            # single item in expression, e.g. "a" when 'a' was previously declared
            result = self.get_var_val(tree)
            return FloatToken(result) if isinstance(result, float) else IntToken(result)
        
        left = tree[0]
        if len(tree) == 1:
            if left.type == 'VAR':
                if left.value.startswith('-') or left.value.startswith('+'):
                    op = left.value[0]
                    left.value = left.value[1::]
                    left = op + str(self.get_var_val(left))
                    left = FloatToken(left) if isinstance(left, float) else IntToken(left)
                else:
                    left = self.get_var_val(left)
            return left
        elif isinstance(tree[0], CtrlFlowToken):
            if tree[0].value == 'if':
                for i, condition in enumerate(tree[1][0]):
                    evaluation = self.interpret(condition)
                    if evaluation.value == 1:
                        return self.interpret(tree[1][1][i])
                
                if len(tree[1]) == 3: # have an else
                    return self.interpret(tree[1][2])
                else:
                    return
            elif tree[0].value == 'while':
                condition = self.interpret(tree[1][0])
                while condition.getval() == 1:
                    self.interpret(tree[1][1])
                    # recheck condition
                    condition = self.interpret(tree[1][0])
                return
        elif len(tree) == 2: # unary op
            expr = tree[1]
            if isinstance(expr, list): # not (1+1)
                expr = self.interpret(expr)
            return self.compute_unary_op(tree[0], expr)
        
        # postorder traversal
        op = tree[1]
        right = tree[2]
        if isinstance(left, list):
            left = self.interpret(left)
        if isinstance(right, list):
            right = self.interpret(right)

        return self.compute_binary_op(op, left, right)

    def compute_unary_op(self, op, operand):
        if op.value == 'not':
            val = self.get_var_val(operand)
            return IntToken(1) if not val else IntToken(0)
        elif op.value in ['+', '-']:
            val = self.get_var_val(operand)
            if op.value == '-':
                val = -val
            return FloatToken(val) if isinstance(val, float) else IntToken(val)

    def compute_binary_op(self, op, left, right):
        result = 0

        lval = left.getval() #if isinstance(left, Token) else left
        if left.type == 'VAR' and lval in self.vars.getall():
            lval = self.vars.getval(lval)

        rval = self.get_var_val(right)

        if op.getval() == '=': # variable assignment
            self.vars.setval(left.getval(), rval)
            result = rval
        else:
            if left.type == 'VAR' and left.getval() not in self.vars.getall():
                raise Exception(f'Variable \'{lval}\' has not been defined.')

            # arithmetic
            if op.getval() == '+':
                result = lval + rval
            elif op.getval() == '-':
                result = lval - rval
            elif op.getval() == '*':
                result = lval * rval
            elif op.getval() == '/':
                result = lval / rval
            # comparison
            elif op.getval() == '>':
                result = 1 if lval > rval else 0
            elif op.getval() == '>=':
                result = 1 if lval >= rval else 0
            elif op.getval() == '<':
                result = 1 if lval < rval else 0
            elif op.getval() == '<=':
                result = 1 if lval <= rval else 0
            elif op.getval() == '==':
                result = 1 if lval == rval else 0
            # boolean
            elif op.getval() == 'and':
                result = 1 if lval and rval else 0
            elif op.getval() == 'or':
                result = 1 if lval or rval else 0

        return FloatToken(result) if isinstance(result, float) else IntToken(result)
    
    def get_var_val(self, var_token):
        val = var_token.getval()
        if var_token.type == 'VAR':
            if val in self.vars.getall():
                val = self.vars.getval(val)
            else:
                raise Exception(f'Variable \'{val}\' has not been defined.')
        
        return val
