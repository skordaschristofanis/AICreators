#!/usr/bin/env python
# SPDX-License-Identifier: MIT

from argparse import ArgumentParser, Namespace

__all__ = ["main"]


def _build_parser() -> ArgumentParser:
    """Builds the argument parser with subparsers for the commands."""
    parser = ArgumentParser(description="AICreators CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    serve = subparsers.add_parser("serve", help="Start the web server")
    serve.add_argument("--host", default="0.0.0.0", help="Bind host")
    serve.add_argument("--port", type=int, default=5000, help="Bind port")
    serve.add_argument("--dev", action="store_true", help="Enable Flask debug mode")
    serve.set_defaults(func=_serve)

    return parser


def _serve(args: Namespace) -> None:
    """Starts the web server."""
    from aicreators.web import create_web_app

    app = create_web_app()
    app.run(host=args.host, port=args.port, debug=args.dev)


def main():
    """Main entry point for the AICreators application."""
    parser = _build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
