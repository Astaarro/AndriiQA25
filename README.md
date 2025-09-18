# QA Automation Course Project

This repository contains a comprehensive QA Automation framework designed for learning and practicing automated testing of API, database, and UI components. The project is structured to demonstrate real-world testing patterns and best practices using Python.

## Project Structure

- **config/**: Centralized configuration management (`config.py`).
- **modules/**: Main source code for automation logic:
	- `api/clients/`: API client implementations (e.g., `github.py`).
	- `common/database.py`: Database access and utility functions.
	- `ui/page_objects/`: Page Object Model classes for UI automation (e.g., `main_page.py`, `cart_page.py`).
- **tests/**: Test suites organized by domain:
	- `api/`: API tests (e.g., `test_github_api.py`).
	- `database/`: Database tests (e.g., `test_database.py`).
	- `ui/`: UI tests (e.g., `test_ui.py`).
- **become_qa_auto.db**: SQLite database used for database testing.
- **conftest.py**: Shared pytest fixtures and hooks.
- **pytest.ini**: Pytest configuration and custom markers for test categorization.

## Key Features

- **API Testing**: Interact with external APIs (e.g., GitHub) using custom clients in `modules/api/clients/`. Example: `Github.get_user(username)` fetches user data from GitHub.
- **Database Testing**: Use the `Database` class in `modules/common/database.py` to connect to and manipulate the SQLite database. Example: `get_all_users()` retrieves all users from the database.
- **UI Testing**: Follows the Page Object Model (POM) pattern. Each page class in `modules/ui/page_objects/` encapsulates selectors and actions for a specific web page. Example: `MainPage.go_to()` navigates to the main page of the target site.

## Developer Workflows

- **Run all tests:**
	```powershell
	pytest
	```
- **Run a specific test suite:**
		```powershell
		pytest -m {mark} -v
		```
	All available marks can be found in `pytest.ini`.

- **Debugging:**
	Use `print()` or logging in test files and modules. Pytest captures output unless run with `-s`.

- **Database:**
	The SQLite database is stored in `become_qa_auto.db`. Use helpers in `modules/common/database.py`.

## Patterns & Conventions

- **Page Object Model:** All UI automation uses page objects in `modules/ui/page_objects/`. Each class encapsulates selectors and actions for a specific page.
- **API Clients:** API interactions are implemented in `modules/api/clients/`. Each client is a separate file/class.
- **Fixtures:** Shared pytest fixtures are defined in `conftest.py` and reused across test suites.
- **Test Naming:** Test files and functions use descriptive names (e.g., `test_github_api.py`, `test_database.py`).

## Integration Points

- **External APIs:** Example: GitHub API via `modules/api/clients/github.py`.
- **Database:** SQLite via `modules/common/database.py`.

## Example: Adding a New Test

1. **UI Test:**
	 - Create a new page object in `modules/ui/page_objects/`.
	 - Add a test in `tests/ui/` using the new page object.
2. **API Test:**
	 - Create a new client in `modules/api/clients/`.
	 - Add corresponding tests in `tests/api/`.

---

This project demonstrates my skills in testing and understanding QA automation processes across API, database, and UI layers.
