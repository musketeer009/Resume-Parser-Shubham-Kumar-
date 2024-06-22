import tkinter as tk
from tkinter import filedialog
import PyPDF2

def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if filepath:
        display_pdf(filepath)


def display_pdf(filepath):
    pdf_text = extract_text_from_pdf(filepath)
    text_area.delete(1.0, tk.END)  
    text_area.insert(tk.END, pdf_text)


def extract_text_from_pdf(filepath):
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text


root = tk.Tk()
root.title("PDF Viewer")


button_frame = tk.Frame(root)
button_frame.pack(pady=10)


open_button = tk.Button(button_frame, text="Open PDF", command=open_file)
open_button.pack(side=tk.LEFT, padx=10)


text_area = tk.Text(root, height=20, width=80)
text_area.pack(padx=10, pady=10)


root.mainloop()
