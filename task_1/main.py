from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QObject
import sys
import ui_handler
import handler


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('task_1.ui', self)
        self.show()


def init_ui(root_elem: QObject):
    interface = ui_handler.get_interface_stub()
    interface = ui_handler.find_interface_elements(root_elem, interface)
    handler.bind_logic_to_interface(interface)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    init_ui(window)
    app.exec_()
