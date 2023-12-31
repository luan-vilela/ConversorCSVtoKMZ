![Logo](https://raw.githubusercontent.com/luan-vilela/ConversorCSVtoKMZ/main/imagens/logo.png)

# Conversor CSV to KMZ

Este é um programa simples em Python para converter dados geográficos de arquivos CSV para o formato KMZ (Keyhole Markup Language Zipped), facilitando a visualização geoespacial.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://raw.githubusercontent.com/luan-vilela/ConversorCSVtoKMZ/main/LICENSE)

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/luan-vilela/ConversorCSVtoKMZ/main/imagens/Captura%20de%20tela%20de%202023-11-30%2010-22-25.png)

## Requisitos

- Python 3.x

## Clonando o Repositório

Para clonar este repositório, execute o seguinte comando no terminal:

`git clone https://github.com/seu-usuario/conversor-csv-to-kmz.git`

Isso criará uma cópia local do repositório em sua máquina.

## Executando o Programa

### No Windows:

1.  Abra um prompt de comando.
2.  Navegue até o diretório do projeto:

`cd caminho\para\conversor-csv-to-kmz`

3.  Execute o programa:

`python conversor.py`

Ou, se preferir, crie um executável usando o PyInstaller:

`pyinstaller --noconsole --onefile --name="ConversorKMZ" --icon="icon.ico" --add-data="icon.ico;." progConversorGraf.py`

Isso criará um executável na pasta `dist`.

### Em Distribuições Linux .deb (como Debian e Ubuntu):

1.  Abra um terminal.
2.  Navegue até o diretório do projeto:

`cd caminho/para/conversor-csv-to-kmz`

3.  Execute o programa:

`python3 conversor.py`

Ou, se preferir, crie um pacote DEB:

`sudo apt-get install python3-stdeb
python3 setup.py --command-packages=stdeb.command bdist_deb
cd deb_dist
sudo dpkg -i nome-do-pacote.deb`

Substitua "nome-do-pacote" pelo nome do pacote gerado.

### Em Distribuições Linux .rpm (como Fedora e CentOS):

1.  Abra um terminal.
2.  Navegue até o diretório do projeto:

`cd caminho/para/conversor-csv-to-kmz`

3.  Execute o programa:

`python3 conversor.py`

Ou, se preferir, crie um pacote RPM:

`python3 setup.py bdist_rpm
cd dist
sudo rpm -i nome-do-pacote.rpm`

Substitua "nome-do-pacote" pelo nome do pacote gerado.

## Contribuindo

Sinta-se à vontade para contribuir fazendo pull requests ou reportando problemas. Se você encontrar algum problema ou tiver sugestões, abra uma issue.

## Licença

Este projeto é licenciado sob a [Licença MIT](https://raw.githubusercontent.com/luan-vilela/ConversorCSVtoKMZ/main/LICENSE).
