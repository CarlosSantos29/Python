sobre_a_variavel = input('Digite algo alaeatorio: ')

print(f'Qual o tipo desse valor solicitado? {type(sobre_a_variavel)}')# retorna o tipo da variavel criada.
print(f'É um espaço? {sobre_a_variavel.isspace()}')# retorna um valor booleano se a variavel criada é um espaço.
print(f'É um valor numerico? {sobre_a_variavel.isnumeric()}') # retorna um valor booleano se a variavel criada é um numero.
print(f'É uma palavra ou letra? {sobre_a_variavel.isalpha()}') # retorna um valor booleano se a variavel criada é uma letra ou palavra.
print(f'É nessa variavel tem mistura de ltras com numeros? {sobre_a_variavel.isalnum()}')# retorna um valor booleano se a variavel criada tem uma mistura de letras com numeros.
print(f'Todas as letras estão em maisculas? {sobre_a_variavel.isupper()}')# retorna um valor booleano se a variavel criada todas as letras estão em maisculas.
print(f'Todas as letras estão em minusculas? {sobre_a_variavel.islower()}')# retorna um valor booleano se a variavel criada todas as letras estão em minusculas.
print(f'A primeira letra é maiscula? {sobre_a_variavel.istitle()}') #retorna um valor booleano se a variavel criada a primeira letra é maiscula (capitalizada).