from jinja2 import Environment, FileSystemLoader
import json

# Eigener Zeilenumbruch-Filter
def nl2br(value):
    return value.replace("\n", "<br>\n")

# Jinja2 vorbereiten
env = Environment(loader=FileSystemLoader("templates"))
env.filters['nl2br'] = nl2br  # Filter aktivieren

# JSON laden
with open("data/data_dennis.json", encoding="utf-8") as f:
    daten = json.load(f)

# Template rendern
template = env.get_template("anschreiben_template.html")
output = template.render(
    name=daten["name"],
    kontakt=daten["kontakt"],
    anschreiben=daten["anschreiben"],
    bewerbung=daten["bewerbung"]
)

# Speichern
with open("output/anschreiben_dennis_maier.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Anschreiben erfolgreich erstellt!")
