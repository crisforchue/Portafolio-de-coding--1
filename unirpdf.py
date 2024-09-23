## EL STREAMLIT NO ABRE, HAY QUE REVISAR
## Ya lo arregue

import streamlit as st #Importamos las librerias de streamlit y pypdf2 
import PyPDF2

def merge_pdfs(output_path, pdf_documents): #Funcion para definir los pdfs, donde el path guardara el pdf final, y el pdf las listas de archivos. Esta funcion va a ser nuestra funcion principal para el funcionamiento de la pagina

    pdf_merger = PyPDF2.PdfMerger() #Es un objeto que va a juntar ambos pdfs.

    for pdf_doc in pdf_documents:
        pdf_merger.append(pdf_doc)
    
    #Escribe el archivo pdf final con el path que le especificamos.
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

def main(): #Funcion principal que maneja la interfaz del usuario, 

    st.image('assets/mergePdf.png') #Pone una imagen de portada 
    st.header("Fusion de PDF") #Pone el header de la webApp
    st.subheader("Adjunte archivos pdf para combinar") 

    attached_pdfs = st.file_uploader(label = '', accept_multiple_files=True) #Nos crea un campo para subir los pdfs, ademas de que acepta varios al mismo tiempo

    merge_button = st.button(label="Fusionar PDFs") #Llama la funcion a trabajar, ademas de que crea un boton para hacerla funcionar.

    if merge_button: 

        if len(attached_pdfs)  <= 1 : #Si no hay mas de un pdf, no se va a adjuntar y se le mostrara una advertencia al usuario
            st.warning("Debe adjuntar mas de un archivo.")
        else: 
            output_pdf = 'assets/pdf_final.pdf' #Le dal nombre al pdf final y espeficifica donde se guardara
            merge_pdfs(output_pdf, attached_pdfs) #Lamma a la funcion de los pdfs con los argumentos 
            st.success("Los archvios se fusionaron correctamente!") #Se mosreara si funciona

            with open(output_pdf, 'rb') as file: #Pone el pdf en modo binario para que se pueda descargar 
                pdf_data = file.read()
            st.download_button(label = "Descargar PDF fusionado", data=pdf_data, file_name='pdf_final.pdf') #Da la posibilidad de descargar el pdf

if __name__ == '__main__': # Ejecuta la app si el script es ejecutado directamente
    main()