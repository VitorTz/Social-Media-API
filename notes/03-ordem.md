

# Exemplo

> método get e path "/"

~~~python
@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to my API"}


@app.get("/")
def get_posts():
    return {"data": "This is your post"}
~~~

O FastAPI vai começar a ler o arquivo de cima para baixo e procurar pelo primeiro método que combine com o método get e path "/", neste caso o método root é o primeiro a combinar e será retornado. o Segundo método que combina o padrão get e "/" não será retornado.