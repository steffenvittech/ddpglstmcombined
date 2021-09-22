import time

from States import memory
import data_resiver as dr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rates = dr.getdata()
    state = []
    print(list(rates[0]))
    for i in range(0,len(list(rates[0]))):
        state.append(0)
    print(state)

    mem = memory.mem(10,state)
    print(mem.state_mem)
    for i in rates:
        mem.add_data(list(i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
