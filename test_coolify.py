import unittest
import coolify as cl

class Test_coolify(unittest.TestCase):
    def test_name(self):
        name="Jash"
        self.assertTrue(cl.coolify(name)=="Jash is cool")
        self.assertFalse(cl.coolify(name)=="Jash")
if __name__ == '__main__':
    unittest.main()