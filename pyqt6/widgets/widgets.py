"""custom PyQt6 widgets"""

from PyQt6.QtWidgets import QLabel


class Label(QLabel):
    """custom PyQt6 QLabel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set properties to modify default behaviour
        self.setToolTip("This is a tooltip")
