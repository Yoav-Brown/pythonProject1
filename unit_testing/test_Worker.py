from unittest import TestCase,mock
from unittest.mock import patch
from Worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.yoav=Worker('yoav','smith', 2000,6,14,'tel_aviv','australia')
        self.yoavnotborn=Worker('yoav','smith', 2023,6,14,'tel_aviv','australia')
        self.yoavborntoday=Worker('yoav','smith', 2022,4,13,'tel_aviv','australia')
    def test_full_name(self):
        with patch('Worker.Worker.__init__') as mocked_init:
            mocked_init.return_value.name='yoav smith'
            print(mocked_init.return_value.name)
            self.assertTrue(self.yoav.full_name()==mocked_init.return_value.name)

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

    # def test_location_url(self):



    def test_location_responce_ok(self):
        with patch('Worker.requests.get') as mock_requests_get_ok:
            mock_requests_get_ok.return_value.ok=True
            mock_requests_get_ok.return_value.text='good responce'
            self.assertTrue(self.yoav.location()=='good responce')
            print(self.yoav.location())


    def test_location_responce_notok(self):
        with patch('Worker.requests.get') as mock_requests_get_notok:
            mock_requests_get_notok.return_value.ok=False
            print(self.yoav.location())
            self.assertTrue(self.yoav.location()=='Bad response!')
