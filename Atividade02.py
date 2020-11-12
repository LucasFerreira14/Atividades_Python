def calcular_salario(dicionario, nome):
    for i in dicionario:
        if nome in dicionario:
            if i == nome:
                if dicionario[i][2] == "DESENVOLVEDOR":
                    if dicionario[i][1] >= 2000:
                        x = dicionario[i][1] * 0.15
                        resultado = dicionario[i][1] - x
                        return resultado
                    else:
                        x = dicionario[i][1] * 0.05
                        resultado = dicionario[i][1] - x
                        return resultado

                elif dicionario[i][2] == "ANALISTA":
                    if dicionario[i][1] >= 3500:
                        x = dicionario[i][1] * 0.20
                        resultado = dicionario[i][1] - x
                        return resultado
                    else:
                        x = dicionario[i][1] * 0.10
                        resultado = dicionario[i][1] - x
                        return resultado

                elif dicionario[i][2] == "GERENTE":
                    if dicionario[i][1] >= 4000:
                        x = dicionario[i][1] * 0.25
                        resultado = dicionario[i][1] - x
                        return resultado
                    else:
                        x = dicionario[i][1] * 0.15
                        resultado = dicionario[i][1] - x
                        return resultado

                else:
                    raise TypeError
        else:
            raise KeyError
