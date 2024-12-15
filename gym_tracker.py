from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class GymTrackerWindow(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Gym Tracker")
        self.setGeometry(200, 200, 400, 300)

        # Create input fields
        layout = QVBoxLayout()
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("Enter Date (YYYY-MM-DD)")
        self.exercise_input = QLineEdit()
        self.exercise_input.setPlaceholderText("Enter Exercise Name")
        self.sets_input = QLineEdit()
        self.sets_input.setPlaceholderText("Enter Sets")
        self.reps_input = QLineEdit()
        self.reps_input.setPlaceholderText("Enter Reps")
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Enter Weight (kg)")

        # Save button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_gym_log)

        # Add widgets to layout
        for widget in [self.date_input, self.exercise_input, self.sets_input, self.reps_input, self.weight_input, save_button]:
            layout.addWidget(widget)

        self.setLayout(layout)

    def save_gym_log(self):
        """Save gym log to the database."""
        date = self.date_input.text()
        exercise = self.exercise_input.text()
        sets = self.sets_input.text()
        reps = self.reps_input.text()
        weight = self.weight_input.text()

        if not all([date, exercise, sets, reps, weight]):
            QMessageBox.warning(self, "Input Error", "Please fill out all fields!")
            return

        try:
            self.db_manager.insert_gym_log(date, exercise, int(sets), int(reps), float(weight))
            QMessageBox.information(self, "Success", "Gym log saved!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
