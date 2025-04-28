import pdfkit
import os

# Pfade zu den bereits generierten HTML-Dateien mit echten Daten
html_files = [
    "output/lebenslauf_dennis_maier.html",
    "output/anschreiben_dennis_maier.html"
]

# Zielpfade für die erzeugten PDF-Dateien
pdf_outputs = [
    "output/lebenslauf_dennis_maier.pdf",
    "output/anschreiben_dennis_maier.pdf"
]

# Konfiguration für Windows: Pfad zu wkhtmltopdf.exe
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

# PDF-Erstellung aus HTML-Dateien
for html_file, pdf_file in zip(html_files, pdf_outputs):
    if os.path.exists(html_file):
        pdfkit.from_file(html_file, pdf_file, configuration=config)
        print(f"✅ Erfolgreich konvertiert: {html_file} → {pdf_file}")
    else:
        print(f"⚠️ Datei nicht gefunden: {html_file}")
