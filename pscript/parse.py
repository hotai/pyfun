# Takes a list of tokens and converts them
# to a binary tree in a list representation, e.g.
# [2, +, [4, *, 7]]
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.curr_token = None if len(self.tokens) < 1 else self.tokens[self.idx]

    def factor(self):
        if self.curr_token.type == 'INT' or self.curr_token.type == 'FLT':
            return self.curr_token
        elif self.curr_token.value == '(':
            self.move_ptr()
            return self.bool_expression()
        elif self.curr_token.type == 'VAR':
            return self.curr_token
        elif self.curr_token.value in ['-', '+']:
            op = self.curr_token
            self.move_ptr()
            return [op, self.factor()]
        elif self.curr_token.value == 'not':
            op = self.curr_token
            self.move_ptr()
            return [op, self.bool_expression()]
    
    def term(self):
        left = self.factor()
        self.move_ptr()
        while self.curr_token.value in ['*', '/']:
            op = self.curr_token
            self.move_ptr()
            right = self.factor()
            self.move_ptr()
            left = [left, op, right]
        
        return left

    def expression(self):
        left = self.term()
        while self.curr_token.value in ['+', '-']:
            op = self.curr_token
            self.move_ptr()
            right = self.term()
            left = [left, op, right]
        
        return left
    
    def compare_expression(self):
        left = self.expression()
        while self.curr_token.type == 'COMP':
            op = self.curr_token
            self.move_ptr()
            right = self.expression()
            left = [left, op, right]

        return left

    def bool_expression(self):
        left = self.compare_expression()
        while self.curr_token.type == 'BOOL':
            op = self.curr_token
            self.move_ptr()
            right = self.compare_expression()
            left = [left, op, right]

        return left

    def variable(self):
        if self.curr_token.type == 'VAR':
            return self.curr_token
    
    def if_statement(self):
        self.move_ptr()
        condition = self.bool_expression()

        if self.curr_token.value == 'then':
            self.move_ptr()
            action = self.statement()
            return [condition, action]
        elif self.tokens[self.idx-1].value == 'then':
            action = self.statement()
            return [condition, action]

    def if_statements(self):
        conditions = []
        actions = []

        if_stmt = self.if_statement()
        conditions.append(if_stmt[0])
        actions.append(if_stmt[1])

        while self.curr_token.value == 'elif':
            if_stmt = self.if_statement()
            conditions.append(if_stmt[0])
            actions.append(if_stmt[1])
        
        if self.curr_token.value == 'else':
            self.move_ptr()
            else_action = self.statement()
            return [conditions, actions, else_action]
        
        return [conditions, actions]

    def while_statement(self):
        self.move_ptr()
        condition = self.bool_expression()

        if self.curr_token.value == 'do':
            self.move_ptr()
            action = self.statement()
            return [condition, action]
        elif self.tokens[self.idx-1].value == 'do':
            action = self.statement()
            return [condition, action]
    
    def statement(self):
        if self.curr_token.type == 'DECL':
            # var assignment
            self.move_ptr()
            left = self.variable()
            self.move_ptr()
            if self.curr_token.value == '=':
                op = self.curr_token
                self.move_ptr()
                right = self.bool_expression()
                return [left, op, right]
        elif self.curr_token.type in ['INT', 'FLT', 'OP', 'VAR', 'BOOL'] or \
            self.curr_token.value == 'not':
            # arithm/bool expression
            return self.bool_expression()
        elif self.curr_token.value in ['+', '-']:
            # unary expression
            return self.factor()
        elif self.curr_token.value == 'if':
            return [self.curr_token, self.if_statements()]
        elif self.curr_token.value == 'while':
            return [self.curr_token, self.while_statement()]
        
    def parse(self):
        return self.statement()

    def move_ptr(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.curr_token = self.tokens[self.idx]
        # else:
        #     self.curr_token = None
        