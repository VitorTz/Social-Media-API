# CRUD

<img src="./images/crud.png" title="crud" alt="" data-align="center">

CRUD é um acrônimo que representa as quatro operações principais de uma aplicação (**Create**, **Read**, **Update** e **Delete**).

No contexto de uma API para uma rede social, a API deve ser capaz de:

- Permitir a um usuário criar uma publicação.

- Retornar o conteudo de uma determinada publicação de um algum usuário ou várias publicações de usuários diferentes entre si ou não.

- Atualizar o conteúdo de uma publicação específica.

- Deletar/Remover uma publicação.

# Nomeação dos paths usados

Como a API permite a criação, leitura, atualização e remoção de publicações em uma rede social, faz sentido que se use a palavra posts (sempre no plural) para preceder todas as operações realizadas pela API. A nomeção utilizada na url das requisições devem ser padronizadas e escolhidas de forma que reflitam suas ações.



# PUT vs PATCH

Ao usar a requisição **PUT** estamos informando que queremos mudar todos os campos de uma publicação e ao usar a requisição **PATCH** estamos informando que queremos mudar apenas alguns campos de uma publicação.

# Implementação base das operações CRUD

Exemplo de uso das quatro operações de uma aplicação CRUD

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


@app.post("/posts")
async def create_post(payload):
    pass


@app.get("/posts")
def get_posts(payload):
    pass


@app.get("/posts/{id}")
def get_posts_by_id(payload):
    pass


@app.put("/posts/{id}")
def update_post(payload):
    pass


@app.delete("/posts/{id}")
def delete_post(payload):
    pass
```
