
    def reverso_complementar(self,id):
        dic_reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  # Dicionário
        nova_seq = []                                           # Cria uma lista auxiliar que será preenchida com valores do Dicionário
        if(self.seq_existe(id)):                                # Verifica se a sequência foi carregada
            if(self.get_tipo_seq(id)=="DNA"):                   # Verifica se a sequência é um DNA
                seq = self.get_sequencia(id)                    # Atribui a string da sequência à variável seq
                seq = seq[::-1]                                 # Inverte a sequência
                for i in range(len(seq)):                       # Percorre a sequência invertida do início ao final
                    nova_seq.append(dic_reverse[seq[i]])        # Alimenta a lista auxiliar com valores do Dicionário
                return ''.join(nova_seq)                        # Retorna a lista auxiliar em formato de string
            else: self.message_view(f"A sequencia informada não é um DNA![{self.get_tipo_seq(id)}]")
        else: self.message_view("A sequencia para o Reverso Complentar não foi encontrada!")
        return None
