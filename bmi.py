def calculate_bmi(height, weight):
    print("height="+str(height))
    print("weight="+str(weight))
    bmi= weight/(height**2)
    print("bmi=",round(bmi,2))

    if bmi<18.5:
        print("Under weight")
        return -1
    elif bmi>25.0:
        print("Over weight")
        return 1
    else:
        print("Nomral weight")
        return 0
calculate_bmi(1.73, 57)