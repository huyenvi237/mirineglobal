import fitz
#import camelot

print(fitz.__doc__)
pdf = fitz.open('company-info/presentation-pdf/PDFfile2.pdf')
print(pdf.page_count)

page=pdf.load_page(0)
print(page.get_text())
