import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from lexer import Lexer

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico de JavaScript")

        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Cargar Archivo", command=self.load_file)
        self.upload_button.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Tipo", "Valor"), show="headings")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Valor", text="Valor")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.clear_button = tk.Button(self.root, text="Limpiar", command=self.clear_table)
        self.clear_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JavaScript Files", "*.js")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
            try:
                lexer = Lexer(code)
                tokens = lexer.tokenize()
                self.display_tokens(tokens)
            except SyntaxError as e:
                messagebox.showerror("Error de Sintaxis", str(e))

    def display_tokens(self, tokens):
        for token in tokens:
            self.tree.insert("", "end", values=(token.type, token.value))

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
