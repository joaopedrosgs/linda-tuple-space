from pubsub.client import Client


def main():
    c = Client(('', 5050))

    c._out(('client_1', 'topic', 'Test message'))

    print(c._rd(('client_2', 'topic', str)))

    c._out(('shared', 'topic', 'Test message from client 1'))

    print(c._in(('shared', 'topic', str)))

    c.close()


if __name__ == '__main__':
    main()
