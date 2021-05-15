#!/usr/bin/env python3

import itertools
def dependent(column):
    relation = [ ] # this list is for dependencies
    # access the column where there is at least one 1 
    for temp_row in range(n):
        if column[temp_row] == 1:
            relation.append(temp_row )
    return relation


def count_indep_prob(variable):
    """this function takes variable number <starts from 1> and counts its indep prob """
    #print('value of variable is ', variable)
    required_column = []
    for _ in range(M):
        required_column.append(data[_][variable])
        # required column contains data_col  
    ##########################################
    prob_list = [ ]
    #print(allowed_values[variable])
    for al_data_val in allowed_values[variable]:
        #print(allowed_values[variable])
        temp = required_column.count(str(al_data_val))
        prob_list.append(temp / M )
       #'%.50f' % 0.1
    prob_list = [ round(element , 5) for element in prob_list]
    print(*prob_list)

def count_dep_prob(variable):
    probs = []    
    for QQQ , i in enumerate(dep_dependent):
        if  QQQ != variable:
            continue
        #print('i',i)
        #print('variable' , variable)
        if len(i) > 0 :
            iterables = [allowed_values[QQQ] for h in i]
            combinations = list(itertools.product(*iterables))
            for pos in allowed_values[QQQ]:
                for comb in combinations:
                    count1 = 0
                    count2 = 0.001
                    for data_point in data:
                        part = [data_point[k] for k in i]
                        if data_point[QQQ] == pos and part == list(comb):
                            count1 += 1
                        if part == list(comb):
                            count2 += 1
                    probs.append(count1 / count2)
                    probs = [ round(element , 4) for element in probs]    
            print(*probs)
n  = int(input())

allowed_values = [ ]
dependancies = [ ]
data = [ ]
for line in range(n):

    read = input()
    read = read.split(', ')
    allowed_values.append(read)
    
for lines in range(n):
    read_new = list(input().split(' '))
    
    read_new = list(map(int , read_new))
    dependancies.append(read_new)
    
M = int(input())

for new_lines in range(M):
    
    read_data = list(input().split(','))
    data.append(read_data)
    

independent = [ ]
temp  = 0

dep_dependent = [ ] # dependencies list, list of list 
for row in range(n):
    test_row = []
    for column in range(n):
        
        test_row.append(dependancies[column][row])
        
        
    if any(test_row):
        dep_dependent.append(dependent(test_row))
        
        
    else:
        dep_dependent.append([])
        independent.append(row  )   # col number
        
        
all_data_types = [ ]   

#print(allowed_values)
#print(len(allowed_values)) # rwo
#print(len(allowed_values[0]))
max_pos_col = []
for col_len in allowed_values:
    max_pos_col.append(len(col_len))


for R in range(len(allowed_values)):
    for C in range(len(allowed_values[R])):
        #print(allowed_values[R][C])
        if allowed_values[R][C] not in all_data_types: # getting all possible values variables can take
            all_data_types.append(allowed_values[R][C])
            

            
#print(all_data_types)           
all_data_types = list(dict.fromkeys(all_data_types))

#print('dependent',dep_dependent)
#print('independent',independent)

#print('allowed values of all variables UNIQUE', all_data_types)

          
        
for variable in range(0 , n): # cols in data 
    if variable in independent:
        count_indep_prob(variable)    
    else:  
        
        count_dep_prob(variable)

