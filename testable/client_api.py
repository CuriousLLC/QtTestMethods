import socket
import select
import threading


class ExternalClientApiThread(threading.Thread):
    """
    This thread represents something that you may have no control over. If you have an
    API using requests maybe. Or a state machine processing TCP or serial data. You
    can't use QThreads because this is an external package.

    This is example of a class that processes data in the background and sends messages
    to any subscribers.
    """

    def __init__(self, *args, **kwargs):
        super(ExternalClientApiThread, self).__init__(*args, **kwargs)

        self.active = threading.Event()
        self.active.set()
        self.subscribers = []

    def add_subscriber(self, fn):
        self.subscribers.append(fn)

    def connect(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def end_connection(self):
        self.active.clear()
        self.sock.close()

    def run(self):
        buffer = ''

        while self.active.isSet():
            try:
                rtr, rtw, e = select.select([self.sock,], [], [], 0.5)
            except select.error as e:
                continue

            if len(rtr) > 0:
                data = self.sock.recv(64)

                if len(data) == 0:
                    self.active.clear()
                else:
                    buffer += data
                    if buffer[-1] == '\n':
                        for s in self.subscribers:
                            for m in buffer.split('\n'):
                                if len(m) > 0:
                                    s(m)

                        buffer = ''