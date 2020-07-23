import numpy as np
#Euclidian Distance

'''Problem: given three different observations (A,B,C) provide which one is closely related to C in term of E.D '''

#Distance formula
''' sqrt((a1-b1)^2+ (a2-b2)^2 +...+ (an-bn)^2)'''

# 1 Define table or lists for data
person_a = [7,1,9, 1,3]
person_b = [4,9, 1,3,1]
person_c = [9, 1,7,2,2]

# 2 Calculate Distance 
#A & C 
a_c = 0.0

for x in range(len(person_a)):
    temp = (person_a[x]-person_c[x])**2
    a_c +=temp 
a_c = np.sqrt(a_c)

  
#B & C 
b_c= 0.0
for x in range(len(person_b)):
    temp = (person_b[x]-person_c[x])**2
    b_c +=temp 
b_c = np.sqrt(b_c)


# 3 Compare results & Conlusion 
if(a_c < b_c):
    print("Person C is closer (more alike) to person A with a score of: ", a_c)
else:
    print("Person C is closer (more alike) to person B with a score of: ",b_c)



