import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()
import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker
fake = Faker()
topics = ["Search","Social Media","MarketPlace","Name","Games"]
def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t
def populate(N = 5):
    for entry in range(N):
        top = add_topic()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()
        webpg = WebPage.objects.get_or_create(topic_ref =top ,url = fake_url,name =fake_name )[0]
        acc_rec = AccessRecord.objects.get_or_create(name_rec = webpg,date = fake_date)[0]
if __name__ == "__main__":
    print("Populating Db")
    populate(23)
    print("Populated Successfully")
