from pubsub.client import Client


def main():
    c = Client(('', 5050))

    print(c._rd(('client_1', 'topic', str)))

    c._out(('client_2', 'topic', 'Test message'))

    print(c._in(('shared', 'topic', str)))

    c._out(('shared', 'topic', 'Test message from client 2'))

    c.close()


if __name__ == '__main__':
    main()