from time import sleep


class Empregados:
    numero_empregados = 0

    def __init__(
        self,
        nome_completo,
        email,
        matricula_funcional,
        salario,
        trabalhando,
        projetos_finalizados,
    ):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario
        self.trabalhando = trabalhando
        self.projetos_finalizados = projetos_finalizados
        self.burnout = False  # Adicionei essa linha para evitar erros

        print(
            f"{self.nome_completo}, foi contratado, com um salário de {self.salario}!"
            + f"\n\t Matricula: {self.matricula_funcional}"
            + f"\n\t Email Profissional: {self.email}"
        )

        Empregados.numero_empregados += 1

    def iniciar_jornada(self):
        self.trabalhando = True
        print(
            f"O funcionário {self.nome_completo} ({self.matricula_funcional}), iniciou sua jornada de trabalho"
        )

    def finalizar_jornada(self):
        self.trabalhando = False
        if self.burnout:
            print(
                f"O funcionário {self.nome_completo} ({self.matricula_funcional}), finalizou sua jornada de trabalho sofrendo um burnout"
            )
        else:
            print(
                f"O funcionário {self.nome_completo} ({self.matricula_funcional}), finalizou sua jornada de trabalho"
            )

    def receber_aumento(self, projetos_finalizados):
        raise NotImplementedError


class Desenvolvedor(Empregados):
    porcentagem_aumento = 0.08

    def __init__(
        self,
        nome_completo,
        email,
        matricula_funcional,
        salario,
        trabalhando,
        projetos_finalizados,
        linguagens_programacao,
        litros_cafe,
        burnout,
    ):
        super(Desenvolvedor, self).__init__(
            nome_completo,
            email,
            matricula_funcional,
            salario,
            trabalhando,
            projetos_finalizados,
        )
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout
        print(f"O Empregado {self.nome_completo}, foi contratado como desenvolvedor!)")

    def adicionar_linguagem(self, linguagem):
        self.linguagens_programacao.append(linguagem)
        print(f"O dev {self.nome_completo} aprendeu {linguagem}!")

    def beber_cafe(self, litros_cafe):
        if litros_cafe > 1.20:
            self.burnout = True
        else:
            self.burnout = False
            print(f"O dev {self.nome_completo} bebeu {litros_cafe} litros de café")

    def terminar_projeto(self, quantidade):
        print(f"O Dev {self.nome_completo} terminou {quantidade} projeto(s)")
        self.projetos_finalizados += quantidade

    def receber_aumento(self, projetos_finalizados):
        if self.projetos_finalizados >= 2 and len(self.linguagens_programacao) >= 2:
            salario_aumentado = (self.salario * self.porcentagem_aumento) + self.salario
            print(
                f"O dev {self.nome_completo}, recebeu um aumento de R$ {self.salario} para R$ {salario_aumentado}"
            )
            self.salario = salario_aumentado

        else:
            print(
                f"O dev {self.nome_completo}, ainda não atende aos requisitos para receber um aumento"
            )


