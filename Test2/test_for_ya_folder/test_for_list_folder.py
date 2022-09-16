import unittest
import requests
from parameterized import parameterized
from yandex_folder import *

class TestFuncs(unittest.TestCase):

    @parameterized.expand(
        [
            ("Photos",),
            ("Music",),
            ("Movies",),
        ]
    )
    def test_yandex_creat_folder(self, PATH):
        TOKEN = ""
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {"Content-Type": "application/json",
                   "Authorization": f"OAuth {TOKEN}",
                   }
        yandex_creat_folder(TOKEN, PATH)
        responce = requests.get(url, params={"path": PATH}, headers=headers)
        self.assertEqual(responce.status_code, 200)