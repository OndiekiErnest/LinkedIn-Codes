"""arrange widgets vertically using the QVBoxLayout"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# create application instance
app = QApplication(sys.argv)
# create window
window = QWidget()

# create vertical layout
layout = QVBoxLayout()
# add widgets to layout (stacked)
layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))
layout.addWidget(QPushButton("Button 3"))

# set layout to window
window.setLayout(layout)
# show window
window.show()
# run event loop; exit when the event loop exits
sys.exit(app.exec())
