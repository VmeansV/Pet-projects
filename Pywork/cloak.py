my_list = ['1111111111111111', '222222222222', '33333333']
def cloak(my_list):
    def count(cntr):
        if cntr == 3:
                print('4444'.center(16))
        if len(my_list) > cntr:
            print(my_list[cntr].center(16))
            count(cntr + 1)
            print(my_list[cntr].center(16))
    count(0)
cloak(my_list)