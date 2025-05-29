# Repositório de Automação

Este repositório contém dois projetos distintos de automação: `extrair_livros` e `python_installer`. Cada projeto foi desenvolvido para atender a diferentes necessidades de automação.

---

## Pré-requisitos

Antes de começar, faça o clone do repositório utilizando o seguinte comando:

```bash
git clone https://github.com/LeonardoVideiraSousaPinto/Projeto-RPA.git
```

Entre na pasta do projeto

```bash
cd .\Projeto-RPA\
```


Crie o ambiente virtual

```bash
python -m venv .venv
```

Entre no ambiente virtual

```bash
.venv\Scripts\activate.ps1
```

---

## Projeto 1: Extrair Livros

### Descrição
O projeto `extrair_livros` realiza a raspagem de dados de livros de uma fonte específica, gera relatórios em formato CSV e PDF, e organiza as informações de forma estruturada.

### Estrutura
- **`extrair_livros.py`**: Script principal que coordena as etapas de raspagem e geração de relatórios.
- **Módulos auxiliares**:
    - `automacoes.extrair_dados`: Contém a classe `RaspadorLivros` para raspagem de dados.
    - `automacoes.gerar_relatorio`: Contém a classe `GeradorRelatorioLivros` para geração de relatórios.

### Uso
1. Execute o script principal:
     ```bash
     python extrair_livros.py
     ```
2. O script realiza as seguintes etapas:
     - Raspagem de dados de livros.
     - Salvamento dos dados em um arquivo CSV.
     - Processamento dos dados e geração de um relatório em PDF.

---

## Projeto 2: Python Installer

### Descrição
O projeto `python_installer` automatiza o processo de download, instalação e verificação da versão do Python. Ele utiliza um sistema de log baseado em MongoDB para registrar o status de cada etapa.

### Estrutura
- **`python_installer.py`**: Script principal que coordena as etapas de download, instalação e verificação.
- **Módulos auxiliares**:
    - `automacoes.baixar_python`: Contém a classe `PythonDownloader` para realizar o download do instalador do Python.
    - `automacoes.instalar_python`: Contém a classe `InstaladorPython` para executar a instalação.
    - `automacoes.verificar_instalacao`: Contém a classe `PythonChecker` para verificar a versão instalada.
    - `logs.mongo_logger`: Sistema de log que registra os eventos no MongoDB.

### Uso

#### Configuração do MongoDB
Antes de executar o script, certifique-se de que o MongoDB está em execução. Você pode iniciar um contêiner Docker com o MongoDB usando o seguinte comando:

```bash
docker run -d -p 27017:27017 --name mongo-rpa mongo
```

#### Execução do Script
1. Execute o script principal:
    ```bash
    python python_installer.py
    ```
2. O script realiza as seguintes etapas:
    - **Download**: Baixa o instalador do Python na versão especificada.
    - **Instalação**: Executa o instalador para instalar o Python.
    - **Verificação**: Confirma se o Python foi instalado corretamente e registra a versão instalada.

#### Logs
Os logs de cada etapa são armazenados no MongoDB, permitindo o acompanhamento detalhado do processo.
