# Usar imagem base do Python
FROM python:3.9-slim

# Configurar o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos necessários
COPY app/ /app/

# Instalar dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que será usada pela aplicação Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
