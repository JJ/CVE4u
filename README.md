# CVE4u

## Introduction

CVE4u is born as a solution for many Spanish speakers who play CTFs
(Capture The Flag). It provides an easy access platform to CVE
(Common Vulnerabilities and Exposures) information based on their
personal needs.

## Technical description

CVE4u works as a web platform that extracts CVE information quickly,
to keep it accessible and up to date for users.

## Installation

### Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Step by step

1. Clone the repository.
2. Run `uv sync --locked`.

## Stack

| Tool | Use |
| --- | --- |
| [Python](https://www.python.org/) | Programming language |
| [uv](https://docs.astral.sh/uv/) | Dependency and environment manager |

Supported versions are defined in `pyproject.toml`,
and the exact versions in `uv.lock`.

## Workflows

The repository uses GitHub Actions to automate tasks, such as publishing this website.
See [docs/workflows.md](docs/workflows.md) for what each workflow does and how to test it.

## Contributions

Please read the [project rules](docs/rules.md) before contributing.
The list of contributors is in [CONTRIBUTORS.md](docs/CONTRIBUTORS.md).
