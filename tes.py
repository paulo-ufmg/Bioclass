from Bioclass import encadear
import os

seq1 = encadear()
seq2 = encadear()

seq1.leiaArquivoFasta('dados' + os.sep + 'teste.fasta')
seq1.adiciona_seq("Genoma","teste","CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")
print(seq1.get_seqs())
seq1.insert_comment("Genoma","Alterei o comentário!")
print(seq1.compara_genomas("Genoma1","Genoma2"))
exit()
print(seq1.get_seqs())
print(seq1.ids)
print(seq1.get_info(2))


for seq,seque in enumerate(seq1.get_seqs()):
    print("Sequencia: ",seq,"   Tamanho: ",seq1.get_tamanho_sequencia(seq)," Tipo: ",seq1.get_tipo_seq(seq), " Percentual GC: ","{:.2f} %".format(seq1.get_percentual_GC(seq)))
    print(seq,":",seq1.get_sequencia(seq))
    print("--",seq,"-------------")
    seq1.ver_info_seq(seq)
print("distancia de dH: ",seq1.dH("Genoma1",'Genoma2'))
print("trancrever Genoma: ",seq1.transc_dna2rna("Genoma"))
seq1.adiciona_seq("Genoma->rna","",seq1.transc_dna2rna("Genoma"))
print("tradução Genoma: ",seq1.rna2proteina("Genoma->rna"))
seq1.dna("Genoma").transcreve().traduz().imprime()
print(seq1.get_kmers("Genoma",3))




"""
seq1.adiciona_seq("genoma1","Sequencia de DNA","CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")
seq2.adiciona_seq("genoma2","Sequencia de DNA","CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

seq1.dna("genoma1").imprime()
seq1.dna("genoma1").rm_introns("CTG").imprime()
seq1.dna("genoma1").rm_introns("CTG").rm_introns("TTC").imprime()
seq2.dna("genoma2").rm_introns("CTG","TTC").imprime()

#seq1.dna("genoma1").rm_introns("CTG","TTC").transcreve().imprime()
seq1.dna("genoma1").rm_introns("CTG","TTC").transcreve().traduz().imprime()





"""