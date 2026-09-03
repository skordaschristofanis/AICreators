#!/usr/bin/env python
# SPDX-License-Identifier: MIT

from pathlib import Path

from flask import Flask

from aicreators.web.routes import register_blueprints

__all__ = ["create_web_app"]

_WEB_DIR = Path(__file__).resolve().parent


def create_web_app() -> Flask:
    """Creates the web application."""
    app = Flask(
        __name__,
        template_folder=str(_WEB_DIR / "templates"),
        static_folder=str(_WEB_DIR / "static"),
        static_url_path="/static",
    )

    register_blueprints(app)

    @app.get("/health")
    def health():
        """Health check endpoint."""
        return {"status": "ok"}

    return app
