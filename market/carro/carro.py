class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        # else:
        self.carro = carro

    def agregar(self, producto, cantidad):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "id_producto": producto.id,
                "nombre": producto.prod_nombre,
                "precio": str(self.__carcular_total(float(cantidad), float(producto.prod_precio))),
                "cantidad": cantidad,
                "imagen": producto.prod_imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = int(value["cantidad"]) + 1
                    value["precio"] = round(value["cantidad"] * producto.prod_precio, 2)
                    break
        self.guardar_carro()

    def __carcular_total(self, cantidad, producto):
        return round(producto * cantidad, 2)

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_productos(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.prod_precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
