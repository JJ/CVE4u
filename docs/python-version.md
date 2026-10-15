# Python version

CVE4u uses CPython from the 3.13 series. The exact version is pinned in the
`.python-version` file at the root of the repository, which is the
only place where it is defined.

This file is read automatically by uv, and by other version managers such as pyenv and pyenv-win.
pyproject.toml only restricts the series (`requires-python = ">=3.13,<3.14"`).

## Why the 3.13 series

- It is mature and widely supported by third-party libraries.
- It will keep receiving security fixes until approximately October 2029 (PEP 719).
- We pin the latest patch release of the series, which includes the latest bug and security fixes.

## How to check it

```bash
python --version
```
The output must match the content of `.python-version`.

## References

- https://peps.python.org/pep-0719/