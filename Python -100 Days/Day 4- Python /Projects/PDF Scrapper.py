import pdfplumber
pdf_path = "/Users/ajeetmacbookm2/Desktop/Python/Python -100 Days/Day 4- Python /Projects/Application.pdf"
print(pdf_path)
with pdfplumber.open(pdf_path)as pdf:
    for page_number,page in enumerate(pdf.pages,start = 1):
        text = page.extract_text()
        print(text)
