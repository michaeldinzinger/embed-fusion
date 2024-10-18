# Embed-Fusion

TODO

## Install dependencies

There are two ways you can install the dependencies to run the code.

### Using Poetry (recommended)

If you have the [Poetry](https://python-poetry.org/) package manager for Python installed already, you can simply set up everything with:

```console
poetry install && poetry shell
```
After the installation of all dependencies, you will end up in a new shell with a loaded venv. You can exit the shell at any time with `exit`.

### Using Pip (alternative)

You can also create a venv yourself and use `pip` to install dependencies:

```console
python3 -m venv venv
source venv/bin/activate
pip install .
```

### Installing flash-attn

The code uses the `flash-attn` library, which has to be installed separately. You can install it with the followinh command after activating the poetry shell or the venv:

```console
pip install flash-attn
```