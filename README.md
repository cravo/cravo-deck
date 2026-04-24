# cravo-deck

[![Container Tests](https://github.com/cravo/cravo-deck/actions/workflows/test.yml/badge.svg)](https://github.com/cravo/cravo-deck/actions/workflows/test.yml)

A super-simple, self-hostable dashboard for organizing and displaying links to your web apps and services in a beautiful, modern interface.

See a live example at [homepage.cravo.cloud](https://homepage.cravo.cloud)

## Features

- 🎨 **Modern, responsive design** – Beautiful card-based layout with atmospheric effects
- ⚙️ **YAML-based configuration** – Easy to customize with a simple config file
- 🐳 **Docker-ready** – Containerized with Gunicorn for production use
- 📦 **Lightweight** – Minimal dependencies (Flask + PyYAML)
- 🔄 **Live config reloading** – Changes to config.yml take effect instantly without restart
- 🌍 **Self-hostable** – Run anywhere you can run Docker
- ♿ **Semantic HTML** – Clean, accessible markup

## Quick Start

### Prerequisites

- Docker and Docker Compose

### Run the Dashboard

1. Clone the repository and navigate to the directory
2. Run the container:

```bash
docker compose up -d --build
```

The dashboard will be available at `http://localhost:3000`

## Configuration

### config.yml

The dashboard is configured entirely through `data/config.yml`. Here's the structure:

```yaml
title: My Dashboard                    # Site title (appears in header and browser tab)
description: "My description"          # Short description shown under the title
footer: "Custom footer text"           # Footer HTML (optional)

sections:                              # Array of section groups
  - title: Category Name               # Section title (e.g., "Games", "Utilities")
    items:                             # Array of items in this section
      - title: App Name                # Item title (displayed in card)
        description: "Short description" # Item description (shown below title)
        link: "https://example.com"    # URL (opens in new tab)
```

### Example config.yml

```yaml
title: cravo.cloud
description: "a collection of small web apps and games"

sections:
  - title: games
    items:
      - title: numbers.cravo.cloud
        description: "a game where you try to collect all the numbers from 0 to 99"
        link: "https://numbers.cravo.cloud/"
      - title: another-game
        description: "some other game"
        link: "https://example.com/game"

  - title: utilities
    items:
      - title: pass.cravo.cloud
        description: "a password generator"
        link: "https://pass.cravo.cloud/"
      - title: qr.cravo.cloud
        description: "a QR code generator"
        link: "https://qr.cravo.cloud/"

  - title: my-services
    items:
      - title: my-blog
        description: "my personal blog"
        link: "https://blog.example.com/"
```

### Update Configuration

Edit `data/config.yml` with your own sections and links. The dashboard reloads the config automatically on each request – no restart needed!

## Environment Configuration

### .env

The `.env` file controls the port the dashboard runs on:

```env
PORT=5000
```

To use a different port, update this value and restart the container:

```bash
docker compose down
docker compose up -d
```

## Running the Container

### Start

```bash
docker compose up -d
```

### Stop

```bash
docker compose down
```

### View Logs

```bash
docker compose logs -f web
```

### Rebuild (after code changes)

```bash
docker compose down
docker compose build --no-cache web
docker compose up -d
```

## Customization

### Styling

The dashboard uses a modern dark theme with gradient backgrounds and card layouts. Customize the colors and styling in `static/style.css`.

### HTML/Template

The main template is `templates/index.html`. It uses Jinja2 templating and renders all content from `config.yml`.

### Local Development

To run locally without Docker:

1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   flask --app server.py run
   ```

The app will be available at `http://localhost:5000`

## Architecture

- **Server**: Flask with Gunicorn (4 workers for production)
- **Configuration**: YAML-based, reloaded on each request (mtime tracking)
- **Frontend**: Vanilla CSS + Jinja2 templates
- **Deployment**: Docker container with python

## License

Feel free to self-host and customize for your own needs!
