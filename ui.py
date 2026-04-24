import tkinter as tk
import pyperclip
import storage


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ManageCoreClipBoard")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        # HEADER
        self.header = tk.Label(
            root,
            text="🧠 ManageCoreClipBoard",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e1e"
        )
        self.header.pack(pady=10)

        # BUTTON
        self.btn = tk.Button(
            root,
            text="Aggiorna Clipboard",
            command=self.add_clipboard,
            bg="#3a86ff",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            padx=10,
            pady=5
        )
        self.btn.pack(pady=5)

        # FRAME LISTA
        self.frame = tk.Frame(root, bg="#1e1e1e")
        self.frame.pack(fill="both", expand=True, pady=10)

        # SCROLLBAR
        self.scroll = tk.Scrollbar(self.frame)
        self.scroll.pack(side="right", fill="y")

        # LISTBOX
        self.listbox = tk.Listbox(
            self.frame,
            font=("Consolas", 11),
            bg="#2b2b2b",
            fg="white",
            selectbackground="#3a86ff",
            activestyle="none",
            yscrollcommand=self.scroll.set,
            border=0
        )
        self.listbox.pack(fill="both", expand=True)

        self.scroll.config(command=self.listbox.yview)

        self.listbox.bind("<Double-Button-1>", self.copy_item)

        self.refresh()
        self.auto_update()

    def add_clipboard(self):
        text = pyperclip.paste()
        storage.add_item(text)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for item in storage.get_all():
            self.listbox.insert(tk.END, item[:120])

    def copy_item(self, event):
        selected = self.listbox.curselection()
        if selected:
            text = storage.get_all()[selected[0]]
            pyperclip.copy(text)

    def auto_update(self):
        self.add_clipboard()
        self.root.after(1500, self.auto_update)


def start_app():
    root = tk.Tk()
    App(root)
    root.mainloop()