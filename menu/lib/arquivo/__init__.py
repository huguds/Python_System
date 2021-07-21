from lib.interface import *
import os

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #read text - verifica se o arquivo é existente.
        a.close()
    except FileNotFoundError:
        return False
    else:
        print('Arquivo já existente !')
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #write text + create - Tenta escrever um texto no arquivo, caso não tenha o arquivo ele cria.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso !')

def deletarArquivo(nome):
    try:
        os.remove(nome) # Delete o arquivo de acordo com o parâmetro
    except:
        print(f'Houve um ERRO ao tentar deletar o arquivo: {nome}')
    else:
        print(f'Arquivo {nome} deletado com sucesso !')

def lerArquivo(nome):
    try:
        a = open(nome,'rt') #read text - responsável por ler o arquivo
    except:
        print('Erro ao ler o arquivo !')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at') #append acrescentar elementos dentro do arquivo
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao cadastrar')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()