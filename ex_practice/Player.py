import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

termcolor.cprint("--Welcome to the Number Guessing Game!--", "yellow")

game_over = False

while not game_over:
    try:
        user_input = input("\nEnter your guess(0-100):")