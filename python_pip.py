# =====================================================
# PYTHON PIP (PACKAGE INSTALLER)
# =====================================================
# PIP is a package manager for Python packages (or modules).
# It allows you to install, remove, and manage packages for Python.

# =====================================================
# WHAT IS A PACKAGE?
# =====================================================
# A package contains all the files needed for a module.
# Modules are Python code libraries you can include in your projects.

# =====================================================
# CHECK IF PIP IS INSTALLED
# =====================================================
# Open Command Prompt or Terminal and type:
# pip --version
# Example:
# C:\> pip --version
# Output might be: pip 21.3.1 from ... (python 3.10)

# =====================================================
# INSTALLING PIP
# =====================================================
# If PIP is not installed, download it from: https://pypi.org/project/pip/
# Follow instructions to install PIP on your system.

# =====================================================
# DOWNLOAD A PACKAGE
# =====================================================
# Example: Install the "camelcase" package
# Open terminal and type:
# pip install camelcase

# =====================================================
# USING AN INSTALLED PACKAGE
# =====================================================
# Once installed, the package is ready to use.
# Example using "camelcase":

import camelcase

# Create CamelCase object
c = camelcase.CamelCase()

txt = "hello world"

# Convert first letter of each word to uppercase
print("CamelCase example:", c.hump(txt))  # Output: Hello World

# =====================================================
# FIND MORE PACKAGES
# =====================================================
# Browse packages at the official Python Package Index:
# https://pypi.org/

# =====================================================
# REMOVE (UNINSTALL) A PACKAGE
# =====================================================
# Use the uninstall command to remove a package.
# Example: Remove "camelcase"
# pip uninstall camelcase

# Terminal will ask to confirm:
# Uninstalling camelcase-0.2:
# Proceed (y/n)?  y

# =====================================================
# LIST INSTALLED PACKAGES
# =====================================================
# Use the command to list all installed packages:
# pip list
# Example output:
# Package         Version
# -----------------------
# camelcase       0.2
# mysql-connector 2.1.6
# pip             21.3.1
# pymongo         3.6.1
# setuptools      39.0.1

# =====================================================
# QUICK NOTES
# =====================================================
# - PIP is included by default in Python 3.4+
# - Use pip install <package_name> to install packages
# - Use pip uninstall <package_name> to remove packages
# - Use pip list to see all installed packages
