from Client0 import Client

IP = "212.128.255.71"
PORT = 8080

for i in range(5):

    c = Client(IP, PORT)

    message = f"Message {i}"

    response = c.talk(message)

    print(f"To Server: {message}")
    print(f"From Server: {response}\n")
