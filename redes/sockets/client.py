import socket


class Client:
    def __init__(self):
        self.address = ('localhost', 2000)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init_connection()
        self.send_message()

    def init_connection(self):
        self.client_socket.connect(self.address)

    def close_connection(self):
        self.client_socket.close()
        print('Close connection! \n')

    def send_message(self):
        while True:
            message = input('Type the message: ')
            self.client_socket.send(message.encode())
            print('Message send with success!\n')

            if message == 'exit':
                self.close_connection()
                break


Client()