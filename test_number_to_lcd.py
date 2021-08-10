import unittest
from number_to_lcd import NumberToLcd

class TestNumberToLcd(unittest.TestCase):

  def test_one(self):
    one = \
"""
   
  |
  |
"""
    self.assertEqual(NumberToLcd().run(1), one)

  def test_two(self):
    two = \
"""
 _ 
 _|
|_ 
"""
    self.assertEqual(NumberToLcd().run(2), two)

  def test_twelve(self):
    twelve = \
"""
    _ 
  | _|
  ||_ 
"""
    self.assertEqual(NumberToLcd().run(12), twelve)

  def test_one_to_zero(self):
    one_to_zero = \
"""
    _  _     _  _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|| |
  ||_  _|  | _||_|  ||_| _||_|
"""
    self.assertEqual(NumberToLcd().run(1234567890), one_to_zero)

  def test_big_two(self):
    big_two = \
"""
 ___ 
    |
 ___|
|    
|___ 
"""
    self.assertEqual(NumberToLcd(2,3).run(2), big_two)

  def test_big_twenty_seven(self):
    big_twenty_seven = \
"""
 ___  ___ 
    |    |
 ___|    |
|        |
|___     |
"""
    self.assertEqual(NumberToLcd(2,3).run(27), big_twenty_seven)

  def test_big_one_to_zero(self):
    big_twenty_seven = \
"""
      ___  ___       ___  ___  ___  ___  ___  ___ 
    |    |    ||   ||    |        ||   ||   ||   |
    | ___| ___||___||___ |___     ||___||___||   |
    ||        |    |    ||   |    ||   |    ||   |
    ||___  ___|    | ___||___|    ||___| ___||___|
"""
    self.assertEqual(NumberToLcd(2,3).run(1234567890), big_twenty_seven)

  def test_really_big_eight(self):
    really_big_eight = \
"""
 ______ 
|      |
|      |
|      |
|______|
|      |
|      |
|      |
|______|
"""
    self.assertEqual(NumberToLcd(4,6).run(8), really_big_eight)

if __name__ == '__main__':
    unittest.main()
