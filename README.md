# Autentificação utilizando token JWT

## Configurando o ambiente antes de rodar os scripts

### Ambiente virtual
```bash
python -m venv venv
```

### Ativando ambiente virtual
```bash
.\venv\Scripts\activate
```

### Instalando pacotes necessários
```bash
pip install -r requirements.txt
```

### Configurações
No arquivo settings.py é possível alterar a chave secreta utilizada no JWT e o tempo de expiração em segundos dos tokens.
Por padrão a chave secreta é "secret" e o tempo de expiração dos tokens é de 3 segundos.
```python
SECRET_KEY = "secret"
TEMPO_EXPIRACAO_SEGUNDOS = 3
```

## Executando o API
```bash
python app.py
```

## Executando um teste pronto
Se desejar executar um teste rápido o arquivo clientSide.py contém um teste pronto

```bash
python clientSide.py
```
