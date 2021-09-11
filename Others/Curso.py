# 82

# Datetime
import datetime
now = datetime.datetime.now()
now_date = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

# Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
# \n nova linha | \t tabulação | title() iniciais em maiúsculo
message = "\n\tHello, " + full_name.title() + "! - " + now_date
print(message)

# Strip
language = " Python "
print(language.strip())
# strip() remove espaços | lstrip / rstrip (left/right)

# Listas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()) # primeiro item da lista
print(bicycles[-1].title()) # último item da lista
bicycles[0] = 'bmx' # altera o item da lista
bicycles.append('bmx') # insere ao final da lista
bicycles.insert(0, 'bmx') # insere na posição informada, desloca os demais
del bicycles[0] # remove o item informado
new_bicycles = bicycles.pop() # remove o último item da lista e insere em uma variável
bicycles.pop(2) # remove o item 3 da lista
bicycles.remove('redline') # remove de acordo com o valor informado
too_expensive = 'redline' | bicycles.remove(too_expensive) # remove apenas apaga a primeira ocorrência

# Sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # ordena alfabeticamente
cars.sort(reverse=True) # ordena alfabeticamente - reverso
print(sorted(cars)) # imprime a lista sem alterar a original

