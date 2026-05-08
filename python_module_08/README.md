# Python Module 08

## 1. What This Module Is About

This module teaches basic tools that are used in real Python projects:

- virtual environments
- dependency management
- package installation with pip
- project dependency management with Poetry
- environment variables
- `.env` files
- safe configuration handling

The main idea is not only to make the programs work. The goal is to understand how Python projects are isolated, installed, configured, and prepared for different environments.

## 2. Theory You Need To Know

### Virtual Environments

A virtual environment is a separate Python environment for one project.

It has its own:

- Python executable
- installed packages
- `site-packages` directory

This is important because different projects can need different package versions. A virtual environment prevents one project from breaking another project or the global Python installation.

### Dependencies

A dependency is an external package that a program needs.

Examples from this module:

- `pandas`
- `numpy`
- `requests`
- `matplotlib`
- `python-dotenv`

### pip

`pip` installs Python packages.

In this module, pip uses:

```txt
requirements.txt
```

Example:

```bash
pip install -r requirements.txt
```

### Poetry

Poetry is a tool for managing Python projects and dependencies.

In this module, Poetry uses:

```txt
pyproject.toml
```

Example:

```bash
poetry install
poetry run python loading.py
```

### Environment Variables

Environment variables are values stored outside the code.

They are useful for configuration, for example:

- database URLs
- API keys
- log levels
- application mode

Python can read them with:

```python
os.getenv("VARIABLE_NAME")
```

### .env Files

A `.env` file stores environment variables for local development.

It must not be committed to Git because it can contain real secrets.

Instead, we commit:

```txt
.env.example
```

This file shows which variables are needed, but it contains only fake example values.

## 3. Lore And Connection To Theory

The module uses a Matrix theme.

The "Matrix" represents the global Python environment. If you install packages there, everything is visible and shared.

The "Construct" represents a virtual environment. It is an isolated training space where packages can be installed safely.

"Loading programs" represents installing and using dependencies.

"The Oracle" represents configuration. The Oracle knows how the system should run because it reads environment variables.

# Exercise 0: Entering The Matrix

## 1. What To Do, What It Teaches, And Theory Needed

File:

```txt
ex0/construct.py
```

The task is to create a program that detects if it is running inside a virtual environment.

It teaches:

- how to detect a virtual environment
- why virtual environments are useful
- where Python installs packages
- the difference between global Python and isolated Python

Theory needed:

- `sys.executable`
- `sys.prefix`
- `sys.base_prefix`
- `site.getsitepackages()`
- virtual environments created with `python3 -m venv`

## 2. How It Is Done In My Code

My `construct.py` checks:

```python
sys.prefix != sys.base_prefix
```

If this is true, the program is inside a virtual environment.

If it is outside a virtual environment, it prints:

- current Python path
- warning about the global environment
- commands to create and activate a virtual environment

If it is inside a virtual environment, it prints:

- current Python path
- virtual environment name
- virtual environment path
- package installation path

## 3. How To Run And Demonstrate

Run outside a virtual environment:

```bash
cd ex0
python3 construct.py
```

Expected idea:

```txt
MATRIX STATUS: You're still plugged in
Virtual Environment: None detected
```

