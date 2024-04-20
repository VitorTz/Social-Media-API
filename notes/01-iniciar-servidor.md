# Iniciar servidor

```python
app = FastAPI()
```

```bash
uvicorn main:app --reload
```

- main: arquivo main.py (modulo Python).
- app: o objeto criado dentro de main.py -> app = FastAPI().
- --reload: Faz o servidor reiniciar após as alterações do no código. Apenas para fins de desenvolvimento.
