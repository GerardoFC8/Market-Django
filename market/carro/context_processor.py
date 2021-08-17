def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated and request.session["carro"]:
        for key, value in request.session["carro"].items():
            total = total + float(value["precio"])
    else:
        request.session["carro"] = {}
        print("no estas logeado")

    # try:
    #     print("=" * 5 + "DEBUG")
    #     print(dir(request))
    #     print(dir(request.session))
    #     print(dir(request.user))
    #     print(request.user.user_permissions)
    #     print("=" * 5 + "END")
    # except Exception as exc:
    #     print("ERROR", exc)

    return {"importe_total_carro": total}
