<h1 align="center">
  &nbsp;AICreators
</h1>

![License](https://img.shields.io/badge/License-MIT-teal.svg) ![Python](https://img.shields.io/badge/Python-3.14-22558a.svg?logo=python&color=22558a)

Content creation tools with online/offline LLM API calls.

## Table of Contents
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Usage
Requires Python 3.14. Clone or download this repository first. The package is installed from the local source tree.

With [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/skordaschristofanis/AICreators.git && cd AICreators && uv sync && uv run aicreators serve
```

You can also install and run it from another environment manager (venv, conda, pixi, etc.) as long as Python 3.14 is available and the project is installed (`pip install .`).

Then open http://127.0.0.1:5000/health — you should see `{"status":"ok"}`.

Optional flags:

```bash
uv run aicreators serve --dev --host 127.0.0.1 --port 5001
```

| Flag | Default | Description |
|------|---------|-------------|
| `--host` | `0.0.0.0` | Bind address |
| `--port` | `5000` | Bind port |
| `--dev` | off | Enable Flask debug / reloader |

## Contribution
Read more [here](CONTRIBUTING.md) for contribution guidance.

## License
AICreators is distributed under the MIT License. You should have received a [copy](LICENSE.txt) of the MIT License along with this program. If not, see https://mit-license.org/ for additional details.