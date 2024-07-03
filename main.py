import tkinter as tk
from tkinter import filedialog, ttk, messagebox, Toplevel
from lexer import Lexer
import esprima
import json
import subprocess

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y sintáctico de JavaScript")
        self.root.geometry("800x600")
        self.root.configure(bg="#D9D9D9")
        self.create_widgets()
        self.ast = None

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#D9D9D9", padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="Analizador Léxico y sintáctico de JavaScript", font=(
            "Consolas", 16, "bold"), bg="#D9D9D9", fg="#001F36")
        self.title_label.pack(pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#cedfdf")
        self.button_frame.pack(pady=10)

        self.upload_button = tk.Button(self.button_frame, text="Cargar Archivo", command=self.load_file, font=(
            "Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5)
        self.upload_button.grid(row=0, column=0, padx=0)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=self.clear_table, font=(
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

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JavaScript Files", "*.js")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
            try:
                lexer = Lexer(code)
                tokens = lexer.tokenize()
                self.display_tokens(tokens)
                self.ast = esprima.parseScript(code, { "tolerant": True, "loc": True, "range": True })
            except SyntaxError as e:
                messagebox.showerror("Error de Sintaxis", str(e))

    def display_tokens(self, tokens):
        self.clear_table()
        for token in tokens:
            self.tree.insert("", "end", values=(token.value, token.type))

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def show_ast(self):
        if self.ast:
            try:
                ast_json = json.dumps(self.ast, default=lambda o: o.__dict__, indent=4)
                subprocess.run(["python", "arbol.py", ast_json])
            except Exception as e:
                messagebox.showerror("Error al mostrar AST", str(e))
        else:
            messagebox.showinfo(
                "Información", "No hay un AST para mostrar. Por favor, cargue un archivo JavaScript primero.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
