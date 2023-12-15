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


class Desenvolvedor(Empregados):
    porcentagem_aumento = 0.08

    def __init__(self, linguagens_programacao, litros_cafe, burnout):
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = 0.0
        self.burnout = bool(burnout)

    def adicionar_linguagem():
        pass

    def beber_cafe(self, litros_cafe, burnout):
        pass


class GerenteProjeto(Empregados):
    porcentagem_aumento = 0.012

    def __init__(self, time, projetos_envolvidos):
        self.time = time #Fazer uma lista com os desenvolvedores do time
        self.projetos_envolvidos = projetos

    def adicionar_desenvolvedor():
        pass

    def remover_desenvolvedor():
        pass

    def participar_projeto():
        pass