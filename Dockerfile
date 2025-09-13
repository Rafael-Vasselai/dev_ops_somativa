
# Usa uma imagem base oficial do Python.
FROM python:3.9-slim

# Define o diretório de trabalho no container.
WORKDIR /app

# Copia o arquivo de dependências para o container.
COPY requirements.txt .

# Instala as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do seu projeto.
COPY . .

# Expõe a porta que a aplicação usará.
EXPOSE 5000

# Comando para iniciar a aplicação.
CMD ["python", "app.py"]