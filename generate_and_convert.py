from pathlib import Path
import json
import pdfkit
from jinja2 import Environment, FileSystemLoader

# Ordner und Pfade
template_dir = Path("templates")
output_dir = Path("output")
data_path = Path("data/data_dennis.json")
output_dir.mkdir(exist_ok=True)

# Daten laden
with data_path.open(encoding="utf-8") as f:
    daten = json.load(f)

# Jinja-Umgebung
env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)

# Templates laden
anschreiben_template = env.get_template("anschreiben_template.html")
lebenslauf_template = env.get_template("lebenslauf_template.html")

# HTML erzeugen
anschreiben_html = anschreiben_template.render(
    name=daten["name"],
    kontakt=daten["kontakt"],
    bewerbung=daten["bewerbung"],
    anschreiben=daten["anschreiben"]
)
lebenslauf_html = lebenslauf_template.render(
    name=daten["name"],
    kontakt=daten["kontakt"],
    profil=daten["profil"],
    ausbildung=daten["ausbildung"],
    zertifikate=daten["zertifikate"],
    technische_faehigkeiten=daten["technische_faehigkeiten"],
    softskills=daten["softskills"],
    berufserfahrung=daten["berufserfahrung"]
)

# HTML-Dateien speichern
anschreiben_html_path = output_dir / "anschreiben_dennis_maier.html"
lebenslauf_html_path = output_dir / "lebenslauf_dennis_maier.html"

anschreiben_html_path.write_text(anschreiben_html, encoding="utf-8")
lebenslauf_html_path.write_text(lebenslauf_html, encoding="utf-8")

print(f"✅ HTML gespeichert: {anschreiben_html_path.name}")
print(f"✅ HTML gespeichert: {lebenslauf_html_path.name}")

# PDF-Konfiguration
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# PDF erzeugen mit A4-Fix & Layout-Korrektur für Lebenslauf
for html_file in [anschreiben_html_path, lebenslauf_html_path]:
    pdf_file = html_file.with_suffix(".pdf")

    options = {
        "page-size": "A4",
        "margin-top": "0mm",
        "margin-right": "0mm",
        "margin-bottom": "0mm",
        "margin-left": "0mm",
        "disable-smart-shrinking": "",
        "print-media-type": ""
    }

    if "lebenslauf" in str(html_file).lower():
        options["zoom"] = "0.73"  # Nur für Lebenslauf-PDF: Skaliert auf 1 Seite

    if html_file.exists():
        pdfkit.from_file(str(html_file), str(pdf_file), configuration=config, options=options)
        print(f"📄 PDF erzeugt: {pdf_file.name}")
    else:
        print(f"⚠️ Datei nicht gefunden: {html_file.name}")
