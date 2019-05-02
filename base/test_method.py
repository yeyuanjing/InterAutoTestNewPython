from demo import RunMain
import unittest

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {'secrect': '8c12a788038a2671b5e0a8a6dc30673d',
                'timestamp': '1530084524251',
                'token': '755ce48a29737df0287a029c7ede5fe5',
                'uid': '5409699'
                }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        print(13423234)

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {'secrect': '8c12a788038a2671b5e0a8a6dc30673d',
                'timestamp': '1530084524251',
                'token': '755ce48a29737df0287a029c7ede5fe5',
                'uid': '5409699'
                }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        print(2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest('test_01')
    suite.addTest('test_02')
    unittest.TextTestRunner(verbosity=2).run(suite)

