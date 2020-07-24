def my_power(basis, exponent):
    result = basis

    if exponent == 0:
        return 1

    elif type(exponent) == float:
        for count in range(0, abs(int(exponent-1))):
            result = result * basis
            return 1/result

    elif exponent < 0:
        for count in range(0,abs(exponent+1)):
            result = result * basis
        return 1/result

    else:
        for count in range(0, exponent-1):
            result = result * basis
        return result

#      type(basis) == int and type(exponent) == int:


if __name__ == '__main__':
    print(my_power(125,15))
    print (pow(125,15))
