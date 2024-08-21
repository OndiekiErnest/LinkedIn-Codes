"""mix layouts to get the desired widget arrangement"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

# create app instance
app = QApplication(sys.argv)
# create window instance
window = QWidget()

# main layout that houses the other inner layouts
main_layout = QVBoxLayout()

# first row horizontal layout
top_layout = QHBoxLayout()
# add widgets to layout
top_layout.addWidget(QPushButton("Top Button 1"))
top_layout.addWidget(QPushButton("Top Button 2"))

# 2nd row horizontal layout
bottom_layout = QHBoxLayout()
bottom_layout.addWidget(QPushButton("Bottom Button 1"))
bottom_layout.addWidget(QPushButton("Bottom Button 2"))

# add inner layouts to main layout
main_layout.addLayout(top_layout)
main_layout.addLayout(bottom_layout)

# add main layout to window
window.setLayout(main_layout)
# show window
window.show()
# start app event loop
sys.exit(app.exec())
