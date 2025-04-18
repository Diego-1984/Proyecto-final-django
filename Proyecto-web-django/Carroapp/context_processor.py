def importe_total(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for k, v in carro.items():
            total += float(v["precio"]) * v["cantidad"]
    
    
    return {"importe_total": total}

