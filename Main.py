from Math_function import Add, Mul, Div


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = Add(data_1, data_2)
    elif operator == "*":
        result = Mul(data_1, data_2)
    elif operator == "/":
        result = Div(data_1, data_2)
    else:
        print("masukkan operator terlebih dahulu")

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()