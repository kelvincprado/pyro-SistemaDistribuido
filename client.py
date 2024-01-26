import Pyro4
import random
import time

def sort(xs):
    lenxs = len(xs)
    if(lenxs <= 1):
        return(xs)
    half_lenxs = lenxs // 2
    left = xs[:half_lenxs]
    right = xs[half_lenxs:]
    return(merge(sort(left), sort(right)))

def merge(left, right):
    nleft = len(left)
    nright = len(right)
    merged = []
    i = 0
    j = 0
    while i < nleft and j < nright:
        if(left[i] < right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

SERVER = '192.168.1.107' #Ip do servidor
ARRAY_LEN = 500000 #Tamanho do vetor que será gerado

# use name server object lookup uri shortcut
# Conexão do cliente com o servidor
server = Pyro4.Proxy('PYRO:Pyro.NameServer@{}:9090'.format(SERVER))
server_obj_uri = server.list()['server']
server = Pyro4.Proxy(server_obj_uri)

# Criação do vetor e gerando números aleatórios 
array = [random.randint(0, ARRAY_LEN) for _ in range(ARRAY_LEN)]
array2 = array.copy() # Faz a cópia do primeiro vetor para um segundo vetor que será testado localmente

start_time = time.time()
print('ARRAY não ordenado:', array)
print()
print('ARRAY ordenado: ', server.sort(array))
print()
total_time = time.time() - start_time
print()
print('REMOTE TIME:', total_time)

start_time = time.time()
sort(array2)
total_time = time.time() - start_time
print()
print('LOCAL TIME:', total_time)
