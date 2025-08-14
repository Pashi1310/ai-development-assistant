# AI Development Assistant

Ein intelligenter Entwicklungsassistent, der Langflow mit modernen Frontend-Technologien kombiniert, um KI-gestützte Entwicklungsworkflows zu ermöglichen.

## Projektübersicht

Dieses Projekt erstellt einen AI-powered Development Assistant, der Entwicklern hilft durch:
- Automatisierte Code-Generierung
- Intelligente Projektanalyse  
- KI-gestützte Problemlösung
- Streamlined Development Workflows

## Features

- **Langflow Integration**: Visuelle KI-Workflow-Erstellung
- **Modernes Frontend**: Intuitive Benutzeroberfläche
- **Supabase Backend**: Sichere Datenspeicherung
- **Streamlit Dashboard**: Echtzeit-Monitoring
- **Schnelle Entwicklung**: Vorkonfigurierte Templates

## Technologie-Stack

- **Backend**: Python, Langflow
- **Frontend**: Streamlit/React (TBD)
- **Datenbank**: Supabase
- **Deployment**: Docker (geplant)
- **Version Control**: Git/GitHub

## Voraussetzungen

- Python 3.8+
- Git
- Node.js (für Frontend-Entwicklung)

## Installation

### 1. Repository klonen
```bash
git clone https://github.com/Pashi1310/ai-development-assistant.git
cd ai-development-assistant
```

### 2. Virtual Environment erstellen
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# oder
venv\Scripts\activate     # Windows
```

### 3. Dependencies installieren
```bash
pip install -r requirements.txt
```

### 4. Umgebungsvariablen konfigurieren
```bash
# .env Datei erstellen
cp .env.example .env
# Anpassen der Konfiguration
```

## Verwendung

### Langflow starten
```bash
langflow run
```

### Frontend starten
```bash
cd frontend
streamlit run app.py
```

## Projektstruktur

```
ai-development-assistant/
├── frontend/              # Frontend-Komponenten
├── langflow-config/       # Langflow-Workflows
├── src/                   # Hauptquellcode
├── tests/                 # Unit Tests
├── docs/                  # Dokumentation
├── requirements.txt       # Python Dependencies
└── README.md             # Projektdokumentation
```

## Konfiguration

### Supabase Setup
1. Supabase Projekt erstellen
2. API Keys in `.env` eintragen
3. Datenbank-Schema importieren

### Langflow Konfiguration
1. Workflows in `langflow-config/` speichern
2. API-Endpunkte konfigurieren
3. Integration testen

## API Dokumentation

### Hauptendpunkte
- `POST /api/generate` - Code-Generierung
- `GET /api/projects` - Projekt-Liste
- `POST /api/analyze` - Code-Analyse

## Beiträge

Beiträge sind willkommen. Bitte:
1. Fork das Repository
2. Feature-Branch erstellen (`git checkout -b feature/FeatureName`)
3. Änderungen committen (`git commit -m 'Add FeatureName'`)
4. Branch pushen (`git push origin feature/FeatureName`)
5. Pull Request erstellen

## Roadmap

### Phase 1 (Aktuell)
- [x] Projekt-Setup
- [x] Basic Repository-Struktur
- [ ] Langflow Integration
- [ ] Minimales Frontend

### Phase 2
- [ ] Supabase Integration
- [ ] User Authentication
- [ ] Advanced Workflows

### Phase 3
- [ ] Docker Deployment
- [ ] Advanced AI Features
- [ ] Performance Optimierung

## Bekannte Issues

- Langflow Setup Documentation pending
- Frontend Framework Selection TBD

## Lizenz

Dieses Projekt steht unter der MIT Lizenz.

## Autor

**Pascal Gdawietz**
- GitHub: [@Pashi1310](https://github.com/Pashi1310)