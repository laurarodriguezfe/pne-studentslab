from Client0 import Client

print(f"-----| Practice 2, Exercise 1 |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
c.ping()
