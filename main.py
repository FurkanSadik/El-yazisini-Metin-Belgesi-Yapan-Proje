import tkinter as tk
from tkinter import filedialog
from ocr_processing import extract_text
from save_file import save_text_to_file

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Tkinter penceresini gizle

    # Kullanıcıdan bir resim dosyası seçmesini iste
    image_path = filedialog.askopenfilename(
        title="Görüntü Seç",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )

    if image_path:
        text = extract_text(image_path)
        print("\nÇıkarılan Metin:\n", text)
        
        # Metni kaydetmeyi öner
        save_text_to_file(text)
    else:
        print("Dosya seçilmedi.")
