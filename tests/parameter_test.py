import unittest
from parameter_verification import ParameterError, verify_params

pass_params = [
    {'param1': ('abc', str)},
    {'param1': ('abc', str, '=abc')},
    {'param1': ('abc', str, 'len=3')},
    {'param1': ('abc', str, 'len=3', '=abc')},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123.0, float)},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123.0, float, '>=100', '<150')},
]

fail_params = [
    {'param1': ('abc', KeyboardInterrupt)},
    {'param1': ('abc', str, '=abcd')},
    {'param1': ('abc', str, 'len=4')},
    {'param1': ('abc', str, 'len=3', '=abcd')},
    {'param1': ('abc', str, 'len=4', '=abcd')},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123, int, 'len=4')},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123.0, float, '=100')},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123.0, float, '<100')},
    {'param1': ('abc', str, 'len=3', '=abc'), 'param2': (123.0, float, '>100', '<110')},
]

class ParamVerifyTests(unittest.TestCase):
    ''' Test caes for the parameter verification '''
    def test_1_pass_tests(self):
        ''' test parameters that should all pass '''
        for params in pass_params:
            self.assertTrue(verify_params(**params))

    def test_2_fail_tests(self):
        ''' test parameters that should fail (one or more non-match parameters) '''
        for params in fail_params:
            self.assertRaises(ParameterError, verify_params, **params)

    def test_3_test_no_raise(self):
        ''' Tests returning False rather than raising an error '''
        for params in fail_params:
            self.assertFalse(verify_params(no_raise=True, **params))

def run_test():
    unittest.main()

if __name__ == '__main__':
    run_test()
