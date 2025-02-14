import tkinter as tk
from tkinter import filedialog

def save_text_to_file(text):
    """
    Kullanıcıya dosyayı nereye kaydedeceğini sorar ve metni belirtilen dosyaya kaydeder.
    """
    root = tk.Tk()
    root.withdraw()  # Tkinter penceresini gizle
    
    # Kullanıcıya dosya kaydetme penceresi aç
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:  # Eğer kullanıcı bir dosya seçtiyse
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Metin şu konuma kaydedildi: {file_path}")
    else:
        print("Kaydetme işlemi iptal edildi.")
