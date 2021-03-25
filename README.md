# Gerador_de_juro_F2

## Sistema para empréstimo de valores para devolução com acréscimo.

# Parametro default para construção do objeto Empréstimo.hoje = date.today()

# Parametro usado para cálculo de taxa (risk) será igual a 8%

# Para cada negação da função (pagou) será chamada função (acrescenta_juro) e a função (aumenta_risco)

## Função pagou retorna True.

## Função (acrescenta_juro) retorna o valor do juro_base + 9.6

# Preciso ter o retorno das operações com as datas subtração e adição.

\*\* Verificar se houve pagamento

\*\* Cada um terá sua margem de risco(risk).

\*\* Para cada inadimplência o (risk aumentara) consequentemente seu risco será maior!

\*\* De forma contrária à número 5 está diminui o risk em caso de pagamento antecipado.

\*\* Caso haja inadimplência além do passo 5 ocorrerá acrescimo em cima do valor total.

\*\* Inicialmente o valor precisa ser devolvido com acréscimo de taxa inicial pré definida.
\*\* Só vou acrescer juro se passar do dia.


Precisa registrar os emprestimos para que seja verificado no loop principal

# # Cria-se classe para registrar os emprestimos, 


Preciso verificar se existem emprestimos em aberto