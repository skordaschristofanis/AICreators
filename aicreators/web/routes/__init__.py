#!/usr/bin/env python
# SPDX-License-Identifier: MIT

from flask import Flask

__all__ = ["register_blueprints"]


def register_blueprints(app: Flask) -> None:
    """Register all web blueprints on the Flask app."""
    from aicreators.web.routes.pages import pages_bp

    app.register_blueprint(pages_bp)
