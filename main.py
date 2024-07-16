import tkinter as tk
from tkinter import filedialog, ttk, messagebox, Toplevel
from lexer import Lexer
import esprima
import json
from semantics import analyze_semantics
import subprocess
import sys

python_executable = sys.executable


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y sintáctico de JavaScript")
        self.root.geometry("1280x800")
        self.root.configure(bg="#D9D9D9")
        self.create_widgets()
        self.ast = None
        self.syntax_error = ""
        self.semantic_error = ""
        self.result = ""
        self.file_path = None

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#D9D9D9", padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="Traductor de Javascript a Python", font=(
            "Consolas", 16, "bold"), bg="#D9D9D9", fg="#001F36")
        self.title_label.pack(pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#cedfdf")
        self.button_frame.pack(pady=10)

        self.upload_button = tk.Button(self.button_frame, text="Cargar Archivo", command=self.load_file, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5)
        self.upload_button.grid(row=0, column=0, padx=0)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=self.clear_data, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=27, pady=5)
        self.clear_button.grid(row=0, column=1, padx=20)

        self.tree_frame = tk.Frame(self.frame, bg="#D9D9D9")
        self.tree_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="D9D9D9",
                        fieldbackground="#8C999A",
                        foreground="#001F36",
                        font=("Consolas", 10))
        style.configure("Treeview.Heading",
                        background="#001F36",
                        foreground="#D9D9D9",
                        font=("Consolas", 11, "bold"))

        self.tree = ttk.Treeview(self.tree_frame, columns=(
            "Literal", "Token"), show="headings")
        self.tree.heading("Literal", text="Literal")
        self.tree.heading("Token", text="Token")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.show_ast_button = tk.Button(self.button_frame, text="Mostrar AST", command=self.show_ast, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5)
        self.show_ast_button.grid(row=0, column=2, padx=20)

        self.semantic_analysis_button = tk.Button(self.button_frame, text="Analizar Semántica", command=self.run_semantic_analysis, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5)
        self.semantic_analysis_button.grid(row=0, column=3, padx=20)

        self.compile_button = tk.Button(self.button_frame, text="Compilar JavaScript", command=self.compile_javascript, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5)
        self.compile_button.grid(row=0, column=4, padx=20)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("JavaScript Files", "*.js")])
        if self.file_path:
            self.clear_table()
            with open(self.file_path, 'r') as file:
                code = file.read()
                lexer = Lexer(code)
                tokens = lexer.tokenize()
                self.display_tokens(tokens)
                try:
                    self.ast = esprima.parseScript(code)
                except esprima.error_handler.Error as e:
                    self.syntax_error = f"Error de sintaxis: {e}"
                    return

    def display_tokens(self, tokens):
        for token in tokens:
            self.tree.insert("", "end", values=(token.value, token.type))

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def clear_data(self):
        self.clear_table()
        self.ast = None
        self.syntax_error = ""
        self.semantic_error = None
        self.result = None
        self.file_path = None

    def show_ast(self):
        if self.ast:
            ast_window = Toplevel(self.root)
            ast_window.title("Abstract Syntax Tree")
            ast_window.geometry("600x400")
            text_widget = tk.Text(ast_window, wrap="word")
            text_widget.pack(expand=True, fill="both", padx=10, pady=10)
            ast_str = str(self.ast)
            text_widget.insert("1.0", ast_str)
        else:
            if self.syntax_error != "":
                messagebox.showerror(
                    "Análisis sintáctico fallido", self.syntax_error)
            else:
                messagebox.showinfo(
                    "Información", "No hay un AST para mostrar. Por favor, cargue un archivo JavaScript primero.")

    def run_semantic_analysis(self):
        if self.file_path:
            self.semantic_error = analyze_semantics(self.file_path)
            if self.semantic_error:
                error_message = "\n".join(self.semantic_error)
                messagebox.showerror("Errores Semánticos", error_message)
            else:
                messagebox.showinfo("Análisis Semántico",
                                    "No se encontraron errores semánticos.")
        else:
            messagebox.showinfo(
                "Información", "No hay un archivo cargado para analizar. Por favor, cargue un archivo JavaScript primero.")

    def compile_javascript(self):
        if self.file_path:
            try:
                output = subprocess.check_output([python_executable, 'compiler.py', self.file_path], stderr=subprocess.STDOUT, universal_newlines=True)
                result, translated_code = output.split("===")
                self.show_compilation_result(result.strip(), translated_code.strip())
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error de compilación", e.output.strip())
        else:
            messagebox.showinfo(
                "Información", "No hay un archivo cargado para compilar. Por favor, cargue un archivo JavaScript primero.")

    def show_compilation_result(self, result, translated_code):
        result_window = Toplevel(self.root)
        result_window.title("Resultado de Compilación")
        result_window.geometry("600x400")

        result_label = tk.Label(result_window, text="Resultado de la Ejecución:", font=("Consolas", 12, "bold"))
        result_label.pack(pady=10)

        result_text = tk.Text(result_window, wrap="word", height=3)
        result_text.pack(expand=True, fill="both", padx=10, pady=10)
        result_text.insert("1.0", result)
        result_text.config(state=tk.DISABLED)

        translated_code_label = tk.Label(result_window, text="Código Traducido:", font=("Consolas", 12, "bold"))
        translated_code_label.pack(pady=10)

        translated_code_text = tk.Text(result_window, wrap="word")
        translated_code_text.pack(expand=True, fill="both", padx=10, pady=10)
        translated_code_text.insert("1.0", translated_code)
        translated_code_text.config(state=tk.DISABLED)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
