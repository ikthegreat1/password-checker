# -*- coding: utf-8 -*-


# Password Strength Checker
# Very simple script to show logic, conditions, and user input

import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak: too short"
    elif not re.search(r"\d", password):
        return "Weak: add at least one number"
    elif not re.search(r"[A-Z]", password):
        return "Medium: add an uppercase letter"
    elif not re.search(r"[!@#$%^&*()_+]", password):
        return "Medium: add a special character"
    elif len(password) < 10:
        return "Medium: make it longer"
    else:
        return "Strong password!"

# Ask the user for a password
pwd = input("Enter a password to check: ")
print(check_password_strength(pwd))