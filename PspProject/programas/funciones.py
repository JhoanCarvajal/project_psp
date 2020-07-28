def matrizResumenTiempos(tiempos_programa, fases, cantidad_fases):
    matriz = []
    lista_fases = []
    lista_plan = []
    lista_actual = []
    lista_to_date = []
    lista_porcentaje = []
    
    for fase in fases:
        lista_fases.append(fase.nombre)
        parcial = 0
        for t in tiempos_programa:
            if t.id_fase == fase:
                parcial += t.tiempo_total
        lista_plan.append("No Aplica")
        lista_actual.append(parcial)
        lista_to_date.append(parcial)
        total = 0
        for tiemp in tiempos_programa:
            if parcial != 0:
                total += tiemp.tiempo_total
        porcen = 0
        porcentaje_redondeado = 0
        if total != 0:
            porcen = ((parcial / total)*100)
        if porcen != 0:
            porcentaje_redondeado = round(porcen, 2)
        lista_porcentaje.append(porcentaje_redondeado)

    for i in range(cantidad_fases):
        fila = []
        fila.append(lista_fases[i])
        fila.append(lista_plan[i])
        fila.append(lista_actual[i])
        fila.append(lista_to_date[i])
        fila.append(lista_porcentaje[i])
        matriz.append(fila)

    return matriz