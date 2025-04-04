def importe_total(request):
    total = 0
    # if request.user.is_authenticated:
    #     carro = request.session.get("carro", {})  # Si no existe, devuelve un diccionario vacío
    #     for k, v in carro.items():
    #         total += float(v["precio"]) * v["cantidad"]
    
    return {"importe_total": total}

