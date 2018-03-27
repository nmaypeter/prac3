import random

def cal_mean(vec):
    def cal_sum(vec):
        return sum(vec[0:len(vec)])
    def cal_num(vec):
        return len(vec)
    return cal_sum(vec) / cal_num(vec)

my_vec = random.sample(range(0, 100), 10)
print(my_vec)
print(sum(my_vec[0:len(my_vec)]))
print(cal_mean(my_vec))