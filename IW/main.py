import os
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit

class PensionProgramRunner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculul pensiei")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # inputs
        self.stagiul_cotizare_label = QLabel("Stagiul de cotizare")
        self.stagiul_cotizare_input = QLineEdit()
        self.layout.addWidget(self.stagiul_cotizare_label)
        self.layout.addWidget(self.stagiul_cotizare_input)

        self.venitul_mediu_lunar_label = QLabel("Venitul mediu lunar asigurat valorizat")
        self.venitul_mediu_lunar_input = QLineEdit()
        self.layout.addWidget(self.venitul_mediu_lunar_label)
        self.layout.addWidget(self.venitul_mediu_lunar_input)
        
        self.submit_button = QPushButton("Calculati pensia")
        self.submit_button.clicked.connect(self.calculate_pension_program)
        self.layout.addWidget(self.submit_button)

        self.result_text_edit = QTextEdit()
        self.result_text_edit.setReadOnly(True)  # Make the output text area non-editable
        self.layout.addWidget(self.result_text_edit)

    def calculate_pension_program(self):
        stagiul_cotizare = self.stagiul_cotizare_input.text()
        venitul_mediu_lunar = self.venitul_mediu_lunar_input.text()

        pension_program_path = os.path.join(os.getcwd(), "pension.cpp")

        if not os.path.exists(pension_program_path):
            self.result_text_edit.setPlainText("Error: pension.cpp not found.")
            return

        try:
            subprocess.run(["g++", "-o", "pension", "pension.cpp"], check=True)
            result = subprocess.run(["./pension", stagiul_cotizare, venitul_mediu_lunar], capture_output=True, text=True)
            self.result_text_edit.setPlainText(result.stdout)
        except subprocess.CalledProcessError as e:
            self.result_text_edit.setPlainText("Error: " + e.stderr)

def main():
    app = QApplication([])
    window = PensionProgramRunner()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