Create a virtual environment:

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
```

Expected idea:

```txt
MATRIX STATUS: Welcome to the construct
SUCCESS: You're in an isolated environment!
```

Important for evaluation:

- do not submit `matrix_env/`
- the evaluator may create a new virtual environment during review
- the program must work both inside and outside a virtual environment

## 4. Subject Questions For This Exercise

### Why are virtual environments important?

They isolate project dependencies. This prevents package conflicts and protects the global Python installation.

### How does the program detect a virtual environment?

It compares `sys.prefix` and `sys.base_prefix`.

If they are different, Python is running inside a virtual environment.

## 5. Tricky Evaluation Questions

### Why should we not install packages globally?

Because global packages are shared by many projects. Installing or upgrading one package can break another project.

### Is a virtual environment part of the project source code?

No. It is generated locally and should not be submitted.

### What is `site-packages`?

It is the directory where Python installs third-party packages.

# Exercise 1: Loading Programs

## 1. What To Do, What It Teaches, And Theory Needed

Files:

```txt
ex1/loading.py
ex1/requirements.txt
ex1/pyproject.toml
```

The task is to create a data analysis program that uses external packages.

It teaches:

- how to check if dependencies are installed
- how to install packages with pip
- how to describe dependencies with Poetry
- how to handle missing packages without crashing
- how to generate, analyze, and visualize data

Theory needed:

- `importlib`
- `requirements.txt`
- `pyproject.toml`
- pip
- Poetry
- `numpy`
- `pandas`
- `requests`
- `matplotlib`

## 2. How It Is Done In My Code

My `loading.py` uses `importlib.import_module()` to check dependencies.

This is important because normal imports at the top of the file would crash immediately if a package is missing.

The program checks:

- `pandas`
- `numpy`
- `requests`
- `matplotlib`

If something is missing, it prints installation instructions:

```bash
pip install -r requirements.txt
```

or:

```bash
poetry install
```

If all dependencies are available, the program:

- tries to get a random seed with `requests`
- uses a fallback seed if the API is unavailable
- generates 1000 Matrix signal values with `numpy`
- stores and analyzes the data with `pandas`
- creates a histogram with `matplotlib`
- saves the result as `matrix_analysis.png`

## 3. How To Run And Demonstrate

### Test Without Dependencies

Use a new clean virtual environment and do not install requirements:

```bash
cd ex1
python3 -m venv test_env
source test_env/bin/activate
python3 loading.py
```

Expected idea:

```txt
[MISSING] pandas - Please install this package.
Missing dependencies detected.
pip install -r requirements.txt
poetry install
```

Important for evaluation:

- do not submit `test_env/`
- this test proves the program handles missing dependencies safely

### Test With pip

```bash
cd ex1
python3 -m venv matrix_env
source matrix_env/bin/activate
pip install -r requirements.txt
python3 loading.py
```

Expected idea:

```txt
[OK] pandas
[OK] numpy
[OK] requests
[OK] matplotlib
Analyzing Matrix data...
Processing 1000 data points...
Analysis complete!
Results saved to: matrix_analysis.png
```

Important for evaluation:

- `matrix_env/` must not be submitted
- `matrix_analysis.png` is generated output and should not be submitted

### Test With Poetry

```bash
cd ex1
poetry install
poetry run python loading.py
```

This proves that Poetry can install dependencies from `pyproject.toml`.

## 4. Subject Questions For This Exercise

### What is the difference between pip and Poetry?

`pip` is mainly a package installer. It installs packages into the current Python environment.

Poetry manages project dependencies and can also manage the virtual environment. It reads dependency information from `pyproject.toml`.

### Why use `requirements.txt`?

It gives pip a list of packages to install.

### Why use `pyproject.toml`?

It gives Poetry structured information about the project and its dependencies.

### Why use `importlib`?

It lets the program check dependencies dynamically. If a package is missing, the program can print a helpful message instead of crashing.

### What does "Matrix data" mean here?

It means simulated data for the theme of the exercise. In my code, it is fake signal data generated with `numpy`.

## 5. Tricky Evaluation Questions

### What happens if `pandas` is missing?

The program prints `[MISSING] pandas` and shows installation commands. It does not crash.

### Why must `numpy` be the source of the dataset?

The subject requires simulated Matrix data to come from `numpy`, not from hardcoded lists or `range()`.

### What happens if the external API is unavailable?

The program catches the error and uses a fallback seed. This keeps the analysis working.

### Why should generated files not be submitted?

They are not source code. They can be recreated by running the program.

# Exercise 2: Accessing The Mainframe

## 1. What To Do, What It Teaches, And Theory Needed

Files:

```txt
ex2/oracle.py
ex2/.env.example
ex2/.gitignore
```

The task is to create a configuration system using environment variables and `.env` files.

It teaches:

- how to load environment variables
- how to use `python-dotenv`
- how to avoid hardcoded secrets
- how to separate development and production configuration
- how to handle missing configuration

Theory needed:

- `os.getenv()`
- environment variables
- `.env`
- `.env.example`
- `.gitignore`
- `python-dotenv`

## 2. How It Is Done In My Code

My `oracle.py` loads configuration with:

```python
load_dotenv()
```

It reads these variables:

- `MATRIX_MODE`
- `DATABASE_URL`
- `API_KEY`
- `LOG_LEVEL`
- `ZION_ENDPOINT`

If a value is missing, the program uses:

```txt
MISSING
```

The program does not print the real API key or full database URL. It only prints safe status messages like:

```txt
API Access: Authenticated
Database: Configured
```

It also shows a visible difference between development and production:

- development prints diagnostics
- production prints optimizations

## 3. How To Run And Demonstrate

### Test Missing Configuration

Make sure there is no `.env` file:

```bash
cd ex2
python3 oracle.py
```

Expected idea:

```txt
Mode: MISSING
Database: Missing DATABASE_URL
API Access: Missing API_KEY
WARNING: Some configuration values are missing.
```

### Test With `.env`

```bash
cp .env.example .env
python3 oracle.py
```

Expected idea:

```txt
Mode: development
Runtime Profile: Development diagnostics enabled
Database: Configured
API Access: Authenticated
Zion Network: Online
```

### Test Production Override

```bash
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

