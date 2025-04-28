from jinja2 import Environment, FileSystemLoader
import json

# Lade die Daten
with open("data_dennis.json", encoding="utf-8") as file:
    daten = json.load(file)

# Jinja2 vorbereiten
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template_dennis.html")

# HTML Rendern
output = template.render(
    name=daten["name"],
    job=daten["job"],
    kontakt=daten["kontakt"],
    profil=daten["profil"],
    berufserfahrung=daten["berufserfahrung"],
    ausbildung=daten["ausbildung"],
    zertifikate=daten["zertifikate"],
    technische_faehigkeiten=daten["skills"],
    softskills=daten["softskills"]
)

# Speichere das HTML-Dokument
with open("lebenslauf_dennis_maier.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Lebenslauf erfolgreich erstellt: lebenslauf_dennis_maier.html")
