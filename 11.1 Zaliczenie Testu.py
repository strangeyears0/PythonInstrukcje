
import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """"Testy dla programu 'name_function.py"""

    def test_first_last_name(self):
        """Czy dane w postaci Janis Joplin są obsługiwane prawidłowo?"""
        formatted_name = get_formated_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()