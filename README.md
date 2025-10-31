# CI/CD Demo with GitHub Actions

This repository is a home assignment for the DevOps course, demonstrating various Continuous Integration concepts using GitHub Actions. It includes several workflows to automate testing, scheduling, and execution on different environments.

---

## Implemented Workflows and Tasks

This project contains multiple workflow files located in the `.github/workflows/` directory, each corresponding to a specific task from the assignment.

### 📜 Task 1: Basic CI Workflow (`task1-basic-workflow.yml`)

* **Purpose**: To demonstrate a fundamental CI pipeline.
* **Trigger**: This workflow runs automatically on every `push` to the `main` branch.
* **Actions**: It performs two main steps:
    1.  Checks out the repository's code.
    2.  Runs a simple shell command to print a "Hello World" message, confirming the workflow was triggered successfully.

### 🧪 Task 2 & 4: Running Tests with a Matrix Build (`task2-tests-workflow.yml`)

* **Purpose**: To automate the testing process across multiple Python environments.
* **Trigger**: Runs on every `push` to the `main` branch.
* **Actions**: This workflow is more advanced and combines two tasks:
    1.  **Matrix Strategy**: It sets up a build matrix to run the same set of jobs across multiple Python versions (`3.8`, `3.9`, `3.10`, `3.11`). This ensures the code is compatible with different environments.
    2.  **Setup & Test**: For each Python version, it installs dependencies from `requirements.txt` and then runs the unit tests located in the `tests/` directory using the `unittest` framework.

### 🕒 Task 3: Scheduled Nightly Build (`task3-scheduled.yml` or `nightly-build.yml`)

* **Purpose**: To show how to run jobs on a recurring schedule instead of in response to a code change.
* **Trigger**: This workflow is triggered by a `schedule` event using cron syntax (`0 0 * * *`), which runs it daily at midnight UTC.
* **Actions**: It runs a simple job that prints a message to the logs, simulating a nightly task like generating a report or running maintenance scripts.

---

### ⭐ Bonus Task: Self-Hosted Runner Demonstration (`self-hosted-demo.yml`)

This task demonstrates how to execute a workflow on a custom, self-managed machine instead of on GitHub's hosted runners.

**🛡️ Security Measures:**
To mitigate the security risks of using a self-hosted runner on a public repository, this workflow is configured to run **only upon manual trigger** using `workflow_dispatch`. This critical step prevents malicious code from external pull requests from being automatically executed on the local machine.

**Execution Demonstration:**
The workflow was successfully run on a local Ubuntu VM. The screenshot below shows the log output, which includes the hostname of the VM (`matan-VirtualBox`), verifying that the job was executed on the self-hosted runner.

_**<img width="2074" height="873" alt="Image" src="https://github.com/user-attachments/assets/aeda0f45-1c64-447e-8dbe-8fa10171d41d" />**_