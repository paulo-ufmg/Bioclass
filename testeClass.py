
from Bioclass import Bioprof #Outra forma de carregar a class é <import Bioclass> e instanciando o objeto com <seq = Bioclass.Bioprof>
import os #Importação do módulo para compatibilizar o sistema operacional com o caractere separador de diretório (Windows [\] Linus [/] ...)

#Referência dos arquivos de sequencias (Fasta) a serem importados
arquivo = 'dados' + os.sep + 'L02E05_file_fasta.txt' 
arquivo2 = 'dados' + os.sep + 'sequencias_spike.fasta.txt'

seq = Bioprof() #Instanciando o objeto da nossa classe

seq.leiaArquivoFasta(arquivo) #Método que carrega as sequências e dados complementares
seq.leiaArquivoFasta(arquivo2) #Método que carrega as sequências e dados complementares

print("Sequencias:",seq.ids) #Atributo Lista da classe (ids). Contém os Id´s das sequências carregadas
#print(seq.composicao_total)  #Para cada sequencia, totaliza a quantidade de nucleotídeos ou aminoácidos da sequência

print(seq.get_seqs()) #Método get_seqs() retorna a lista das sequências importadas
for i in seq.get_seqs():
    seq.ver_info_seq(i) #método get_info_seq(id) retorna dados sobre a sequência
print("Visualizando a sequenca de id = sp|P59594|SPIKE_SARS")
print("====================================================")
seq.ver_info_seq("sp|P59594|SPIKE_SARS")
print(seq.get_sequencia("sp|P59594|SPIKE_SARS"))    
print("Composição:")
print (seq.get_composicao_seq("sp|P59594|SPIKE_SARS"))
print("------------------------Done!")
