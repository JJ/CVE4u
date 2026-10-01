# Python version

CVE4u uses **Python 3.13.16**.

The version is pinned in the `.python-version` file at the root of the repository.
This file is read automatically by version managers such as pyenv, pyenv-win and uv,
and by GitHub Actions (`actions/setup-python` with `python-version-file`).

## Why Python 3.13.16

- It is the latest release of the 3.13 series (released 30 September 2026) and the
  last one with official binary installers for Windows and macOS.
- The 3.13 series is mature and widely supported by third-party libraries.
- It will keep receiving security fixes until approximately October 2029 (PEP 719).

## How to check it

```bash
python --version
# Python 3.13.16
```

## References

- https://www.python.org/downloads/release/python-31316/
- https://peps.python.org/pep-0719/