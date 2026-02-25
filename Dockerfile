FROM python:3.9-slim

WORKDIR /app

# Instalação das dependências do sistema para Kivy e SQLite
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instala as bibliotecas Python
RUN pip install --no-cache-dir -r requirements.txt
# Instala pytest para testes automatizados
RUN pip install pytest

COPY . .

# Comando padrão para rodar a aplicação
CMD ["python", "main.py"]
