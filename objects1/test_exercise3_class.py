from unittest import TestCase,mock
from unittest.mock import patch
from exercise3_class import person

class Testperson(TestCase):
    def setUp(self):
        self.yoav=person('yoav',21,2)
        self.yoavnochild=person('yoav',21,0)
    def test_haschildren_with(self):
        self.assertTrue(self.yoav.haschildren())

    def test_haschildren_without(self):
        self.assertFalse(self.yoavnochild.haschildren())

    def test_agegroup(self):
        self.assertTrue(self.yoav.agegroup()=='Adult')
