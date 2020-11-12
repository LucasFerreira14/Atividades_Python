# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Lucas Ferreira da Silva (1903769)


'''
Escreva uma função com o nome quantidade, que recebe como argumentos de
entrada uma tupla e um item e retorna quantas vezes esse item aparece na
tupla.
'''

def quantidade(tupla, item):
  qtd = 0
  tamanho = len(tupla)
  cont = 0
  while cont < tamanho:
    if tupla[cont] == item:
      qtd += 1
    cont += 1
  return qtd


'''
Escreva uma função chamada excluir que recebe como argumentos de entrada uma 
lista e um item e retorna a lista sem o item informado. 
'''

def excluir(lista, item):
  x = []
  for i in range(len(lista)):
    if lista[i] != item:
      x.append(lista[i])
  lista = x
  return lista


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todas os índices em que o
item aparece na lista.
'''

def posicoes_lista(lista, item):
  x = []
  m = len(lista)
  for i in range(m):
    if lista[i] == item:
      x.append(i)
  return x

'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
3 notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
'''

def aprovados(alunos):
  soma = 0
  aprovados = []
  for i in alunos:
    soma = 0
    for j in range(len(alunos[i])):
      soma += alunos[i][j]
    media = soma / len(alunos[i])
    if media >= 6:
      aprovados.append(i)
  return aprovados

'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
3 notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''

def incluir_nota(alunos, nome, nota):''
  for i in alunos:
    if i == nome:
        alunos[i].append(nota)
        
  return alunos
    

