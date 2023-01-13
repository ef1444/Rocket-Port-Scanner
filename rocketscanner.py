#!/usr/bin/python
import socket
import click
from termcolor import colored

@click.command()
@click.option("--host","-h",help="Host",required = True)
def connect(host):
    for i in range (1,10):
        try:
            sock.connect((host,i))
            click.echo(colored(f"[+]Connection established on {host}:{i}","green"))
        except:
            click.echo(colored(f"[-]The connection to {host}:{i} was refused"))
            continue
        

def main():
    global sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connect()

main()
