import os
#Mal exemplo Nao utilizar
#def leituraDeArquivo()
def leitura_de_arquivo(nome_arquivo):
  arquivo_caminho = os.path.join("/home/mkom/Workfromao/Course/authp/auth/project/", nome_arquivo)
  arquivo = open(arquivo_caminho, "r")
  #print(arquivo.readlines())
  lista = []
  for linha in arquivo:
    nomes = linha.strip()
    lista.append(nomes)
    #print(lista_de_bebes)
  
  arquivo.close()
  return lista
