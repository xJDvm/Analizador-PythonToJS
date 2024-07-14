import esprima
from lexer import Lexer


def find_variable_declaration(identifier, ast):
    """
    Encuentra una declaración de variable para el identificador dado en el AST generado por Esprima.
    Retorna True si se encuentra y no es un objeto o propiedad, de lo contrario False.
    """
    for node in ast['body']:
        match node['type']:
            case 'VariableDeclaration':
                for decl in node['declarations']:
                    if decl['id']['type'] == 'Identifier' and decl['id']['name'] == identifier:
                        if 'init' in decl:
                            return True
    if identifier == 'console' or 'log':
        return True
    return False


def esprima_node_to_dict(node):
    if isinstance(node, esprima.nodes.Node):
        node_dict = {"type": node.type}
        for key, value in node.__dict__.items():
            if key != 'type':
                if isinstance(value, list):
                    node_dict[key] = [
                        esprima_node_to_dict(item) for item in value]
                else:
                    node_dict[key] = esprima_node_to_dict(value)
        return node_dict
    elif isinstance(node, list):
        return [esprima_node_to_dict(item) for item in node]
    else:
        return node


def esprima_ast_to_dict(ast):
    return esprima_node_to_dict(ast)


def collect_declarations(ast_node, declared_vars, const_vars, semantic_errors):
    if isinstance(ast_node, dict):
        if ast_node.get('type') == 'VariableDeclaration':
            kind = ast_node['kind']
            for decl in ast_node['declarations']:
                var_name = decl['id']['name']
                if var_name in declared_vars:
                    semantic_errors.append(f"Variable redeclarada: {var_name}")
                declared_vars.add(var_name)
                if kind == 'const':
                    const_vars.add(var_name)
        for key, value in ast_node.items():
            collect_declarations(value, declared_vars,
                                 const_vars, semantic_errors)
    elif isinstance(ast_node, list):
        for item in ast_node:
            collect_declarations(item, declared_vars,
                                 const_vars, semantic_errors)


def check_const_reassignment(ast_node, const_vars, semantic_errors):
    if isinstance(ast_node, dict):
        if ast_node.get('type') == 'AssignmentExpression' and ast_node['left']['type'] == 'Identifier':
            var_name = ast_node['left']['name']
            if var_name in const_vars:
                semantic_errors.append(
                    f"Reasignación de variable constante: {var_name}")
        for key, value in ast_node.items():
            check_const_reassignment(value, const_vars, semantic_errors)
    elif isinstance(ast_node, list):
        for item in ast_node:
            check_const_reassignment(item, const_vars, semantic_errors)


def analyze_semantics(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    esprima_output = esprima.parseScript(code)
    ast = esprima_ast_to_dict(esprima_output)
    lexer = Lexer(code)
    lexer.tokenize()
    symbol_table = lexer.tokens

    # Realiza comprobaciones de análisis semántico
    semantic_errors = []

    # Comprobar variables no definidas
    for token in symbol_table:
        if token.type == 'IDENTIFIER':
            if not find_variable_declaration(token.value, ast):
                semantic_errors.append(f"Variable no definida: {token.value}")

    # Comprobar redeclaraciones y recolectar declaraciones const
    declared_vars = set()
    const_vars = set()
    collect_declarations(ast, declared_vars, const_vars, semantic_errors)

    # Comprobar reasignación de variables constantes
    check_const_reassignment(ast, const_vars, semantic_errors)

    return semantic_errors
