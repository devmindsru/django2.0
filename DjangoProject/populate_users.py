import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoProject.settings')

import django
django.setup()

import random
from ProjectApp.models import user
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        femail = fakegen.email()

        users = user.objects.get_or_create(firstname=fake_fname,
                                            lastname=fake_lname,
                                            email=femail)[0]


if __name__=='__main__':
        print('POPULATING DATABASES')
        populate(20)
        print('COMPLETE')
