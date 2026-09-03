#!/usr/bin/env python
# SPDX-License-Identifier: MIT

from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


def _coming_soon(active: str, title: str, description: str):
    return render_template(
        "coming_soon.html",
        active=active,
        page_title=title,
        page_description=description,
    )


@pages_bp.get("/")
def overview():
    return render_template("overview.html", active="overview", page_title="Overview")


@pages_bp.get("/analyze")
def analyze():
    return render_template("analyze.html", active="analyze", page_title="Analyze")


@pages_bp.get("/ideas")
def ideas():
    return _coming_soon("ideas", "Ideas", "Generate short-form ideas from an analysis.")


@pages_bp.get("/scripts")
def scripts():
    return _coming_soon("scripts", "Scripts", "Turn an idea into a timed short-form script.")


@pages_bp.get("/storyboard")
def storyboard():
    return _coming_soon("storyboard", "Storyboard", "Generate keyframe visuals per scene.")


@pages_bp.get("/voice")
def voice():
    return _coming_soon("voice", "Voice", "Create narration audio for script scenes.")


@pages_bp.get("/jobs")
def jobs():
    return _coming_soon("jobs", "Jobs", "Browse past runs and generated artifacts.")


@pages_bp.get("/settings")
def settings():
    return _coming_soon("settings", "Settings", "Configure models, paths, and defaults.")
