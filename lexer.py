import re
from token_1 import token_specification

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


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


def main(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python lexer.py <file_path>")
    else:
        main(sys.argv[1])
