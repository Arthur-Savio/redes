import socket
from threading import Thread


class Server:
    def __init__(self):
        self.address = ('localhost', 2000)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None
        self.client = None
        self.message = None
        self.threads = list()
        self.init_server()

    def init_server(self):
        print('Initializing server...')
        self.server_socket.bind(self.address)
        self.server_socket.listen(1)
        print('Server is initialized with success! \n')
        self.create_thread()

    def create_thread(self):
        new_thread = Thread(target=self.accept_connection())
        self.threads.append(new_thread)
        print('test')
        print(len(self.threads))
        new_thread.start()

    def accept_connection(self):
        self.connection, self.client = self.server_socket.accept()
        print('Connected by: ', self.client)
        self.receive_message()

    def close_server(self):
        self.server_socket.close()
        print('Serve Stopped! \n')

    def receive_message(self):
        try:
            while True:
                self.message = self.connection.recv(1024)
                self.message = self.message.decode()
                self.message.rstrip()

                if self.message == 'exit':
                    self.close_server()
                    break
                else:
                    print('Received message: ', self.message)
        except:
            self.close_server()

Server()