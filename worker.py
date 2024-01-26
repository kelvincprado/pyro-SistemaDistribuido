import Pyro4

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

class Worker():
    @Pyro4.expose
    def sort(self, xs):
        lenxs = len(xs)
        if(lenxs <= 1):
            return(xs)
        half_lenxs = lenxs // 2
        left = xs[:half_lenxs]
        right = xs[half_lenxs:]
        return(merge(self.sort(left), self.sort(right)))


def start_worker():
    worker = Worker()
    # make a Pyro daemon
    daemon = Pyro4.Daemon(host='192.168.1.107') #Ip do worker
    # Localiza o nome do servidor em execução
    ns = Pyro4.locateNS()
    # Registrar um servidor como um objeto Pyro
    uri = daemon.register(worker)
    # Registrar o objeto com o nome do servidor
    ns.register('worker', uri)
    # Mostrando o valor de Uri
    print('Worker Ready. Object uri =', uri)
    # Inicializar o loop de eventos do servidor para aguardar chamadas 
    daemon.requestLoop()

if __name__ == '__main__':
    start_worker()
