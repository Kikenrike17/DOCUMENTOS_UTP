import os

carpeta_origen = r"C:\Program Files (x86)\Ricoh\RPE Print Text to PDF\Workfolder\Output"

# Buscar todos los PDFs
pdfs = [os.path.join(carpeta_origen, f) for f in os.listdir(carpeta_origen) if f.lower().endswith(".pdf")]

if not pdfs:
    print("No hay PDFs en la carpeta")
else:
    # Tomar el más reciente
    pdf_mas_reciente = max(pdfs, key=os.path.getmtime)
    print(pdf_mas_reciente)