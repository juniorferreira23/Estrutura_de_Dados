import pilha

def main():
    p = pilha.Pilha()
    
    print('--------------------------')
    print('Programa gerador de pilha:')
    print('--------------------------')
    
    while True:
        print('')
        print('Opção 0 para parar o programa!')
        print('Opção 1 para inserir um elemento')
        print('Opção 2 para remover um elemento')
        print('Opção 3 para imprimir a pilha')
        print('Opção 4 para verificar o tamanho da pilha')
        print('Opção 5 para verificar se a pilha está cheia')
        print('Opção 6 para verificar se a pilha está vazia')
        opcao = int(input('Digite a opção desejada: '))
        
        if opcao == 0:
            break
        
        elif opcao == 1:
            item = int(input('Digite o elemente a ser inserido: '))
            p.inserir(item)
            
        elif opcao == 2:
            item = p.remover()
            if p.esta_cheia:
                print(f'Elemento removido: {item}')
                
        elif opcao == 3:
            p.imprimir()
            
        elif opcao == 4:
            tamanho = p.qual_tamanho()
            print(f'Tamanho da pilha: {tamanho}')
        
        elif opcao == 5:
            esta_cheia = p.esta_cheia()
            print(f'A pilha está cheia? {esta_cheia}')
            
        elif opcao == 6:
            esta_vazia = p.esta_vazia()
            print(f'A pilha está vazia? {esta_vazia}')
            
        else:
            print('Opção não encontrada')

    
if __name__ == "__main__":
    main()