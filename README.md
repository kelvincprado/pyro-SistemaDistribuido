# pyro-SistemaDistribuido
 Implementação de Sistema Distribuído
 
A programação distribuida é uma tecnologia projetada para aumentar a quantidade de poder de processamento disponível para uma tarefa específica, esse método é usado para resolver problemas que exigem grandes capacidades computacionais. As partes de um problema podem ser calculadas por vários processadores simultaneamente. Isso permite que mais poder de processamento seja exercido sobre o problema do que pode ser fornecido por um único processador. 
A principal diferença entre processamento paralelo e distribuído é que as configurações paralelas incluem muitos processadores em um único sistema, enquanto as configurações distribuídas exploram o poder de processamento de muitos computadores distintos.

Objetivo:
O objetivo deste trabalho é implementar um sistema distribuido e demonstrar como ela pode ser usada para reduzir o tempo de processamento de um algoritmo.

Ideia:
A ideia do trabalho é fazer com que um vetor muito grande seja ordenado através do algoritmo merge sort, fazendo com que um servidor divida esse vetor em duas partes e mande para dois sub-servidores, sendo eles chamados de "workers", ordenando os vetores e retornando o resultado para o cliente.

Como executar:
1º Passo: Instale o pip3 (Caso nao tenha), segundo os seguintes comandos:
	1.1: Atualize o gerenciador de pacotes com o comando: sudo apt-get update
	1.2: Agora use o seguinte comando para instalar o programa: sudo apt-get install python-pip
	1.3: Para verificar se o pip está instalado corretamente, execute o seguinte comando: pip --version
	
2º Passo: Instale o pyro4 (Caso nao tenha), com o comando: pip3 install pyro4
3º Passo: Inicialize o servidor de nomes em todas as maquinas que serão utilizadas, no terminal digite o comando: pyro4-ns -n IP
	Obs: Em "IP" substitua pelo IP da sua maquina, que pode ser encontrado pelo comando hostname -I.
4º Passo: Entre na pasta onde se encontra os arquivos salvos.
5º Passo: Inicialize a execução do servidor, com o comando python3 server.py, e faça o mesmo em um novo terminal para o codigo do worker e do cliente.
