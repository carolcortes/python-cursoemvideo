def notas(*n, sit=True):
    """
    -> Função para cálculo e análise das notas inseridas.
    :param n: Notas a serem calculadas (recebe um ou mais valores)
    :param sit: Parâmetro opcional para verificar a situação geral das notas.
    :return: Retorna dicionário com o número total de notas, a maior nota inserida, a menor nota inserida,
    a média da turma e, opcionalmente, a sdef notas(*n, sit=True):
    """
    -> Função para cálculo e análise das notas inseridas.
    :param n: Notas a serem calculadas (recebe um ou mais valores)
    :param sit: Parâmetro opcional para verificar a situação geral das notas.
    :return: Retorna dicionário com o número total de notas, a maior nota inserida, a menor nota inserida,
    a média da turma e, opcionalmente, a situação geral das notas da turma.
    """
    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n)/len(n)}
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
