"""
Python Virtual Environment
==========================

This file explains how to use Python virtual environments.
It contains examples, explanations, and Python code where applicable.

A virtual environment is an isolated container for Python projects:
- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different versions of the same package
"""

# =========================
# 1. Creating a Virtual Environment
# =========================
# Python has a built-in module called venv to create virtual environments.
# Run the following command in your terminal to create a virtual environment
# called 'myfirstproject':
#
# Windows / macOS / Linux:
# python -m venv myfirstproject
#
# This creates a folder named 'myfirstproject' with subfolders:
# Include, Lib, Scripts, pyvenv.cfg

# =========================
# 2. Activating a Virtual Environment
# =========================
# Activate it before using Python or installing packages.
#
# Windows:
# myfirstproject\Scripts\activate
#
# macOS / Linux:
# source myfirstproject/bin/activate
#
# After activation, your terminal prompt will look like:
# (myfirstproject) C:\Users\Your Name>

# =========================
# 3. Installing Packages
# =========================
# Once activated, you can install packages using pip:
# Example: Install 'cowsay'
#
# pip install cowsay

# =========================
# 4. Using Packages
# =========================
# After installing, you can use the package in Python code.
# Example: cowsay

# Uncomment the lines below after installing cowsay in your virtual environment
# import cowsay
# cowsay.cow("Good Mooooorning!")

# =========================
# 5. Deactivating the Virtual Environment
# =========================
# To exit the virtual environment:
#
# deactivate
#
# You are now back to your system Python environment.

# =========================
# 6. Running Python Scripts Outside the Virtual Environment
# =========================
# If you run a script that uses a package installed in a virtual environment
# without activating it, Python will throw an error:
#
# ModuleNotFoundError: No module named 'cowsay'

# =========================
# 7. Deleting a Virtual Environment
# =========================
# Simply delete the folder for the virtual environment.
#
# Windows:
# rmdir /s /q myfirstproject
#
# macOS / Linux:
# rm -rf myfirstproject
#
# Only the virtual environment and its packages are removed. Other projects are safe.

# =========================
# Notes for Students:
# =========================
# - Virtual environments help manage dependencies per project.
# - Always activate the environment before installing or using packages.
# - You can have multiple virtual environments on the same machine.
# - Python code inside a virtual environment works the same as system Python.
