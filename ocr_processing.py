import cv2
import pytesseract

# Tesseract'ın yolunu belirt (Windows için gerekli olabilir)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """
    Seçilen görüntüden OCR işlemi ile metin çıkarır.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    extracted_text = pytesseract.image_to_string(gray, lang="eng")

    return extracted_text
