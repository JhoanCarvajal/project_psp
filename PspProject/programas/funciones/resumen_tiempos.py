def matrizResumenTiempos(tiempos_programa, fases, cantidad_fases):
    matriz = []
    lista_fases = []
    lista_plan = []
    lista_actual = []
    lista_to_date = []
    lista_porcentaje = []

    def total_actual():
        total = 0
        for tiemp in tiempos_programa:
            if tiemp.tiempo_total:
                total += tiemp.tiempo_total
        return total
    
    for fase in fases:
        lista_fases.append(fase.nombre)
        parcial = 0
        for t in tiempos_programa:
            if t.id_fase == fase:
                if t.tiempo_total:
                    parcial += t.tiempo_total
        lista_plan.append("No Aplica")
        lista_actual.append(parcial)
        lista_to_date.append(parcial/60)
        total = total_actual()
        porcen = 0
        if total != 0:
            porcen = ((parcial / total)*100)
        if porcen != 0:
            porcen = round(porcen, 2)
        lista_porcentaje.append(porcen)

    for i in range(cantidad_fases):
        fila = []
        fila.append(lista_fases[i])
        fila.append(lista_plan[i])
        fila.append(lista_actual[i])
        fila.append(lista_to_date[i])
        fila.append(lista_porcentaje[i])
        matriz.append(fila)

    return matriz, total_actual()

