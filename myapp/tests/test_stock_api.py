from django.test import TestCase
from datetime import datetime
from myapp.exceptions.stock_service import StockServerUnReachable, StockSymbolNotFound, InvalidTimeRange
from myapp.stock_api import get_stock_info, get_stock_historic_prices, get_top_stocks


MAX_DAYS_PER_MONTH = 31
MAX_DAYS_PER_YEAR = 366  # On a leap year


class StockApiTestCase(TestCase):

    def setUp(self):
        self.existed_symbols = ['AAL', 'WFC', "DFS"]
        self.not_existed_symbols = ['kamal', 'murad', 'malak']

        self.valid_time_ranges = ['1d', '5d', '1m', '3m', '6m', '1y', '5y']
        self.invalid_time_ranges = ['1x', '42z', 'rt', 'test']


    def test_service_is_up(self):
        try:
            get_stock_info(self.existed_symbols[0])
        except StockServerUnReachable as e:
            raise AssertionError(e)


    def test_get_stock_info(self):
        for symbol in self.not_existed_symbols:
            self.assertRaises(StockSymbolNotFound, get_stock_info, symbol)
        for symbol in self.existed_symbols:
            response = get_stock_info(symbol)
            self.assertIsInstance(response, dict)


    def test_get_stock_historic_prices_symbol(self):
        for symbol in self.not_existed_symbols:
            self.assertRaises(StockSymbolNotFound, get_stock_historic_prices, symbol)
        for symbol in self.existed_symbols:
            response = get_stock_historic_prices(symbol)
            self.assertIsInstance(response, list)


    def test_get_stock_historic_prices_time(self):
        for time_range in self.valid_time_ranges:
            response = get_stock_historic_prices(self.existed_symbols[0], time_range)

            first_date = datetime.fromisoformat(response[0].get('date'))
            final_date = datetime.fromisoformat(response[-1].get('date'))
            days_in_range = (final_date - first_date).days

            if time_range == '1d':
                self.assertEquals(days_in_range, 0)

            elif time_range == '5d':
                self.assertLessEqual(days_in_range, 7)

            elif time_range.endswith('m'):
                self.assertLessEqual(days_in_range, 
                                    int(time_range[0]) * MAX_DAYS_PER_MONTH)

            elif time_range.endswith('y'):
                self.assertLessEqual(days_in_range, 
                                    int(time_range[0]) * MAX_DAYS_PER_YEAR)

            today = datetime.today().day
            days_since_last_result = (datetime.today() - final_date).days
            self.assertLessEqual(days_since_last_result, 3)

        for time_range in self.invalid_time_ranges:
            self.assertRaises(InvalidTimeRange, get_stock_historic_prices,
                              self.existed_symbols[0], time_range)


    def test_get_top_stocks(self):
        response = get_top_stocks()
        self.assertIsInstance(response, list)
