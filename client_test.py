import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quotes_results = []
    expected_results = [
      ('ABC', 120.48, 121.2, 120.84),
      ('DEF', 117.87, 121.68, 119.775)
    ]

    for quote in quotes:
        quotes_results.append(getDataPoint(quote))
    self.assertEqual(quotes_results, expected_results)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quotes_results = []
    expected_results = [
      ('ABC', 120.48, 119.2, 119.84),
      ('DEF', 117.87, 121.68, 119.775)
    ]

    for quote in quotes:
        quotes_results.append(getDataPoint(quote))
    self.assertEqual(quotes_results, expected_results)

  """ ------------ Add more unit tests ------------ """


  def test_getRatio_calculateRatio(self):
    prices = [
      {'price_a': 1, 'price_b': 1},
      {'price_a': 3, 'price_b': 4},
      {'price_a': 10, 'price_b': 2}
    ]
    """ We testing for normal calculations, if the numbers the same, if A is smaller, and if B is smaller"""
    prices_results = []
    expected_p_results = [1.0, 0.75, 5.0]
    for i in prices:
        prices_results.append(getRatio(i['price_a'], i['price_b']))

    self.assertEqual(prices_results, expected_p_results)


  def test_getRatio_calculateRatio(self):
    price_a = 1
    price_b = 0

    """ We are now testing for the one special case, which is when the price b is 0 there should be nothing returned"""
    self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
    unittest.main()
