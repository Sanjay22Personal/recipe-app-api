'''
Module is created for performing simple test case.
'''

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    '''test the calc module'''

    def test_add_numbers(self):
        '''Test adding number together.'''
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
