from django.core.management.base import BaseCommand
from home.models import Products,Catagory
from random import randint

class Command(BaseCommand):
    def handle(self, *args, **options):
        Products.objects.all().delete()
        # Names
        names = [
            "Carrot", "Broccoli", "Spinach", "Tomato", "Cucumber",
            "Milk", "Cheese", "Butter", "Yogurt", "Paneer",
            "Quinoa", "Brown Rice", "Oats", "Barley", "Chia Seeds",
            "Apple", "Banana", "Grapes", "Orange", "Mango"
        ]

        # Descriptions
        descriptions = [
            "Fresh and crunchy carrots.", "Green and healthy broccoli.",
            "Rich in iron, fresh spinach.", "Juicy and ripe tomatoes.",
            "Crisp and hydrating cucumbers.", "Full cream milk, fresh from the farm.",
            "Rich and creamy cheddar cheese.", "Smooth and salted butter.",
            "Natural and probiotic-rich yogurt.", "Fresh cottage cheese blocks.",
            "Organic, protein-rich quinoa.", "Nutritious whole-grain brown rice.",
            "Healthy rolled oats.", "Rich in fiber barley grains.",
            "Small yet nutritious chia seeds.", "Crisp and sweet apples.",
            "Freshly ripened bananas.", "Juicy seedless grapes.",
            "Citrus-rich, juicy oranges.", "Sweet and flavorful mangoes."
        ]

        # Actual Prices
        actual_prices = [
            20, 40, 30, 15, 10,
            50, 80, 60, 40, 90,
            100, 70, 50, 60, 120,
            30, 25, 50, 40, 70
        ]

        # New Prices
        new_prices = [
            18, 36, 27, 14, 9,
            45, 72, 54, 36, 81,
            90, 63, 45, 54, 108,
            27, 22, 45, 36, 63
        ]

        # Vendors
        vendors = [
            "FreshFarm", "GreenValley", "HealthyHarvest", "AgroFresh", "Nature's Basket",
            "DairyDelight", "CreamyWay", "ButterLand", "YogurtKing", "PaneerWonders",
            "OrganicSource", "WholeGrainsCo", "HealthyBites", "GrainMasters", "SuperSeeds",
            "FruitFusion", "BananaSpot", "GrapeVine", "CitrusWorld", "MangoMania"
        ]
        category_id=1
        count =0
        for name,description,acprice,nprice,vendor in zip(names,descriptions,actual_prices,new_prices,vendors):
            quantity = randint(5,15)
            catagory_obj = Catagory.objects.get(pk=category_id)
            print(f"{catagory_obj} is {category_id}")
            Products.objects.create(name=name,catagory=catagory_obj,description=description,actuall_price=acprice,new_price=nprice,vendor=vendor,quantity=quantity)
            count+=1
            if count%5 == 0:
                category_id+=1
        
        self.stdout.write("Post Created Successfully")