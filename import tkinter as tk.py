import tkinter as tk
from tkinter import ttk, font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        
        # Custom styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 14), padding=10)
        self.style.map("TButton",
                      foreground=[("active", "white")],
                      background=[("active", "#4a6baf")])
        
        # Fonts
        self.display_font = font.Font(family="Segoe UI", size=24, weight="bold")
        
        # Display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(root, textvariable=self.display_var, 
                               font=self.display_font, justify="right", 
                               state="readonly")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)
        
        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 1, 4)
        ]
        
        for (text, row, col, *span) in buttons:
            col_span = span[0] if span else 1
            btn = ttk.Button(root, text=text, 
                           command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=col_span, 
                    sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            
        # Keyboard support
        root.bind("<Key>", self.on_key_press)
        
    def on_button_click(self, char):
        current = self.display_var.get()
        
        if char == "C":
            self.display_var.set("")
        elif char == "=":
            try:
                result = eval(current)
                self.display_var.set(str(result))
            except Exception:
                self.display_var.set("Error")
        else:
            self.display_var.set(current + char)
    
    def on_key_press(self, event):
        key = event.char
        
        if key in "0123456789+-*/.=":
            self.on_button_click(key)
        elif event.keysym == "Return":
            self.on_button_click("=")
        elif event.keysym == "Escape":
            self.on_button_click("C")
        elif event.keysym == "BackSpace":
            current = self.display_var.get()
            self.display_var.set(current[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()