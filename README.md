# Password Generator with Graphical Interface (PyQt5)

This project is a Python application using the **PyQt5** library to generate secure passwords. The application allows users to specify the password length, include letters, digits, and special characters, and then generates a password based on these criteria. It also allows the user to copy, save the password, and open external links (YouTube, GitHub, and Linktree) via clickable icons.

## Features:

### 1. **Graphical Interface with PyQt5**:
   - A simple and user-friendly interface that allows users to customize their password generation criteria.
   - Fields to specify **minimum** and **maximum** password length.
   - Checkboxes to include **letters**, **digits**, and **special characters**.

### 2. **Password Generation**:
   - Based on the selected options (length and character types), the application generates a password by randomly selecting characters from the allowed set.
   - The generated password is displayed in a read-only text field.

### 3. **Copy to Clipboard**:
   - After generating a password, the user can click a "Copy" button to copy the password to the clipboard for easy pasting.

### 4. **Save Password to File**:
   - The application allows the user to save the generated password to a text file by clicking a "Save" button. The file can be saved with a user-defined name and location.

### 6. **Customization**:
   - The minimum password length is set to **10** by default, and the maximum length is set to **16**.
   - The checkboxes for including letters and digits are checked by default, ensuring that these character types are included in the password generation process.

### 7. **Error Handling**:
   - The application checks if the input values for password length are valid (e.g., minimum must be less than or equal to maximum).
   - If no character types are selected, an error message prompts the user to include at least one type of character (letters, digits, or special characters).

---

## Requirements:
- Python 3.x
- PyQt5 (Install with `pip install PyQt5`)
```bash
pip install PyQt5 pypresence
```

## How to Run:
1. Clone or download the repository.
2. Install PyQt5 by running `pip install PyQt5` in your terminal.
3. Run the script using Python: `python password_generator.py`

---

This password generator tool is ideal for quickly creating secure and customizable passwords, with an easy-to-use interface and extra features like copying, saving, and accessing external sites.
