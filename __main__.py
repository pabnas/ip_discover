#!/usr/bin/python3

import socket
import psutil
from tabulate import tabulate
from tkinter import *

UPDATE_TIME = 1000

def get_ip_addresses(family=socket.AF_INET):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address)
                # yield snic.address
                
def update():
    ipv4s = list(get_ip_addresses(socket.AF_INET))
    table = tabulate(ipv4s, headers=["Interface", "IPv4"], tablefmt="double_outline")
    host = socket.gethostname()

    localIP.config(text=table)
    hostName.config(text=host)
    root.after(UPDATE_TIME, update)
    
    
root = Tk()
root.title('IP Addresses')

hostName = Label(root, font = ('monospace', 20),)
hostName.grid(sticky = N, row = 1, column = 1, pady = (20,0))
localIP = Label(root, font = ('monospace', 20),justify=CENTER, anchor='nw')
localIP.grid(sticky = N, row = 2, column = 1)

root.resizable(0,0)
update()
root.mainloop()
