import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

import django
django.setup()

from assassin.models import Person, Group

def populate():
	test_group = add_group("Building 12 Floor 2", 20)

	add_person(group=test_group, name="Stanley", alive=False)
	add_person(group=test_group, name="Alex")
	add_person(group=test_group, name="Ross")
	add_person(group=test_group, name="Nicole")
	add_person(group=test_group, name="Anbitch", alive=False)
	add_person(group=test_group, name="Avi")
	add_person(group=test_group, name="Kunal")
	add_person(group=test_group, name="Camila")
	add_person(group=test_group, name="Tristan", alive=False)

	test_group_2 = add_group("Some other group", 300)

	add_person(group=test_group_2, name="Tester")
	add_person(group=test_group_2, name="Tester2")

	for g in Group.objects.all():
		for p in Person.objects.filter(group_id=g):
			print("{0} and is in group {1}".format(str(p), str(g)))

def add_person(group, name, alive=True):
    p = Person.objects.get_or_create(group_id=group, name=name)[0]
    p.alive = alive
    p.save()
    return p

def add_group(group_name, prize):
    g = Group.objects.get_or_create(group_name=group_name)[0]
    g.prize = prize
    g.save()
    return g

if __name__ == '__main__':
    print("Starting assassin population script...")
    populate()