from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem

# Exactly 36 product entries transcribed from the supplied C3 printed menu.
# Cheese is an option on the burger item; French Fries has Small/Large sizes.
# The printed menu's Loaded Fries price is ₹169 (PRC-179 is retained in the description).
MENU = [
    ("Broasted", "broasted", "🍗", 1, [
        ("2 Pcs Broasted", "2 pieces of crispy broasted chicken.", 109, "broasted-2-pcs.jpg"),
        ("4 Pcs Broasted", "4 pieces of crispy broasted chicken.", 199, "broasted-4-pcs.jpg"),
        ("6 Pcs Broasted", "6 pieces of crispy broasted chicken.", 299, "broasted-6-pcs.jpg"),
        ("8 Pcs Broasted", "8 pieces of crispy broasted chicken.", 399, "broasted-8-pcs.jpg"),
        ("10 Pcs Broasted", "10 pieces of crispy broasted chicken.", 489, "broasted-10-pcs.jpg"),
        ("12 Pcs Broasted", "12 pieces of crispy broasted chicken.", 589, "broasted-12-pcs.jpg"),
    ]),
    ("Momos & Snacks", "momos-snacks", "🥟", 2, [
        ("Chicken Momos Fried (5 Pcs)", "Fried chicken momos, 5 pieces.", 79, "chicken-momos.jpg"),
        ("Schezwan Momos Fried (5 Pcs)", "Schezwan fried momos, 5 pieces.", 89, "schezwan-momos.jpg"),
        ("Nuggets (5 Pcs)", "Chicken nuggets, 5 pieces.", 59, "nuggets.jpg"),
        ("French Fries", "French fries: Small ₹69 / Large ₹89. Select the size when ordering.", 69, "french-fries.jpg"),
        ("Chicken Popcorn (10 Pcs)", "Chicken popcorn, 10 pieces.", 59, "chicken-popcorn.jpg"),
        ("Chicken Finger (5 Pcs)", "Chicken fingers, 5 pieces.", 59, "chicken-finger.jpg"),
        ("Loaded Fries", "Loaded fries. Printed menu shows ₹169 (PRC-179).", 169, "loaded-fries.jpg"),
    ]),
    ("Burgers", "burgers", "🍔", 3, [
        ("Chicken Burger", "Chicken burger ₹59; with cheese ₹69.", 59, "chicken-burger.jpg"),
        ("Veg Burger", "Vegetable burger ₹59; with cheese ₹69.", 59, "veg-burger.jpg"),
        ("Beef Burger", "Beef burger ₹69; with cheese ₹79.", 69, "beef-burger.jpg"),
        ("Zinger Burger", "Zinger burger.", 99, "zinger-burger.jpg"),
    ]),
    ("Tea & Hot Drinks", "tea-hot-drinks", "☕", 4, [
        ("Tea", "Tea.", 12, "tea.jpg"),
        ("Coffee", "Coffee.", 15, "coffee.jpg"),
        ("Horlicks", "Horlicks drink.", 20, "horlicks.jpg"),
        ("Boost", "Boost drink.", 20, "boost.jpg"),
    ]),
    ("Juices & Drinks", "juices-drinks", "🥤", 5, [
        ("Mango Juice", "Mango juice.", 69, "mango-juice.jpg"),
        ("Pomegranate Juice", "Pomegranate juice.", 69, "pomegranate-juice.jpg"),
        ("Apple Juice", "Apple juice.", 69, "apple-juice.jpg"),
        ("Pineapple Juice", "Pineapple juice.", 59, "pineapple-juice.jpg"),
        ("Tender Coconut", "Tender coconut drink.", 79, "tender-coconut.jpg"),
        ("Chicku Juice", "Chicku (sapodilla) juice.", 69, "chikku-juice.jpg"),
        ("Mojitos", "Mojitos.", 59, "mojito.jpg"),
        ("Lime", "Lime drink.", 20, "lime.jpg"),
        ("Mint Lime", "Mint lime drink.", 25, "mint-lime.jpg"),
        ("Orange Juice", "Orange juice.", 59, "orange-juice.jpg"),
        ("Avil Milk", "Avil milk.", 59, "avil-milk.jpg"),
    ]),
    ("Extras", "extras", "➕", 6, [
        ("Extra Kubboos (1 Pc)", "Extra kubboos, 1 piece.", 10, "extra-kubboos.jpg"),
        ("Extra Mayonnaise (1 Pc)", "Extra mayonnaise, 1 portion.", 10, "extra-mayonnaise.jpg"),
        ("Extra Ketchup (1 Pc)", "Extra ketchup, 1 portion.", 10, "extra-ketchup.jpg"),
        ("Extra Bun", "Extra bun.", 10, "extra-bun.jpg"),
    ]),
]

class Command(BaseCommand):
    help = "Create/update exactly the 36 products from the supplied C3 printed menu."

    def handle(self, *args, **options):
        keep_slugs = []
        for cat_name, cat_slug, icon, cat_order, entries in MENU:
            category, _ = Category.objects.update_or_create(
                slug=cat_slug,
                defaults={"name": cat_name, "icon": icon, "order": cat_order, "active": True},
            )
            for item_order, (name, description, price, image_name) in enumerate(entries, 1):
                slug = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
                keep_slugs.append(slug)
                MenuItem.objects.update_or_create(
                    slug=slug,
                    defaults={
                        "category": category,
                        "name": name,
                        "description": description,
                        "price": price,
                        "image_url": f"/static/product-images/{image_name}",
                        "image": None,
                        "available": True,
                        "order": item_order,
                    },
                )
        # Remove old duplicate variants from previous seed data so only the menu's 36 items remain.
        MenuItem.objects.exclude(slug__in=keep_slugs).delete()
        self.stdout.write(self.style.SUCCESS(
            f"C3 printed menu synchronized: {MenuItem.objects.filter(available=True).count()} available products."
        ))
