import sys
import csv
from PyQt6.QtWidgets import QApplication, QDialog
from gui.assigment_grader import Ui_Grader
from logic import calculate_grades

class GradeApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Grader()
        self.ui.setupUi(self)
        self.ui.calculate_button.clicked.connect(self.calculate)
        self.ui.export_button.clicked.connect(self.export)
        self.success = False
        self.result = []

    def calculate(self):
        '''hanfles calculate button being pressed'''
        total = self.ui.student_line.text()
        grades = self.ui.grade_line.text()
        self.success, self.result = calculate_grades(total, grades)
        if self.success:
            text = '\n'.join(self.result)
            self.ui.output_box.setText(text)
        else:
            self.ui.output_box.setText(self.result)

    def export(self):
        '''sends grades to the csv file'''
        if self.success:
            file = open('grades_output.csv', 'w', newline='')
            writer = csv.writer(file)
            writer.writerow(['Score', 'Grade'])
            for line in self.result:
                line = line.replace('Student score: ', '').replace(' Grade: ', ',')
                seperate = line.split(',')
                writer.writerow(seperate)
            file.close()
            self.ui.output_box.setText('Saved to grades_output.csv.')
        else:
            self.ui.output_box.setText('Nothing to export.')

app = QApplication(sys.argv)
window = GradeApp()
window.show()
sys.exit(app.exec())
