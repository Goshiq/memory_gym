from unittest import TestCase

from db.DataBase import DB


class TestDB(TestCase):

    def test_get_top_five_no_data(self):
        db = DB()
        self.assertEqual(0, len(db.get_top_five()))

    def test_write_result_and_get_top_five(self):
        db = DB()
        db.write_result("Petya", 10)
        self.assertEqual(1, len(db.get_top_five()))

    def test_sorted_insert(self):
        db = DB()
        vasya = "Vasya", 100
        masha = "Masha", 200
        db.write_result(*vasya)
        db.write_result(*masha)
        top = db.get_top_five()
        self.assertEqual(2, len(top))
        self.assertEqual(masha[0], top[0][1])
        self.assertEqual(masha[1], top[0][0])

