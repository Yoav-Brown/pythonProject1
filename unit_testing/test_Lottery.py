from unittest import TestCase, mock
from unittest.mock import patch
from Lottery import Lottery


class TestLottery(TestCase):
    def setUp(self):
        self.myloto = Lottery()
        # self.myloto.rand_numbers()
        # print('num are',self.myloto.)


    def test_rand_numbers(self):
        self.assertTrue(len(self.myloto.rand_numbers())==6)

    @mock.patch('Lottery.Lottery.rand_numbers', return_value =[1,2,3,4,4,5])
    def test_valid_numbers_false(self,mock_rand_numbers):
        # print(self.myloto.rand_numbers())
        # print(self.myloto.numbers)
        print(self.myloto.rand_numbers())
        self.assertFalse(self.myloto.valid_numbers())


    def test_valid_range(self):
        with patch('Lottery.Lottery.rand_numbers') as mock_rand_numbers_outofrange:
            mock_rand_numbers_outofrange.return_value = [47, 3, 4, 6, 7, 8]
            print(mock_rand_numbers_outofrange.return_value)
            self.assertFalse(self.myloto.valid_range())

            mock_rand_numbers_outofrange.return_value= [-8,3,45,6,7,3]
            print(mock_rand_numbers_outofrange.return_value)
            self.assertFalse(self.myloto.valid_range())

            mock_rand_numbers_outofrange.return_value= [5,8,3,0,3,24]
            print(mock_rand_numbers_outofrange.return_value)
            self.assertFalse(self.myloto.valid_range())


