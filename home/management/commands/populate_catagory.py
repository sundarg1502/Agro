from django.core.management.base import BaseCommand
from home.models import Catagory

class Command(BaseCommand):

    def handle(self, *args, **options):
        Catagory.objects.all().delete()

        catagory_names = ['Vegetables',"Dairy Products","Organic Grains","Fruits"]
        descriptions = [
    "Fresh and locally sourced vegetables to add flavor and nutrition to your meals.",
    "High-quality dairy products including milk, cheese, yogurt, and more, essential for a healthy diet.",
    "Wholesome organic grains grown naturally, perfect for balanced and sustainable meals.",
    "Juicy and seasonal fruits bursting with natural sweetness and rich in vitamins."
]
        image = 'static/images/catagory/'
        i = 1
        for catagory_name, description in zip(catagory_names,descriptions):
            Catagory.objects.create(catagory_name=catagory_name,description=description,image=f"/images/catagory/ct{i}")
            i+=1
