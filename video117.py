user_input = int(input("Number: "))
import random
def rohan_table(x):
   result = [i*x for i in range(1,11)]
   rt = random.randint(3,8)
   rand = random.randint(10,100)
   result[rt] = rand
   return result
def my_table(x):
   result = [i*x for i in range(1,11)]
   return result
roh_ret = rohan_table(user_input)
my_ret = my_table(user_input)
if roh_ret == my_ret:
   print("true")