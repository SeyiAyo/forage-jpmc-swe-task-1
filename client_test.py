import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (bid_price + ask_price) / 2
      self.assertEqual(price, expected_price)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (bid_price + ask_price) / 2
      self.assertEqual(price, expected_price)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    from client3 import getRatio
    self.assertEqual(getRatio(120.48, 119.2), 120.48 / 119.2)
    self.assertIsNone(getRatio(120.48, 0))
    self.assertEqual(getRatio(0, 119.2), 0)
    self.assertEqual(getRatio(119.2, 119.2), 1)


if __name__ == '__main__':
    unittest.main()
