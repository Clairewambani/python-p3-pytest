import unittest
from not_none_functions import return_not_none

class TestNotNoneFunctions(unittest.TestCase):
    def test_return_not_none(self):
        '''In the not_none_functions module, the function "return_not_none" returns a value that is not None.'''
        result = return_not_none()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()