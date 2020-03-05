from evaluators import dict_of_op





def main():



    while True:
        operation = input("Enter operation ")
        try:
            evaluator = dict_of_op[operation]
            break
        except KeyError:
            print("Wrong input\n")



    x, y = int(input("Enter number ")), int(input("Enter number "))
    print(evaluator.eval(x,y))

if __name__ == '__main__':
    main()


