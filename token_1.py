token_specification = [
    # Numerical literals
    ('NUMBER',      r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b'),
    ('STRING',      r'["\'](?:\\.|[^"\\])*["\']'),      # String literals
    # Identifiers (excluding reserved words)
    ('IDENTIFIER',
     r'(?!\b(?:if|else|while|for|function|var|let|const|return|abstract|arguments|await|boolean|break|byte|case|catch|char|class|continue|debugger|default|delete|do|double|enum|eval|export|extends|final|finally|float|goto|implements|import|in|instanceof|int|interface|long|native|new|package|private|protected|public|short|static|super|switch|synchronized|this|throw|throws|transient|try|typeof|void|volatile|with|yield)\b)\b[A-Za-z_]\w*\b'),
    # Reserved words
    ('IF', r'\bif\b'),
    ('ELSE', r'\belse\b'),
    ('WHILE', r'\bwhile\b'),
    ('FOR', r'\bfor\b'),
    ('FUNCTION', r'\bfunction\b'),
    ('VAR', r'\bvar\b'),
    ('LET', r'\blet\b'),
    ('CONST', r'\bconst\b'),
    ('RETURN', r'\breturn\b'),
    ('ABSTRACT', r'\babstract\b'),
    ('ARGUMENTS', r'\barguments\b'),
    ('AWAIT', r'\bawait\b'),
    ('BOOLEAN', r'\bboolean\b'),
    ('BREAK', r'\bbreak\b'),
    ('BYTE', r'\bbyte\b'),
    ('CASE', r'\bcase\b'),
    ('CATCH', r'\bcatch\b'),
    ('CHAR', r'\bchar\b'),
    ('CLASS', r'\bclass\b'),
    ('CONTINUE', r'\bcontinue\b'),
    ('DEBUGGER', r'\bdebugger\b'),
    ('DEFAULT', r'\bdefault\b'),
    ('DELETE', r'\bdelete\b'),
    ('DO', r'\bdo\b'),
    ('DOUBLE', r'\bdouble\b'),
    ('ENUM', r'\benum\b'),
    ('EVAL', r'\beval\b'),
    ('EXPORT', r'\bexport\b'),
    ('EXTENDS', r'\bextends\b'),
    ('FINAL', r'\bfinal\b'),
    ('FINALLY', r'\bfinally\b'),
    ('FLOAT', r'\bfloat\b'),
    ('GOTO', r'\bgoto\b'),
    ('IMPLEMENTS', r'\bimplements\b'),
    ('IMPORT', r'\bimport\b'),
    ('IN', r'\bin\b'),
    ('INSTANCEOF', r'\binstanceof\b'),
    ('INT', r'\bint\b'),
    ('INTERFACE', r'\binterface\b'),
    ('LONG', r'\blong\b'),
    ('NATIVE', r'\bnative\b'),
    ('NEW', r'\bnew\b'),
    ('PACKAGE', r'\bpackage\b'),
    ('PRIVATE', r'\bprivate\b'),
    ('PROTECTED', r'\bprotected\b'),
    ('PUBLIC', r'\bpublic\b'),
    ('SHORT', r'\bshort\b'),
    ('STATIC', r'\bstatic\b'),
    ('SUPER', r'\bsuper\b'),
    ('SWITCH', r'\bswitch\b'),
    ('SYNCHRONIZED', r'\bsynchronized\b'),
    ('THIS', r'\bthis\b'),
    ('THROW', r'\bthrow\b'),
    ('THROWS', r'\bthrows\b'),
    ('TRANSIENT', r'\btransient\b'),
    ('TRY', r'\btry\b'),
    ('TYPEOF', r'\btypeof\b'),
    ('VOID', r'\bvoid\b'),
    ('VOLATILE', r'\bvolatile\b'),
    ('WITH', r'\bwith\b'),
    ('YIELD', r'\byield\b'),
    ('ADDITION',    r'\+'),  # Addition operator
    ('SUBTRACTION', r'-'),  # Subtraction operator
    ('MULTIPLICATION', r'\*'),  # Multiplication operator
    ('MODULUS', r'%'),  # Modulus operator
    ('ASSIGNMENT',  r'='),  # Assignment operator
    ('INCREMENT', r'\+\+'),  # Increment operator
    ('DECREMENT', r'--'),    # Decrement operator
    ('LESS', r'<'),         # Less than operator
    ('GREATER', r'>'),      # Greater than operator
    ('LESS_EQUAL', r'<='),  # Less than or equal to operator
    ('GREATER_EQUAL', r'>='),  # Greater than or equal to operator
    ('EQUAL', r'=='),       # Equal to operator
    ('NOT_EQUAL', r'!='),   # Not equal to operator
    ('AND', r'&&'),  # Logical AND operator
    ('OR', r'\|\|'),  # Logical OR operator
    # Delimiters and symbols (including dot)
    ('SEMICOLON', r';'),    # Semicolon delimiter
    ('COMMA', r','),        # Comma delimiter
    ('OPENING_PARENTHESIS', r'\('),      # Left parenthesis
    ('CLOSING_PARENTHESIS', r'\)'),      # Right parenthesis
    ('OPENING_BRACE', r'\{'),      # Left curly brace
    ('CLOSING_BRACE', r'\}'),      # Right curly brace
    ('OPENING_BRACKET', r'\['),    # Left square bracket
    ('CLOSING_BRACKET', r'\]'),    # Right square bracket
    ('DOT', r'\.'),         # Dot delimiter
    ('WHITESPACE',  r'\s+'),  # Whitespace
    ('NEWLINE',     r'\n'),  # Newlines
    ('ONELINE_COMMENT',     r'//.*'),  # Double slash comments
    ('MULTILINE_COMMENT',     r'\/[*](.|\n)*?[*]\/'),
    ('DIVISION',    r'/'),  # Division operator
    ('MISMATCH',    r'.'),  # Any other invalid character
]
