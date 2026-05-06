# Python Module 08

This module is about basic tools used in real Python projects:

- virtual environments
- dependency management with pip and Poetry
- environment variables and `.env` files

The subject uses a Matrix theme, but the real goal is to understand how to keep a Python project isolated, reproducible, and configurable.

## Exercise 0: Entering the Matrix

File:

```txt
ex0/construct.py
```

This program checks if Python is running inside a virtual environment.

If it is outside a virtual environment, it prints a warning and shows how to create one.
If it is inside a virtual environment, it prints the virtual environment name, path, Python executable, and package installation path.

### Theory

Python can run from the global system installation or from a virtual environment.

The global installation belongs to the operating system or the user account. Installing packages globally can create conflicts, because every project may use the same package location.

A virtual environment is a separate Python environment for one project. It has its own Python executable and its own `site-packages` directory. This means packages installed there do not affect the global system.

In Python, `sys.prefix` shows the current Python environment. `sys.base_prefix` shows the base Python installation. If they are different, the program is running inside a virtual environment.

The `site` module shows where Python installs third-party packages. In a virtual environment, this path points inside the virtual environment folder.

### How to show it working

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

Create and activate a virtual environment:

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

Do not submit `matrix_env/`.

## Exercise 1: Loading Programs

Files:

```txt
ex1/loading.py
ex1/requirements.txt
ex1/pyproject.toml
```

This program demonstrates package management.

It checks if the required packages are installed:

- `pandas`
- `numpy`
- `requests`
- `matplotlib`

If packages are missing, the program does not crash. It prints installation instructions for both pip and Poetry.

When all dependencies are installed, it:

- uses `requests` to try to get a random seed from an API
- uses a fallback seed if the API is unavailable
- uses `numpy` to generate 1000 fake Matrix signal values
- uses `pandas` to analyze the data
- uses `matplotlib` to save `matrix_analysis.png`

### Theory

Most real Python projects need external packages. These packages are called dependencies.

`pip` installs dependencies into the current Python environment. In this exercise, `requirements.txt` is the dependency list for pip. It is simple and common.

Poetry is a project and dependency management tool. It uses `pyproject.toml` to describe the project and its dependencies. Poetry can also manage a virtual environment for the project.

The program uses `importlib` to import packages dynamically. This is useful because direct imports at the top of the file would crash immediately if a package is missing. With `importlib`, the program can check each dependency and print a helpful message.

`numpy` is used for numerical data generation. In this exercise, it creates fake Matrix signal values.

`pandas` is used for data analysis. It stores the generated data in a DataFrame and calculates values like minimum, maximum, and average.

`matplotlib` is used for visualization. It creates and saves a histogram image.

`requests` is used to try to fetch data from an external API. If the request fails, the program catches the error and continues with a fallback value. This is important because data programs should handle external failures safely.

### How to show missing dependencies

Use a clean environment without installing the requirements:

```bash
cd ex1
python3 -m venv test_env
source test_env/bin/activate
python3 loading.py
```

Expected idea:

```txt
[MISSING] pandas - Please install this package.
Install them with pip:
pip install -r requirements.txt

Or install them with Poetry:
poetry install
```

Do not submit `test_env/`.

### How to show pip dependency management

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

### How to show Poetry dependency management

```bash
cd ex1
poetry install
poetry run python loading.py
```

Poetry reads dependencies from `pyproject.toml`.

Do not submit virtual environments or generated cache files.

## Exercise 2: Accessing the Mainframe

Files:

```txt
ex2/oracle.py
ex2/.env.example
ex2/.gitignore
```

This program demonstrates configuration with environment variables.

It uses `python-dotenv` to load values from a `.env` file.

The required configuration keys are:

- `MATRIX_MODE`
- `DATABASE_URL`
- `API_KEY`
- `LOG_LEVEL`
- `ZION_ENDPOINT`

The program does not print secret values directly. For example, it prints `API Access: Authenticated` instead of printing the real API key.

### Theory

Configuration is data that changes between environments but should not require code changes.

Examples of configuration are:

- database URLs
- API keys
- log levels
- application mode
- service endpoints

Environment variables are values stored outside the source code. Python can read them with `os.getenv()`.

A `.env` file is a local development file that stores environment variables in a simple format. The `python-dotenv` package loads these values into the program.

The `.env.example` file is safe to commit because it contains fake example values. It documents which variables the program needs.

The real `.env` file should not be committed, because it may contain real secrets.

Development configuration is for local testing. It can use local databases, fake keys, and verbose logs.

Production configuration is for the real application. It should use real services, real secrets, and safer logging.

In this exercise, `MATRIX_MODE` shows the difference between development and production in the output.

### How to show missing configuration

Run without a `.env` file:

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

### How to show configuration from `.env`

Create a local `.env` file from the example:

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

The `.env` file is ignored by Git because it can contain real secrets.

### How to show production override

Run:

```bash
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

Expected idea:

```txt
Mode: production
Runtime Profile: Production optimizations enabled
```

This shows that real environment variables can override values from `.env`.

## Peer-Review Answers

### What is a virtual environment, and why is it important?

A virtual environment is an isolated Python environment for one project.

It is important because each project can have its own packages and package versions. This avoids breaking the global Python installation and avoids conflicts between different projects.

Example: one project may need an old version of `numpy`, and another project may need a new version. Virtual environments keep them separate.

### What is the difference between pip and Poetry?

`pip` is a package installer. In this module, it installs packages from `requirements.txt`.

Example:

```bash
pip install -r requirements.txt
```

Poetry is a dependency and project management tool. It reads project information and dependencies from `pyproject.toml`. It can also create and manage the virtual environment.

Example:

```bash
poetry install
poetry run python loading.py
```

Simple difference:

- pip is simple and direct
- Poetry gives more project structure and environment management

### How do environment variables keep applications secure and configurable?

Environment variables let the program read configuration from outside the code.

This is useful because secrets like API keys and database passwords should not be written directly in source code.

For local development, we can use a `.env` file. For production, the server can provide real environment variables.

The same code can run in different places with different configuration.

### Why should `.env` be in `.gitignore`?

`.env` can contain real secrets, like:

- API keys
- database passwords
- private URLs

If `.env` is committed to Git, other people may see those secrets. That is a security risk.

We commit `.env.example` instead. It shows which variables are needed, but it only contains fake example values.

### What is the difference between development and production configuration?

Development configuration is for local testing. It can use local databases, fake keys, and debug logs.

Production configuration is for the real application. It should use real services, real secrets, and safer logging.

In `ex2`, the difference is visible with `MATRIX_MODE`:

- `development` prints development diagnostics
- `production` prints production optimizations

### What should be submitted?

Submit only the required source files.

For this module:

```txt
ex0/construct.py
ex1/loading.py
ex1/requirements.txt
ex1/pyproject.toml
ex2/oracle.py
ex2/.env.example
ex2/.gitignore
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

## Useful Checks

Run these before evaluation:

```bash
flake8 ex0/construct.py
flake8 ex1/loading.py
flake8 ex2/oracle.py
mypy ex0/construct.py
mypy ex1/loading.py
mypy ex2/oracle.py
```

If dependencies are missing, activate the correct virtual environment and install them first.
