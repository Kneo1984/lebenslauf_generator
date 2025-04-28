# 📄 Lebenslauf- und Anschreiben-Generator

Ein automatisiertes Projekt, um professionelle Lebensläufe und personalisierte Anschreiben direkt aus strukturierten JSON-Daten zu generieren – perfekt für Bewerbungen im modernen Stil!

---

## 📚 Projektstruktur

Lebenslau_Generator/ │ ├── data/ │ └── data_dennis.json # Persönliche Bewerberdaten │ ├── templates/ │ ├── lebenslauf_template.html # Lebenslauf-HTML-Template │ ├── anschreiben_template.html # Anschreiben-HTML-Template │ ├── output/ │ ├── lebenslauf_dennis_maier.html # Generierter Lebenslauf │ ├── anschreiben_dennis_maier.html # Generiertes Anschreiben │ ├── lebenslauf_generator.py # Skript für Lebenslauf-Generierung ├── anschreiben_generator.py # Skript für Anschreiben-Generierung ├── push.ps1 # Powershell-Skript für automatischen GitHub-Upload ├── README.md # (dieses Dokument)


---

## 🚀 Installation & Nutzung

### Voraussetzungen

- Python 3.10+
- Module: `jinja2`
- Git (für Repository-Verwaltung)

### Setup

```bash
git clone https://github.com/Kneo1984/lebenslauf_generator.git
cd lebenslauf_generator
pip install jinja2


python lebenslauf_generator.py
python anschreiben_generator.py

✨ Highlights
Blitzschnelle Erstellung moderner Bewerbungsunterlagen

Strukturierte Verwaltung von Lebensläufen & Anschreiben

Flexibel anpassbar über JSON-Daten

Perfekt für PDF-Generierung oder Online-Bewerbungen

Einsatz moderner Webtechnologien (HTML5, CSS3)

📬 Kontakt
Dennis Maier
📍 Krefeld, Deutschland
✉️ kneolekks@gmail.com
🔗 GitHub-Profil
