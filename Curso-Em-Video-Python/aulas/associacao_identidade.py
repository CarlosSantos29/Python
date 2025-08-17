algo = input('Digite qualquer coisa: ')
print(f'A mensagem enviada é um numero? {algo.isnumeric()}')# é um numero
print(f'A mensagem enviada é do alfabeto? {algo.isalpha()}')# é uma letra/palavra
print(f'A mensagem enviada é alfanumerico? {algo.isalnum()}')# é uma letra/palavra com numeros.
print(f'A palavra a seguir é tudo em maisculo? {algo.isupper()}')