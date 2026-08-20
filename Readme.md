# Organizador de Arquivos

Automação desenvolvida em Python para organizar arquivos
automaticamente de acordo com suas extensões.

## Funcionamento

O programa percorre a pasta de origem selecionada, verifica os arquivos
e lê suas respectivas extensões, movendo-os automaticamente para as
pastas correspondentes.

Caso a pasta de destino já exista, o programa a identifica e informa
o usuário. Caso não exista, o programa cria uma nova pasta.

Extensões que não estão cadastradas não são movidas.

## Funcionalidades

- Indentificar arquivos
- Ignorar pastas
- Organização por extensão
- Criação automática de pastas
- Tratamento de arquivos não cadastrados
- Tratamento de erros

## Tecnologias utilizadas

- Python
- pathlib
- shutil

## Como executar

1. Clone este repositório
2. Abra o arquivo "organizador.py"
3. Configure o caminho da pasta que deseja organizar
4. Execute o programa

## Extensões suportadas
| Extensão | Pasta |
|---|---|
| `.pdf` | PDFs |
| `.mp3` | Musicas |
| `.jpg` | Imagens |
| `.png` | Imagens |
| `.txt` | Textos |
| `.mp4` | Videos |