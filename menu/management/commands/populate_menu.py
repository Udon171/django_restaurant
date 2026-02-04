from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem


class Command(BaseCommand):
    help = 'Populates the menu database with restaurant menu items'

    def handle(self, *args, **options):
        # Clear existing menu items
        MenuItem.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Cleared existing menu items...')

        # Create categories
        categories = {
            'starters': Category.objects.create(name='Starters', description='Begin your dining experience', order=1),
            'brunch_mains': Category.objects.create(name='Brunch Mains', description='Available 12PM - 4PM, Monday to Saturday. 2 Courses £16.50', order=2),
            'brunch_desserts': Category.objects.create(name='Brunch Desserts', description='Sweet treats for brunch', order=3),
            'pasta': Category.objects.create(name='Pasta & Risotto', description='All pastas can be made gluten-free on request', order=4),
            'pizza': Category.objects.create(name='Pizza', description='Stone-baked Italian pizzas', order=5),
            'steaks': Category.objects.create(name='Steaks', description='All steaks are 10oz, served with rocket, grilled tomatoes, mushrooms, peppercorn sauce and chips', order=6),
            'mains': Category.objects.create(name='Main Courses', description='Chef\'s signature dishes', order=7),
            'fish': Category.objects.create(name='Fish & Seafood', description='Fresh catches from the sea', order=8),
            'sides': Category.objects.create(name='Sides', description='Perfect accompaniments', order=9),
            'desserts': Category.objects.create(name='Desserts', description='Indulgent endings', order=10),
            'kids': Category.objects.create(name='Children\'s Menu', description='For our younger guests', order=11),
            'sunday': Category.objects.create(name='Sunday Lunch', description='Available 12:00-5:00. Main £15.95, 2 Courses £18.95 adults/£14.95 children, 3 Courses £21.95 adults/£16.95 children', order=12),
            'tapas': Category.objects.create(name='Tapas', description='Wednesday after 4PM only. Please book in advance.', order=13),
        }

        # Starters
        starters = [
            ('Freshly Baked Bread with Balsamic and Olive Oil', 'Warm bread served with premium balsamic and olive oil.', 4.95, True, True, False),
            ('Freshly Marinated Mixed Olives', 'A selection of marinated olives. Add feta cheese +£1.00.', 4.95, True, True, True),
            ('Homemade Garlic Pizza Bread', 'Freshly baked garlic bread. With cheese +£1.00.', 8.45, True, False, False),
            ('Soup of the Day', 'Served with home baked bread and butter.', 6.95, True, False, False),
            ('Honey & Rosemary Camembert', 'Served with bread sticks and date chutney.', 9.95, True, False, False),
            ('Mediterranean Style Burrata Salad', 'Cherry tomatoes, onions, spinach, peppers and rocket.', 8.50, True, False, True),
            ('Harissa Halloumi & Homemade Chilli Jam', 'Grilled halloumi with house-made chilli jam.', 6.95, True, False, False),
            ('Sicilian Chicken Liver Bruschetta', 'Smooth Italian pate with pancetta, served with bread and caramelised balsamic onions.', 7.95, False, False, False),
            ('Hot Tiger Prawns', 'Pan fried with garlic, chilli, parsley and lemon, served with bread.', 8.95, False, False, False),
            ('Three Cheese Arancini', 'Served with smoked peppers and tomato sauce.', 6.95, True, False, False),
            ('Pulled Brisket on Sourdough', 'Tender pulled brisket on toasted sourdough with dressed wild rocket.', 8.50, False, False, False),
            ('Queen Scallops', 'Served with pea puree and crispy bacon.', 10.45, False, False, True),
            ('Goat\'s Cheese Salad', 'Tomato chilli rocket salad, topped with pesto (contains pine nuts).', 8.50, True, False, True),
            ('Wild Mushrooms & Chorizo Bruschetta', 'Sautéed wild mushrooms with chorizo on toasted bread.', 7.95, False, False, False),
        ]
        for name, desc, price, veg, vegan, gf in starters:
            MenuItem.objects.create(category=categories['starters'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Brunch Mains
        brunch_mains = [
            ('Chicken Caesar Salad', 'Gem lettuce, bacon, crunchy croutons, parmesan and caesar dressing.', 10.95, False, False, False),
            ('Smashed Avocado on Sourdough', 'Two poached eggs, dressed salad.', 9.95, True, False, False),
            ('Beer Battered Haddock', 'Served with mushy peas, tartare sauce, chips and lemon.', 12.95, False, False, False),
            ('Lasagne', 'Served with dressed salad and home baked garlic bread.', 10.95, False, False, False),
            ('Greek Style Stuffed Pitta Bread', 'Olives, yoghurt, feta, peppers, pulled pork and dressed rocket.', 10.95, False, False, False),
            ('Cajun Chicken Wrap', 'Spinach, onions, tomatoes and chips.', 10.95, False, False, False),
            ('Harissa Halloumi Wrap', 'Hummus, tomatoes, dressed salad, chips.', 10.95, True, True, False),
        ]
        for name, desc, price, veg, vegan, gf in brunch_mains:
            MenuItem.objects.create(category=categories['brunch_mains'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Brunch Desserts
        brunch_desserts = [
            ('Crepes Suzette', 'Served with chocolate ice cream.', 6.95, True, False, False),
            ('Sticky Toffee Pudding (Brunch)', 'Served with custard or strawberry ice cream.', 6.95, True, False, False),
            ('Orange Brownie', 'Served with ice cream.', 6.95, True, False, False),
        ]
        for name, desc, price, veg, vegan, gf in brunch_desserts:
            MenuItem.objects.create(category=categories['brunch_desserts'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Pasta & Risotto
        pasta = [
            ('Spaghetti Bolognese', 'Slow cooked beef ragu and parmesan.', 14.95, False, False, False),
            ('Genovese Ragu Tagliatelline', 'Slow cooked lamb ragu with carrots, celery and onions.', 14.95, False, False, False),
            ('Spaghetti Carbonara', 'Pancetta, garlic and onion creamy sauce and parmesan.', 15.95, False, False, False),
            ('Penne al Pollo', 'Chicken, mushrooms, garlic, pesto (contains pine nuts), double cream and parmesan.', 15.95, False, False, False),
            ('Penne Arrabbiata', 'Bell peppers, sliced onions, chilli and garlic tomato sauce.', 12.95, True, False, False),
            ('Scampi Linguine', 'Cherry tomatoes and garlic sweet chilli sauce. Add chorizo +£1.45.', 16.50, False, False, False),
            ('Chicken & Chorizo Risotto', 'With garden peas, chilli, garlic and parmesan.', 15.95, False, False, True),
            ('Seafood Risotto', 'Prawns, mussels, mixed seafood in white wine chilli tomato sauce and parmesan.', 17.95, False, False, True),
            ('Mixed Mushroom Risotto', 'Chestnut, close cup and portobello mushrooms, white wine creamy garlic sauce, rocket and parmesan.', 13.95, True, False, True),
        ]
        for name, desc, price, veg, vegan, gf in pasta:
            MenuItem.objects.create(category=categories['pasta'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Pizza
        pizza = [
            ('Margherita', 'Classic tomato and mozzarella.', 11.95, True, False, False),
            ('Chicken & Bacon', 'Topped with chicken and crispy bacon.', 15.95, False, False, False),
            ('Pizza Toscana', 'Topped with buffalo mozzarella, prosciutto and wild rocket.', 14.95, False, False, False),
            ('Diavola', 'Fresh chilli, chorizo, pepperoni, olives.', 14.95, False, False, False),
            ('Vegetarian Pizza', 'Mushrooms, tomatoes, peppers, onions and spinach.', 13.95, True, False, False),
            ('Calzone', 'Slow cooked beef ragu, mushrooms, chicken, pepperoni.', 16.45, False, False, False),
            ('Korean BBQ Pizza', 'BBQ base, jalapenos, spring onions, balsamic vinegar.', 14.45, False, False, False),
            ('Pepperoni', 'Classic pepperoni pizza.', 14.45, False, False, False),
            ('Pizza Frutti di Mare', 'Mixed seafood, capers.', 15.95, False, False, False),
        ]
        for name, desc, price, veg, vegan, gf in pizza:
            MenuItem.objects.create(category=categories['pizza'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Steaks
        steaks = [
            ('Sirloin Steak', 'Served with rocket, grilled tomatoes, mushrooms, peppercorn sauce and chips.', 25.95, False, False, True),
            ('Ribeye Steak', 'Served with rocket, grilled tomatoes, mushrooms, peppercorn sauce and chips.', 28.50, False, False, True),
            ('Fillet Steak', 'Served with buttered spinach, peppercorn sauce and mash.', 32.95, False, False, True),
        ]
        for name, desc, price, veg, vegan, gf in steaks:
            MenuItem.objects.create(category=categories['steaks'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Mains
        mains = [
            ('Roasted Pear & Goat\'s Cheese Salad', 'Honey mustard dressing salad, pecans, and pickled onions.', 14.95, True, False, True),
            ('Stuffed Wild Mushrooms Cornfed Chicken', 'Served with asparagus, saute potatoes and thyme lemon sauce.', 16.95, False, False, True),
            ('Involtini Chicken', 'Chicken breast filled with asparagus and gorgonzola cheese, wrapped in pancetta, served with creamy mash, seasonal veg and white wine dill sauce.', 18.95, False, False, True),
            ('Italian Herb Rotisserie Chicken', 'Served with chunky chips, coleslaw and gravy.', 17.95, False, False, True),
            ('Chicken Burger', 'Buttermilk chicken, bacon, cheese, tomatoes, lettuce, burger sauce, chips and onion ring.', 16.95, False, False, False),
            ('Confit Pork Belly', 'Tenderstem broccoli, saffron baby potatoes, chorizo, apple cider reduction and cracklings.', 19.95, False, False, True),
            ('Calves Liver', 'Pan fried, served with creamy mash, spinach, crispy pancetta and red wine jus.', 21.95, False, False, True),
            ('Lamb Rump', 'Pan roasted lamb rump with Lyonnaise potatoes, provencal vegetables and lamb jus.', 21.95, False, False, True),
            ('Rack of Lamb', 'Served with creamy mash, butter fine beans, port & rosemary reduction sauce.', 22.95, False, False, True),
        ]
        for name, desc, price, veg, vegan, gf in mains:
            MenuItem.objects.create(category=categories['mains'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Fish
        fish = [
            ('Fillet of Seabass', 'Served with creamy leeks, chorizo, saute baby potatoes, and white wine sauce.', 19.95, False, False, True),
            ('Pan Roasted Salmon Fillet', 'Tenderstem broccoli, ginger steamed rice, soy sweet chilli & sesame sauce.', 20.95, False, False, False),
            ('Mix Grilled Fish & Prawns', 'Served with spring onion crushed potatoes & buttered fine beans and garlic lemon butter sauce.', 22.95, False, False, True),
        ]
        for name, desc, price, veg, vegan, gf in fish:
            MenuItem.objects.create(category=categories['fish'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Sides
        sides = [
            ('Chunky Chips', 'Thick cut chips.', 5.00, True, True, True),
            ('Truffle Oil & Parmesan Chips', 'Chips with truffle oil and parmesan.', 6.00, True, False, True),
            ('Loaded Fries', 'Chips, cheese, pulled brisket, jalapenos, crispy onions and pork crackling.', 9.95, False, False, True),
            ('Creamy Mash', 'Smooth mashed potatoes.', 4.50, True, False, True),
            ('Bacon & Onion Saute Potatoes', 'Pan fried potatoes with bacon and onion.', 5.50, False, False, True),
            ('Onion Rings', 'Crispy battered onion rings.', 4.00, True, True, False),
            ('Greek Salad', 'Fresh Mediterranean salad.', 6.00, True, True, True),
            ('Mixed Vegetables', 'Seasonal vegetables.', 4.75, True, True, True),
            ('Buttered Spinach', 'Sautéed spinach in butter.', 4.00, True, False, True),
        ]
        for name, desc, price, veg, vegan, gf in sides:
            MenuItem.objects.create(category=categories['sides'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Desserts
        desserts = [
            ('Vanilla Crème Brulee', 'Classic French custard with caramelised sugar top.', 6.95, True, False, False),
            ('Tiramisu', 'Italian coffee-flavoured dessert.', 7.25, True, False, False),
            ('Sticky Toffee Pudding', 'Served with vanilla ice cream.', 7.50, True, False, False),
            ('Selection of Ice Cream', 'Strawberry, vanilla and chocolate.', 6.25, True, False, False),
            ('Sorbets', 'Lemon, mango and raspberry.', 6.25, True, True, True),
            ('Burnt Basque Cheesecake', 'Served with wild berry sauce.', 7.25, True, False, False),
            ('Chocolate Brownie', 'Served with vanilla ice cream or cream.', 7.50, True, False, False),
            ('Boozy Chocolate Berries Mess', 'Chocolate and berries with a boozy twist.', 7.50, True, False, False),
            ('Salted Caramel Brownie Sundae', 'Brownie with salted caramel and ice cream.', 7.50, True, False, False),
        ]
        for name, desc, price, veg, vegan, gf in desserts:
            MenuItem.objects.create(category=categories['desserts'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Kids Menu
        kids = [
            ('Spaghetti Napoletana', 'Pasta cooked in tomato sauce.', 6.95, True, False, False),
            ('Pasta Bolognese', 'Slow cooked beef ragu and parmesan.', 6.95, False, False, False),
            ('Meatballs Pasta', 'Pasta with meatballs in tomato sauce.', 6.95, False, False, False),
            ('Pizza Margherita (Kids)', 'Classic tomato and mozzarella.', 7.95, True, False, False),
            ('Mac & Cheese', 'Creamy macaroni cheese.', 6.95, True, False, False),
            ('Chicken Goujons', 'Served with chips and salad.', 7.50, False, False, False),
            ('Fish Goujons', 'Served with chips and salad.', 7.50, False, False, False),
            ('Nutella Cookies', 'Warm cookies with Nutella.', 3.45, True, False, False),
            ('Brownie (Kids)', 'Chocolate brownie. Add ice cream +£2.00.', 3.45, True, False, False),
        ]
        for name, desc, price, veg, vegan, gf in kids:
            MenuItem.objects.create(category=categories['kids'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Sunday Lunch
        sunday = [
            ('Sunday Soup of the Day', 'Served with home baked bread and butter.', 6.95, True, False, False),
            ('Homemade Pate', 'Smooth Italian style pate served with home baked bread & cranberry sauce.', 7.95, False, False, False),
            ('Prawn Cocktail', 'Avocado and lettuce served with homemade Marie-Rose sauce.', 8.95, False, False, True),
            ('Creamy White Wine Mushrooms', 'Served with freshly baked bread.', 6.95, True, False, False),
            ('Roast Sirloin Beef', 'Served with seasonal vegetables, Yorkshire pudding, roasted potatoes, honey glazed carrots and parsnips, and gravy.', 15.95, False, False, False),
            ('Roast Rump of Lamb', 'Served with seasonal vegetables, Yorkshire pudding, roasted potatoes, honey glazed carrots and parsnips, and gravy.', 15.95, False, False, False),
            ('Roast Confit Pork Belly', 'Served with seasonal vegetables, Yorkshire pudding, roasted potatoes, honey glazed carrots and parsnips, and gravy.', 15.95, False, False, False),
            ('Roast Turkey', 'Served with stuffing, pigs in blankets, seasonal vegetables, Yorkshire pudding, roasted potatoes, honey glazed carrots and parsnips, and gravy.', 15.95, False, False, False),
            ('Roast Veg & Celeriac Wellington', 'Vegan roast option with all the trimmings.', 15.95, True, True, False),
            ('Sunday Mash', 'Creamy mashed potatoes.', 4.50, True, False, True),
            ('Cauliflower & Cheese', 'Baked cauliflower in cheese sauce.', 5.00, True, False, False),
            ('Pigs in Blankets', 'Sausages wrapped in bacon.', 5.50, False, False, False),
            ('Leek & Cheese', 'Creamy leeks with cheese.', 5.00, True, False, False),
            ('Pork Stuffing', 'Traditional pork stuffing.', 5.50, False, False, False),
        ]
        for name, desc, price, veg, vegan, gf in sunday:
            MenuItem.objects.create(category=categories['sunday'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        # Tapas
        tapas = [
            ('Homemade Baked Bread (Tapas)', 'Freshly baked bread.', 3.00, True, True, False),
            ('Baked Egg & Feta', 'Baked eggs with crumbled feta.', 7.50, True, False, True),
            ('Cajun & Honey Halloumi Fries', 'Served with sweet chilli sauce.', 5.95, True, False, False),
            ('Cauliflower Florets', 'Served with wasabi dip.', 5.95, True, True, False),
            ('Patatas Bravas', 'Served with garlic and herbed dip.', 5.95, True, True, True),
            ('Hot Southern Fried Chicken', 'Crispy fried chicken pieces.', 7.50, False, False, False),
            ('Nachos with Barbacoa Pulled Beef', 'Nachos with guacamole, sour cream, and pulled beef.', 9.50, False, False, False),
            ('Italian Meatballs', 'In rich tomato sauce.', 7.50, False, False, False),
            ('Steak Teriyaki', 'Served with mixed peppers and onions.', 7.50, False, False, False),
            ('Gambas Pil Pil', 'Prawns in garlic and chilli oil.', 8.95, False, False, True),
            ('Sticky Spare Ribs', 'Glazed pork ribs.', 9.95, False, False, False),
            ('Sausage & Leeks', 'Pan fried sausages with leeks.', 7.50, False, False, False),
            ('Beef Shin Bonbons', 'Served with sriracha.', 7.50, False, False, False),
        ]
        for name, desc, price, veg, vegan, gf in tapas:
            MenuItem.objects.create(category=categories['tapas'], name=name, description=desc, price=price, is_vegetarian=veg, is_vegan=vegan, is_gluten_free=gf)

        total_items = MenuItem.objects.count()
        total_categories = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total_categories} categories and {total_items} menu items!'))
