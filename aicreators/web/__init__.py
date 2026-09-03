#!/usr/bin/env python
# SPDX-License-Identifier: MIT

from flask import Flask

__all__ = ["create_web_app"]


def create_web_app() -> Flask:
    """Creates the web application."""
    app = Flask(__name__)

    @app.get("/health")
    def health():
        """Health check endpoint."""
        return {"status": "ok"}

    return app
