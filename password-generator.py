import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox, QMessageBox, QFileDialog, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import webbrowser

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 400)

        self.setWindowIcon(QIcon("icons/icon_password-generator.png"))

        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
                color: #333;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #4CAF50;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
                border-radius: 5px;
                background-color: #fff;
                border: 1px solid #ccc;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QCheckBox {
                font-size: 14px;
                color: #4CAF50;
            }
            .link-icons {
                padding: 10px;
            }
            .link-icons img {
                width: 40px;
                height: 40px;
                margin: 10px;
                cursor: pointer;
            }
        """)

        self.min_length_label = QLabel("Minimum Length:", self)
        self.min_length_input = QLineEdit(self)
        self.min_length_input.setText("10")
        self.min_length_input.setAlignment(Qt.AlignCenter)

        self.max_length_label = QLabel("Maximum Length:", self)
        self.max_length_input = QLineEdit(self)
        self.max_length_input.setText("16")
        self.max_length_input.setAlignment(Qt.AlignCenter)

        self.include_letters_checkbox = QCheckBox("Include Letters", self)
        self.include_letters_checkbox.setChecked(True)

        self.include_digits_checkbox = QCheckBox("Include Digits", self)
        self.include_digits_checkbox.setChecked(True)

        self.special_chars_checkbox = QCheckBox("Include Special Characters", self)

        self.generate_button = QPushButton("Generate", self)
        self.generate_button.clicked.connect(self.generate_password)

        self.password_output = QLineEdit(self)
        self.password_output.setReadOnly(True)

        self.copy_button = QPushButton("Copy", self)
        self.copy_button.clicked.connect(self.copy_password)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_password)

        self.link_icons_layout = QHBoxLayout()

        self.youtube_icon = QPushButton(self)
        self.youtube_icon.setIcon(QIcon("icons/youtube_icon.png"))
        self.youtube_icon.clicked.connect(self.open_youtube)
        self.youtube_icon.setStyleSheet("background: transparent; border: none;")
        self.link_icons_layout.addWidget(self.youtube_icon)

        self.github_icon = QPushButton(self)
        self.github_icon.setIcon(QIcon("icons/github_icon.png"))
        self.github_icon.clicked.connect(self.open_github)
        self.github_icon.setStyleSheet("background: transparent; border: none;")
        self.link_icons_layout.addWidget(self.github_icon)

        self.linktree_icon = QPushButton(self)
        self.linktree_icon.setIcon(QIcon("icons/linktree_icon.png"))
        self.linktree_icon.clicked.connect(self.open_linktree)
        self.linktree_icon.setStyleSheet("background: transparent; border: none;")
        self.link_icons_layout.addWidget(self.linktree_icon)

        layout = QVBoxLayout()
        layout.addWidget(self.min_length_label)
        layout.addWidget(self.min_length_input)
        layout.addWidget(self.max_length_label)
        layout.addWidget(self.max_length_input)
        layout.addWidget(self.include_letters_checkbox)
        layout.addWidget(self.include_digits_checkbox)
        layout.addWidget(self.special_chars_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_output)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.save_button)

        layout.addLayout(self.link_icons_layout)

        self.setLayout(layout)

    def generate_password(self):
        try:
            min_length = int(self.min_length_input.text())
            max_length = int(self.max_length_input.text())

            if min_length < 1 or max_length < min_length:
                raise ValueError("Invalid lengths.")

            length = random.randint(min_length, max_length)

            chars = ""
            if self.include_letters_checkbox.isChecked():
                chars += string.ascii_letters
            if self.include_digits_checkbox.isChecked():
                chars += string.digits
            if self.special_chars_checkbox.isChecked():
                chars += string.punctuation

            if not chars:
                raise ValueError("Please include at least one type of character (letters, digits, or special).")

            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_output.setText(password)

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_output.text())
        QMessageBox.information(self, "Copied", "Password copied to clipboard.")

    def save_password(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Password", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.password_output.text())
                QMessageBox.information(self, "Saved", "Password saved successfully.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Unable to save the file: {str(e)}")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/@theodenegamer1263")

    def open_github(self):
        webbrowser.open("https://github.com/Theodenegamer12")

    def open_linktree(self):
        webbrowser.open("https://linktr.ee/theodenegamer12")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
