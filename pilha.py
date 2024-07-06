# pilha = stack

class Pilha:
    def __init__(self): # construtor //stack
        self._max_itens = 100
        self._tamanho = 0
        self._estrutura = [None] * self._max_itens
        
        
    def __del__(self): # destrutora //~stack
        del self._estrutura[:]
        
    def esta_cheia(self) -> bool: # verifica se a pilha está cheia //isfull
        return self._tamanho == self._max_itens
    
    def esta_vazia(self) -> bool: # verifica se a pilha está vazia //isempty
        return self._tamanho == 0
    
    def inserir(self, item: int) -> None: # push
        if self.esta_cheia():
            print('A pilha está cheia, não foi possível inserir o elemento!')
        else:
            self._estrutura[self._tamanho] = item
            self._tamanho += 1
            
    def remover(self) -> int: # pop
        if self.esta_vazia():
            print('A pilha está vazia, não tem elemento para ser removido')
            return 0
        else:
            item_removido = self._estrutura[self._tamanho - 1]
            self._tamanho -= 1
            return item_removido
        
    def imprimir(self) -> None: # print
        print('Pilha: [', end='')
        for i in range(self._tamanho):
            print(f'{self._estrutura[i]}, ', end='')
        print(']')
    
    def qual_tamanho(self) -> int: # lenght
        return self._tamanho
