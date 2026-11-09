from .calculator import Calculator

def main():
    c1 = Calculator()
    c2 = Calculator()

    # Cambia esto a True para ejecutar la lista entera
    _run_list = True

    expr = [
        'c1.add("1", "1.600")',       # 2.6
        'c1.add("three", "1.600")',   # 4.6
        'c1.add("cinco", "siete")',   # 12
        'c1.add("семь", "восемь")',   # 15
        'c1.add("III", "   VIII")',  # 11
        'c1.add("三", "五")',          # 8
        'c1.add("0", "X")',           # 10
        'c2.add("ocho", "nueve")',    # 17
        'c2.sub("ocho", "nueve")',    # -1
        'c2.mul("ocho", "nueve")',    # 72
        'c2.div("ocho", "dos")',      # 4.0
        '',
        'c2.factorize("три")',        # [3]
        'c2.factorize("X")',          # [2, 5]
        'c2.factorize("ocho")',       # [2, 2, 2]
        'c2.factorize(3+5)',          # [2, 2, 2]
        'c2.factorize(27)',           # [3, 3, 3]
        'c2.factorize(1092)',         # [2, 2, 3, 7, 13]
        'c2.factorize(32768)',        # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        'c2.factorize(10952347)',     # [7, 23, 59, 1153]
        'c2.factorize(100000039)',    # [100000039]
    ] if _run_list else []

    for e in expr:
        if e:
            print(f'{e}\t-> {eval(e)}')
        else:
            print()

if __name__ == '__main__':
    main()