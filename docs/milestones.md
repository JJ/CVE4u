## [M1] Reproducible development environment

**Deliverable:** A repository where any collaborator can set up the same Python environment and get every change checked automatically.

**It includes:**

- Python version pinned in `.python-version` (single source of truth).
- Dependencies managed with `uv` (`pyproject.toml` + `uv.lock`).
- A linter configured and justified.
- A CI workflow that runs the linter and the tests on every PR and push to `main`.

**Validation:**

- On a clean clone, `uv sync --locked` installs the environment without errors.
- `uv run ruff check .` passes locally.
- The CI workflow is green on `main` and runs on every PR.

**User story:** #10 (HU001)

**Milestone:** https://github.com/JJ/CVE4u/milestone/3

---

## [M2] Domain model

**Deliverable:** Source code in `src/cve4u/` with the entities and value objects that represent the problem domain, based on the user stories of the CTF player (#65) and the challenge creator (#66).

**It includes:**

- The domain concepts (CVE, affected software and version, challenge clues, compatibility between CVEs) described in `docs/`.
- One class per domain concept, with only the data and invariants that the user stories need.

**Validation:**

- Every concept used in #65 and #66 is represented by a class in `src/cve4u/`.
- The CI workflow from M1 passes on `main` (lint and syntax check of the new code).

**User stories:** #65 (HU002), #66 (HU003)

**Milestone:** https://github.com/JJ/CVE4u/milestone/4