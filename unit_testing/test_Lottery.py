from unittest import TestCase
from Lottery import Lottery
class TestLottery(TestCase):
    def test_rand_numbers(self):
        mylotto=Lottery()
        self.assertTrue(mylotto.valid_numbers())

    def test_valid_numbers(self):
        mylotto=Lottery()
        self.assertTrue(len(se))
    def test_valid_range(self):
        self.fail()
