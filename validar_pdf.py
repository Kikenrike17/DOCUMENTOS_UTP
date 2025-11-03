import os
import shutil
from PyPDF2 import PdfReader

# Parámetros
carpeta_origen = r"C:\Program Files (x86)\Ricoh\RPE Print Text to PDF\Workfolder\Output"
carpeta_destino = r"D:\final"
lc_numero = "204060"  # Ejemplo
lc_anio = "2025"     # Ejemplo

# 1. Buscar el PDF más reciente
pdfs = [os.path.join(carpeta_origen, f) for f in os.listdir(carpeta_origen) if f.lower().endswith(".pdf")]
if not pdfs:
    print("")  # No hay archivos
    exit()

pdf_mas_reciente = max(pdfs, key=os.path.getmtime)

# 2. Leer texto del PDF
reader = PdfReader(pdf_mas_reciente)
texto = ""
for page in reader.pages:
    texto += page.extract_text() or ""

# 3. Validar contenido
if lc_numero in texto and lc_anio in texto:
    # 4. Copiar y renombrar
    nuevo_nombre = f"LC_{lc_anio}_{lc_numero}.pdf"
    ruta_final = os.path.join(carpeta_destino, nuevo_nombre)
    shutil.copy2(pdf_mas_reciente, ruta_final)
    print(ruta_final)  # Para PAD
else:
    print("")  # No válido