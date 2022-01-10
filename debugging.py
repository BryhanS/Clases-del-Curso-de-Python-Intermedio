def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def divisors_list(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))

        try:
            if num < 0:
                raise ValueError("Ingresa un numero positivo")    

            print(divisors_list(num))
            print("Termino mi programa")
        except ValueError as ve:
            print(ve)
        
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()