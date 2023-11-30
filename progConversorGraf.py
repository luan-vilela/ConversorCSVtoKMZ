import csv
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if arquivo:
        dados.clear()
        with open(arquivo, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dados.append({
                    "SIGLA": row["SIGLA"],
                    "SITIO": row["SÍTIO"],
                    "x": float(row["COORDENADA_2"]),
                    "y": float(row["COORDENADA_1"]),
                    "MUNICIPIO": row["MUNICÍPIO"]
                })
        entrada_arquivo.delete(0, tk.END)
        entrada_arquivo.insert(0, arquivo)

def adicionar_filtro():
    novo_input = tk.Entry(frame_filtro, width=30)
    novo_input.grid(row=len(inputs_filtros), column=0, padx=5)
    inputs_filtros.append(novo_input)

def exibir_sobre():
    sobre_modal = tk.Toplevel(janela)
    sobre_modal.title("Sobre o Programa")

    descricao = """
    Descrição do Programa Trilha Rupestre - UFMS

    Desenvolvedores:
    Luan Vilela Lopes
    Giovanni Pratto

    Projeto: Trilha Rupestre - UFMS

    Versão: 1.0

    Descrição:
    O programa Trilha Rupestre, desenvolvido pelos talentosos programadores Luan Vilela Lopes e Giovanni Pratto, é uma ferramenta projetada para simplificar a conversão de dados geográficos. Especificamente criado para atender às necessidades do projeto Trilha Rupestre da UFMS, este software tem como objetivo facilitar a transformação de informações contidas em arquivos CSV para o formato KMZ.

    Funcionalidades Principais:

    - Importa dados a partir de arquivos CSV seguindo o formato padrão com as colunas: SIGLA, SÍTIO, COORDENADA_1, COORDENADA_2, MUNICÍPIO.
    - Converte eficientemente esses dados para o formato KMZ, facilitando a visualização geográfica.
    - Oferece uma solução ágil e amigável para profissionais envolvidos no projeto Trilha Rupestre, simplificando a manipulação de informações geoespaciais.

    Data de Lançamento: 12/2023

    github: https://github.com/luan-vilela/ConversorCSVtoKMZ
    """

    texto_sobre = tk.Text(sobre_modal, wrap="word", height=30, width=80)
    texto_sobre.insert(tk.END, descricao)
    texto_sobre.pack(padx=10, pady=10)

def converter_kmz():
    palavras_chave = [entrada.get().strip().lower() for entrada in inputs_filtros]

    if aplicar_filtro.get():
        dados_filtrados = [item for item in dados if
                           any(palavra_chave in item["SIGLA"].lower() or
                               palavra_chave in item["SITIO"].lower() or
                               palavra_chave in item["MUNICIPIO"].lower() for palavra_chave in palavras_chave)]
    else:
        dados_filtrados = dados

    nome_arquivo_saida = "output"
    if aplicar_filtro.get():
        nome_arquivo_saida += "_" + "_".join(palavras_chave)

    placemarks = ""
    for item in dados_filtrados:
        placemarks += placemark_template.format(**item)

    kml_content = template.format(placemarks=placemarks)

    total_linhas = len(dados)
    linhas_convertidas = len(dados_filtrados)
    linhas_nao_convertidas = total_linhas - linhas_convertidas

    with open(f"{nome_arquivo_saida}.kml", "w", encoding="utf-8") as file:
        file.write(kml_content)

    mensagem_conclusao = f"Conversão concluída!\n\n\nLinhas convertidas: {linhas_convertidas}\nLinhas não convertidas: {linhas_nao_convertidas}\n\nArquivo de saída: \n{nome_arquivo_saida}.kml\n"
    resposta = messagebox.showinfo("Conclusão", mensagem_conclusao)

    # Abrir a pasta com o arquivo de saída
    if resposta == "ok":
        pasta_saida = os.path.dirname(os.path.abspath(f"{nome_arquivo_saida}.kml"))
        subprocess.run(['xdg-open', pasta_saida])  # Isso funciona no Linux, ajuste conforme o sistema operacional
        
janela = tk.Tk()
janela.title("Conversor KMZ")

dados = []

template = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Camada sem título</name>
    <Style id="icon-1507-673AB7-labelson">
      <IconStyle>
        <color>ffb73a67</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
      </IconStyle>
    </Style>
    {placemarks}
  </Document>
</kml>
"""

# Substituir as tags no template
placemark_template = """
    <Placemark>
      <name>{SITIO}</name>
      <description>{SIGLA} : Sítio {MUNICIPIO} </description>
      <styleUrl>#icon-1507-673AB7-labelson</styleUrl>
      <Point>
        <coordinates>
          {x},{y},0
        </coordinates>
      </Point>
    </Placemark>
"""

aplicar_filtro = tk.BooleanVar()
aplicar_filtro.set(False)  # Configurar como False por padrão

label_logo = tk.Label(janela, image=None)  # Adicione a imagem como argumento para `image`
label_logo.grid(row=0, column=0, pady=10, sticky='w')

label_titulo = tk.Label(janela, text="Selecione o arquivo CSV:")
label_titulo.grid(row=0, column=1, pady=10, sticky='w')

frame_arquivo = tk.Frame(janela)
frame_arquivo.grid(row=1, column=1, pady=10, sticky='w')

entrada_arquivo = tk.Entry(frame_arquivo, width=30)
entrada_arquivo.grid(row=0, column=0, padx=5)

botao_selecionar = tk.Button(frame_arquivo, text="Selecionar Arquivo", command=abrir_arquivo)
botao_selecionar.grid(row=0, column=1, padx=5)

label_palavra_chave = tk.Label(janela, text="Palavra-chave para filtrar:")
label_palavra_chave.grid(row=2, column=1, pady=10, sticky='w')

frame_filtro = tk.Frame(janela)
frame_filtro.grid(row=3, column=1, pady=10, sticky='w')

inputs_filtros = [tk.Entry(frame_filtro, width=30)]
inputs_filtros[0].grid(row=0, column=0, padx=5)

check_aplicar_filtro = tk.Checkbutton(frame_filtro, text="Aplicar Filtro", variable=aplicar_filtro)
check_aplicar_filtro.grid(row=0, column=2, padx=5)

botao_adicionar_filtro = tk.Button(frame_filtro, text="+", command=adicionar_filtro)
botao_adicionar_filtro.grid(row=0, column=1, padx=5)

botao_converter = tk.Button(janela, text="Converter para KMZ", command=converter_kmz)
botao_converter.grid(row=4, column=1, pady=20)

link_sobre = tk.Label(janela, text="Sobre", fg="blue", cursor="hand2", font="Helvetica 9 ")
link_sobre.grid(row=5, column=1, pady=10)
link_sobre.bind("<Button-1>", lambda e: exibir_sobre())

janela.mainloop()
