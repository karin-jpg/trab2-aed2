import cv2
from os import walk




class No:
     
    def __init__(self, key, dir, esq):
         self.valor = key
         self.dir = dir
         self.esq = esq

class Arvore:

    def __init__(self):
         self.raiz = No(None,None,None)
         self.raiz = None

    def inserir(self, v):
         novo = No(v,None,None)
         if self.raiz == None:
              self.raiz = novo
         else:
              atual = self.raiz
              while True:
                   anterior = atual
                   if v <= atual.valor:
                        atual = atual.esq
                        if atual == None:
                               anterior.esq = novo
                               return
                   
                   else:
                        atual = atual.dir
                        if atual == None:
                                anterior.dir = novo
                                return

    def buscar(self, chave):
        if self.raiz == None:
             return None 
        atual = self.raiz 
        while atual.valor != chave: 
              if chave < atual.valor:
                   atual = atual.esq
              else:
                   atual = atual.dir
              if atual == None:
                   return None
        return atual

    def sucessor(self, apaga):
         paiSucessor = apaga
         sucessor = apaga
         atual = apaga.dir

         while atual != None:
              paiSucessor = sucessor
              sucessor = atual
              atual = atual.esq

         if sucessor != apaga.dir:
              paiSucessor.esq = sucessor.dir
              sucessor.dir = apaga.dir 
                                       
         return sucessor

    def remover(self, v):
        if self.raiz == None:
              return False 
        atual = self.raiz
        pai = self.raiz
        filho1 = True
        
        while atual.valor != v: 
              pai = atual
              if v < atual.valor: 
                   atual = atual.esq
                   filho1 = True
              else: 
                   atual = atual.dir 
                   filho1 = False
              if atual == None:
                   return False 

        if atual.esq == None and atual.dir == None:
              if atual == self.raiz:
                   self.raiz = None 
              else:
                   if filho1:
                        pai.esq =  None
                   else:
                        pai.dir = None 

        
        elif atual.dir == None:
              if atual == self.raiz:
                   self.raiz = atual.esq 
              else:
                   if filho1:
                        pai.esq = atual.esq 
                   else:
                        pai.dir = atual.esq 
        
        elif atual.esq == None:
              if atual == self.raiz:
                   self.raiz = atual.dir 
              else:
                   if filho1:
                        pai.esq = atual.dir 
                   else:
                        pai.dir = atual.dir 

        else:
              sucessor = self.sucessor(atual)

              if atual == self.raiz:
                   self.raiz = sucessor 
              else:
                   if filho1:
                        pai.esq = sucessor 
                   else:
                        pai.dir = sucessor
              sucessor.esq = atual.esq 

        return True
  
    def emOrdem(self, atual):
        if atual != None:
             self.emOrdem(atual.esq)
             print(atual.valor,end=" ")
             self.emOrdem(atual.dir)


    def imprimirCategoria(self, categoria, imagens):
        for i in imagens:
            if x in i:
                nome = i.replace(".jpg", "")
                if self.buscar(nome) != None:        
                    imagem = cv2.imread("imagens/"+i)
                    janela = "janela"
                    cv2.imshow(janela, imagem)
                    cv2.waitKey(0)
            else:
                print(" Valor nao encontrado!")
    


diretorio = 'imagens'
imagens = []
for (dirpath, dirnames, filenames) in walk(diretorio):
  imagens.extend(filenames)
  break
print(imagens)


arv = Arvore()
print("Recuperação de imagens usando árvore binária")
opcao = 0

while opcao != 6:
    print("Entre com a opcao:")
    print("1: Inserir")
    print("2: Inserir todas as imagens")
    print("3: Pesquisar")
    print("4: Excluir")
    print("5: Imprimir")
    print("6: Sair")
    opcao = int(input("-> "))
    if opcao == 1:
        x = input(" Informe o valor -> ")
        nome = x+".jpg"
        if nome in imagens:
            arv.inserir(x)
        else:
            print("Imagem não existe")
    
    elif opcao == 2:
        for i in imagens:
            nome = i.replace(".jpg", "")
            if arv.buscar(nome) == None:
                arv.inserir(nome)
     
    elif opcao == 3:
        x = input(" Informe o valor -> ")
        arv.imprimirCategoria(x, imagens) 

    elif opcao == 4:
        x = input(" Informe o valor -> ")
        for i in imagens:
            nome = i.replace(".jpg", "")
            if x in nome:
                arv.remover(nome)

    elif opcao == 5:
        arv.emOrdem(arv)
    elif opcao == 6:
        break