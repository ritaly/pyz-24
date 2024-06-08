[![Run pytest](https://github.com/PyrkiTeam/HabitHero/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/PyrkiTeam/HabitHero/actions/workflows/pytest.yml)

# HABIT HERO HABIT TRACKER APP

Introducing Habit Hero – your personal ally in building positive habits and breaking bad ones! 
Try Habit Hero today and start your journey towards becoming the best version of yourself!

## PREREQUIREMENTS
- Python 3.10 or higher
- for more details check the 'requirements.txt' file

## SETUP
1. **Clone the repository:**    
```bash     
git clone https://github.com/PyrkiTeam/HabitHero.git   
cd HabitHero 
```

2. **Create a virtual environment:**   
 ```bash     
 python3 -m venv .venv    
```

3. **Activate the virtual environment:**   

On macOS and Linux:     
```bash     
source .venv/bin/activate     
```    
On Windows:     
```bash     
.venv\Scripts\activate     
```

4. **Install the dependencies:**    
```bash     
pip install -r requirements.txt     
```

5. **Run seeds to fill database:**   

```bash     
python seed.py
```

## PROJECT STRUCTURE AND DEVELOPMENT GUIDELINES

![multilayered architecture](./web/assets/multilayers.jpg)


### Project structure
Overview of the project structure:

```
HabitHero/
├── app.py
├── app_init.py
├── config.py
├── seed.py
├── dal/
│   ├── db.py
│   ├── models/
│   └── ...repositories
│
├── handlers/
│   ├── habits/
│   └── ...handlers & use_cases
├── routes/
├── seeds/
│   ├── seed_habits.py
│   └── ...seeding data
├── tests/
│   ├── config_test.py
│   └── client_test.py
└── web/
    ├── index.html
    └── ... UI files

```

### Data Access Layer (dal/):

- Dal directory stores all database interaction code in the dal directory.
- New file for each database model or set of related database functions.
- Ensure new files have an __init__.py if creating a new subpackage.

Example:

```
dal/
├── __init__.py
├── models/
└── new_repository.py
```

### Handler (handler/):

- Handler directory stores all business logic (use_cases) and handler functions.
- New Python file for each major feature or set of related functionalities.

Example:

```
handler/
└── new_feature_handler.py
```

### Web (web/):

- Web directrory stores all web-related files such as HTML, CSS, and JavaScript.
- Organize files by type, if necesarry create subdirectories for CSS and JS files:

Example:

```
web/
├── index.html
└── styles/
    └── main.css
└── scripts/
    └── main.js
 ```
### Tests

Organize your project structure to keep your test code separate from your application code. 

#### `tests` Directory

- **Location**: Place the `tests` directory at the root of your project. This keeps it separate from your application code and makes it easy to locate.
- **Subdirectories**: If your project grows, you can create subdirectories within `tests` for different types of tests (e.g., `unit`, `integration`, `functional`).

#### `conftest.py`

- **Purpose**: Use `conftest.py` to define fixtures that can be shared across multiple test modules. This is particularly useful for setting up and tearing down the testing environment.
- **Location**: Place `conftest.py` in the `tests` directory. Pytest will automatically discover fixtures defined here.

#### Test Files

- **Naming**: Use a consistent naming convention for your test files, such as `test_*.py` for pytest to automatically discover them.
- **Structure**: Group related tests together in a single file. For example, `test_habits_integration.py` for all integration tests related to the habits functionality.

#### Writing Tests

- **Fixtures**: Use fixtures for setting up your test environment, such as creating an instance of the Flask app, initializing the database, and providing a test client.
- **Happy and Unhappy Paths**: Ensure your tests cover both positive (happy path) and negative (unhappy path) scenarios to thoroughly validate your application's behavior.

#### Example `conftest.py`

```python
@pytest.fixture(scope='module')
def app():
    app = create_app('testing')  # Create the app with the testing configuration
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def db(app):
    _db.app = app
    _db.create_all()
    yield _db
    _db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()
```
#### Running Tests

To run your tests, use the following command in the terminal:

```sh
pytest
```

By following these best practices, you ensure that your tests are well-organized, maintainable, and effectively cover your application's functionality.

---
### Updating Documentation:

Update the README.md file with information about any major new features. If needed document new modules and their usage within the code comments.