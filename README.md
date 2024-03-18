# Integração com OpenIA. 

## Introdução
Esta integração foi desenvolvida para criar perguntas com base em texto a partir de arquivos PDF. O processo envolve a extração de todo o texto de um arquivo PDF e o envio desse texto para a OpenAI, que gera perguntas de múltipla escolha com base no conteúdo. Uma vez obtida a resposta da OpenAI, um novo arquivo PDF é gerado contendo as perguntas e suas respectivas respostas.

## Configuração do Arquivo .env

Para configurar a integração, é necessário criar um arquivo `.env` na raiz do projeto. Você pode seguir o exemplo fornecido no arquivo `.env.example` e ajustar os valores de acordo com suas necessidades:

- `ENV`: Para executar localmente, deixe o valor como `LOCAL`.
- `PATH_FILE`: Caminho para o arquivo PDF que será lido. Por exemplo, `debug/testFile.pdf`.
- `IA_API_KEY`: Token de API fornecido pela OpenAI.
- `IA_MODE`L: Modelo da API fornecido pela OpenAI. Por exemplo, `gpt-3.5-turbo`
- `NUMBER_QUESTIONS`: Número de perguntas a serem geradas. Por exemplo, `3`.
- `NUMBER_QUESTIONS_RESPONSE`: Número de respostas para cada pergunta. Por exemplo, `4`.

## Instalação das Dependências
Antes de executar o script, é necessário instalar as dependências do projeto. Para isso, execute o seguinte comando no terminal:
```
pip install -r requirements.txt
``` 
Este comando instalará todas as dependências listadas no arquivo requirements.txt, garantindo que todas as bibliotecas necessárias estejam disponíveis para o projeto.

## Execução

Para executar a integração, basta usar o seguinte comando:
```
python main.py
``` 

Este comando iniciará o processo de extração de texto do arquivo PDF, geração de perguntas pela OpenAI e criação de um novo arquivo PDF com as perguntas e respostas.

Certifique-se de que todas as dependências necessárias estejam instaladas e que você tenha configurado corretamente as variáveis de ambiente no arquivo .env antes de executar o script.