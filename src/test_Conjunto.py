import unittest
from Conjunto import Conjunto

class ConjuntoTest(unittest.TestCase):
    def setUp(self):
        self.set1 = Conjunto(3, "A")
        self.set2 = Conjunto(3, "B")

    def test_add(self):
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.assertEqual(str(self.set1), "[[3], [1], [2]]")

    def test_remove(self):
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.set1.remove(2)
        self.assertEqual(str(self.set1), "[[1], [3], []]")

    def test_contains(self):
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.assertTrue(self.set1.contains(2))
        self.assertFalse(self.set1.contains(4))

    def test_union(self):
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.set2.add(3)
        self.set2.add(4)
        self.set2.add(5)
        union_set = self.set1.union(self.set2)
        self.assertEqual(str(union_set), "[[1, 2, 3, 4, 5], [], []]")

    def test_complemento(self):
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.set2.add(3)
        self.set2.add(4)
        self.set2.add(5)
        complemento_set = self.set1.complemento(self.set2)
        self.assertEqual(str(complemento_set), "[[1, 2], [], []]")

if __name__ == '__main__':
    unittest.main()