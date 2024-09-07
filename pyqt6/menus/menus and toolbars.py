"""minimal example showing how to re-use actions"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QMenu,
    QLabel,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    """main app window"""

    def __init__(self):
        super().__init__()

        # minimum window size
        self.setMinimumSize(600, 300)

        self.label = QLabel("Right-click or use the toolbar to trigger actions.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # add label to main window
        self.setCentralWidget(self.label)

        # create a shared action
        self.shared_action = QAction("Shared Action", self)
        # hook signal to a function - called when action is clicked
        self.shared_action.triggered.connect(self.shared_action_triggered)

        # setup toolbar
        self.create_toolbar()

        # setup menu bar
        self.create_menus()

        # setup context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def create_toolbar(self):
        """create app toolbar"""

        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(self.shared_action)

    def create_menus(self):
        """create app menu bar"""
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.shared_action)

    def show_context_menu(self, pos):
        """create context menu shown on right-click"""
        context_menu = QMenu(self)
        context_menu.addAction(self.shared_action)
        context_menu.exec(self.mapToGlobal(pos))

    def shared_action_triggered(self):
        """shared slot/function"""
        self.label.setText("Shared Action Clicked!")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
