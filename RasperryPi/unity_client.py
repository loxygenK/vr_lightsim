# -*- coding:utf-8 -*-
import socket
import struct
import sys

host = "" #お使いのサーバーのホスト名を入れます
port = 0#適当なPORTを指定してあげます
buffer_size = 1024

def LightUp():

    with open("socket_info.txt", mode="r") as f:
        raw_socket_info = f.readlines()

    host = raw_socket_info[0].replace("\n","")
    port = int(raw_socket_info[1].replace("\n",""))

    print("Will connect to " + host + ":" + str(port) + ".")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

    client.connect((host, port)) #これでサーバーに接続します

    massage = 1
    massage2 = struct.pack('>i',massage)
    client.send(massage2) #適当なデータを送信します（届く側にわかるように）

    response = client.recv(buffer_size)

    print(response)

    sys.exit()
    
def LightDown():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

    client.connect((host, port)) #これでサーバーに接続します

    massage = 0
    massage2 = struct.pack('>i',massage)
    client.send(massage2) #適当なデータを送信します（届く側にわかるように）

    response = client.recv(buffer_size)

    print(response)

    sys.exit()

LightUp()
    
    

    
