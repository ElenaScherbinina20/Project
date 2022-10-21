import unittest
import requests

base_url = "https://paymatrix.net"  # базовая url

post_resource = "/api/support/new"  # Ресурс метода POST

json_body = {

            "phone":"79994544022",
            "telegram_username":"@Albookerka",
            "token": {
              "date": 1665943913,
              "key": "ddc6a76079772408c449e04ae0e817265346f2b8",
              "phone": "79045840415",
              "hight_right": "1",
              "signature": "95d6d24573ccc3a0eab91a29efd4451c8a69a22dbe5230c3335116e17b1af0c72b82afc96127af0a99993a6239162f1e"
}
     }

post_url = base_url + post_resource
response = requests.post(post_url, json = json_body)
check_post = response.json()

class TestMain(unittest.TestCase):
    def test_getRequest(self):
        self.assertEqual(response.status_code, 200)

    def test_phone(self):
        check_phone = check_post.get("phone")
        self.assertEqual(response.check_phone, "79994544022")

    def test_username(self):
        check_username = check_post.get("telegram_username")
        self.assertEqual(response.check_username, "@Albookerka")

if __name__ == "__main__":
    unittest.main()
