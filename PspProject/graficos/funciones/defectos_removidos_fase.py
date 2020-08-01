def defectos_removidos_fase(defectos_programa, fases, cantidad_fases):
    resumen_defectos_removidos = []
    def total_defectos():
        total=0
        for defecto in defectos_programa:
            total+=1
        return total
    for fase in fases:
        lista_cantidad_actual_defectos = []
        cont = 0
        for defecto in defectos_programa:
            if defecto.id_fase_eliminacion.id == fase.id:
                cont += 1
        lista_cantidad_actual_defectos.append(fase.nombre)
        lista_cantidad_actual_defectos.append("No Aplica")
        lista_cantidad_actual_defectos.append(cont)
        lista_cantidad_actual_defectos.append(cont)
        total = total_defectos()
        porcen = 0
        if total != 0:
            porcen = ((cont / total)*100)
        lista_cantidad_actual_defectos.append(porcen)
        resumen_defectos_removidos.append(lista_cantidad_actual_defectos)

    return resumen_defectos_removidos 