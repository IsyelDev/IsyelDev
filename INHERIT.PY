class Militar:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self._activo = True  # Encapsulación correcta

    def __str__(self):
        return f'{self._nombre}, edad {self._edad}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena válida")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad: int):
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    @property
    def activo(self):
        return self._activo

    def encender(self):
        """Alterna el estado activo del militar"""
        self._activo = not self._activo


def main():
    militares = [
        Militar("Elmer", 20),
        Militar("Manuel", 28),
        Militar("Carlos", 25),  # Cambié el duplicado por otro nombre
    ]

    for mil in militares:
        print(mil)
        print(f"{mil.nombre} tiene {mil.edad} años.")  # Evitar acceso directo a _nombre y _edad
        mil.encender()

        estado = "Encendido" if mil.activo else "Apagado"
        print(f"Estado de {mil.nombre}: {estado}\n")


class CocheDeportivo(Militar):
    def __init__(self,nombre,edad,cv):
        super().__init__(nombre,edad)
        self.cv =cv

    def __str__(self):
        return f'{self.nombre} ,Edad {self.edad} cv is {self.cv}'


cochesito = CocheDeportivo("Elmer",1,45)
print(cochesito)


if __name__ == "__main__":
    main()
