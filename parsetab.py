_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE IDENTIFIER LPAREN MINUS NUMBER PLUS RPAREN STRING TIMESexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : expression TIMES expressionexpression : expression DIVIDE expressionexpression : NUMBERexpression : IDENTIFIERexpression : LPAREN expression RPAREN'

_lr_action_items = {'NUMBER': ([0, 4, 5, 6, 7, 8,], [2, 2, 2, 2, 2, 2,]), 'IDENTIFIER': ([0, 4, 5, 6, 7, 8,], [3, 3, 3, 3, 3, 3,]), 'LPAREN': ([0, 4, 5, 6, 7, 8,], [4, 4, 4, 4, 4, 4,]), '$end': ([1, 2, 3, 10, 11, 12, 13, 14,], [0, -5, -6, -1, -2, -3, -4, -7,]), 'PLUS': ([1, 2, 3, 9, 10, 11, 12, 13, 14,], [5, -5, -6, 5, 5, 5, 5, 5, -7,]),
                    'MINUS': ([1, 2, 3, 9, 10, 11, 12, 13, 14,], [6, -5, -6, 6, 6, 6, 6, 6, -7,]), 'TIMES': ([1, 2, 3, 9, 10, 11, 12, 13, 14,], [7, -5, -6, 7, 7, 7, 7, 7, -7,]), 'DIVIDE': ([1, 2, 3, 9, 10, 11, 12, 13, 14,], [8, -5, -6, 8, 8, 8, 8, 8, -7,]), 'RPAREN': ([2, 3, 9, 10, 11, 12, 13, 14,], [-5, -6, 14, -1, -2, -3, -4, -7,]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:
            _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression': (
    [0, 4, 5, 6, 7, 8,], [1, 9, 10, 11, 12, 13,]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto:
            _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> expression", "S'", 1, None, None, None),
    ('expression -> expression PLUS expression',
        'expression', 3, 'p_expression_plus', 'parser.py', 46),
    ('expression -> expression MINUS expression',
        'expression', 3, 'p_expression_minus', 'parser.py', 51),
    ('expression -> expression TIMES expression',
        'expression', 3, 'p_expression_times', 'parser.py', 56),
    ('expression -> expression DIVIDE expression',
        'expression', 3, 'p_expression_divide', 'parser.py', 61),
    ('expression -> NUMBER', 'expression', 1,
        'p_expression_number', 'parser.py', 66),
    ('expression -> IDENTIFIER', 'expression', 1,
        'p_expression_identifier', 'parser.py', 71),
    ('expression -> LPAREN expression RPAREN', 'expression',
        3, 'p_expression_parentheses', 'parser.py', 76),
]
