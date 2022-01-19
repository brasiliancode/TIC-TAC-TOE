
X = 'X'
O = 'O'
VAZIO = ''

tabuleiro = [X, O, X,
             O, X, O,
             O, VAZIO, X]

jogada = 0 
# tabuleiro =  [0, 1, 2,
#               3, 4, 5,
#               6, 6, 7]

jogo_valido = True
vencedor = False

jogador1 = VAZIO
jogador2 = VAZIO

jogador1 = input('Escolha X ou O:')

if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X

for i in range(0, 9, 3):
    print(i, '|', i+1, '|', i+2, '    ', tabuleiro[i], '|', tabuleiro[i+1], '|', tabuleiro[i+2])




