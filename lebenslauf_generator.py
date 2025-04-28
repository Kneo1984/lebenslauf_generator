from jinja2 import Environment, FileSystemLoader
import json
from pathlib import Path

# Lade die JSON-Daten
with open("data/data_dennis.json", encoding="utf-8") as f:
    daten = json.load(f)

# Jinja2-Umgebung konfigurieren
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("lebenslauf_template.html")

# HTML aus Template + Daten erzeugen
output = template.render(daten)

# Ausgabeordner vorbereiten
Path("output").mkdir(exist_ok=True)

# HTML-Datei speichern
with open("output/lebenslauf_dennis_maier.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Lebenslauf erfolgreich erstellt unter: output/lebenslauf_dennis_maier.html")
