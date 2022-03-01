import socket
import time
import tkinter as tk
from ttkbootstrap import Style
from ReadIniFile import ReadIniFile


class Client:
    @staticmethod
    def run_client(event=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = ''
        with sock:
           while conn == '':
               sock.bind(("localhost", 8888))
               sock.connect((ReadIniFile.read()['ip'], int(ReadIniFile.read()['port'])))
               sock.sendall(Interface.text().get('1.0', tk.END).encode())
               sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
               Interface.text().delete('1.0', tk.END)
               conn = sock.recv(1024)
               print(conn.decode())
               print("RESPOSTA ", conn.decode())
               Interface.textbox.insert('1.0', f"Servidor diz {conn.decode()}")
         # sock.close()


class Interface(tk.Frame):
    container = tk.Frame()
    label = tk.Label(container, text="Cliente", font=("Monospace", 15), pady=10)
    textbox = tk.Text(container, width=80, height=20)
    textbox2 = tk.Text(container, width=80, height=1, pady=3)
    textbox.configure(font=("Monospace", 13))
    button = tk.Button(text="Enviar", command=Client.run_client, pady=10, padx=10, font=("Monospace", 13))
    label.grid(row=0, column=0)
    textbox.grid(row=2, column=0)
    textbox2.grid(row=1, column=0)
    container.pack()
    button.pack(padx=10, pady=10)

    def __init__(self, master):
        super().__init__(master)
        self.master = master.title("Cliente")
        self.pack()
        self.__credentials = ReadIniFile.read()
        self.__ip = self.__credentials['ip']
        self.__port = int(self.__credentials['port'])

    @classmethod
    def text(cls):
        return cls.textbox2


if __name__ == '__main__':
    style = Style('litera')
    master = style.master
    master.geometry('520x500')
    client = Interface(master)
    # server.build()
    # client.run_client()
    client.mainloop()
