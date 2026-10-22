# Rules

Rules marked *(enforced by GitHub)* are applied automatically by the ruleset that protects `main`:
GitHub blocks the merge, or the push, until they are met.
The rest depend on everyone following them and on the reviewers.

1. Every pull request needs at least 2 approvals. *(enforced by GitHub)*
2. At least one of those approvals must come from a code owner: `diego-vigil-sosa`, `Carlitros20` or `jjavier2005`.
   They are listed in [CODEOWNERS](https://github.com/JJ/CVE4u/blob/main/.github/CODEOWNERS).
3. Pushing new commits to a pull request dismisses its previous approvals. *(enforced by GitHub)*
4. A pull request can only be merged when all CI checks pass.
5. Before merging, the branch must be up to date with `main`.
6. You can never work on main branch. Changes reach `main` only through pull requests. *(enforced by GitHub)*
7. `main` cannot be deleted or force-pushed. *(enforced by GitHub)*
8. Each branch solves one issue and is named `<type>/<issue-number>-<short-description>`, in lowercase with words separated by hyphens.
   `<type>` says what kind of change the branch makes:
   - `feat`: a new feature
   - `fix`: a bug fix
   - `docs`: documentation only
   - `refactor`: code changes that neither fix a bug nor add a feature
   - `test`: adding or fixing tests
   - `ci`: changes to the workflows
   - `chore`: maintenance, such as dependencies or configuration

   Examples: `fix/67-pages-node-deprecation`, `docs/63-python-version-ssot`.
9. When a pull request is accepted, the branch used for working in it, will be erased.
10. Language used in all documents must be English. Issues and pull requests are not documents.
11. Issues and pull requests must follow their templates: [issue template](https://github.com/JJ/CVE4u/blob/main/.github/ISSUE_TEMPLATE.md) and [pull request template](https://github.com/JJ/CVE4u/blob/main/.github/PULL_REQUEST_TEMPLATE.md).
12. Issues and pull requests are classified with labels (`bug`, `documentation`, `enhancement`, `user-stories`...), never with title prefixes such as `[Bug]` or `[Feature]`.
13. Commit messages are written in English, in the imperative mood ("Add...", "Fix...", not "Added..." or "Fixes..."), with a short first line that summarizes the change.
