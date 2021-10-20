import sys
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QStyleOptionViewItem, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

testVariavel = "teste"

window = QWidget()
window.setWindowTitle('Japacama')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('center'))
layout.addWidget(QPushButton('Left'))
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
