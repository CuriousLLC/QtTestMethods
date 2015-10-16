from PySide.QtGui import QMainWindow
from PySide.QtCore import QThread, Signal, Slot
from mainwindow import Ui_MainWindow
from name_manager import NameManager
from network_manager import NetworkManager


GREETING = "Hello"


class MainWindow(QMainWindow, Ui_MainWindow):

    add_name_signal = Signal(unicode)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Create the name manager instance and move it to another thread.
        # This will cause all the slots to be run in that other thread
        # instead of our GUI thread.
        self.name_manager = NameManager()
        self.name_manager_thread = QThread()
        self.name_manager.moveToThread(self.name_manager_thread)
        self.name_manager_thread.start()

        # Create our network manager
        self.network_manager = NetworkManager()

        # When the name manager emits it's full name list, we want to
        # repopulate our list.
        self.name_manager.names_signal.connect(self.populate_list)

        # When the restore list button is clicked, let the name manager
        # know we need all the names in long term storage
        self.restore_list_button.clicked.connect(self.name_manager.get_all_names)

        self.add_name_signal.connect(self.name_manager.store_name)
        self.add_name_signal.connect(self.cache_name)
        self.submit_button.clicked.connect(self.say_hello)
        self.clear_list_button.clicked.connect(self.clear_list)

    def clean_up(self):
        """
        You can't rely on __del__ properly closing down all your threads. So use
        a clean_up method that will be called manually.
        :return:
        """
        if hasattr(self, 'network_manager_thread'):
            self.network_manager.api.end_connection()
            self.network_manager.api.join()
            self.network_manager_thread.quit()

        self.name_manager_thread.quit()

    def start_api(self, ip, port):
        """
        Connect to an external API service which will send us names
        :param ip: IP address of server
        :param port: Port of service
        :return:
        """
        self.network_manager_thread = QThread()
        self.network_manager.moveToThread(self.network_manager_thread)
        self.network_manager.message_signal.connect(self.handle_message)
        self.network_manager_thread.start()

        self.network_manager.connect_signal.emit(ip, port)

    @Slot()
    def handle_message(self, message):
        """
        Handle incoming names from the API. We simply want to follow the
        established procedure to add a new name. So we just emit on that
        signal.
        :param message: String name
        :return:
        """
        self.add_name_signal.emit(message)

    @Slot()
    def say_hello(self):
        self.add_name_signal.emit(self.name_text.text())
        self.hello_label.setText(u"{} {}".format(GREETING, self.name_text.text()))
        self.name_text.setText('')

    @Slot()
    def cache_name(self, name):
        self.names_list.addItem(name)

    @Slot()
    def clear_list(self):
        self.names_list.clear()

    @Slot()
    def populate_list(self, names):
        """
        Clears and repopulates the list with the given list
        :param names: List of names
        :return:
        """
        self.clear_list()
        for name in names:
            self.names_list.addItem(name)