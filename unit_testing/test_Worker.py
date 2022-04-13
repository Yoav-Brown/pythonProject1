from unittest import TestCase
from Worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.yoav=Worker('yoav','smith', 2000,6,14,'tel_aviv','australia')
        self.yoavnotborn=Worker('yoav','smith', 2023,6,14,'tel_aviv','australia')
        self.yoavborntoday=Worker('yoav','smith', 2022,4,13,'tel_aviv','australia')
    def test_full_name(self):

        self.assertTrue(self.yoav.full_name()=='yoav smith')

    def test_age_normal(self):
        self.assertIn('22',self.yoav.age())

    def test_age_not_born(self):
        self.assertFalse(self.yoavnotborn.age())

    def test_age_born_today(self):
        self.assertIn('0', self.yoavborntoday.age())

    def test_days_to_birthday_bigger(self):
        self.yoavbigger = Worker('yoav', 'smith', 2000, 4, 14, 'tel_aviv', 'australia')
        self.assertIn('1',self.yoavbigger.days_to_birthday())

    def test_days_to_birthday_smaller(self):
        self.yoavsmaller = Worker('yoav', 'smith', 2000, 3, 12, 'tel_aviv', 'australia')
        self.assertIn('333', self.yoavsmaller.days_to_birthday())

    # def test_greet(self):
    #     self.fail()
