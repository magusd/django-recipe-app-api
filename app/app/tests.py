"""
sample tests
"""

from django.test import SimpleTestCase
from . import calc

class AppTestCase(SimpleTestCase):
    def test_calc(self):
        self.assertEquals(calc.add(1, 2), 3)