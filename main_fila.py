import fila

def main():
    f = fila.Fila()
    
    print('--------------------------')
    print('Programa gerador de Fila:')
    print('--------------------------')
    
    while True:
        print('')
        print('Opção 0 para parar o programa!')
        print('Opção 1 para inserir um elemento')
        print('Opção 2 para remover um elemento')
        print('Opção 3 para imprimir a Fila')
        print('Opção 4 para verificar o tamanho da Fila')
        print('Opção 5 para verificar se a Fila está cheia')
        print('Opção 6 para verificar se a Fila está vazia')
        opcao = int(input('Digite a opção desejada: '))
        
        if opcao == 0:
            break
        
        elif opcao == 1:
            item = int(input('Digite o elemente a ser inserido: '))
            f.inserir(item)
            
        elif opcao == 2:
            item = f.remover()
            if f.esta_cheia:
                print(f'Elemento removido: {item}')
                
        elif opcao == 3:
            f.imprimir()
            
        elif opcao == 4:
            tamanho = f.qual_tamanho()
            print(f'Tamanho da Fila: {tamanho}')
        
        elif opcao == 5:
            esta_cheia = f.esta_cheia()
            print(f'A Fila está cheia? {esta_cheia}')
            
        elif opcao == 6:
            esta_vazia = f.esta_vazia()
            print(f'A Fila está vazia? {esta_vazia}')
            
        else:
            print('Opção não encontrada')

    
if __name__ == "__main__":
    main()