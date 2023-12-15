class Empregados:
    numero_empregados = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = 0
        self.trabalhando = trabalhando

        print(f'O empregado {self.nome_completo}, foi contratado, com um salário de {self.salario}!'
        + f'\n\t Matricula: {self.matricula_funcional}'
        + f'\n\t Email Profissional: {self.email}')

    def inicar_jornada(self, trabalhando):
        Empregados.numero_empregados += 1
        self.trabalhando = true

        print(f'O funcionário {nome_completo}, ({matricula_funcional}) iniciou sua jornada de trabalho')

    def finalizar_jornada(self):
        self.trabalhando = false

        print(f'O funcionário {nome_completo} finalizou sua jornada de trabalho')

    def receber_aumento(self, projetos_finalizados):
        raise NotImplementedError

