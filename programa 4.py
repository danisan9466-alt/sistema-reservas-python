
# IMPORTS

import datetime


# FUNCION LOG

def guardar_log(mensaje):
    with open("log.txt", "a") as archivo:
        fecha = datetime.datetime.now()
        archivo.write(f"{fecha} - {mensaje}\n")



# CLASE CLIENTE

class Cliente:
    def __init__(self, nombre, cedula, edad):
        try:
            self.nombre = self.validar_nombre(nombre)
            self.cedula = self.validar_cedula(cedula)
            self.edad = self.validar_edad(edad)
        except Exception as e:
            error = f"Error al crear cliente: {e}"
            print(error)
            guardar_log(error)

    def validar_nombre(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        return nombre

    def validar_cedula(self, cedula):
        if not cedula.isdigit():
            raise ValueError("La cédula debe ser numérica")
        return cedula

    def validar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("Edad no válida")
        return edad

    def mostrar(self):
        print(f"Cliente: {self.nombre}, CC: {self.cedula}, Edad: {self.edad}")



# CLASE SERVICIO (BASE)

class Servicio:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_costo(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def mostrar(self):
        print(f"Servicio: {self.nombre}")



# CLASE HIJA: RESERVA SALA

class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 5000



# CLASE HIJA: ALQUILER EQUIPO

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Alquiler de Equipo")
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 10000



# CLASE RESERVA

class Reserva:
    def __init__(self, cliente, servicio):
        try:
            if not isinstance(cliente, Cliente):
                raise ValueError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ValueError("Servicio inválido")

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "Pendiente"

        except Exception as e:
            error = f"Error al crear reserva: {e}"
            print(error)
            guardar_log(error)

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo()
            self.estado = "Confirmada"
            print(f"Reserva confirmada para {self.cliente.nombre}")
            print(f"Costo total: {costo}")
        except Exception as e:
            error = f"Error al confirmar reserva: {e}"
            print(error)
            guardar_log(error)

    def cancelar(self):
        self.estado = "Cancelada"
        print(f"Reserva cancelada para {self.cliente.nombre}")



# PRUEBAS (SIMULACIÓN)


print("---- PRUEBA CLIENTE ----")
c1 = Cliente("Andrea", "123456", 20)
c1.mostrar()

c2 = Cliente("", "abc", -5)

print("\n---- PRUEBA SERVICIOS ----")
s1 = ReservaSala(3)
print(f"{s1.nombre} cuesta: {s1.calcular_costo()}")

s2 = AlquilerEquipo(2)
print(f"{s2.nombre} cuesta: {s2.calcular_costo()}")

print("\n---- PRUEBA RESERVAS ----")
cliente1 = Cliente("Carlos", "789456", 30)
servicio1 = ReservaSala(2)

reserva1 = Reserva(cliente1, servicio1)
reserva1.confirmar()

reserva2 = Reserva("cliente falso", servicio1)

print("\n==== SIMULACIONES ====")

# 1. Cliente válido
c1 = Cliente("Laura", "111111", 25)

# 2. Cliente inválido
c2 = Cliente("", "222", 30)

# 3. Servicio válido
s1 = ReservaSala(4)

# 4. Servicio válido
s2 = AlquilerEquipo(3)

# 5. Reserva correcta
r1 = Reserva(c1, s1)
r1.confirmar()

# 6. Reserva con cliente inválido
r2 = Reserva("falso", s1)

# 7. Reserva con servicio inválido
r3 = Reserva(c1, "servicio falso")

# 8. Otra reserva correcta
r4 = Reserva(c1, s2)
r4.confirmar()

# 9. Cliente con edad inválida
c3 = Cliente("Pedro", "333333", -10)

# 10. Cliente con cédula inválida
c4 = Cliente("Ana", "abc", 22)
