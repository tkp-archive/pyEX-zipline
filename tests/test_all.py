# for Coverage
from datetime import datetime
from mock import patch, MagicMock
import pyEXzipline


class TestAll:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_all(self):
        from pyEXzipline import load_from_iex
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock()
            mock.return_value.json.return_value = [{'open':1, 'close':1, 'high':1, 'low':1, 'volume':1, 'date':'2017-1-1'}]
            load_from_iex('aapl', datetime(2017, 1, 1), datetime(2017, 2, 1))
