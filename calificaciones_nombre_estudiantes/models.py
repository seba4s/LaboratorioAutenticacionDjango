from django.db import models

class Calificacion(models.Model):
    # Definición de campos según el requerimiento del laboratorio
    nombre_estudiante = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    asignatura = models.CharField(max_length=100)
    
    # Campos decimales para notas (máximo 5 dígitos, 2 decimales)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Campo calculado, no editable en el formulario
    promedio = models.DecimalField(max_digits=5, decimal_places=2, editable=False)

    # Función personalizada para calcular el promedio
    def calcular_promedio(self):
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

    # Sobreescritura del método save para automatizar el cálculo
    def save(self, *args, **kwargs):
        self.promedio = self.calcular_promedio()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.asignatura}"