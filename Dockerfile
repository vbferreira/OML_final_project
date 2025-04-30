# Usar uma imagem base com Python
FROM python:3.12-slim

# Criar diretório de trabalho dentro do container
WORKDIR /app

# Copiar os ficheiros do projeto para o container
COPY . /app

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta onde o serviço será disponibilizado
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
