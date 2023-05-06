import csv
class PlanAhorro:
    __codigo= ""
    __modelo= ""
    __version= ""
    __valor= ""
    __cant_cuotas=""
    __cant_cuotas_licitacion=""
    def __init__(self, codigo, modelo, version, valor, cant_cuotas, cant_cuotas_licitacion):
        self.codigo = codigo
        self.modelo = modelo
        self.version = version
        self.valor = valor
        self.cant_cuotas = cant_cuotas
        self.cant_cuotas_licitacion = cant_cuotas_licitacion
    
    def actualizar_valor(self, valor):
        self.valor = valor
    
    def calcular_valor_cuota(self):
        valor_cuota = (self.valor/self.cant_cuotas) + self.valor * 0.10
        return valor_cuota
    
    def calcular_monto_licitacion(self):
        monto_licitacion = self.cant_cuotas_licitacion * self.calcular_valor_cuota()
        return monto_licitacion
