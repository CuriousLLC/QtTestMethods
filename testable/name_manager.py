from PySide.QtCore import QObject, Signal, Slot


class NameManager(QObject):
    """
    The NameManager class runs in its own thread. Even though we are only using a
    list for storage, imagine we are using some other mechanism like a database or
    an API service. Those other mechanisms have latency while we interact with them.

    We want the main GUI thread to be responsive while we store/retrieve names.
    That's why we run this class in its own thread.
    """
    names_signal = Signal(list)

    def __init__(self):
        super(NameManager, self).__init__()

        self.names = []


    @Slot()
    def store_name(self, name):
        """
        This method puts a name in long term storage. Here it's just
        a list of course, but let's say it's a database or redis or something.
        :param name: String
        :return:
        """
        self.names.append(name)

    @Slot()
    def get_all_names(self):
        self.names_signal.emit(self.names)
