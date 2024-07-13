class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def consume(self, expected_kind=None):
        if expected_kind and self.peek().type != expected_kind:
            raise SyntaxError(f"Expected {expected_kind}, found {
                              self.peek().type}")
        current_token = self.tokens[self.position]
        self.position += 1
        return current_token

    def parse_expression(self):
        # For simplicity, let's assume an expression is just a number for now
        token = self.consume('NUMBER')
        return ASTNode('Number', value=token.value)

    def parse_assignment(self):
        # Assuming the form: IDENTIFIER = EXPRESSION
        identifier_token = self.consume('IDENTIFIER')
        self.consume('ASSIGNMENT')
        expression_node = self.parse_expression()
        return ASTNode('Assignment', value=identifier_token.value, children=[expression_node])

    def parse(self):
        # Assuming the top-level structure is a series of assignments
        assignments = []
        while self.peek() is not None:
            assignments.append(self.parse_assignment())
        return ASTNode('Program', children=assignments)


# Example usage:
tokens = [
    Token('IDENTIFIER', 'x'),
    Token('ASSIGNMENT', '='),
    Token('NUMBER', '5'),
    # Add more tokens for a complete example
]
parser = Parser(tokens)
ast = parser.parse()
print(ast)
