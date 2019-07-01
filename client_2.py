from pubsub.client import Client


def main():
    c = Client(('', 5050))

    # ler a mensagem que o client 1 enviou em topic
    print(c._rd(('client_1', 'topic', str)))

    # enviar mensagem em topic
    c._out(('client_2', 'topic', 'Test message'))

    # receber mensagem shared no topic
    print(c._in(('shared', 'topic', str)))

    # enviar mensagem shared no topic
    c._out(('shared', 'topic', 'Test message from client 2'))

    c.close()


if __name__ == '__main__':
    main()