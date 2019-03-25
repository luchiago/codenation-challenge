# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
import csv
import heapq 
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
reader = open('data.csv', 'r', encoding="utf8")
reader = csv.DictReader(reader)

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
    return names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
	salaries = {}
	s = []

	for row in reader:
		salaries[row['full_name']] = float(row['eur_wage'])

	for salary in sorted(salaries.items(), key=lambda x: x[1], reverse=True)[:10]:
		s.append(salary[0])

	return s
# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
	ages = {}
	a = []

	for row in reader:
		ages[row['full_name']] = int(row['age'])

	for salary in sorted(ages.items(), key=lambda x: x[1], reverse=True)[:10]:
		a.append(salary[0])

	return a
# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    count_age = {}
    
    for row in reader:
    	age = row['age']
    	if age in count_age.keys():
    		count_age[age] += 1
    	else:
    		count_age[age] = 1

    return count_age