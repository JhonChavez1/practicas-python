from pypdf import PdfReader, PdfWriter

archivo_protegido = r"C:\Users\jfcm6\Downloads\WIM23C.pdf"
archivo_libre = r"C:\Users\jfcm6\Downloads\libre.pdf"
contraseña = "1061723108"

lector = PdfReader(archivo_protegido)

if lector.is_encrypted:
    lector.decrypt(contraseña)

escritor = PdfWriter()


for pagina in lector.pages:
    escritor.add_page(pagina)


with open(archivo_protegido, "wb") as f:
    escritor.write(f)

print("PDF guardado sin contraseña.")
