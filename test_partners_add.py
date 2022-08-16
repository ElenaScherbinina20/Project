import requests

base_url = "https://payment.test.paymatrix.ru"  # базовая url

post_resource = "/api/partners/add"  # Ресурс метода POST

json_for_create_new_connection = {
             "name": "salmon_1111133211333131331111111",
             "gateway": "testTerminal",
             "limit": 0,
             "token": {
                 "date": 1660483191,
                 "key": "ca03227a6ae65b8e2e2f00a069763f5b44f01e7e",
                 "phone": "79994544022",
                 "hight_right": "1",
                 "signature": "9f18ebc1a920aee99b500a76041abbab946bddd8148d72a3b712b3971ffeb1e286dee53f233b50f575cbfef62d7fbde8"
             }
     }
headers = {'Content-Type': 'application/json'}

def test_create_new_connection(base_url, post_resource, headers, json_for_create_new_connection):

    post_url = base_url + post_resource
    print("URL: " + post_url)
    result_post = requests.post(post_url, json=json_for_create_new_connection, headers = headers)
    print(result_post.text)

test_create_new_connection(base_url, post_resource, headers, json_for_create_new_connection)
