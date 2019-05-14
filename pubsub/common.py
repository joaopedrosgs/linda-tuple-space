import json


# este metodo compacta a mensagem
def pack(data: dict):
    message_json = json.dumps(data)
    message = f'{len(message_json)}:{message_json}'

    return message.encode('utf-8')


# este metodo descompacta a mensagem em um dicionario
def unpack(data: str):
    message_struct = {
        'operation': "",
        'author': "",
        'topic': "",
        'message': ""
    }
    try:
        message_struct = json.loads(data)
    except Exception as erro_msg:
        print("Deu erro ao decompactar?: ", erro_msg)

    return message_struct