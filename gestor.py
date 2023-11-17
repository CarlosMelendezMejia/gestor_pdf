import PyPDF2 as pdf


def join_pdf(files,output_name):

    final_pdf = pdf.PdfMerger()

    for file_name in files:
        final_pdf.append(file_name)

    final_pdf.write(output_name)
    final_pdf.close()

def split_pdf_pages(file):
    
    pdf_reader = pdf.PdfReader(file)
    
    for index, page in enumerate(pdf_reader.pages):
        pdf_writer = pdf.PdfWriter()
        pdf_writer.add_page(page)
        
        with open(f"page_{index+1}.pdf","wb") as out:
            pdf_writer.writer(out)
