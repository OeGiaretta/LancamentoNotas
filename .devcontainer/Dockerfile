FROM python:3.11-slim

# Evitar prompts interativos durante instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /workspace

# Criar usuário não-root
RUN useradd -m -s /bin/bash vscode && \
    chown -R vscode:vscode /workspace

# Mudar para usuário vscode
USER vscode

# Definir variáveis de ambiente Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copiar e instalar dependências Python
COPY --chown=vscode:vscode requirements.txt /workspace/
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# Adicionar pip local ao PATH
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Definir diretório padrão
WORKDIR /workspace/code