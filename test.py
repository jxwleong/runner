import psutil
import subprocess
import random

print("hello world!")

for _ in range(1):
    print(psutil.cpu_percent(interval=1, percpu=True))

no_of_processor = psutil.cpu_count(logical=True)

# Must have at least one core
random_processor = random.randint(1, no_of_processor)


def number_to_list_of_ascending_integer(num, start_number=0):
    list_ = []
    for x in range(start_number, num + start_number):
        list_.append(x)
    return list_


print(random_processor)
cpu = number_to_list_of_ascending_integer(random_processor)
print(cpu)