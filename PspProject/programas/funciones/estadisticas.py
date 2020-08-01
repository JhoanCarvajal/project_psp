def timpo_actual():
    pass

def porcentajes(agre,base,reu):
    tamaño_actual = 0
    tamaño_a = 0
    tamaño_b = 0
    tamaño_r = 0
    produc_actual= 0
    tamaño_e = 0
    for a in agre:
        tamaño_actual += a.tamaño_actual
        tamaño_a += a.tamaño_actual
    for b in base:
        tamaño_actual += b.actualBase
        tamaño_b += b.actualBase
    for b in base:
        tamaño_e += b.actualDel
    for r in reu:
        tamaño_actual += r.actual
        tamaño_r += r.actual

    if tamaño_a != 0:
        tamaño_a = ((tamaño_a / tamaño_actual)*100)
        tamaño_a = round(tamaño_a, 2)
    if tamaño_b != 0:
        tamaño_b = ((tamaño_b / tamaño_actual)*100)
        tamaño_b = round(tamaño_b, 2)
    if tamaño_r != 0:
        tamaño_r = ((tamaño_r / tamaño_actual)*100)
        tamaño_r = round(tamaño_r, 2)
    if tamaño_e != 0:
        tamaño_e = ((tamaño_e / tamaño_actual)*100)
        tamaño_e = round(tamaño_e, 2)

    produc_actual = round((tamaño_actual / 60), 2)

    return tamaño_actual, tamaño_a, tamaño_b, tamaño_r, produc_actual, tamaño_e

def porcentajes_planeados(agre,base,reu):
    tamaño_actual = 0
    tamaño_a = 0
    tamaño_b = 0
    tamaño_r = 0
    tamaño_e = 0
    produc_actual= 0
    for a in agre:
        tamaño_actual += a.tamaño_planeado
        tamaño_a += a.tamaño_planeado
    for b in base:
        tamaño_actual += b.baseplan
        tamaño_b += b.baseplan
    for b in base:
        tamaño_e += b.planDel
    for r in reu:
        tamaño_actual += r.plan
        tamaño_r += r.plan

    if tamaño_a != 0:
        tamaño_a = ((tamaño_a / tamaño_actual)*100)
        tamaño_a = round(tamaño_a, 2)
    if tamaño_b != 0:
        tamaño_b = ((tamaño_b / tamaño_actual)*100)
        tamaño_b = round(tamaño_b, 2)
    if tamaño_r != 0:
        tamaño_r = ((tamaño_r / tamaño_actual)*100)
        tamaño_r = round(tamaño_r, 2)
    if tamaño_e != 0:
        tamaño_e = ((tamaño_e / tamaño_actual)*100)
        tamaño_e = round(tamaño_e, 2)

    produc_actual = round((tamaño_actual / 60), 2)
    
    return tamaño_actual, tamaño_a, tamaño_b, tamaño_r, produc_actual, tamaño_e