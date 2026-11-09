import math

class Calculator:
    # Diccionario multilingüe para dígitos del 0 al 9
    NUM_MAP = {
        # Inglés
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        # Alemán
        "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
        "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
        # Español
        "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
        "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
        # Ruso (Cirílico)
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
        "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
        # Chino
        "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
        "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
        # Números Romanos (I al X)
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
        "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10
    }

    def _to_number(self, val):
        """Convierte strings (números, palabras multilingües, romanos) a int/float."""
        if isinstance(val, (int, float)):
            return val

        if isinstance(val, str):
            s = val.strip().lower()
            
            # 1. Intentar convertir a int o float directamente (ej. "1", "1.600")
            try:
                if "." in s:
                    return float(s)
                return int(s)
            except ValueError:
                pass

            # 2. Buscar en el mapa multilingüe y romanos
            if s in self.NUM_MAP:
                return self.NUM_MAP[s]

        raise ValueError(f"No se puede convertir '{val}' a número.")

    def add(self, a, b):
        return self._to_number(a) + self._to_number(b)

    def sub(self, a, b):
        return self._to_number(a) - self._to_number(b)

    def mul(self, a, b):
        return self._to_number(a) * self._to_number(b)

    def div(self, a, b):
        return self._to_number(a) / self._to_number(b)

    def factorize(self, n):
        """Devuelve la lista de factores primos de n."""
        num = int(self._to_number(n))
        factors = []
        
        # Factor de 2
        while num % 2 == 0:
            factors.append(2)
            num //= 2
        
        # Factores impares a partir de 3
        i = 3
        while i * i <= num:
            while num % i == 0:
                factors.append(i)
                num //= i
            i += 2
            
        if num > 1:
            factors.append(num)
            
        return factors