"""arrange widgets in a grid layout"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

# create app instance
app = QApplication(sys.argv)
# create window instance
window = QWidget()

# create grid layout
grid_layout = QGridLayout()

# add widgets to grid layout (2x2 grid)
grid_layout.addWidget(QPushButton("Button 1"), 0, 0)  # row, column
grid_layout.addWidget(QPushButton("Button 2"), 0, 1)  # row=0, column=1
grid_layout.addWidget(QPushButton("Button 3"), 1, 0)
grid_layout.addWidget(QPushButton("Button 4"), 1, 1)

# set the grid layout to the window
window.setLayout(grid_layout)

# show window
window.show()
# start app event loop; exit when event loop exits
sys.exit(app.exec())
