import unittest
from PySide.QtGui import QApplication
from testable import MainWindow
from testable.main import GREETING


class QtTest(unittest.TestCase):
    def setUp(self):
        """
        Initialize our QApplication
        :return: None
        """
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication([])

        self.main_window = MainWindow(None)

    def tearDown(self):
        self.main_window.clean_up()

    def testGreeting(self):
        self.main_window.name_text.setText('Ryan')
        self.main_window.submit_button.click()

        assert self.main_window.hello_label.text() == u"{} {}".format(GREETING, 'Ryan')

    def testNamesList(self):
        self.main_window.name_text.setText('Ryan')
        self.main_window.submit_button.click()

        self.main_window.name_text.setText('Meg')
        self.main_window.submit_button.click()

        assert self.main_window.names_list.count() == 2
        assert self.main_window.names_list.item(0).text() == 'Ryan'
        assert self.main_window.names_list.item(1).text() == 'Meg'

    def testClearList(self):
        self.main_window.name_text.setText('Ryan')
        self.main_window.submit_button.click()

        self.main_window.name_text.setText('Meg')
        self.main_window.submit_button.click()

        self.main_window.clear_list_button.click()
        assert self.main_window.names_list.count() == 0

    def testRestoreList(self):
        """
        Using this method to test the Restore List procedure, we need
        to know exactly how many signals are going to be emitted. This could
        change over time without affecting our desired functionality.
        :return:
        """
        self.main_window.name_text.setText('Ryan')
        self.main_window.submit_button.click()

        self.main_window.name_text.setText('Meg')
        self.main_window.submit_button.click()

        assert self.main_window.names_list.count() == 2

        self.main_window.clear_list_button.click()
        assert self.main_window.names_list.count() == 0

        # This is running in another thread and we can't test
        # it the same way we tested other methods!
        self.main_window.restore_list_button.click()

        # First a signal is emitted to the NameManager thread to
        # get all the names. We have to process this event manually.
        self.app.processEvents()

        # The NameManager thread emits all the names to its names_signal.
        # We have to process this event as well!
        self.app.processEvents()

        # There must be a better way
        assert self.main_window.names_list.count() == 2

    def testRestoreListBetter(self):
        """
        Now we just keep processing events until we run out of work to do.
        Then we should have a deterministic state that we can test.
        :return:
        """
        self.main_window.name_text.setText('Ryan')
        self.main_window.submit_button.click()

        self.main_window.name_text.setText('Meg')
        self.main_window.submit_button.click()

        assert self.main_window.names_list.count() == 2

        self.main_window.clear_list_button.click()
        assert self.main_window.names_list.count() == 0

        # Simulate our restore button click
        self.main_window.restore_list_button.click()

        # While there is work to do, do it.
        while self.app.hasPendingEvents():
            self.app.processEvents()

        # Now let's see what our state is
        assert self.main_window.names_list.count() == 2