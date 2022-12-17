'''sample tests '''
from django.test import SimpleTestCase

from app import calc


class calcTests(SimpleTestCase):
    '''Test the calc function'''

    def test_calc(self):
        '''test adding number together'''
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        ''' test subtracting numbers together'''
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
