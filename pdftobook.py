import pypdf
pdf_in = open('stories.pdf', 'rb')
pdf_reader = pypdf.PdfReader(pdf_in)
b = (- len(pdf_reader.pages)) % 4
mid = (len(pdf_reader.pages)-b) // 2
first_half_pdf  = reversed(pdf_reader.pages[:(mid+b)]) 
second_half_pdf = pdf_reader.pages[(mid+b):]
i = 1
pdf_writer = pypdf.PdfWriter()
for pagea,pageb in zip(first_half_pdf,second_half_pdf):
    if i%2:
        pdf_writer.add_page(pagea)
        pdf_writer.add_page(pageb)
    else: 
        pdf_writer.add_page(pageb)
        pdf_writer.add_page(pagea)
    i += 1
i = 0
for c in range(b):
    if i%2:
        pdf_writer.add_page(pdf_reader.pages[b-c-1])
        pdf_writer.add_blank_page()
    else:
        pdf_writer.add_blank_page()
        pdf_writer.add_page(pdf_reader.pages[b-c-1])
    i += 1
pdf_out = open('stories (1).pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
