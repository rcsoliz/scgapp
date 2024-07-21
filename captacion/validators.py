from django.core.exceptions import ValidationError

def validar_camposvacios(value):
    if value is None:    
        raise ValidationError("%(valor)s no puede ser nulo", params={'valor': value})
    
def validar_logitud(value):
    if len(value)>10:
        raise ValidationError("%(valor)s no puede ser maximo es de 10 caracteres", params={"valor": value})