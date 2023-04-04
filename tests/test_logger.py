import unittest
from unittest.mock import patch
from logging_tool.src.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger('test_logger')

    def test_debug(self):
        with patch('logging.Logger.debug') as mocked_debug:
            self.logger.debug('debug message')
            mocked_debug.assert_called_with('debug message')

    def test_info(self):
        with patch('logging.Logger.info') as mocked_info:
            self.logger.info('info message')
            mocked_info.assert_called_with('info message')

    def test_warning(self):
        with patch('logging.Logger.warning') as mocked_warning:
            self.logger.warning('warning message')
            mocked_warning.assert_called_with('warning message')

    def test_error(self):
        with patch('logging.Logger.error') as mocked_error:
            self.logger.error('error message')
            mocked_error.assert_called_with('error message')

if __name__ == '__main__':
    unittest.main()
