import random
suites = ['♡', '♢', '♤', '♧']
values = list(range(1,14))

def get_random_card(list1,list2):
    # your code here

    suite_index = random.randint(0,len(list1)-1)
    values_index = random.randint(0,len(list2)-1)

    return list1[suite_index] + " " + str(list2[values_index])
  
print(get_random_card(suites,values))

