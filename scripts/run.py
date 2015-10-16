from PySide.QtGui import QApplication
from testable import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()
    app.exec_()
    main_window.clean_up()