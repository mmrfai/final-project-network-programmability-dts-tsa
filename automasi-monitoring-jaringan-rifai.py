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
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

# Fungsi untuk menghitung managed device yang terdeteksi/terkoneksi
def get_network_device_count():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/network-device/count", headers=headers)
    managed_device_count = response.json()
    print("Total Managed Device :", managed_device_count["response"])

# Fungsi untuk mendapatkan list managed network device yang terkoneksi dengan SDN
def get_network_device():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/network-device", headers=headers)
    managed_device = response.json()
    networkDevices = managed_device["response"]

    for networkDevice in networkDevices:
        print(networkDevice["hostname"], "\t\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])

if __name__ == "__main__":
    print("===================================================================================")
    print("==============MONITORING JARINGAN MENGGUNAKAN SDN CONTROLLER REST API==============")
    print("===================FINAL PROJECT DTS-TSA NETWORK PROGRAMMABILITY===================")
    print("========================MUHAMAMD MA'RUF NUR RIFAI/1910501038=======================")
    print("===================================================================================")
    print('Berhasil mendapatkan ticket')
    print("Kode REST API : " + get_ticket())
    get_network_device_count()
    print("Hostname \t Platform \t IPAddress")
    get_network_device()
    

