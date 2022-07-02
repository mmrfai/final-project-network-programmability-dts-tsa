# Import library yang dibutuhkan
import json
import requests
from time import *

# Menambahkan base_url, serta autentikasi user dan password untuk masuk ke website sdn
base_url = "http://localhost:58000/api/v1"
user = "cisco"
password = "sdncisco"

# Fungsi untuk mendapatkan ticket rest API
def get_ticket():
    # Menentukan header dan data yang dibutuhkan untuk login
    headers = {"content-type": "application/json"}
    data = {"username": user, "password": password}

    # Membaut wadah untuk melakukan requests post untuk meminta ticket dalam bentuk json
    response = requests.post(base_url+"/ticket", headers=headers, json=data)
    ticket = response.json()
    # Parsing data untuk mendapatkan ticket
    print('Berhasil mendapatkan ticket')
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

if __name__ == "__main__":
    print("===================================================================================")
    print("==============MONITORING JARINGAN MENGGUNAKAN SDN CONTROLLER REST API==============")
    print("===================FINAL PROJECT DTS-TSA NETWORK PROGRAMMABILITY===================")
    print("========================MUHAMAMD MA'RUF NUR RIFAI/1910501038=======================")
    print("===================================================================================")
    print("Kode REST API : " + get_ticket())

