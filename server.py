from array import array
import Pyro4
from threading import Thread
from queue import Queue

WORKER_LIST = ['192.168.1.107', '192.168.1.107'] #Endereço IP dos computadores que serão usados como worker
QUEUE = Queue()

def worker_sort(host, array): # Conexão do servidor com o worker
    worker_host = Pyro4.Proxy('PYRO:Pyro.NameServer@{}:9090'.format(host))
    worker_uri = worker_host.list()['worker']
    worker = Pyro4.Proxy(worker_uri)
    array_merge = worker.sort(array) # Chamando a função sort do worker
    QUEUE.put(array_merge)

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

class Server():
    @Pyro4.expose
    def sort(self, xs): 
        lenxs = len(xs)
        if(lenxs <= 1):
            return(xs)
        half_lenxs = lenxs // 2 #Divide o vetor na metade
        left = xs[:half_lenxs] #A metade esquerda do vetor
        right = xs[half_lenxs:] #A metade direita do vetor
        thread_list = []
        array_list = [left, right] #Coloca as partes do vetor
        for count, host in enumerate(WORKER_LIST):
            sub_array = array_list[count]
            thread = Thread(target=worker_sort, args=(host, sub_array)) #Passa as partes do vetor para a função worker_sort
            thread_list.append(thread)
            thread.start()
        for thread in thread_list:
            thread.join()
        left = QUEUE.queue[0]
        right = QUEUE.queue[1]
        QUEUE.queue.clear()
        return (merge(left, right))

def start_server():
    server = Server()
    # make a Pyro daemon
    daemon = Pyro4.Daemon(host='192.168.1.107') #Ip da maquina do servidor
    # Localiza o nome do servidor em execução
    ns = Pyro4.locateNS() 
    # Registrar um servidor como um objeto Pyro
    uri = daemon.register(server)
    # Registrar o objeto com o nome do servidor
    ns.register('server', uri)
    # Mostrando o valor de Uri
    print('Server Ready. Object uri =', uri)
    # Inicializar o loop de eventos do servidor para aguardar chamadas 
    daemon.requestLoop()

if __name__ == '__main__':
    start_server()
