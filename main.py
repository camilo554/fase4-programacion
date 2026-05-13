from abc import ABC, abstractmethod
from datetime import datetime

# =========================
# LOGS
# =========================

def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass


# =========================
# CLASE ABSTRACTA PERSONA
# =========================

class Persona(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# =========================
# CLIENTE
# =========================

class Cliente(Persona):

    def __init__(self, nombre, edad):
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        if edad < 18:
            raise ClienteError("El cliente debe ser mayor de edad")

        self.__nombre = nombre
        self.__edad = edad

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Edad: {self.__edad}"

    @property
    def nombre(self):
        return self.__nombre


# =========================
# CLASE ABSTRACTA SERVICIO
# =========================

class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# SERVICIOS
# =========================

class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):
        return self.precio * horas

    def descripcion(self):
        return "Reserva de sala empresarial"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):
        return self.precio * dias

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, sesiones=1):
        return self.precio * sesiones

    def descripcion(self):
        return "Asesoría profesional especializada"


# =========================
# RESERVA
# =========================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo(self.duracion)

            self.confirmar()

            print("\n=== RESERVA EXITOSA ===")
            print(self.cliente.mostrar_info())
            print(f"Servicio: {self.servicio.descripcion()}")
            print(f"Costo total: ${costo}")
            print(f"Estado: {self.estado}")

            registrar_log(
                f"Reserva exitosa para {self.cliente.nombre}"
            )

        except Exception as e:

            registrar_log(f"Error procesando reserva: {str(e)}")

            raise ReservaError(
                "No fue posible procesar la reserva"
            ) from e


# =========================
# SIMULACIONES
# =========================

def simulaciones():

    operaciones = [

        ("Carlos", 25, ReservaSala("Sala VIP", 100), 2),

        ("Ana", 30, AlquilerEquipo("Laptop Gamer", 80), 3),

        ("Luis", 45, AsesoriaEspecializada("Asesoría IT", 150), 1),

        ("", 20, ReservaSala("Sala Básica", 50), 1),

        ("Pedro", 15, AlquilerEquipo("Proyector", 40), 2),

        ("Marta", 28, ReservaSala("Sala Premium", 120), -1),

        ("Lucia", 35, AsesoriaEspecializada("Consultoría", 200), 2),

        ("Andres", 50, AlquilerEquipo("Servidor", 300), 5),

        ("Sofia", 22, ReservaSala("Sala Reunión", 90), 4),

        ("Miguel", 40, AsesoriaEspecializada("Auditoría", 250), 3)

    ]

    for datos in operaciones:

        try:

            nombre, edad, servicio, duracion = datos

            cliente = Cliente(nombre, edad)

            reserva = Reserva(cliente, servicio, duracion)

            reserva.procesar()

        except ClienteError as ce:

            print(f"\nError de cliente: {ce}")

            registrar_log(f"ClienteError: {ce}")

        except ReservaError as re:

            print(f"\nError de reserva: {re}")

            registrar_log(f"ReservaError: {re}")

        except Exception as e:

            print(f"\nError inesperado: {e}")

            registrar_log(f"Error inesperado: {e}")

        finally:

            print("\nProceso finalizado.\n")


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    print("===== SOFTWARE FJ =====")

    simulaciones()

    print("\nSistema ejecutado correctamente.")