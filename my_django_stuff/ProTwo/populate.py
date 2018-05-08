import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')


import django
django.setup()


from faker import Faker

fakegen=Faker()

from appTwo.models import User

def populate(n=10):

    for entry in range(n):
        fake_name=fakegen.first_name()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.email()

        #new entry
        temp_user=User.objects.get_or_create(first_name=fake_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print('populating')
    populate(20)
    print('complete')
