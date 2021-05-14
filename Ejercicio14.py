class Profesores_PUCV (object):
    #----------------------------------------------------------------------
    def __init__(self, NombreApellido, Plantaoparcial, email, telefono):
        self.Nombrecompleto = NombreApellido
        self.Plantaoparcial = Plantaoparcial
        self.email = email
        self.telefono = telefono
    #----------------------------------------------------------------------
    def get_name(self):
        return self.Nombrecompleto
    #----------------------------------------------------------------------
    def get_oc(self):
        return self.Plantaoparcial
    #----------------------------------------------------------------------
    def get_email(self):
        return self.email
    #----------------------------------------------------------------------
    def get_telefono(self):
        return self.telefono
    #----------------------------------------------------------------------
    def set_name(self, new_name):
        self.Nombrecompleto = new_name
    #----------------------------------------------------------------------
    def set_oc(self, new_oc):
        self.Plantaoparcial = new_oc
    #----------------------------------------------------------------------
    def set_email(self, new_email):
        self.email = new_email
    #----------------------------------------------------------------------
    def set_telefono(self, new_telefono):
        self.telefono = new_telefono
#--------------------------------------------------------------------------
class Profesores_Planta_EIE (Profesores_PUCV):
    def __init__(self, NombreApellido, Plantaoparcial, email, telefono, ramo):
        super().__init__(NombreApellido, Plantaoparcial, email, telefono)
        self.ramo = ramo
    #---------------------------------------------------------------------
    def get_ramo(self):
        return self.ramo
    #----------------------------------------------------------------------
    def set_ramo(self, new_ramo):
        self.ramo = new_ramo
    def __str__(self):
        return ("Profesor: " + self.Nombrecompleto + "| Tipo: " + self.Plantaoparcial + "| ramo: " + self.ramo )
#--------------------------------------------------------------------------
class Profesores_Parciales_EIE (Profesores_PUCV):
    #----------------------------------------------------------------------
    def __init__(self, NombreApellido, Plantaoparcial, email, telefono, horas_semanales):
        super().__init__(NombreApellido, Plantaoparcial, email, telefono)
        self.horas_semanales = horas_semanales
    #----------------------------------------------------------------------
    def get_horas(self):
        return self.horas_semanales
    #----------------------------------------------------------------------
    def set_horas(self, new_horas):
        self.horas_semanales = new_horas
    def __str__(self):
        return ("Profesor: " + self.Nombrecompleto + "| Tipo: " + self.Plantaoparcial + "| horas: " + self.horas_semanales )
#--------------------------------------------------------------------------
class Equipo_Directivo(Profesores_Planta_EIE):
    def __init__(self, NombreApellido, Plantaoparcial, email, telefono, ramo, cargo):
        super().__init__(NombreApellido, Plantaoparcial, email, telefono, ramo)
        self.cargo = cargo
    #----------------------------------------------------------------------
    def get_cargo(self):
        return self.cargo
    #----------------------------------------------------------------------
    def set_cargo(self, new_cargo):
        self.cargo = new_cargo
    def __str__(self):
        return ("Profesor: " + self.Nombrecompleto + "| Tipo: " + self.Plantaoparcial + "| Cargo: " + self.cargo )
#--------------------------------------------------------------------------
