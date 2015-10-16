import unittest
import threading
import SocketServer
from PySide.QtGui import QApplication
from testable import MainWindow


class MockHandler(SocketServer.BaseRequestHandler):
    """
    This class would normally handle any data we send to the server.
    Of course, this is all fake.
    """
    def handle(self):
        self.request.sendall('Name1\n')
        self.request.sendall('Name2\n')
        self.request.sendall('Name3\n')


class MockServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    Basic mock server. We want to send some data when a client connects.
    """
    allow_reuse_address = True

    def __init__(self, *args, **kwargs):
        SocketServer.TCPServer.__init__(self, *args, **kwargs)


class QtTest(unittest.TestCase):
    def setUp(self):
        """
        Initialize our QApplication
        :return: None
        """

        # We need to be able to test our code without a real device. So we setup
        # our Mock server here. Then we connect our client to that mock server.
        self.server = MockServer(('localhost', 0), MockHandler)
        self.listen_ip, self.listen_port = self.server.server_address
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = False
        self.server_thread.start()

        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication([])

        self.main_window = MainWindow(None)

    def tearDown(self):
        self.server.shutdown()
        self.main_window.clean_up()

    def testNames(self):
        self.cnt = 0

        def _watch(msg):
            self.cnt += 1

        # We know our mock server should emit 3 messages to the message_signal. So
        # we can use this as a way to count that all 3 have been sent before trying
        # to verify that our names list was updated correctly.
        self.main_window.network_manager.message_signal.connect(_watch)

        # This is how we normally would start the connection. Just now we are pointing
        # to our mock server.
        self.main_window.start_api(self.listen_ip, self.listen_port)

        # We know our mock server is going to send 3 names. So keep processing
        # until all 3 have been sent.
        while self.cnt < 3:
            if self.app.hasPendingEvents():
                self.app.processEvents()

        # Finally, assert that our end goal has been met.
        assert self.main_window.names_list.count() == 3
