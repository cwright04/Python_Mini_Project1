#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:19:35 2022

"""

# =============================================================================
# Your task is to write a program that reads input from a file in a specific 
#format, regarding all your friends’ names and phone numbers 
#(see attached friends.txt). Your program should store that information 
#and show the user where their friends live based on the area code of the 
#phone numbers, and the number of states where they live 
#(see attached map_areacodes_states.txt).
# =============================================================================

def pull_data(file):
    f= open(file + ".txt", "r")
    c = f.readlines()
    c = [x.strip() for x in c]
    f.close()
    return c


area_codes = pull_data("area_codes")

state_lookup = {}
for i in range(0, len(area_codes), 2):
    num = area_codes[i]
    place = area_codes[i+1]
    state_lookup[num] = place



friends = pull_data("friends")
specialChars = "!#$%^&*()-" 
for specialChar in specialChars:
    friends = [x.replace(specialChar, '') for x in friends]

a = []
for i in range(0, len(friends), 2):
    a.append((str(friends[i+1])[:3],friends[i]))

friends_tup = tuple(a)


first_tuple_elements = []
first_tuple_elements2 = []

for a_tuple in friends_tup:
    first_tuple_elements.append(a_tuple[0])
    first_tuple_elements2.append(a_tuple[1])


for i in range(0, len(first_tuple_elements)):
    check = first_tuple_elements[i]
    for key in state_lookup:
        if check == key:
            print(first_tuple_elements2[i],":",first_tuple_elements[i],",", 
                  state_lookup[key])
        
        
        
        
        


                
           
