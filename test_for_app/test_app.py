import unittest
from parameterized import parameterized
from app import *

class TestFunctions(unittest.TestCase):

    @parameterized.expand(
        [
            ("11-2", "Геннадий Покемонов"),
            ("4572", None)
        ]
    )
    def test_get_doc_owner_name(self, a, res):
        result = get_doc_owner_name(a)
        self.assertEqual(result, res)

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        res = {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}
        self.assertEqual(result, res)

    def test_show_all_docs_info(self):
        res = show_all_docs_info()
        self.assertTrue(res)

    @parameterized.expand(
        [
            ("11-2", "1"),
            ("456.2", None)
        ]
    )
    def test_get_doc_shelf(self, num, res):
        result = get_doc_shelf(num)
        self.assertEqual(result, res)

    @parameterized.expand(
        [
            ("1234", "student ticket", "Tom", "1"),
            ("12345", "permit", "Emma", "2"),
        ]
    )
    def test_add_new_doc(self, ndn, ndt, ndon, ndsn):
        add_new_doc(ndn, ndt, ndon, ndsn)
        for i, doc in enumerate(documents):
            if ndn in doc.values():
                break
        res = ndt == documents[i]["type"] and ndon == documents[i]["name"]
        self.assertTrue(res)

    @parameterized.expand(
        [
            ("1234", True),
            ("12345", True),
            ("100024", False),
        ]
    )
    def test_delete_doc(self, num, res):
        result = delete_doc(num)[1]
        self.assertEqual(result, res)

    @parameterized.expand(
        [
            ("10006", "1"),
            ("11-2", "2"),
        ]
    )
    def test_move_doc_to_shelf(self, doc_num, shelf_num):
        result = move_doc_to_shelf(doc_num, shelf_num)
        self.assertTrue(result)

    @parameterized.expand(
        [
            ("5", True),
            ("2", False),
        ]
    )
    def test_add_new_shelf(self, shelf_num, res):
        result = add_new_shelf(shelf_num)
        self.assertEqual(result, (shelf_num, res))