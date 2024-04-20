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
// post
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

A mensagem diz que dentro do conteudo do body da requisição **POST** está faltando o campo **title**


