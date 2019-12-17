import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import pizza, ingrediente, contiene

def poblar():
	p1=pizza.objects.get_or_create(id=1001, nombreP='pizza_a')[0]
	p1.save()

	p2=pizza.objects.get_or_create(id=1002, nombreP='pizza_b')[0]
	p2.save()

	p3=pizza.objects.get_or_create(id=1003, nombreP='pizza_c')[0]
	p3.save()


	i1=ingrediente.objects.get_or_create(id=1001, nombreI='ingrediente_a')[0]
	i1.save()

	i2=ingrediente.objects.get_or_create(id=1002, nombreI='ingrediente_b')[0]
	i2.save()

	i3=ingrediente.objects.get_or_create(id=1003, nombreI='ingrediente_c')[0]
	i3.save()

	i4=ingrediente.objects.get_or_create(id=1004, nombreI='ingrediente_d')[0]
	i4.save()


	c1=contiene.objects.get_or_create(id=1001, pizza=p1, ingrediente=i1, porcentaje=43.2)[0]
	c1.save()

	c2=contiene.objects.get_or_create(id=1002, pizza=p2, ingrediente=i2, porcentaje=34.2)[0]
	c2.save()

	c3=contiene.objects.get_or_create(id=1003, pizza=p2, ingrediente=i3, porcentaje=27.4)[0]
	c3.save()

	c4=contiene.objects.get_or_create(id=1004, pizza=p1, ingrediente=i3, porcentaje=13.2)[0]
	c4.save()


# Start execution here!
if __name__ == '__main__':
    print('Comenzando script de poblar Aplicacion...')
    poblar()
