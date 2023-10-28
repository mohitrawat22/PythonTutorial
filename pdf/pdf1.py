import PyPDF2
f = open('pdf/pdf1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
print(page_one.extract_text())
f.close()


f = open('pdf/pdf1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
page_one = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open('pdf/pdf2.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()

