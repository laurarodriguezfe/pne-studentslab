from Client0 import Client

print(f"-----| Practice 2, Exercise 3 |------")

IP = "212.128.255.79"
PORT = 8080
c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: \n{response}")