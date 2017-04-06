from django.db import models


# Create your models here.
class TipoDeVeiculo(models.Model):
    tipo = models.CharField('Tipo de Veiculo', max_length=20,
                            help_text='Ex. Carro ou Moto')

    def __str__(self):
        return "{}".format(self.tipo)

    class Meta:
        ordering = ('tipo',)
        verbose_name = 'Tipo de Veiculo'
        verbose_name_plural = 'Tpos de Veiculos'


class MarcaDoVeiculo(models.Model):
    marca = models.CharField('Marca do Veiculo', max_length=20,
                             help_text='Ex. Nissam, Honda,'
                                       'Fiat')

    def __str__(self):
        return '{}'.format(self.marca)

    class Meta:
        ordering = ('marca',)
        verbose_name = 'Marca do Veiculo'
        verbose_name_plural = 'Marca dos Veiculos'


class Veiculo(models.Model):
    tipo = models.ForeignKey(TipoDeVeiculo)
    marca = models.ForeignKey(MarcaDoVeiculo)

    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=8)
    cor = models.CharField('Modelo', max_length=10)

    def __str__(self):
        return '{} - {}'.format(self.placa, self.modelo)

    class Meta:
        ordering = ('tipo', 'marca', 'modelo')
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
