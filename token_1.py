token_specification = [
    ('NUMBER',      r'\b\d+(\.\d*)?\b'),        # Numerical literals
    ('STRING',      r'"(?:\\.|[^"\\])*"'),      # String literals
    # Identifiers (excluding reserved words)
    ('IDENTIFIER',
     r'(?!\b(?:if|else|while|for|function|var|let|const|return|abstract|arguments|await|boolean|break|byte|case|catch|char|class|const|continue|debugger|default|delete|do|double|else|enum|eval|export|extends|false|final|finally|float|for|function|goto|if|implements|import|in|instanceof|int|interface|let|long|native|new|null|package|private|protected|public|return|short|static|super|switch|synchronized|this|throw|throws|transient|true|try|typeof|var|void|volatile|while|with|yield)\b)\b[A-Za-z_]\w*\b'),
    # Reserved words
    ('RESERVED',    r'\b(?:if|else|while|for|function|var|let|const|return|true|false|null|abstract|arguments|await|boolean|break|byte|case|catch|char|class|const|continue|debugger|default|delete|do|double|else|enum|eval|export|extends|false|final|finally|float|for|function|goto|if|implements|import|in|instanceof|int|interface|let|long|native|new|null|package|private|protected|public|return|short|static|super|switch|synchronized|this|throw|throws|transient|true|try|typeof|var|void|volatile|while|with|yield)\b'),
    ('ADDITION',    r'\+'),  # Addition operator
    ('SUBTRACTION', r'-'),  # Subtraction operator
    ('MULTIPLICATION', r'\*'),  # Multiplication operator
    ('MODULUS', r'%'),  # Modulus operator
    ('ASSIGNMENT',  r'='),  # Assignment operator
    ('INCREMENT',   r'\+\+|--'),  # Increment and decrement operators
    ('COMPARISON',  r'<|>|<=|>=|==|!='),  # Comparison operators
    ('LOGICAL',     r'&&|\|\|'),   # Logical operators
    # Delimiters and symbols (including dot)
    ('DELIMITER',   r'[;,\(\)\{\}\[\]\.]'),
    ('WHITESPACE',  r'\s+'),  # Whitespace
    ('NEWLINE',     r'\n'),  # Newlines
    ('COMMENT',     r'//.*'),  # Double slash comments
    ('DIVISION',    r'/'),  # Division operator
    ('MISMATCH',    r'.'),  # Any other invalid character
]
