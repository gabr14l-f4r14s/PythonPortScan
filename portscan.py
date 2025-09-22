#!/usr/bin/python3
import socket,sys

VERDE = "\033[92m"
RESET = "\033[0m"

if len(sys.argv) <2 :
	print("Modo de uso: python3 porstscan.py 192.168.0.1")
else:
	for porta in range (1, 65535):
		meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		meusocket.settimeout(0.5)
		if meusocket.connect_ex((sys.argv[1],porta)) == 0:
			print(f"{VERDE}Porta {porta} [ABERTA]{RESET}")
		meusocket.close()
