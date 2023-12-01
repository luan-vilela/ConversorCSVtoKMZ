import csv
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import zipfile

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

def selecionar_imagem():
  caminho_imagem = filedialog.askopenfilename(filetypes=[('image files', ('.png', '.jpg', '.jpeg'))])
  
  if caminho_imagem:
      pasta_images = os.path.join(os.getcwd(), "images")
      if not os.path.exists(pasta_images):
          os.makedirs(pasta_images)
      
      destino_imagem = os.path.join(pasta_images, "icon-1" + os.path.splitext(caminho_imagem)[1])
      shutil.copyfile(caminho_imagem, destino_imagem)
      
      imagem = tk.PhotoImage(file=destino_imagem)
      
      canvas_imagem.create_image(0, 0, anchor=tk.NW, image=imagem)
      canvas_imagem.image = imagem

      global template
      atualizar_estilo_kml(destino_imagem)

      messagebox.showinfo("Sucesso", "Imagem copiada com sucesso!")


def atualizar_estilo_kml(caminho_imagem):
  extensoes_foto = ['.png', '.jpg', '.jpeg']
  novo_estilo = ""
  if any(caminho_imagem.lower().endswith(ext) for ext in extensoes_foto):
      novo_estilo = """
    <Style id="icon-ci-1-normal">
      <IconStyle>
        <scale>1.1</scale>
        <Icon>
          <href>images/icon-1.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>0</scale>
      </LabelStyle>
    </Style>
    <Style id="icon-ci-1-highlight">
      <IconStyle>
        <scale>1.1</scale>
        <Icon>
          <href>images/icon-1.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>1.1</scale>
      </LabelStyle>
    </Style>
    <StyleMap id="icon-ci-1">
      <Pair>
        <key>normal</key>
        <styleUrl>#icon-ci-1-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#icon-ci-1-highlight</styleUrl>
      </Pair>
    </StyleMap>
      """
  else:
      novo_estilo = """
    <Style id="icon-ci-1-normal">
      <IconStyle>
        <color>ffb73a67</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>0</scale>
      </LabelStyle>
    </Style>
    <Style id="icon-ci-1-highlight">
      <IconStyle>
        <color>ffb73a67</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>1</scale>
      </LabelStyle>
    </Style>
    <StyleMap id="icon-ci-1">
      <Pair>
        <key>normal</key>
        <styleUrl>#icon-ci-1-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#icon-ci-1-highlight</styleUrl>
      </Pair>
    </StyleMap>
      """

  global template
  template = template.replace('<#ROTA369-1>', novo_estilo)

def atualizar_estilo_default_kml():
  novo_estilo = """
    <Style id="icon-ci-1-normal">
      <IconStyle>
        <color>ff007cf5</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>0</scale>
      </LabelStyle>
    </Style>
    <Style id="icon-ci-1-highlight">
      <IconStyle>
        <color>ff007cf5</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
      </IconStyle>
      <LabelStyle>
        <scale>1</scale>
      </LabelStyle>
    </Style>
    <StyleMap id="icon-ci-1-nodesc">
      <Pair>
        <key>normal</key>
        <styleUrl>#icon-ci-1-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#icon-ci-1-highlight</styleUrl>
      </Pair>
    </StyleMap>
      """

  global template
  template = template.replace('<#ROTA369-1>', novo_estilo)

def compactar_em_kmz(pasta_images, nome_arquivo_saida):
  with zipfile.ZipFile(f"{nome_arquivo_saida}.kmz", 'w') as kmz:
      for root, dirs, files in os.walk(pasta_images):
          for file in files:
              caminho_completo = os.path.join(root, file)
              rel_path = os.path.relpath(caminho_completo, pasta_images)
              kmz.write(caminho_completo, os.path.join("images", rel_path))

      kmz.write(f"doc.kml", os.path.basename(f"doc.kml"))


def converter_kmz():

  pasta_images = os.path.join(os.getcwd(), "images")
  if not os.path.exists(pasta_images):
    atualizar_estilo_default_kml()

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

  with open(f"doc.kml", "w", encoding="utf-8") as file:
      file.write(kml_content)

  compactar_em_kmz(os.path.join(os.getcwd(), "images"), nome_arquivo_saida)

  os.remove(f"doc.kml")
  pasta_images = os.path.join(os.getcwd(), "images")
  if os.path.exists(pasta_images):
    shutil.rmtree(os.path.join(os.getcwd(), "images"))

  mensagem_conclusao = f"Conversão concluída!\n\n\nLinhas convertidas: {linhas_convertidas}\nLinhas não convertidas: {linhas_nao_convertidas}\n\nArquivo de saída: \n{nome_arquivo_saida}.kmz\n"
  resposta = messagebox.showinfo("Conclusão", mensagem_conclusao)

  if resposta == "ok":
      pasta_saida = os.path.dirname(os.path.abspath(f"doc.kml"))
      subprocess.run(['xdg-open', pasta_saida]) 

janela = tk.Tk()
janela.title("Conversor KMZ")

dados = []

template = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Camada sem título</name>
    <#ROTA369-1>
    {placemarks}
  </Document>
</kml>
"""

placemark_template = """
    <Placemark>
      <name>{SITIO}</name>
      <description>{SIGLA} : Sítio {MUNICIPIO} </description>
      <styleUrl>#icon-ci-1</styleUrl>
      <Point>
        <coordinates>
          {x},{y},0
        </coordinates>
      </Point>
    </Placemark>
"""

aplicar_filtro = tk.BooleanVar()
aplicar_filtro.set(False)  # Configurar como False por padrão

label_logo = tk.Label(janela, image=None)
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

botao_selecionar_imagem = tk.Button(janela, text="Selecionar Imagem", command=selecionar_imagem)
botao_selecionar_imagem.grid(row=4, column=1, pady=10)

canvas_imagem = tk.Canvas(janela, width=80, height=80)
canvas_imagem.grid(row=5, column=1)

botao_converter = tk.Button(janela, text="Converter para KMZ", command=converter_kmz)
botao_converter.grid(row=8, column=1, pady=20)




link_sobre = tk.Label(janela, text="Sobre", fg="blue", cursor="hand2", font="Helvetica 9 ")
link_sobre.grid(row=9, column=1, pady=10)
link_sobre.bind("<Button-1>", lambda e: exibir_sobre())

janela.mainloop()
