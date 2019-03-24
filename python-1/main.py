# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
import csv
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
with open('data.csv', newline = '', encoding='utf8') as csvfile:
	reader = csv.DictReader(csvfile)


def q_1():
	nations = []
	for row in reader:
		n = row['nationality']
		if n in nations:
			pass
		else:
			nations.append(n)
	print(len(nations))
	return len(nations)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    clubs = []
    for row in reader:
    	c = row['club']
    	if c in clubs:
    		pass
    	else:
    		clubs.append(n)
    return len(clubs)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    length = 0
    names = []
    for row in reader:
    	if length == 20:
    		break
    	else:
    		names.append(row['full_name'])
    		length += 1

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    pass

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    pass

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    pass
