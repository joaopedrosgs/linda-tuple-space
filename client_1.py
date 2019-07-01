from pubsub.client import Client


def main():
    c = Client(('', 5050))
    # enviar mensagem em topic
    c._out(('client_1', 'topic', 'Test message'))

    # ler a mensagem que o client 2 enviou em topic
    print(c._rd(('client_2', 'topic', str)))

    # enviar mensagem shared no topic
    c._out(('shared', 'topic', 'Test message from client 1'))
    
    # receber mensagem shared no topic
    print(c._in(('shared', 'topic', str)))

    c.close()


if __name__ == '__main__':
    main()
