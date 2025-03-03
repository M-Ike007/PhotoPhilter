# import sys
#
#
# # 1. Import QApplication and all the required widgets
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget
# # 2. Create an instance of QApplication
# app = QApplication([])
#
# # 3. Create your application's GUI
# window = QWidget()
# window.setWindowTitle("PyQt App")
# window.setGeometry(100, 100, 280, 80)
# helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
# helloMsg.move(60, 15)
#
# # 4. Show your application's GUI
# window.show()
#
# # 5. Run your application's event loop
# sys.exit(app.exec())

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)

window.get_image()
sys.exit(app.exec())