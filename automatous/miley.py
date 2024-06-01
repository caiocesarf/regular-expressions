class VendingMachine:
    def __init__(self):
        self.total = 0

    def insert_coin(self, coin):
        self.total += coin
        if self.total >= 100:
            self.total -= 100
            return 1
        else:
            return 0

# Função para processar a sequência de moedas
def process_coins(coins):
    machine = VendingMachine()
    outputs = []
    for coin in coins:
        output = machine.insert_coin(coin)
        outputs.append(output)
    return outputs

if __name__ == "__main__":
    coins = [50, 25, 50, 100, 25, 50, 100, 25, 25, 25, 25, 50, 50, 100, 50, 50, 25, 25, 25, 25, 100]
    outputs = process_coins(coins)
    print(outputs)  # Saída esperada: [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]