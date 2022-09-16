import requests
import os

def yandex_creat_folder(token: str, name_folder: str):
    host = "https://cloud-api.yandex.net"
    url = host+"/v1/disk/resources"
    headers = {"Content-Type": "application/json",
               "Authorization": f"OAuth {token}",
               }
    params = {"path": name_folder}
    responce = requests.put(url, params=params, headers= headers)
    # print(responce.status_code)
    if responce.status_code == 201:
        return (name_folder)
    return responce.status_code

