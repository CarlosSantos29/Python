# e and v v v (1 1 1_),    v f f (1 0 0),  fff (0 0 0)
# ou or v v v (1 1 1),    v f v (1 0 1),  fff (0 0 0)
# ! not v = f (1 = 0),    f = v (0 = 1)

saldo = 1000
saque = 250
limite = 200
conta_especial = True 

#print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

#print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

print(1 == True)
print(0 != False)
print(0 == False)


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
print(f'O saldo da conta normal é suficiente? {conta_normal_com_saldo_suficiente}')

conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
print(f'E a conta especial, tem saldo suficente? {conta_especial_com_saldo_suficiente}')

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)

#and = 1 1 1   1 0 0  0 0 0
#or = 1 1 1  1 0 1  0 0 0
#not = 1 = 0  0 = 1
