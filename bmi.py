def calculate_bmi(height, weight):
    print("height="+str(height))
    print("weight="+str(weight))
    bmi= weight/(height**2)
    print("bmi="+str(bmi))

calculate_bmi(1.73, 57)