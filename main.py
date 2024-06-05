import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from lexer import Lexer

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico de JavaScript")
        self.root.geometry("800x600")
        self.root.configure(bg="#D9D9D9")  
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#D9D9D9", padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="Analizador Léxico de JavaScript", font=("Consolas", 16, "bold"), bg="#D9D9D9", fg="#001F36")  
        self.title_label.pack(pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#cedfdf")
        self.button_frame.pack(pady=10)

        self.upload_button = tk.Button(self.button_frame, text="Cargar Archivo", command=self.load_file, font=("Consolas", 12 , "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=5, pady=5) 
        self.upload_button.grid(row=0, column=0, padx=0)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=self.clear_table, font=("Consolas", 12, "bold"), bg="#1C5560", fg="#D9D9D9", bd=0, padx=27, pady=5)  
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

        self.tree = ttk.Treeview(self.tree_frame, columns=("Tipo", "Valor"), show="headings")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Valor", text="Valor")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscroll=self.scrollbar_y.set)

        self.scrollbar_x = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscroll=self.scrollbar_x.set)

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
        self.clear_table()
        for token in tokens:
            self.tree.insert("", "end", values=(token.type, token.value))

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

