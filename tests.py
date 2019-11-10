import unittest
import box


class TestBox(unittest.TestCase):

    def test_box_dimensions_too_small(self):
        with self.assertRaises(ValueError):
            box.box(-1, -1)
        with self.assertRaises(ValueError):
            box.box(0, 0)
        with self.assertRaises(ValueError):
            box.box(1, 1)
        with self.assertRaises(ValueError):
            box.box(10, 1)
        with self.assertRaises(ValueError):
            box.box(1, 10)
        with self.assertRaises(ValueError):
            box.box(-2, -2)

    def test_box(self):
        self.assertEqual(box.box(2, 2), '┌┐\n└┘')
        self.assertEqual(box.box(2, 4), '┌┐\n||\n||\n└┘')
        self.assertEqual(box.box(4, 2), '┌--┐\n└--┘')
        self.assertEqual(box.box(4, 4), '┌--┐\n|  |\n|  |\n└--┘')
        self.assertEqual(box.box(3, 2), '┌-┐\n└-┘')
        self.assertEqual(box.box(2, 3), '┌┐\n||\n└┘')
        self.assertEqual(box.box(10, 2), '┌--------┐\n└--------┘')
        self.assertEqual(
            box.box(10, 4), '┌--------┐\n|        |\n|        |\n└--------┘')


if __name__ == '__main__':
    unittest.main()
