# Dockerfile

FROM python:3.10

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos para o contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Defina o PYTHONPATH
ENV PYTHONPATH=/app

# Execute a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
