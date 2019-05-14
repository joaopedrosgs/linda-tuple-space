# Publish - Subscribe

Esse projeto apresenta uma implementação simples de uma biblioteca para o
modelo "publish subcribe" de troca de mensagens. As funcionalidades são baseadas
na biblioteca Linda.

## Dependências

* `python 3.7`;

## Como executar

Para executar o servidor:

* `python main.py`;

Para executar os clientes:

* `python client_1.py` e `python client_2.py`;

## Execução em computadores diferentes

Primeiro é necessário configurar sua rede para que conexões na porta desejada
sejam passadas para o computador que executará o servidor.

Em seguida, alterar os valores de IP e da porta nos arquivos `main.py`,
`client_1.py`, `client_2.py`.

* `main.py`

```python
Server.start_server(host='IP', port=Porta)
```

* `client_1.py` e `client_2.py`

```python
c = Client(('IP', porta))
```
