import unittest
from card import Card

class TestMemoryCalculator(unittest.TestCase):
  def test_card_initialization(self):
    card = Card(2, 'S')
    self.assertEqual(2, card.rank)
    self.assertEqual('S', card.suit)

  def test_card_equal(self):
    card1 = Card(2, 'S')
    card2 = Card(2, 'H')
    self.assertEqual(True, card1 == card2)

  def test_card_notEqual(self):
    self.assertEqual(False, Card(2, 'S') != Card(2, 'H'))
    self.assertEqual(True, Card(3, 'S') != Card(2, 'H'))

  def test_card_lessThan(self):
    self.assertEqual(False, Card(14, 'S') < Card(11, 'H'))
    self.assertEqual(True, Card(1, 'S') < Card(14, 'H'))

  def test_card_greaterThan(self):
    self.assertEqual(False, Card(2, 'S') > Card(2, 'H'))
    self.assertEqual(True, Card(3, 'S') > Card(2, 'H'))

  def test_card_greaterOrEqual(self):
    self.assertEqual(False, Card(8, 'S') >= Card(11, 'H'))
    self.assertEqual(True, Card(3, 'S') >= Card(3, 'D'))
    self.assertEqual(True, Card(8, 'S') >= Card(7, 'H'))
    
  def test_stringify_cards(self):
    self.assertEqual("JS", str(Card(11, 'S')))
    self.assertEqual("AC", str(Card(14, 'C')))
    self.assertEqual("8C", str(Card(8, 'C')))