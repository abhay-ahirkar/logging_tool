import unittest
from unittest.mock import patch
from logging_tool.src.error_catcher import error_catcher

class TestErrorCatcher(unittest.TestCase):
    def test_error_catcher(self):
        with patch('builtins.print') as mocked_print:
            error_catcher()
            mocked_print.assert_called_with('Error caught!')

if __name__ == '__main__':
    unittest.main()
