"""first application window using PyQt6"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# create a class for the main window
class MainWindow(QMainWindow):
    """application window"""

    def __init__(self):
        super().__init__()
        # set the window title
        self.setWindowTitle("Hello PyQt6")
        # set the window size and position
        self.setGeometry(100, 100, 800, 600)
        # add button with text "Change"
        button = QPushButton("Change")
        self.setCentralWidget(button)


if __name__ == "__main__":
    # create the application object
    app = QApplication(sys.argv)
    # create an instance of the main window
    window = MainWindow()
    window.show()  # show the window
    sys.exit(app.exec())  # start the application's event loop
