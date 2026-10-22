# Workflows

CVE4u uses [GitHub Actions](https://docs.github.com/en/actions) to automate tasks.
The workflows live in [`.github/workflows/`](https://github.com/JJ/CVE4u/tree/main/.github/workflows),
and their runs are listed in the [Actions tab](https://github.com/JJ/CVE4u/actions).

## Python CI

File: [`python-CI.yml`](https://github.com/JJ/CVE4u/blob/main/.github/workflows/python-CI.yml)

Checks the Python code on every change, so problems are found before they reach `main`.

- **When it runs:** on every pull request to `main` and on every push to `main`.
- **`lint-and-test` job:** installs uv, runs `uv sync --locked` to install Python and the dependencies from `uv.lock`,
  runs the linter (`ruff check .`) and then the tests (`pytest`).
- It fails if `uv.lock` is out of date, if ruff finds a problem or if a test fails.
  Having no tests yet is not a failure.

### How to check it

The result appears at the bottom of every pull request, next to the merge button, and in the [Actions tab](https://github.com/JJ/CVE4u/actions).

### How to run it locally

Run the same steps from the root of the repository:

```bash
uv sync --locked
uv run ruff check .
uv run pytest
```

## Markdown lint

File: [`markdown-lint.yml`](https://github.com/JJ/CVE4u/blob/main/.github/workflows/markdown-lint.yml)

Checks the format of every Markdown file, so errors no longer depend on who has the editor extension installed.

- **When it runs:** on every pull request to `main` and on every push to `main`.
- **`markdownlint` job:** runs [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) on every `.md` file.
- The rules are in `.markdownlint-cli2.jsonc`, which the VS Code markdownlint extension also reads,
  so the editor and the CI show the same warnings.
- It fails if any Markdown file breaks a rule.

### How to run it locally

Run it from the root of the repository. It needs [Node.js](https://nodejs.org/):

```bash
npx markdownlint-cli2
```

Add `--fix` to correct the errors that can be fixed automatically.

## Deploy GitHub Pages

File: [`jekyll-gh-pages.yml`](https://github.com/JJ/CVE4u/blob/main/.github/workflows/jekyll-gh-pages.yml)

Builds a website from the repository's Markdown files and publishes it at <https://jj.github.io/CVE4u/>.

- **When it runs:** on every push to `main`, or manually from the Actions tab.
- **`build` job:** uses Jekyll to turn `README.md` into the home page and every other `.md` file into a page.
- **`deploy` job:** publishes the site. It only runs on `main`.

### How to check it on `main`

1. Open the [Actions tab](https://github.com/JJ/CVE4u/actions) and select *Deploy Jekyll with GitHub Pages dependencies preinstalled*.
2. Open the latest run on `main`. Both jobs should be green, and the `deploy` job shows the URL of the site.
3. Warnings, if any, are listed under *Annotations* in the run summary.

### How to test it before opening a pull request

Run these commands from the root of the repository. They need [Docker](https://docs.docker.com/get-docker/).

Check the workflow syntax with [actionlint](https://github.com/rhysd/actionlint). It prints nothing if there are no errors:

```bash
docker run --rm -v "$PWD":/repo:ro -w /repo rhysd/actionlint:1.7.7 -no-color
```

Build the site locally with the same image the workflow uses:

```bash
mkdir -p /tmp/cve4u-site
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -e JEKYLL_ENV=production -e PAGES_REPO_NWO=JJ/CVE4u \
  -v "$PWD":/github/workspace:ro -v /tmp/cve4u-site:/site \
  --entrypoint bash ghcr.io/actions/jekyll-build-pages:v1.0.13 \
  -c 'cd $BUNDLE_APP_CONFIG && bin/github-pages build --source /github/workspace --destination /site'
```

Serve it and open <http://localhost:8000/pages/JJ/CVE4u/> in the browser.
Run the build again after every change and reload the page:

```bash
mkdir -p /tmp/cve4u-srv/pages/JJ
ln -sfn /tmp/cve4u-site /tmp/cve4u-srv/pages/JJ/CVE4u
python3 -m http.server 8000 -d /tmp/cve4u-srv
```

To test it on GitHub without publishing, push your branch and click *Run workflow* in the Actions tab, choosing your branch.
Only the `build` job runs. The generated site can be downloaded with:

```bash
gh run download <run-id> -n github-pages
```
