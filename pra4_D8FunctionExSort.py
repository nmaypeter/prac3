import random

def exSort(vector, reverse = False):
    vec = vector
    if reverse == True:
        for i in range(0, len(vec)):
            for j in range(i+1, len(vec)):
                if vec[i] > vec[j]:
                    vec[i], vec[j] = vec[j], vec[i]
    else:
        for i in range(0, len(vec)):
            for j in range(i+1, len(vec)):
                if vec[i] < vec[j]:
                    vec[i], vec[j] = vec[j], vec[i]
    return vec

my_vec = random.sample(range(0, 100), 10)
print(my_vec)
print(exSort(my_vec))
print(exSort(my_vec, True))