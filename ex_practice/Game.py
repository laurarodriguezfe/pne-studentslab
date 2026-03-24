import random
import socket

class NumberGuesser:
    def __init__(self, secret_number):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        n = int(number)
        self.attempts.append(n)
        if n == self.secret_number:
            return (f"You won after {len(self.attempts)} attempts")
        elif number < self.secret_number:
            return "Higher"
        elif number > self.secret_number:
            return "Lower"

IP = "127.0.0.1"
PORT = 8080
my_game = NumberGuesser()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((IP, PORT))
    server_socket.listen(5)
    print("---Server ready in port 8080---")

    while True:
        (clientsocket, adress) = server_socket.accept()
        data = clientsocket.recv(2048)
        if data:
            msg = data.decode("utf-8").strip()
            received_number = int(msg)
            answer = my_game.guess(received_number)
            clientsocket.send(answer.encode("utf-8"))
            print("Attempt to " + str(address) + ": " + str(received_number))
        clientsocket.close()
except socket.error:
    print("Error: The port 8080 is already being used")
except KeyboardInterrupt:
    print("\nServer stopped")
    server_socket.close()