Expected idea:

```txt
Mode: production
Runtime Profile: Production optimizations enabled
```

Important for evaluation:

- `.env` must not be submitted
- `.env.example` must be submitted
- `.gitignore` must ignore `.env`
- the evaluator can create their own `.env` from `.env.example`

## 4. Subject Questions For This Exercise

### Why should secrets not be hardcoded?

Hardcoded secrets can be leaked through Git. If an API key or password is committed, other people may see it.

### Why use environment variables?

They let the same program run with different configuration without changing the code.

### Why commit `.env.example` but not `.env`?

`.env.example` documents required variables with fake values.

`.env` can contain real secrets, so it must stay local.

### How does the program show development and production configuration?

It reads `MATRIX_MODE`.

If the mode is `development`, it prints development diagnostics.

If the mode is `production`, it prints production optimizations.

## 5. Tricky Evaluation Questions

### Does `python-dotenv` replace real environment variables?

No. Real environment variables can override values from `.env`.

### What happens if `API_KEY` is missing?

The program prints a warning and exits with an error status.

### Why not print the API key?

Because it is secret. The program should only say if API access is configured.

### What should be in `.gitignore`?

```gitignore
.env
__pycache__/
.mypy_cache/
matrix_env/
```

# Note About Pydantic Questions

The question below is not from `python_module_08` and this module does not use Pydantic:

```txt
Think About: How does Pydantic's automatic type conversion work?
What happens when you pass a string timestamp to a datetime field?
```

General answer:

Pydantic validates data using type annotations. It can also convert compatible input values automatically.

For example, if a model has a `datetime` field and you pass a valid timestamp string, Pydantic tries to parse the string into a real `datetime` object.

If the string has a valid datetime format, validation succeeds.

If the string is not a valid datetime, Pydantic raises a validation error.

# General Peer-Review Answers

## Why Are Virtual Environments Important?

They isolate project dependencies. This prevents package conflicts and protects the global Python installation.

## What Is The Difference Between pip And Poetry?

`pip` installs packages.

Poetry manages dependencies and project metadata with `pyproject.toml`.

## How Do Environment Variables Keep Applications Secure?

They keep secrets and configuration outside the source code.

This means the same code can run in development and production with different settings.

## What Should Be Submitted?

Submit:

```txt
ex0/construct.py
ex1/loading.py
ex1/requirements.txt
ex1/pyproject.toml
ex2/oracle.py
ex2/.env.example
ex2/.gitignore
README.md
```

Do not submit:

```txt
matrix_env/
test_env/
.env
__pycache__/
.mypy_cache/
matrix_analysis.png
```

# Useful Checks

Run before evaluation:

```bash
flake8 ex0/construct.py
flake8 ex1/loading.py
flake8 ex2/oracle.py
mypy ex0/construct.py
mypy ex1/loading.py
mypy ex2/oracle.py
```
