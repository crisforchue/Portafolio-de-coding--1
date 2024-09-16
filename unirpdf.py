## EL STREAMLIT NO ABRE, HAY QUE REVISAR

import streamlit as st
import PyPDF2

def merge_pdfs(output_path, pdf_documents):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_doc in pdf_documents:
        pdf_merger.append(pdf_doc)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

def main():

    st.image('assets/mergePdf.png')
    st.header("Fusion de PDF")
    st.subheader("Adjunte archivos pdf para combinar")

    attached_pdfs = st.file_uploader(label = '', accept_multiple_files=True)

    merge_button = st.button(label="Fusionar PDFs")

    if merge_button: 

        if len(attached_pdfs <= 1):
            st.warning("Debe adjuntar mas de un archivo.")
        else: 
            output_pdf = 'assets/pdf_final.pdf'
            merge_pdfs(output_pdf, attached_pdfs)
            st.success("Los archvios se fusionaron correctamente!")

            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label = "Descargar PDF fusionado", data=pdf_data, file_name='pdf_final.pdf')

if __name__ == '__main__':
    main()