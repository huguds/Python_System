from lib.interface import * # importação dos métodos
from lib.arquivo import * # importação do arquivo
from time import sleep # importação do timer


arq = 'projetoPython.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu([' Criar arquivo',' Deletar aquivo',' Cadastrar pessoas',' Listar pessoas',' Sair do sistema'])
    if resposta == 1:
        # Opção de criar o arquivo
        cabeçalho('Criar arquivo')
        nomeArq = str(input('Digite o nome do arquivo de Texto que deseja criar: '))
        txt = nomeArq+'.txt'
        criarArquivo(txt)           
    elif resposta == 2:
        # Opção de deletar o arquivo
        deleteArquivo = str(input('Digite o nome do arquivo que deseja deletar: '))
        txt = deleteArquivo+'.txt'
        deletarArquivo(txt)
    elif resposta == 3:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 4:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 5:
        cabeçalho('saindo do sistema...')
        break
    else:
        print('\033[31m ERRO! Digite uma opção válida ! \033[m')
    sleep(2)