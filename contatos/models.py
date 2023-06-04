from django.db import models

class Cliente(models.Model):
   
    nome = models.CharField(max_length=50, null=False, blank=False)    
    contato = models.CharField(max_length=20, null=False, blank=False)  
    endereco = models.CharField(max_length=50)  
    observacao = models.TextField()  

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aparelho = models.CharField(max_length=50, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    serial = models.CharField(max_length=20, null=False, blank=False)
    observacao = models.TextField()




   
