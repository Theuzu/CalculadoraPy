class Empregados:
    numero_empregados = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario
        self.trabalhando = False

        print(f'O empregado {self.nome_completo}, foi contratado, com um salário de {self.salario}!'
        + f'\n\t Matricula: {self.matricula_funcional}'
        + f'\n\t Email Profissional: {self.email}')

    def inicar_jornada(self, trabalhando):
        Empregados.numero_empregados += 1
        self.trabalhando = true

        print(f'O funcionário {nome_completo}, ({matricula_funcional}) iniciou sua jornada de trabalho')

    def finalizar_jornada(self):
        self.trabalhando = false

        print(f'O funcionário {nome_completo}, ({matricula_funcional}) finalizou sua jornada de trabalho')

    def receber_aumento(self, projetos_finalizados):
        raise NotImplementedError


class Desenvolvedor(Empregados):
    porcentagem_aumento = 0.08

    def __init__(self, nome_completo, email, matricula_funcional, salario, linguagens_programacao, litros_cafe, burnout):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario)
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout
        print(f'O Empregado {nome_completo}, foi contratado como desenvolvedor!)')

    def adicionar_linguagem():
        pass

    def beber_cafe(self, litros_cafe, burnout):
        if litros_cafe > 1.20:
          self.burnout = true

        else:
          self.burnout = false


class GerenteProjeto(Empregados):
    porcentagem_aumento = 0.012

    def __init__(self, nome_completo, email, matricula_funcional, salario, time, projetos_envolvidos):
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario)
        self.time = time #Fazer uma lista com os desenvolvedores do time
        self.projetos_envolvidos = projetos
        print(f'O Gerente {nome_completo}foi contratado como um Gerente!)')

    def adicionar_desenvolvedor(self, Desenvolvedor):
        self.time.append(Desenvolvedor)

    def remover_desenvolvedor():
        pass

    def participar_projeto():
        pass


#---------------------------------------------------------------------------------Exemplos

# desenvolvedor1 = Desenvolvedor(
#     nome_completo="Matheus",
#     email="matheus@example.com",
#     matricula_funcional="001",
#     salario= 50000,  # Substitua pelo salário desejado
#     linguagens_programacao=["Python", "JavaScript"],
#     litros_cafe=1.5,  # Substitua pela quantidade desejada
#     burnout=False
# )
