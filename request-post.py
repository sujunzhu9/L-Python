import requests
#
# # -----------------------------------------------------------
# # get请求 example 1
# # r=requests.get("https://www.httpbin.org/get?id=1&name=one")
# # print(r.text)
#
# # ----------------------------------------------------------
# #  get请求 example 2
# # data = {
# #     "name": "two",
# #     "id": 2
# # }
# # r = requests.get("https://httpbin.org/get", params=data)
# # print(r.json())
#
# # ----------------------------------------------------------
# # post请求 example 1
# # data = {
# #     "name": "three",
# #     "id": 3
# # }
# # r=requests.post("https://httpbin.org/post",data=data)
# # print(r.text)
#
#
# # ----------------------------------------------------------
# # post请求 example 2
# # data = {"firstName": "Duke", "lastName": "Java", "age": 18, "streetAddress": "100 Internet Dr", "city": "JavaTown",
# #         "state": "JA", "postalCode": "12345", "phoneNumbers": [{"Mobile": "111-111-1111"}, {"Home": "222-222-2222"}]}
# #
# # url = "https://httpbin.org/post"
# #
# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#
# r = requests.post(url, data=data, headers=headers)
#
# print(r.text)
# print(r.json())

Token1 = "yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9eyJkZWhvb3B1c2VyaWQiOiIzNTI0MjQ2MzQ0MzM0MDQ5MjgiLCJleH"
Token2 = "AiOjE2NjIwOTE4NTEsImlhdCI6MTY2MTgzMjY1MX04Lr6CayDrBOTN7DnlX6-smhjtfamp6bLORPYLwkps7ygry3"
Token3 = "n35BxqCVvf-CIYMAY0RjAF6dRwQn0iaPYjEuiow"
Token=Token1+Token2+Token3
data = '{"page": 1, "pageSize": 10, "searchWord": "aaaa"}'
header = {
    'Accept': 'application/json, text/plain',
    'Accept-Language': 'zh-CN',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cache-Control': 'no-cache',
    'DNT': '1',
    'Origin': 'http://dehoop-dev.definesys.cn',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://dehoop-dev.definesys.cn/',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 "
                  "Safari/537.36 Edg/104.0.1293.70",
    'dehooptoken': Token}
data = {"page": 1, "pageSize": 10, "searchWord": ""}
r = requests.request("post",'http://www.httpbin.org/post?',
                  data=data, headers=header)
print(r.text)
# # -------------------------------------------------------------------------------------------------------
# # import requests
# #
# # url = "http://121.89.247.94:30104/dehoop-admin/modeling/queryModelingEntity?timestamp=1661840117838"
# #
# # payload = "{\"page\":1,\"pageSize\":10,\"searchWord\":\"\"}"
# # headers = {
# #     'DNT': '1',
# #     'Pragma': 'no-cache',
# #     'Proxy-Connection': 'keep-alive',
# #     'dehooptoken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9'
# #                    '.eyJkZWhvb3B1c2VyaWQiOiIzNTI0MjQ2MzQ0MzM0MDQ5MjgiLCJleHAiOjE2NjIwOTE4NTEsImlhdCI6MTY2MTgzMjY1MX0'
# #                    '.4Lr6CayDrBOTN7DnlX6-smhjtfamp6bLORPYLwkps7ygry3n35BxqCVvf-CIYMAY0RjAF6dRwQn0iaPYjEuiow',
# #     'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
# #     'Content-Type': 'application/json;charset=UTF-8'
# # }
# #
# # response = requests.post(url, headers=headers, data=payload)
# #
# # print(response.text)
