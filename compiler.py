import sys
import py_mini_racer

def compile_javascript(file_path):
    try:
        with open(file_path, 'r') as file:
            javascript_code = file.read()

        ctx = py_mini_racer.MiniRacer()
        compiled_code = ctx.eval(javascript_code)

        return compiled_code, javascript_code  # Devuelve tanto el resultado como el código

    except Exception as e:
        return str(e), javascript_code if 'javascript_code' in locals() else ''

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compiler.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result, translated_code = compile_javascript(file_path)
    print(result)
    print("===")
    print(translated_code)
