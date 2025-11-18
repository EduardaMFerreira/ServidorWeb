# Servidor Web em Python

## Sobre o projeto
Este projeto implementa um **servidor web simples** utilizando apenas o módulo nativo `socket` do Python.  
Ele foi criado com finalidade **didática**, para demonstrar:

- Como funciona um **socket TCP**
- Estrutura básica de **requisições e respostas HTTP**
- Comunicação entre **cliente (navegador)** e **servidor**
- Servir arquivos HTML estáticos via protocolo HTTP

---

## Funcionalidades
- Criação de socket TCP (IPv4)
- Aceita conexões de navegadores
- Processa requisições HTTP do tipo `GET`
- Lê e envia arquivos HTML ao cliente
- Retornos:
  - **200 OK** (arquivo encontrado)
  - **404 Not Found** (arquivo inexistente)
- Fecha a conexão após a resposta

---

## Tecnologias utilizadas
- **Python 3**
- **Módulo nativo: `socket`**

Nenhuma biblioteca externa é necessária.

---

## Como executar

### 1. Clone o repositório:
```bash
git clone https://github.com/ServidorWeb/ServidorWeb.git
```

### 2. Acesse o diretório:
```bash
cd ServidorWeb
```

### 3. Execute o servidor:
```bash
python3 server.py
```

### 4. Acesse no navegador:
```bash
http://127.0.0.1:6789/HelloWorld.html
```





