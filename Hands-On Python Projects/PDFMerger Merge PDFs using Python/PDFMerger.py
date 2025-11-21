# PyPDF2 is a free and open-source pure-python PDF library capable of splitting, 
# merging, cropping, and transforming the pages of PDF files. It can also add custom data,
# viewing options, and passwords to PDF files. PyPDF2 can retrieve text and 
# metadata from PDFs as well.
#pip install PyPDF2
# "https://pypdf2.readthedocs.io/en/3.x/"

from PyPDF2 import PdfWriter

merger = PdfWriter()
num = int(input("Enter a how many pdf you want Merge :-"))
pdfs = []

for i in range(0,num) :
    name = input(f"Enter name of {i+1} pdf :-")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)


merger.write("merged-pdf.pdf")
merger.close()