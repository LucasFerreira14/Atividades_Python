# Criar classe pessoa com nome, tel, RG, CPF

class Pessoa:
    def __init__(self, nome, tel, rg, cpf):
        self.nome = nome
        self.tel = tel
        self.rg = rg
        self.cpf = cpf

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Telefone: ", self.tel)
        print("RG: ", self.rg)
        print("CPF: ", self.cpf)

# Medico possui CRM, CPF, RG, nome, tel, salario, especialidade


class Medico(Pessoa):
    def __init__(self, nome, tel, rg, cpf, crm, salario, especialidade):
        super().__init__(nome, tel, rg, cpf)
        self.__crm = crm
        self.__salario = salario
        self.especialidade = especialidade

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("CRM: ", self.__crm)
        print("Especialidade: ", self.especialidade)


# Paciente possui nome, RG, CPF, endereco, tel, data de nasc, localizacao na clinica


class Paciente(Pessoa):
    def __init__(self, nome, tel, rg, cpf, endereco, data_nascimento, localizacao, medico_responsavel):
        super().__init__(nome, tel, rg, cpf)
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.localizacao = localizacao
        self.medico_responsavel = medico_responsavel

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Telefone: ", self.tel)
        print("RG: ", self.rg)
        print("CPF: ", self.cpf)
        print("Endereço: ", self.endereco)
        print("Data de Nascimento: ", self.data_nascimento)
        print("Andar: ", self.localizacao.get_andar())
        print("Quarto: ", self.localizacao.get_quarto())
        print("Médico Responsavel: ", self.medico_responsavel)


# Quarto possui numero, andar


class Quarto:
    def __init__(self, quarto, andar):
        self.__quarto = quarto
        self.__andar = andar

    def get_andar(self):
        return self.__andar

    def get_quarto(self):
        return self.__quarto

# Historico possui data, horario, obs do medico, nome do medico


class Historico:
    def __init__(self, data, horario, obs_do_medico, nome_do_medico):
        self.data = data
        self.horario = horario
        self.obs_do_medico = obs_do_medico
        self.nome_do_medico = nome_do_medico

    def exibe_resultado(self):
        print("Data: ", self.data)
        print("Horário: ", self.horario)
        print("Nome do Médico: ", self.nome_do_medico)
        print("Observação do Médico: ", self.obs_do_medico)

# Criação do Quarto


quarto01 = Quarto("A", 1)
quarto02 = Quarto("B", 2)


# Criação de Médico

medico01 = Medico("Fernando de Paula Filho", 965038045,
                  753159662, 25424525436, 35689, 8000, "Ortopedia")

medico02 = Medico("Marcelo de Oliveira", 965878547,
                  542986143, 25455502065, 25415, 7000, "Traumatologia")


# Criação de Paciente

paciente01 = Paciente("Lucas Ferreira", 11985236547,
                      74558695, 53565841432, "Rua 01", "18/02/1996", quarto01,
                      medico01.nome)
paciente02 = Paciente("Lucas Silva", 519524687321, 652549223,
                      85634829751, "Rua 02", "25/10/2002", quarto02,
                      medico02.nome)

# Criação do Historico


historico_paciente01 = Historico(
    "23/10/2020", "18:52:03", "Alta para o Paciente", medico01.nome)
historico_paciente02 = Historico(
    "15/10/2020", "08:40:58", "Mais 2 dias de UTI", medico02.nome)


def resultado(n, quarto, paciente, medico, historico):
    print("=" * 50)
    print("                     Médico", n)
    print("=" * 50)
    medico.exibir_dados()
    print("-" * 50)
    print("                    Paciente", n)
    print("-" * 50)
    paciente.exibir_dados()
    print("-" * 50)
    historico.exibe_resultado()
    print("=" * 50)


resultado("01", quarto01, paciente01, medico01, historico_paciente01)
resultado("02", quarto02, paciente02, medico02, historico_paciente02)

input()