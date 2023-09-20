import random


def particao(vetor, inicio, final):
  pivo = final / 2
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  return i + 1


def quickSort(vetor, inicio, final):
  if inicio < final:
    posicao = particao(vetor, inicio, final)
    quickSort(vetor, inicio, final - 1)
    quickSort(vetor, posicao + 1, final)
  return vetor


#arq = ('arquivo.csv', 'r')
#arq.readlines()
#arq.close()

a = [random.randint(0, 255) for x in range(1000)]

quickSort(a, 0, len(a) - 1)

print(a)
