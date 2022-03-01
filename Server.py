import socket
import tkinter as tk
from ttkbootstrap import Style
from ReadIniFile import ReadIniFile


class Server:
    @staticmethod
    def run_server(event=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        credenciais = ReadIniFile.read()
        sock.bind((credenciais['ip'], int(credenciais['port'])))
        sock.listen(5)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        new_sock, address = sock.accept()
        if new_sock:
            message: str = new_sock.recv(1024).decode()
            Interface.text().insert(f"1.0", f"{address} diz: {message}")
            message: str = Interface.textbox2.get('1.0', tk.END)
            new_sock.sendall(message.encode())
            print(message)
            Interface.textbox2.delete('1.0', tk.END)
            new_sock.close()


class Interface(tk.Frame):
    container = tk.Frame()
    label = tk.Label(container, text="Servidor", font=("Monospace", 15), pady=10)
    textbox = tk.Text(container, width=80, height=20)
    textbox2 = tk.Text(container, width=80, height=1, pady=3)
    textbox.configure(font=("Monospace", 13))
    button = tk.Button(text="Enviar", command=Server.run_server, pady=10, padx=10, font=("Monospace", 13))
    label.grid(row=0, column=0)
    textbox2.grid(row=1, column=0)
    textbox.grid(row=2, column=0)
    container.pack()
    button.pack(padx=10, pady=10)

    def __init__(self, master):
        super().__init__(master)
        self.master = master.title("Servidor")
        self.pack()
        self.__credentials = ReadIniFile.read()
        self.__ip = self.__credentials['ip']
        self.__port = int(self.__credentials['port'])

    @classmethod
    def text(cls):
        return cls.textbox


if __name__ == '__main__':
    style = Style('litera')
    master = style.master
    master.geometry('520x500')
    client = Interface(master)
    # server.build()
    # client.run_client()
    client.mainloop()
