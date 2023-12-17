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

        print(f'{self.nome_completo}, foi contratado, com um salário de {self.salario}!'
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

    def __init__(self, nome_completo, email, matricula_funcional, salario, trabalhando, linguagens_programacao, litros_cafe, burnout, projetos_finalizados):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario, trabalhando)
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout
        self.projetos_finalizados = 0
        print(f'O Empregado {self.nome_completo}, foi contratado como desenvolvedor!)')

    def adicionar_linguagem(self, linguagem):
        self.linguagens_programacao.append(linguagem)
        print(f'O dev {self.nome_completo} aprendeu {linguagem}!')

    def beber_cafe(self, litros_cafe):
        if litros_cafe > 1.20:
            self.burnout = True
        else:
            self.burnout = False
            print(f'O dev {self.nome_completo} bebeu {litros_cafe} litros de café')

    def receber_aumento(self, projetos_finalizados):
                if projetos_finalizados >= 3 and len(self.linguagens_programacao) >=2:
                    salario_aumentado = (self.salario * self.porcentagem_aumento) + self.salario
                    print(f'O dev {self.nome_completo}, recebeu um aumento de R$ {self.salario} para R$ {salario_aumentado}.')
                    self.salario = salario_aumentado
                    
                else:
                    print(f'O dev {self.nome_completo}, ainda não atende aos requisitos para receber um aumento')


class GerenteProjeto(Empregados):
    porcentagem_aumento = 0.012

    def __init__(self, nome_completo, email, matricula_funcional, salario, trabalhando, time, projetos_envolvidos):
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario, trabalhando)
        self.time = time  # Fazer uma lista com os desenvolvedores do time
        self.projetos_envolvidos = projetos_envolvidos
        print(f'O Empregado {self.nome_completo}, foi contratado como um Gerente!)')

    def adicionar_desenvolvedor(self, time):
        self.time.append(Desenvolvedor)

    def remover_desenvolvedor(self):
        pass

    def participar_projeto(self):
        pass


# ---------------------------------------------------------------------------------

desenvolvedor1 = Desenvolvedor(
    nome_completo="Matheus Santos",
    email="matheus@example.com",
    matricula_funcional="001",
    salario=10000,  # Substitua pelo salário desejado
    trabalhando=False,  # Comece com False
    linguagens_programacao=["Python", "JavaScript"],
    litros_cafe=0,  # Comece com 0
    burnout=False,  # Comece com False
    projetos_finalizados=0, #Comece com 0
)

sleep(3.00)
desenvolvedor1.iniciar_jornada()
sleep(2.00)
desenvolvedor1.beber_cafe(1.0)  # Passe quantos litros de café o dev bebeu
sleep(2.00)
desenvolvedor1.adicionar_linguagem("C++") # Adicione uma linguagem que o dev aprendeu
sleep(2.00)
desenvolvedor1.receber_aumento(3) # Passe quantos projetos o dev finalizou
sleep(2.00)
desenvolvedor1.finalizar_jornada()