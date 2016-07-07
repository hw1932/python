import unittest

class ArithTest(unittest.TestCase):
    def runTest(self):
        ''' Test addition and succed. '''
        self.failUnless(1+1==2, 'one plus one fails')
        self.failIf(1+1 !=2, 'one plus one fails again!')
        self.failUnlessEqual(1+1, 2, 'more trouble with one plus one')

def suite(self):
    suite = unittest.TestCase()
    suite.addTest(ArithTest())
    return suite


def assert0():
    broken_int = 0
    try:
        assert type(broken_int)==type(''),'broken_int is broken'
    except AssertionError:
        print('handle the error here')

if __name__ == '__main__':
    #assert0()
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)