from PySide.QtCore import QObject, Signal, Slot
from client_api import ExternalClientApiThread


class NetworkManager(QObject):
    """
    This NetworkManager controls a connection to an external device. The API for
    the device reads data over a socket. It has to run in a background thread
    because data is constantly streaming in. You can't block the GUI while reading
    the device data.
    """
    message_signal = Signal(unicode)
    connect_signal = Signal(str, int)

    def __init__(self):
        super(NetworkManager, self).__init__()

        self.connect_signal.connect(self.start_connection)

    @Slot()
    def start_connection(self, ip, port):
        self.api = ExternalClientApiThread()
        self.api.add_subscriber(self.handle_message)
        self.api.connect(ip, port)
        self.api.start()

    def handle_message(self, message):
        self.message_signal.emit(message)
