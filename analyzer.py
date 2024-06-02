from token_1 import token_specification, Token
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        patterns = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        token_regex = re.compile(patterns)

        for match in re.finditer(token_regex, self.code):
            kind = match.lastgroup
            value = match.group(kind)

            if kind == 'WHITESPACE' or kind == 'NEWLINE':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {value}')
            else:
                self.tokens.append(Token(kind, value))

        return self.tokens
