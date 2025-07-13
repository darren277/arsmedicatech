# Contributing to ArsMedicaTech

First off, **thank you** for taking the time to contribute!  Together we can democratise safe, privacy-respecting digital health tools.

---

## 📜 Code of Conduct

We follow **Contributor Covenant v2.1**  
<https://www.contributor-covenant.org/version/2/1/code_of_conduct>  

In short: be respectful, assume good faith, zero tolerance for harassment.

---

## 🛠️ How to Contribute

1. **Fork** the repo & create your feature branch  
   ```bash
   git checkout -b feat/my-awesome-thing
   ```

2. Write tests where relevant (`pytest`).

3. Run linters & type-checks.
   ```bash
   scripts/format.sh  &&  scripts/typecheck.sh
   mypy .
   ```
4. Commit with conventional commit style `feat:`, `fix:`, `docs:` ...

5. Open a PR and fill out the template.

### Small Tasks to Get Started
* 📚 Improve documentation (docs/, /README screenshots, tutorials).
* 🐞 Reproduce / fix issues tagged good first issue.
* 🩺 Contribute clinical ontologies or FHIR mapping scripts.

## 🔄 Reciprocity Reminder

Under **AGPLv3**, if you deploy a fork in production you are required to publish those modifications. **Private patches are welcome, but please upstream them so every patient benefits.**

## 📝 Developer Certificate of Origin

By submitting code you assert you have the right to license it under AGPL v3 and you agree to the DCO:

```bash
Signed-off-by: Jane Developer <jane@example.com>
```
