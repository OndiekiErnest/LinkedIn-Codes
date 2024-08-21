"""modify the size behaviour by using the sizepolicy"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSizePolicy

# create application instance
app = QApplication(sys.argv)
# create window
window = QWidget()

# create vertical layout
layout = QVBoxLayout()
# create widget
button = QPushButton("Expanding Button")
# modify the size policy
button.setSizePolicy(
    QSizePolicy.Policy.Fixed,  # horizontal fixed
    QSizePolicy.Policy.Expanding,  # vertical expanding
)
# add widget to layout
layout.addWidget(button)

# set layout to window
window.setLayout(layout)
# show window
window.show()
# run event loop; exit when the event loop exits
sys.exit(app.exec())
