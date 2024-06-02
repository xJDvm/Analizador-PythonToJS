
token_specification = [
    ('NUMBER',      r'\b\d+(\.\d*)?\b'),        # Literales numéricos
    ('STRING',      r'"(?:\\.|[^"\\])*"'),      # Literales de cadena
    ('IDENTIFIER',  r'\b[A-Za-z_]\w*\b'),       # Identificadores
    ('OPERATOR',    r'[+\-*/%=]|==|!=|<=|>=|&&|\|\|'),  # Operadores
    ('DELIMITER',   r'[;,\(\)\{\}\[\]\.]'),     # Delimitadores y símbolos (incluyendo punto)
    ('WHITESPACE',  r'\s+'),                    # Espacios en blanco
    ('NEWLINE',     r'\n'),                     # Nuevas líneas
    ('MISMATCH',    r'.'),                      # Cualquier otro carácter no válido
]