import unittest
from cards import Card, EmptyDeck, ClassicDeck


class TestCards(unittest.TestCase):

    def setUp(self) -> None:
        self.card = Card("♥", "K", 10)

    def test_init_values(self):
        self.assertEqual(self.card.suit, "♥")
        self.assertEqual(self.card.symbol, "K")
        self.assertEqual(self.card.value, 10)
        self.assertEqual(self.card.face_up, True)

    def test_update_ace_values_non_ace(self):
        for i in range(5):
            with self.subTest(i=i):
                self.card.update_ace_value()
                self.assertEqual(self.card.value, 10)

    def test_update_ace_values_ace_once(self):
        self.card = Card("♥", "A", 11)
        self.card.update_ace_value()
        self.assertEqual(self.card.value, 1)

    def test_update_ace_values_ace_twice(self):
        self.card = Card("♥", "A", 11)
        self.card.update_ace_value()
        self.card.update_ace_value()
        self.assertEqual(self.card.value, 11)

    def test_flip_face_once(self):
        self.card.flip_face()
        self.assertEqual(self.card.face_up, False)

    def test_flip_face_twice(self):
        self.card.flip_face()
        self.card.flip_face()
        self.assertEqual(self.card.face_up, True)

    def test_str_normal(self):
        self.assertEqual(str(self.card), "[♥ K]")

    # def test_str_normal(self):
    #     self.assertEqual(str(self.card), "[♥ K]")


if __name__ == '__main__':
    unittest.main()
