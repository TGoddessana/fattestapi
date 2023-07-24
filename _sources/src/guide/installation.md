-------------------------------------------
title: Installation
-------------------------------------------

# Installation
in this section, we will learn how to install `FattestAPI` package.

## Python version
`FattestAPI` supports Python3.9 and newer. make sure you have installed python3.9 or newer.
to check your python version, run this command in your terminal:

```shell
python --version
```

## Virtual Environment setup

### What is a virtual environment, and why do I need it?

In Python, a virtual environment is a self-contained directory that contains a specific Python interpreter and its
associated libraries. It allows you to create an isolated environment for your Python projects, ensuring that each
project can have its own dependencies without interfering with other projects or the system-wide Python installation.

### How to create a virtual environment

now that you know what a virtual environment is and why you need it, let's see how to create one.

#### Windows:

1. Open Command Prompt:
    - Open a prompt at the project location.

2. Create a Virtual Environment:
   ```
   python -m venv venv
   ```

   This will create a new virtual environment named "venv" in the current directory.

3. Activate the Virtual Environment:
   ```
   venv\Scripts\activate
   ```

   You'll notice that the Command Prompt prompt changes to show the active virtual environment.

#### macOS/Linux:

1. Open Terminal:
    - Open a terminal at the project location.

2. Create a Virtual Environment:
   ```
   python3 -m venv venv
   ```

   This will create a new virtual environment named "venv" in the current directory.

3. Activate the Virtual Environment:
   ```
   source venv/bin/activate
   ```

   The Terminal prompt will change to indicate that the virtual environment is active.

## Install FattestAPI
now the virtual environment is ready, let's install `FattestAPI` package.
you can install `FattestAPI` using `pip`:

```shell
pip install fattestapi
```

now that's it! you have installed `FattestAPI` package successfully.

