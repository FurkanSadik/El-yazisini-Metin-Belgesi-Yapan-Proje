import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle
    file_path = filedialog.askopenfilename(title="Bir resim dosyası seç", 
                                           filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path