class GerenteProjeto(Empregados):
    porcentagem_aumento = 0.012

    def __init__(
        self,
        nome_completo,
        email,
        matricula_funcional,
        salario,
        trabalhando,
        projetos_finalizados,
        time=None,
        projetos_envolvidos=None,
    ):
        super(GerenteProjeto, self).__init__(
            nome_completo,
            email,
            matricula_funcional,
            salario,
            trabalhando,
            projetos_finalizados,
        )
        self.time = [] if time is None else time
        self.projetos_envolvidos = projetos_envolvidos
        print(f"O Empregado {self.nome_completo}, foi contratado como um Gerente!")

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.time.append(desenvolvedor)
        print(
            f"{desenvolvedor.nome_completo} foi adicionado ao time do gerente {self.nome_completo}."
        )

    def remover_desenvolvedor(self, desenvolvedor):
        if desenvolvedor in self.time:
            self.time.remove(desenvolvedor)
            print(
                f"{desenvolvedor.nome_completo} foi removido do time do gerente {self.nome_completo}."
            )
        else:
            print(
                f"{desenvolvedor.nome_completo} não faz parte do time do gerente {self.nome_completo}."
            )

    def participar_projeto(self, projeto):
        self.projetos_envolvidos.append(projeto)
        print(f"O gerente {self.nome_completo} está entrou no projeto: {projeto}")

    def terminar_projeto(self, quantidade):
        print(f"O gerente {self.nome_completo} terminou {quantidade} projeto(s)")
        self.projetos_finalizados += quantidade

    def sair_projeto(self, projeto):
        if projeto in self.projetos_envolvidos:
            self.projetos_envolvidos.remove(projeto)
            print(f"O gerente {self.nome_completo} saiu do projeto: {projeto}")
        else:
            print(f"O gerente {self.nome_completo} não estava neste projeto")

    def receber_aumento(self, projetos_finalizados):
        if self.projetos_finalizados >= 2 and len(self.projetos_envolvidos) >= 1:
            salario_aumentado = (self.salario * self.porcentagem_aumento) + self.salario
            print(
                f"O Gerente {self.nome_completo}, recebeu um aumento de R$ {self.salario} para R$ {salario_aumentado}"
            )
            self.salario = salario_aumentado

        else:
            print(
                f"O gerente {self.nome_completo}, ainda não atende aos requisitos para receber um aumento"
            )


# ---------------------------------------------------------------------------------

desenvolvedor1 = Desenvolvedor(
    nome_completo="Matheus Santos",
    email="matheus@example.com",
    matricula_funcional="001",
    salario=10000.00,  # Substitua pelo salário desejado
    trabalhando=False,  # Comece com False
    linguagens_programacao=["Python", "JavaScript"],
    litros_cafe=0,  # Comece com 0
    burnout=False,  # Comece com False
    projetos_finalizados=0,  # Comece com 0
)

sleep(2.00)
# Iniciando jornada de trabalho
desenvolvedor1.iniciar_jornada()
sleep(2.00)
# Bebendo café
desenvolvedor1.beber_cafe(1.0)  # Passe quantos litros de café o dev bebeu
sleep(2.00)
# Adicionando linguagens
desenvolvedor1.adicionar_linguagem("C++")  # Adicione uma linguagem que o dev aprendeu
# Terminar projetos para determinar o aumento de salário
desenvolvedor1.terminar_projeto(3)  # Passe quantos projetos foram finalizados
sleep(2.00)
# Recebendo o aumento do salario
desenvolvedor1.receber_aumento(desenvolvedor1.projetos_finalizados)
sleep(3.00)
# Finalizando jornada de trabalho
desenvolvedor1.finalizar_jornada()

sleep(1.00)
gerente_projeto1 = GerenteProjeto(
    nome_completo="Lucas oliveira",
    email="lucas@example.com",
    matricula_funcional="002",
    salario=15000.00,  # Substitua pelo salário desejado
    trabalhando=False,  # Comece com False
    projetos_finalizados=0,  # Comece com 0
    projetos_envolvidos=["Projeto Vendas"],
)

sleep(2.00)
# Iniciando jornada de trabalho
gerente_projeto1.iniciar_jornada()
sleep(2.00)
# Adicionando um novo projeto
gerente_projeto1.participar_projeto(
    "Projeto Segurança"
)  # Adicione o nome de um projeto
sleep(2.00)
# Adicionando desenvolvedor ao time do gerente de projeto
gerente_projeto1.adicionar_desenvolvedor(
    desenvolvedor1
)  # passe um dos desenvolvedores definidos anteriormente
sleep(2.00)
# Removendo desenvolvedor do time do gerente de projeto
gerente_projeto1.remover_desenvolvedor(
    desenvolvedor1
)  # passe um dos desenvolvedores definidos anteriormente
sleep(2.00)
# Terminar projetos para determinar o aumento de salário
gerente_projeto1.terminar_projeto(3)  # Passe quantos projetos foram finalizados
sleep(2.00)
# Saindo de um projeto
gerente_projeto1.sair_projeto("Projeto Segurança")
sleep(2.00)
# Recebendo o aumento do salario
gerente_projeto1.receber_aumento(gerente_projeto1.projetos_finalizados)
sleep(3.00)
# Finalizando jornada de trabalho
gerente_projeto1.finalizar_jornada()
