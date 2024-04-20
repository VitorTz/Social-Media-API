# Schema

---

- Uma forma de definir como os dados devem ser enviados.

- É definida previamente e o usuário deve ser forçado a enviar os dados  de acordo com o que foi definido na Schema.

- Se os dados não estiverem de acordo com a Schema, uma mensagem de erro deverá ser retornada.

## Criar um Schema

Em python, a biblioteca chamada [pydantic](https://docs.pydantic.dev/latest/) é usada para criar uma Schema que possa ser utilizada junto da API.

---

## Exemplo

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):

    title: str
    content: str

@app.post("/posts")
def post(payload: Post):
    return {
        "data": {
            "title": payload.title,
            "content": payload.content
        }
    }
```

 Através da classe **Post** podemos definir como os dados devem ser enviados. Também podemos extrair os dados mais facilmente através dos métodos da classe.

## Validação

No exemplo anterior, a validação dos dados é feita automaticamente. Digamos que o usuário envie apenas o **content** e esqueça do **title** como na requisição a seguir

```json
{
    "content": "Check this awesome beatches"
}
```

Neste caso, a seguinte mensagem será enviada **automaticamente**

```json
{
    "detail": [
        {
            "loc": [
                "body",
                "title"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

A mensagem diz que dentro do conteudo do body da requisição **POST** está faltando o campo **title**.

## Valores pré-definidos e opicionais

Podemos definir valores pré-definidos ou opicionais para os atributos de um Schema

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None   


@app.post("/posts")
def post(payload: Post):
    return {
        "data": {
            "title": payload.title,
            "content": payload.content,
            "published": payload.published
        }
    }
```



Neste caso, estamos dizendo que se o usuário não fornecer o campo **published** em sua requisição **POST**, então o valor de **published** deve ser considerado **True**. Caso o usuário forneça o campo **published** então seu valor deve ser um boolean.

E estamos dizendo que o campo **rating** é opicional (pode ou não ser enviado), caso não seja enviado então seu valor será None. Porém, se o campo **rating** for enviado, o valor de seu conteudo deve ser um inteiro, caso o contrário o FastAPI automaticamente retornará uma mensagem de erro.



## Convertendo um Schema em um dicionário

 Um Schema pode ser definido através da class BaseModel da biblioteca pydantic. Para extrair as informações presentes em uma Schema em formato de dicionário basta apenas seguir o exemplo a seguir



```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.post("/posts")
def post(payload: Post):
    post = payload.dict()
    return {
        "data": post
    }
```


