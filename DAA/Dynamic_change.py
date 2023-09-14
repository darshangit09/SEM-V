def coin_change(coins, amount):
    n = len(coins)
    table = [[float('inf')] * (amount + 1) for _ in range(n)]
    denominations = [[[] for _ in range(amount + 1)] for _ in range(n)]
    for i in range(n):
        table[i][0] = 0

    for i in range(n):
        for j in range(1, amount + 1):
            if i > 0:
                table[i][j] = table[i-1][j]
                denominations[i][j] = denominations[i-1][j]
            if j >= coins[i]:
                if table[i][j] > 1 + table[i][j-coins[i]]:
                    table[i][j] = 1 + table[i][j-coins[i]]
                    denominations[i][j] = denominations[i][j-coins[i]] + [coins[i]]

    return table, denominations

table, denominations = coin_change([1, 4, 6], 8)
print("Coins used : " + str(denominations[-1][-1]))
print("Min. number of coins : " +  str(len(denominations[-1][-1])))
print("Denominations table are as below : ")
for row in table:
    print(row)
