from pathlib import Path

from flask import Flask, jsonify, render_template
import yaml


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.yml"
config = {}
config_mtime_ns = None


def load_config(force: bool = False) -> None:
    global config, config_mtime_ns

    if not CONFIG_FILE.exists():
        if force or config:
            config = {}
            config_mtime_ns = None
        return

    current_mtime_ns = CONFIG_FILE.stat().st_mtime_ns
    if not force and current_mtime_ns == config_mtime_ns:
        return

    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    config_mtime_ns = current_mtime_ns


@app.before_request
def refresh_config() -> None:
    load_config()

@app.route("/")
def index() -> str:
    return render_template("index.html", config=config)


@app.route("/healthz")
def healthz() -> tuple:
    return jsonify({"status": "ok"}), 200


load_config(force=True)

if __name__ == "__main__":
    app.run(debug=False)
