from django.db import models

class DadosTurma(models.Model):
    codigo_turma = models.CharField(max_length=20)
    codigo_subtipo_atividade = models.IntegerField()
    horario = models.CharField(max_length=20)
    dia_semana = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    codigo_instrutor = models.CharField(max_length=20)
    numero_vagas = models.IntegerField()

    class Meta:
        db_table = 'dadosturma'
    
    def __str__(self):
        return f"{self.codigo_turma} - {self.horario} - {self.dia_semana}"
