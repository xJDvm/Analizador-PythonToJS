import re
import sys

def translate_js_to_py(js_code):
    # Diccionario de traducciones básicas
    translations = {
        r'var\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'let\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'const\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'function\s+(\w+)\((.*)\)\s*{': r'def \1(\2):',
        r'console\.log\((.*)\);': r'print(\1)',
        r'if\s*\((.*)\)\s*{': r'if \1:',
        r'else\s*if\s*\((.*)\)\s*{': r'elif \1:',
        r'else\s*{': r'else:',
        r'for\s*\((.*);(.*);(.*)\)\s*{': r'for \1 in range(\2, \3):',
        r'while\s*\((.*)\)\s*{': r'while \1:',
        r'}': r'',
        r'(\w+)\.push\((.*)\);': r'\1.append(\2)',
    }

    # Aplicar las traducciones básicas
    py_code = js_code
    for js_pattern, py_replacement in translations.items():
        py_code = re.sub(js_pattern, py_replacement, py_code)
    
    # Ajustar la indentación
    indent_level = 0
    py_lines = []
    for line in py_code.split('\n'):
        stripped_line = line.strip()
        if stripped_line.endswith(':') and not stripped_line.startswith('#'):
            py_lines.append('    ' * indent_level + stripped_line)
            indent_level += 1
        elif stripped_line == '':
            py_lines.append('')
        else:
            if indent_level > 0 and stripped_line == '}':
                indent_level -= 1
            py_lines.append('    ' * indent_level + stripped_line)
    
    return '\n'.join(py_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        js_code = file.read()
    
    py_code = translate_js_to_py(js_code)
    print(py_code)
