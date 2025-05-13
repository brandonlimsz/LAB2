def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5, 67, 32)")

def calc_average(stringlist):
    print("calc_average")
    total=0.0
    for eachstr in stringlist:
        total=total+float(eachstr)
    average = total/len(stringlist)
    print(f'average: {average}')
    return average


def get_user_input():
    print("List of floats")
    inputstr=input("get_user_input: ")
    strlist=inputstr.split(",")
    print(f'strlist: {strlist}')
    return strlist

def find_min_max(stringlist):
    print("find_min_max")
    floatlist=[]
    for eachstr in stringlist:
        floatlist.append(float(eachstr))
    min_max=[]
    min_max.append(min(floatlist))
    min_max.append(max(floatlist))
    print('The minimum and maximum are respectivley, ',min_max)

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print("Ex3")
    display_main_menu()
    temp_list =get_user_input()
    calc_average(temp_list)
    find_min_max(temp_list)

main()
