import tkinter as tk
from tkinter import messagebox
import os
import datetime

class StickyNote:
    def __init__(self, master):
        self.master = master
        self.master.title("Sticky Note")
        self.master.geometry("300x300")

        self.text = tk.Text(self.master, font=("Arial", 12))
        self.text.pack(expand=True, fill='both')

        self.save_button = tk.Button(self.master, text="Save Note", command=self.save_note)
        self.save_button.pack(side='left', padx=10, pady=5)

        self.load_button = tk.Button(self.master, text="Load Last", command=self.load_last_note)
        self.load_button.pack(side='right', padx=10, pady=5)

        self.notes_dir = "notes"
        os.makedirs(self.notes_dir, exist_ok=True)

    def save_note(self):
        content = self.text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Note", "Cannot save an empty note!")
            return

        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
        filepath = os.path.join(self.notes_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)

        messagebox.showinfo("Note Saved", f"Note saved as {filename}")

    def load_last_note(self):
        files = sorted(os.listdir(self.notes_dir), reverse=True)
        if not files:
            messagebox.showinfo("No Notes", "No saved notes found.")
            return

        latest_file = os.path.join(self.notes_dir, files[0])
        with open(latest_file, 'r') as f:
            content = f.read()

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)
        messagebox.showinfo("Note Loaded", f"Loaded note: {files[0]}")

if __name__ == '__main__':
    root = tk.Tk()
    app = StickyNote(root)
    root.mainloop()