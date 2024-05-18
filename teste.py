class Bioprof:
    def get_tipo_seq(self,id):
        pass
        

    def message_view(self,mensagem,interrupt=False):
        pass



    def reversa_sequencia(self,id):
        """ comente aqui o que faz esse método"""
        #Parâmentro de entrada: id (Identificação da sequência)
        seq = self.get_sequencia(self,id) #obtem a sequência solicitada no parâmetro de entrada
        if(self.get_tipo_seq(id)=="DNA"): #Verifica se a sequência é um DNA


            pass #Insira o código para fazer o DNA reverso

              
        else:
            self.message_view(f"A sequência informada não é um DNA") 

        

