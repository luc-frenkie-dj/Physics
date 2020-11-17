from math import sqrt

def calculate_hyp1(adj, opp):
    src = adj**2 + opp**2
    answer = sqrt(src)
    return round(answer, 2)

def calculate_adj1(hyp, opp):
    src = hyp**2 - opp**2
    answer = sqrt(src)
    return round(answer, 2)

def calculate_opp(hyp, adj):
    src = hyp**2 + adj**2
    answer = sqrt(src)
    return round(answer, 2)

run = True

while run == True:
    run = True
    print("--------------------")
    print(" Physics Calculator ")
    print("--------------------")
    print("1) Calculate Hypotenuse")
    print("2) Calculate Adjacent")
    print("3) Calculate Opposite")
    print("4) Press q to quit")
    option = input("Choose option: ")

    if option == '1':
        adj = float(input("Enter the value for adjacent: "))
        opp = float(input("Enter the value for opposite: "))
        print(calculate_hyp1(adj, opp))

    elif option == '2':
        hyp = float(input("Enter the value for hypotenuse: "))
        opp = float(input("Enter the value for opposite: "))
        print(calculate_adj1(hyp, opp))
    
    elif option == 'q':
        run = False

    else:
        hyp = float(input("Enter the value for hypotenuse: "))
        adj = float(input("Enter the value for adjacent: "))
        print(calculate_opp(hyp, adj))