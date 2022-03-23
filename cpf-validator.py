#cpf_validator.py
from random import randint

class cpf_validator:
    def __init__(self, cpf):
        self.cpf = cpf
    def cpf_validate(self):
        """
        Valida um CPF
        """
        #  Obtém os números do CPF e ignora outros caracteres
        self.cpf = [int(char) for char in self.cpf if char.isdigit()]

        #  Verifica se o CPF tem 11 dígitos e se não são repetidos

        if (len(self.cpf) != 11 or len(set(self.cpf)) == 1):
            return False
        
        for i in range(9, 11):
            value = sum((self.cpf[num] * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != self.cpf[i]:
                return False

        return(True)

    def cpf_generator(self):
        """
        Gera um CPF aleatório válido
        """
        # 012 (345 67(8)) 9[10]
        self.cpf = list()
        #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
        while True:
            self.temp = [self.cpf.append(randint(0,9)) for i in range(9)]
            if(self.cpf != self.cpf[::-1]):
                break

        # Primeiro digito verificador
        sum_1 = sum(a*b for a, b in zip(self.cpf[0:9], range(10, 1, -1)))
        digit_1 = (sum_1 * 10 % 11) % 10

        # Segundo digito verificador
        sum_2 = sum(a*b for a, b in zip(self.cpf[0:10], range(11, 1, -1)))
        digit_2 = (sum_2 * 10 % 11) % 10

        self.cpf.append(digit_1)
        self.cpf.append(digit_2)

        # Retorna o CPF como string
        result = ''.join(map(str, self.cpf))
        return(result)

if __name__ == "__main__":
    p = cpf_validator(input("Digite o CPF para validar: "))
    print(p.cpf_validate())

    #p = cpf_validator("")
    #print(f"O CPF gerador foi: {p.cpf_generator()}")