from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()    


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()    
    
    class Meta:
       verbose_name = "Cor"
       verbose_name_plural = "Cores"

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nome.upper()                                 

class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    cor =models.ForeignKey(
        Cor, on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor}" 