####### Método 1 ######
# from tika import parser

# raw = parser.from_file('bonaldi-giovanni-alfredo_certidao-de-nascimento.pdf')
# print(raw['content'])

###### Método 2 #######
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (
    r'C:/Users/lucas.assis/AppData/Local/Programs/Tesseract-OCR/tesseract'
)
imagem = cv2.imread("certidao-a.png")
# Extraindo o texto da imagem
print(pytesseract.image_to_string(imagem))

####### Método 3 ######

# import pdf2image
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = (
#     r'C:/Users/lucas.assis/AppData/Local/Programs/Tesseract-OCR/tesseract'
# )


# def pdf_to_img(pdf_file):
#     poppler_path = r"C:/Users/lucas.assis/AppData/Local/Programs/poppler-23.01.0/Library/bin"
#     return pdf2image.convert_from_path(pdf_file,poppler_path=poppler_path)


# def ocr_core(file):
#     text = pytesseract.image_to_string(file)
#     return text


# def print_pages(pdf_file):
#     images = pdf_to_img(pdf_file)
#     for pg, img in enumerate(images):
#         if pg==0:
#             print(ocr_core(img))

# print_pages('bonaldi-giovanni-alfredo_certidao-de-nascimento.pdf')