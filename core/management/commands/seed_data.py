import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
from products.models import AgeGroup, Category, Product, ProductImage
from pages.models import Banner, Testimonial, USP, TeamMember, FAQ
from blog.models import BlogCategory, BlogPost, Recipe

class Command(BaseCommand):
    help = 'Seeds the database with Highness sample data and generates mockup images'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting database seeding...")

        # 0. Clean old data if any
        self.clean_data()

        # Helper to generate physical image files in media
        def make_mock_image(relative_path, text, bg_color=(248, 190, 21), text_color=(44, 4, 9), size=(400, 400)):
            full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            img = Image.new('RGB', size, color=bg_color)
            draw = ImageDraw.Draw(img)

            # Simple text drawing
            draw.text((20, size[1] // 2 - 10), text, fill=text_color)
            img.save(full_path)
            return relative_path

        # Colors for images
        c_yellow = (248, 190, 21)
        c_red = (193, 33, 38)
        c_cream = (255, 249, 230)
        c_green = (76, 175, 80)
        c_dark = (44, 4, 9)

        # 1. Create Age Groups
        self.stdout.write("Creating Age Groups...")
        age_6m = AgeGroup.objects.create(
            name="6+ Months",
            slug="6-months",
            icon=make_mock_image("age_groups/6m.png", "6+ Months", c_yellow),
            description="First foods, smooth purees and single grain porridges.",
            order=1
        )
        age_12m = AgeGroup.objects.create(
            name="12+ Months",
            slug="12-months",
            icon=make_mock_image("age_groups/12m.png", "12+ Months", c_red, (255,255,255)),
            description="Textured foods, small bites, and nutritious cereals.",
            order=2
        )
        age_2y = AgeGroup.objects.create(
            name="2+ Years",
            slug="2-years",
            icon=make_mock_image("age_groups/2y.png", "2+ Years", c_green, (255,255,255)),
            description="Pancakes, cookies, and delicious wholesome snacks.",
            order=3
        )
        age_4y = AgeGroup.objects.create(
            name="4+ Years",
            slug="4-years",
            icon=make_mock_image("age_groups/4y.png", "4+ Years", c_cream, c_dark),
            description="School lunchbox snacks, milk mixes, and family meals.",
            order=4
        )

        # 2. Create Categories
        self.stdout.write("Creating Categories...")
        cat_cereals = Category.objects.create(
            name="Cereals & Porridge",
            slug="cereals-porridge",
            icon=make_mock_image("categories/cereals_icon.png", "Cereals", c_cream),
            image=make_mock_image("categories/cereals_banner.png", "Cereals & Porridge Range", c_yellow, size=(600, 300)),
            description="Organic ragi, oats, and millet porridges for babies.",
            order=1,
            is_featured=True
        )
        cat_pancakes = Category.objects.create(
            name="Pancake Mixes",
            slug="pancake-mixes",
            icon=make_mock_image("categories/pancake_icon.png", "Pancakes", c_cream),
            image=make_mock_image("categories/pancake_banner.png", "Pancake Mixes Range", c_red, (255,255,255), size=(600, 300)),
            description="Easy to make, nutrient-dense pancakes with millet goodness.",
            order=2,
            is_featured=True
        )
        cat_cookies = Category.objects.create(
            name="Millet Cookies",
            slug="millet-cookies",
            icon=make_mock_image("categories/cookies_icon.png", "Cookies", c_cream),
            image=make_mock_image("categories/cookies_banner.png", "Healthy Cookies Range", c_green, (255,255,255), size=(600, 300)),
            description="Wholesome butter cookies made with ragi, amaranth, and jaggery.",
            order=3,
            is_featured=True
        )
        cat_snacks = Category.objects.create(
            name="Healthy Snacks",
            slug="healthy-snacks",
            icon=make_mock_image("categories/snacks_icon.png", "Snacks", c_cream),
            image=make_mock_image("categories/snacks_banner.png", "Healthy Snacks Range", c_yellow, size=(600, 300)),
            description="Millet puffs and star-shaped snacks baked to perfection.",
            order=4,
            is_featured=True
        )
        cat_drinks = Category.objects.create(
            name="Super Drinks",
            slug="super-drinks",
            icon=make_mock_image("categories/drinks_icon.png", "Drinks", c_cream),
            image=make_mock_image("categories/drinks_banner.png", "Super Milk Mixes Range", c_red, (255,255,255), size=(600, 300)),
            description="Chocolate and almond milk mixes loaded with millets, no refined sugar.",
            order=5,
            is_featured=False
        )

        # 3. Create Products
        self.stdout.write("Creating Products & Product Images...")

        # Product 1: Ragi Strawberry Porridge
        p1 = Product.objects.create(
            name="Organic Ragi & Strawberry Porridge",
            slug="organic-ragi-strawberry-porridge",
            category=cat_cereals,
            short_description="Gentle baby food cereal sweetened with real strawberries, made with sprouted ragi.",
            description="Our Sprouted Ragi & Strawberry Cereal is perfect for babies starting solids. Sprouting ragi increases iron bioavailability and makes it extremely easy to digest. Mixed with freeze-dried strawberry powder, it offers a natural fruity flavor without any artificial colors or added white sugar. Just cook with water or milk for 3 minutes!",
            ingredients="Organic Sprouted Ragi (Finger Millet) - 85%\nNatural Strawberry Powder - 10%\nOrganic Amaranth - 5%",
            nutritional_info="Energy: 365 kcal\nProtein: 7.2 g\nCarbohydrates: 78.4 g\nFat: 1.5 g\nIron: 4.8 mg\nCalcium: 340 mg",
            weight="200g Pack",
            mrp=199.00,
            selling_price=179.00,
            rating=4.8,
            review_count=142,
            is_bestseller=True,
            is_featured=True
        )
        p1.age_groups.add(age_6m, age_12m)
        ProductImage.objects.create(product=p1, image=make_mock_image("products/ragi_straw_1.png", "Ragi Strawberry Cereal Front", c_red, (255,255,255)), is_primary=True, order=1)
        ProductImage.objects.create(product=p1, image=make_mock_image("products/ragi_straw_2.png", "Ragi Strawberry Nutritional Info", c_cream), is_primary=False, order=2)

        # Product 2: Sprouted Ragi Powder
        p2 = Product.objects.create(
            name="100% Sprouted Ragi Powder Cereal",
            slug="100-sprouted-ragi-powder-cereal",
            category=cat_cereals,
            short_description="Single ingredient first baby food porridge, rich in calcium and iron.",
            description="A traditional recipe made modern. Single ingredient sprouted ragi powder is the absolute best starting solid for 6 months+ infants. The sprouting process enhances the calcium absorption and makes the cereal light on little tummies. No additives, no milk powder, completely vegan.",
            ingredients="100% Organic Sprouted Ragi (Finger Millet) Flour",
            nutritional_info="Energy: 358 kcal\nProtein: 7.5 g\nCarbohydrates: 79.1 g\nFat: 1.3 g\nIron: 5.2 mg\nCalcium: 350 mg",
            weight="250g Pack",
            mrp=150.00,
            selling_price=135.00,
            rating=4.9,
            review_count=320,
            is_bestseller=True,
            is_featured=False
        )
        p2.age_groups.add(age_6m)
        ProductImage.objects.create(product=p2, image=make_mock_image("products/ragi_pure_1.png", "Sprouted Ragi Powder Front", c_yellow), is_primary=True, order=1)

        # Product 3: Chocolate Millet Pancake Mix
        p3 = Product.objects.create(
            name="Chocolate Millet & Oats Pancake Mix",
            slug="chocolate-millet-oats-pancake-mix",
            category=cat_pancakes,
            short_description="Super fluffy, rich chocolate pancakes made with foxtail millet, oats and raw cacao.",
            description="Say goodbye to refined flour (maida) and hello to the goodness of Foxtail Millet and Oats! This pancake mix makes breakfast fun and nutrient-rich. Sweetened with healthy coconut sugar, it has a delicious chocolate flavor from raw, organic cacao powder. Just add milk/water and butter, pan fry, and enjoy fluffiness!",
            ingredients="Oats Flour - 40%\nFoxtail Millet Flour - 30%\nCoconut Sugar - 15%\nRaw Cacao Powder - 10%\nBaking Powder - 5%",
            nutritional_info="Energy: 382 kcal\nProtein: 9.8 g\nCarbohydrates: 72.1 g\nFat: 4.5 g\nCalcium: 120 mg",
            weight="150g Pack",
            mrp=250.00,
            selling_price=225.00,
            rating=4.7,
            review_count=98,
            is_bestseller=True,
            is_featured=True
        )
        p3.age_groups.add(age_12m, age_2y, age_4y)
        ProductImage.objects.create(product=p3, image=make_mock_image("products/choc_pan_1.png", "Chocolate Pancake Mix Front", c_dark, c_yellow), is_primary=True, order=1)
        ProductImage.objects.create(product=p3, image=make_mock_image("products/choc_pan_2.png", "Chocolate Pancakes Stack", c_cream), is_primary=False, order=2)

        # Product 4: Banana Oats Pancake Mix
        p4 = Product.objects.create(
            name="Banana Oats & Wheat Pancake Mix",
            slug="banana-oats-wheat-pancake-mix",
            category=cat_pancakes,
            short_description="Naturally sweet banana pancakes with oats and whole wheat, zero white sugar.",
            description="Wholesome and easy pancakes with the sweet goodness of real bananas. Perfect for toddlers and busy mornings. Made with rolled oats, whole wheat flour, and sweetened naturally with freeze-dried banana powder. Easy to bite, soft, and yummy.",
            ingredients="Whole Wheat Flour - 45%\nOats Flour - 30%\nBanana Fruit Powder - 20%\nBaking Powder - 5%",
            nutritional_info="Energy: 370 kcal\nProtein: 8.9 g\nCarbohydrates: 75.3 g\nFat: 2.1 g",
            weight="150g Pack",
            mrp=220.00,
            selling_price=198.00,
            rating=4.6,
            review_count=74,
            is_bestseller=False,
            is_featured=True
        )
        p4.age_groups.add(age_12m, age_2y)
        ProductImage.objects.create(product=p4, image=make_mock_image("products/banana_pan_1.png", "Banana Pancake Mix Front", c_yellow), is_primary=True, order=1)

        # Product 5: Ragi Butter Cookies
        p5 = Product.objects.create(
            name="Healthy Ragi & Chocolate Butter Cookies",
            slug="healthy-ragi-chocolate-butter-cookies",
            category=cat_cookies,
            short_description="Crispy baked ragi butter cookies sweetened with jaggery, no maida.",
            description="Our Ragi Butter Cookies are a guilt-free snack for school boxes. Baked with pure butter, ragi flour, and whole wheat, they are sweetened with mineral-rich jaggery instead of refined sugar. Kids love the subtle chocolate flavor, and parents love the nutrition profile!",
            ingredients="Organic Ragi Flour - 35%\nWhole Wheat Flour - 25%\nPure Butter - 20%\nJaggery Powder - 15%\nCacao Powder - 5%",
            nutritional_info="Energy: 485 kcal\nProtein: 6.8 g\nCarbohydrates: 61.2 g\nFat: 22.4 g\nCalcium: 210 mg",
            weight="120g Box (Pack of 12)",
            mrp=120.00,
            selling_price=99.00,
            rating=4.5,
            review_count=185,
            is_bestseller=True,
            is_featured=True
        )
        p5.age_groups.add(age_2y, age_4y)
        ProductImage.objects.create(product=p5, image=make_mock_image("products/ragi_cook_1.png", "Ragi Cookies Box Front", c_red, (255,255,255)), is_primary=True, order=1)

        # Product 6: Tangy Tomato Millet Puffs
        p6 = Product.objects.create(
            name="Baked Millet Puffs - Tangy Tomato",
            slug="baked-millet-puffs-tangy-tomato",
            category=cat_snacks,
            short_description="Crispy, baked (not fried) millet puffs with natural tomato seasoning.",
            description="Snack-time made healthy! These puffs are made from supergrains Jowar, Ragi, and Corn. Baked, seasoned with real dried tomatoes and mild spices, they make the perfect travel companion or evening snack. Vegan, gluten-free, and absolutely delicious.",
            ingredients="Jowar (Sorghum) - 40%\nCorn - 30%\nRagi - 15%\nCold Pressed Sunflower Oil - 10%\nTomato Powder & Mild Spices - 5%",
            nutritional_info="Energy: 410 kcal\nProtein: 8.2 g\nCarbohydrates: 70.4 g\nFat: 9.8 g",
            weight="50g Bag",
            mrp=80.00,
            selling_price=69.00,
            rating=4.7,
            review_count=62,
            is_bestseller=False,
            is_featured=True
        )
        p6.age_groups.add(age_2y, age_4y)
        ProductImage.objects.create(product=p6, image=make_mock_image("products/tomato_puff_1.png", "Tomato Puffs Front", c_green, (255,255,255)), is_primary=True, order=1)

        # Product 7: Millet Chocolate Drink Mix
        p7 = Product.objects.create(
            name="Natural Chocolate Millet Milk Mix",
            slug="natural-chocolate-millet-milk-mix",
            category=cat_drinks,
            short_description="Wholesome milk mix made with ragi, amaranth, dates and cocoa.",
            description="Upgrade your child's milk glass! Instead of standard malt powders loaded with 60% sugar, our Milk Mix is made of 80% millets and nuts, sweetened only with date powder. It provides sustained energy and is rich in calcium.",
            ingredients="Ragi Flour - 30%\nAlmond Powder - 25%\nDate Powder - 20%\nRaw Cacao - 15%\nAmaranth Flour - 10%",
            nutritional_info="Energy: 430 kcal\nProtein: 12.4 g\nCarbohydrates: 65.2 g\nFat: 11.2 g\nCalcium: 280 mg",
            weight="200g Jar",
            mrp=299.00,
            selling_price=269.00,
            rating=4.8,
            review_count=110,
            is_bestseller=False,
            is_featured=False
        )
        p7.age_groups.add(age_4y)
        ProductImage.objects.create(product=p7, image=make_mock_image("products/choco_drink_1.png", "Choco Milk Mix Jar", c_dark, c_yellow), is_primary=True, order=1)

        # 4. Create Homepage Banners
        self.stdout.write("Creating Banners...")
        Banner.objects.create(
            title="Yes to Millets, No to Junk!",
            subtitle="Wholesome organic cereals, pancakes, and cookies made with ragi, amaranth, dates & pure butter. Made by 2 Mothers.",
            image_desktop=make_mock_image("banners/banner1.png", "", c_yellow, size=(1920, 600)),
            cta_text="Shop Millet Range",
            cta_link="/products/",
            order=1
        )
        Banner.objects.create(
            title="Pancake Mornings Made Wholesome",
            subtitle="Ditch the maida! Fluffy millet pancakes packed with oats and banana. Made in 3 easy steps.",
            image_desktop=make_mock_image("banners/banner2.png", "FLUFFY MILLET PANCAKES BANNER", c_red, (255,255,255), size=(1920, 600)),
            cta_text="Browse Pancake Mixes",
            cta_link="/products/category/pancake-mixes/",
            order=2
        )

        # 5. Create Testimonials
        self.stdout.write("Creating Testimonials...")
        Testimonial.objects.create(
            customer_name="Trupti Sharma",
            rating=5,
            review_text="My 8-month-old absolutely loves the Sprouted Ragi Strawberry Porridge. It is so easy to prepare in the mornings and I feel confident about the honest ingredients list.",
            product=p1,
            is_featured=True
        )
        Testimonial.objects.create(
            customer_name="Ananya Mathur",
            rating=5,
            review_text="The Chocolate Millet Pancakes are a lifesaver on Sundays. My twins eat them without complaining, and I'm happy because there is zero maida or refined sugar.",
            product=p3,
            is_featured=True
        )
        Testimonial.objects.create(
            customer_name="Vikram Rathore",
            rating=5,
            review_text="I was looking for a healthy snack box option for school. The Ragi Butter Cookies are delicious! Very crispy, and sweetened with jaggery.",
            product=p5,
            is_featured=True
        )

        # 6. Create USPs
        self.stdout.write("Creating USPs...")
        USP.objects.create(title="No Maida", description="100% whole grain millets and oats. Absolutely zero refined wheat flour.", order=1)
        USP.objects.create(title="No Refined Sugar", description="Sweetened only with mineral-rich jaggery, coconut sugar, or dates.", order=2)
        USP.objects.create(title="Made with Millets", description="Powered by climate-resilient supergrains like Ragi, Jowar, and Bajra.", order=3)
        USP.objects.create(title="No Preservatives", description="Zero artificial colors, synthetic flavors, or chemical shelf-stabilizers.", order=4)

        # 7. Create Team Members
        self.stdout.write("Creating Team Members...")
        TeamMember.objects.create(
            name="Shauravi Malik",
            role="Co-Founder",
            bio="Shauravi worked in investment banking at J.P. Morgan but wanted to build an honest brand for children's food.",
            photo=make_mock_image("team/shauravi.png", "Shauravi Malik Portrait", c_red, (255,255,255)),
            linkedin_url="https://linkedin.com",
            order=1
        )
        TeamMember.objects.create(
            name="Meghana Narayan",
            role="Co-Founder",
            bio="Former international swimmer, Rhodes Scholar, and McKinsey consultant passionate about nutritional education.",
            photo=make_mock_image("team/meghana.png", "Meghana Narayan Portrait", c_yellow),
            linkedin_url="https://linkedin.com",
            order=2
        )

        # 8. Create FAQs
        self.stdout.write("Creating FAQs...")
        FAQ.objects.create(question="Are your products safe for babies starting solids?", answer="Yes! Our Cereals and Porridges range is specifically formulated for infants 6 months and older. The sprouted grains are highly digestible.", category="Products", order=1)
        FAQ.objects.create(question="Do you add any synthetic preservatives to increase shelf life?", answer="Absolutely not. We use advanced packaging techniques and dry formulations (porridge powders, dry cookies) to naturally extend shelf life without any chemical preservatives.", category="Ingredients", order=2)
        FAQ.objects.create(question="Where do you ship your products from?", answer="We ship all orders directly from our state-of-the-art, hygienic facility in New Delhi, India.", category="Shipping", order=3)

        # 9. Create Blog Categories & Posts
        self.stdout.write("Creating Blog posts...")
        bcat_nutrition = BlogCategory.objects.create(name="Child Nutrition", slug="child-nutrition")
        bcat_recipes = BlogCategory.objects.create(name="Parenting Hacks", slug="parenting-hacks")

        BlogPost.objects.create(
            title="The Miracle of Millets: Why Ragi is the Ultimate Superfood for Babies",
            slug="miracle-of-millets-ragi-baby-superfood",
            category=bcat_nutrition,
            featured_image=make_mock_image("blog/blog1.png", "Ragi Supergrain Info", c_red, (255,255,255), size=(800, 400)),
            excerpt="Discover how sprouted finger millet (ragi) provides 3x more calcium than milk and helps build strong bones in growing babies.",
            content="<p>Millets have been a staple of Indian agriculture for thousands of years. Among them, Ragi (Finger Millet) stands out as a true nutritional powerhouse. It is exceptionally rich in calcium, iron, and dietary fiber, making it the perfect first food for infants starting solids.</p><h3>Why Sprout Ragi?</h3><p>Sprouting is a natural process that activates enzymes within the grain. This increases the bioavailability of minerals (especially iron) and breaks down complex starches, making it incredibly gentle on a baby's developing digestive system.</p><h3>Key Benefits:</h3><ul><li><strong>Calcium Rich:</strong> Helps in bone development and strengthening teeth.</li><li><strong>Iron Bioavailability:</strong> Fights baby anemia naturally.</li><li><strong>Gluten-Free:</strong> Safe for infants with wheat sensitivities.</li></ul>",
            author="Shauravi Malik",
            is_featured=True,
            published_at=timezone.now()
        )

        BlogPost.objects.create(
            title="5 Healthy Breakfast Ideas for Toddlers (Ready in 10 Minutes!)",
            slug="5-healthy-breakfast-ideas-toddlers-10-mins",
            category=bcat_recipes,
            featured_image=make_mock_image("blog/blog2.png", "Toddler Breakfast Ideas", c_yellow, size=(800, 400)),
            excerpt="Busy mornings? Ditch the sugary cereal loops and try these easy millet-based breakfast recipes that take less than 10 minutes to cook.",
            content="<p>Mornings can be chaotic, especially when you have toddlers running around. It is tempting to pour a bowl of sugary, highly processed cereals, but this leads to mid-morning sugar crashes. Here are 5 quick, wholesome ideas to fuel your child's day:</p><h4>1. Millet Chocolate Pancakes</h4><p>Use Highness Chocolate Pancake Mix. Whisk with milk, pour on a hot griddle, and cook for 2 minutes on each side. Serve with honey or banana slices.</p><h4>2. Fruit & Yogurt Cereal Bowl</h4><p>Mix cook ragi porridge with thick curd, honey, and top with fresh mango or banana slices.</p>",
            author="Meghana Narayan",
            is_featured=True,
            published_at=timezone.now() - timezone.timedelta(days=2)
        )

        # 10. Create Recipes
        self.stdout.write("Creating Recipes...")

        r1 = Recipe.objects.create(
            title="Sprouted Ragi Chocolate Pancake Tower",
            slug="sprouted-ragi-chocolate-pancake-tower",
            featured_image=make_mock_image("recipes/recipe1.png", "Chocolate Pancake Stack", c_dark, c_yellow, size=(800, 400)),
            prep_time=5,
            cook_time=10,
            servings=3,
            age_group=age_12m,
            difficulty="easy",
            ingredients_list="1 cup Highness Chocolate Pancake Mix\n1/2 cup Milk or Water\n1 tbsp Butter (for cooking)\n1 Banana (sliced)\n1 tbsp Honey or Maple Syrup (optional)",
            instructions="<div class='instruction-step'><span class='instruction-step-num'>1</span><p class='text-muted fs-5'>Whisk 1 cup of Chocolate Pancake Mix with 1/2 cup of milk or water in a medium bowl until a smooth batter forms. Let it rest for 2 minutes.</p></div><div class='instruction-step'><span class='instruction-step-num'>2</span><p class='text-muted fs-5'>Heat a non-stick pan over medium-low heat and grease lightly with butter. Pour a ladle of batter onto the pan.</p></div><div class='instruction-step'><span class='instruction-step-num'>3</span><p class='text-muted fs-5'>Cook until bubbles form on the surface (about 2 minutes), then flip and cook the other side for another 1-2 minutes until golden brown.</p></div><div class='instruction-step'><span class='instruction-step-num'>4</span><p class='text-muted fs-5'>Stack the warm pancakes on a plate, layering with banana slices in between. Drizzle honey on top and serve warm!</p></div>",
            is_featured=True,
            published_at=timezone.now()
        )
        r1.related_products.add(p3, p4)

        r2 = Recipe.objects.create(
            title="Fresh Banana Millet Porridge Bowl",
            slug="fresh-banana-millet-porridge-bowl",
            featured_image=make_mock_image("recipes/recipe2.png", "Millet Porridge Bowl", c_cream, c_dark, size=(800, 400)),
            prep_time=2,
            cook_time=5,
            servings=1,
            age_group=age_6m,
            difficulty="easy",
            ingredients_list="3 tbsp Highness Sprouted Ragi Powder\n1 cup Water or Milk\n1/2 ripe Banana (mashed)",
            instructions="<div class='instruction-step'><span class='instruction-step-num'>1</span><p class='text-muted fs-5'>In a small saucepan, whisk 3 tablespoons of Sprouted Ragi Powder into 1 cup of cold water or milk until no lumps remain.</p></div><div class='instruction-step'><span class='instruction-step-num'>2</span><p class='text-muted fs-5'>Place the saucepan over medium heat and cook, stirring continuously to prevent sticking, for 4-5 minutes until the mixture thickens.</p></div><div class='instruction-step'><span class='instruction-step-num'>3</span><p class='text-muted fs-5'>Remove from heat and stir in the mashed ripe banana for natural sweetness. Let it cool to lukewarm before feeding.</p></div>",
            is_featured=True,
            published_at=timezone.now() - timezone.timedelta(days=1)
        )
        r2.related_products.add(p1, p2)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully with all mock assets!"))

    def clean_data(self):
        """Cleans existing data to prevent duplicate seeding issues"""
        self.stdout.write("Cleaning existing database tables...")
        AgeGroup.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        ProductImage.objects.all().delete()
        Banner.objects.all().delete()
        Testimonial.objects.all().delete()
        USP.objects.all().delete()
        TeamMember.objects.all().delete()
        FAQ.objects.all().delete()
        BlogCategory.objects.all().delete()
        BlogPost.objects.all().delete()
        Recipe.objects.all().delete()
