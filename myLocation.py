class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def MyLocation (self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")
# Primera instancia de la clase Location
loc1 = Location("Martin", "Perú")
# Llamar a un método de la clase instanciada
loc1.MyLocation()
# Tres instancias más y llamadas a métodos para la clase Location
loc2 = Location("Pedro", "Italia")
loc3 = Location("Gabriel", "Colombia")
loc2.MyLocation()
loc3.MyLocation()
