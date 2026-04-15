[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KQahFieU)

# ICE Middleware - RPC Demo

Baseado no exemplo 3.21 do livro de Maarten van Steen, com dois metodos adicionais.

## Metodos da interface Printer

1. **printString(string s)** - Imprime a string no servidor e retorna com "*" (original)
2. **reverseString(string s)** - Reverte a string recebida (novo)
3. **toUpperCase(string s)** - Converte a string para maiusculas (novo)

## Instalacao

```
sudo dnf install python3-ice ice-compilers
```

## Como executar

```
python server.py     # Terminal 1
python client.py     # Terminal 2
```

Ou com dois objetos:
```
python server2.py    # Terminal 1
python client2.py    # Terminal 2
```
