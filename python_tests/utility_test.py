import unittest

# from simple_add import addition

# import utils
import simple_add


# all python tests starts with "test_"

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)  # add assertion here

    @classmethod
    def tearDownClass(cls) -> None:
        print("i run always")

    @classmethod
    def setUpClass(cls) -> None:
        print("Run once")

    def setUp(self) -> None:
        print("I run before any case test")

    def tearDown(self) -> None:
        print("I run after every test case")

    def test_something(self) -> None:
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEquals(12, simple_add.addition(3, 9))

    def test_lis(self):
        self.assertEqual([1, 4, 9], simple_add.square_list([1, 2, 3]))

    # def test_Errors(self) -> None:
    #     with self.assertRaiseRegex(TypeError, str) as e:
    #         self.assertRaiseRegex("anything", simple_add.addition("4", 2))
    #
    # # def assertRaiseRegex(self, param, param1):
    # #     pass


if __name__ == '__main__':
    unittest.main()
