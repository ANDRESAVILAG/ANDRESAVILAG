class persona():
    def __init__(self, name):
        self.nombre = name
        
    def caminar(self):
        print("estoy caminando", self.nombre)
        
    def comer(self,comida):
        print("estoy comiendo",comida)
        
admin = persona("Lorena")
estudiante01 = persona("Carlos")
profesorMat = persona("Francisco")

profesorMat.caminar()
admin.caminar()
estudiante01.comer("arroz")
admin.comer("pasta")
    
    
    
        
    
    
    