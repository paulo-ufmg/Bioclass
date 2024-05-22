from Bioclass import Bioprof #Outra forma de carregar a class é <import Bioclass> e instanciando o objeto com <seq = Bioclass.Bioprof>
import os #Importação do módulo para compatibilizar o sistema operacional com o caractere separador de diretório (Windows [\] Linus [/] ...)

arquivo2 = 'dados' + os.sep + 'sequencias_spike.fasta.txt'
seq = Bioprof() #Instanciando o objeto da nossa classe
seq.leiaArquivoFasta(arquivo2) #Método que carrega as sequências e dados complementares

seq.matriz_d()# Fredy 