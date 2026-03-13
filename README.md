# Data 8 Public Materials

This repo contains the publicly available materials that are used in the Data 8 Foundations of Data Science course (homeworks, labs, lectures).

---

## Run assignments flawlessly

| Where | What you get |
|-------|----------------|
| **GitHub Pages (this site)** | Browse and run notebooks in the browser. The in-browser kernel does **not** include the `datascience` package or real otter grading. |
| **Binder** | Full Python environment with `datascience`, `otter-grader`, and all dependencies. **Use this to run and grade assignments.** |

**→ [Launch with Binder (run assignments here)](https://mybinder.org/v2/gh/ankbiy/materials-fds-draft/HEAD)**

When you open the **deployed GitHub Pages site**, open **`START_HERE.md`** in the file browser for the same Binder link.

---

Course Calendars:
- [Example Course Calendar from UCB Data 8](http://data8.org/materials-fds/)
- [Course Calendar with link to Demo JupyterHub, Colab, CodeSpaces, JupyterLite and HTML Versions](http://data8.org/materials-fds/demo.html)

The contents of this repository are licensed for reuse under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/)

You can launch these materials in an interactive Jupyter environment:

### Binder (full Python + otter-grader for grading)
Use Binder when you need to **run and grade** assignments (otter checks, export, etc.). Binder gives you a full Python kernel with all dependencies from `requirements.txt`.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ankbiy/materials-fds-draft/HEAD)

*(If you forked this repo, replace `ankbiy/materials-fds-draft` in the badge URL with your `OWNER/REPO`.)*

### Other options
- **Official Data 8 materials (Binder):** [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/data-8/materials-fds/main)
- **This repo on GitHub Pages (XeusLite):** in-browser notebooks; otter cells run but don’t perform real grading—use Binder above for that.

## VS Code/CodeSpace Usage

**Launching**

1) From the Github repository home page click the Green button labelled, "Code".
2) Click the plus("+") on the right of the drop-down panel. 
3) A Code Space will launch and load all the materials for you to use.
![CodeSpace](./assets/codespace.png)

**Kernel:**
You will need to select a Python kernel when you run a cell in a notebook for the first time. The default is `Python 3.10.XX`. There may be other Python versions available to select. They all should work.

**Live Share**
This allows you to collaborate with a partner on same set of code. 
1) Click "Live Share" on the status bar ![Live Share](./assets/live.png)
2) Follow the on-screen pop-up dialog instructions
3) Send the invitation to your partner

**Saving Work**

When you save your work(Ctrl-S or File --> Save), you are saving your changes to the Virtual Machine running VSCode in CodeSpace. This does **not** mean you are changes are saved to the repository.

In order to permanently save your work, you need to:

1) Click the "Source Control" button on the left-hand side menu bar. ![Source Control](./assets/source.png)
2) You will see a list of files that have changes that are not saved to your repository.
3) In the message box, give a descriptive(and short) sentence explaining the changes.
4) Click "Commit"
5) After a few seconds, the button will say "Sync Changes". Click it again to save the changes to your repository.

**CodeSpace Retention**

By default a codespace is deleted after 30 days of inactivity. You can set this value much
lower:
1) Go to our user Settings
2) Click Codespaces
3) Scroll down page to find "Default Retention Period"