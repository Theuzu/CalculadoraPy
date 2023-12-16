from time import sleep

class Empregados:
    numero_empregados = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario, trabalhando):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario
        self.trabalhando = trabalhando
        self.burnout = False  # Adicione essa linha para evitar erros

        print(f'O empregado {self.nome_completo}, foi contratado, com um salário de {self.salario}!'
              + f'\n\t Matricula: {self.matricula_funcional}'
              + f'\n\t Email Profissional: {self.email}')

        Empregados.numero_empregados += 1

    def iniciar_jornada(self):
        self.trabalhando = True
        print(f'O funcionário {self.nome_completo} ({self.matricula_funcional}), iniciou sua jornada de trabalho')

    def finalizar_jornada(self):
        self.trabalhando = False
        if self.burnout:
            print(f'O funcionário {self.nome_completo} ({self.matricula_funcional}), finalizou sua jornada de trabalho sofrendo um burnout')
        else: 
            print(f'O funcionário {self.nome_completo} ({self.matricula_funcional}), finalizou sua jornada de trabalho')

    def receber_aumento(self, projetos_finalizados):
        raise NotImplementedError


class Desenvolvedor(Empregados):
    porcentagem_aumento = 0.08

    def __init__(self, nome_completo, email, matricula_funcional, salario, trabalhando, linguagens_programacao, litros_cafe, burnout):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario, trabalhando)
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout
        print(f'O Empregado {self.nome_completo}, foi contratado como desenvolvedor!)')

    def adicionar_linguagem(self, linguagem):
        self.linguagens_programacao.append(linguagem)
        print(f'O dev {self.nome_completo} aprendeu {linguagem}!')

    def beber_cafe(self, litros_cafe):
        if litros_cafe > 1.20:
            self.burnout = True
        else:
            self.burnout = False


class GerenteProjeto(Empregados):
    porcentagem_aumento = 0.012

    def __init__(self, nome_completo, email, matricula_funcional, salario, trabalhando, time, projetos_envolvidos):
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario, trabalhando)
        self.time = time  # Fazer uma lista com os desenvolvedores do time
        self.projetos_envolvidos = projetos_envolvidos
        print(f'O Empregado {self.nome_completo}, foi contratado como um Gerente!)')

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.time.append(desenvolvedor)

    def remover_desenvolvedor(self):
        pass

    def participar_projeto(self):
        pass


# ---------------------------------------------------------------------------------

desenvolvedor1 = Desenvolvedor(
    nome_completo="Matheus",
    email="matheus@example.com",
    matricula_funcional="001",
    salario=50000,  # Substitua pelo salário desejado
    trabalhando=False,  # Comece com False
    linguagens_programacao=["Python", "JavaScript"],
    litros_cafe=0,  # Comece com 0
    burnout=False,  # Comece com False
)

sleep(3.00)

desenvolvedor1.iniciar_jornada()

sleep(3.00)
desenvolvedor1.beber_cafe(1.0)  # Passe quantos litros de café o dev bebeu
desenvolvedor1.adicionar_linguagem("C++")

sleep(3.00)
desenvolvedor1.finalizar_jornada()