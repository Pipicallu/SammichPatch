
# [SammichPatch](https://sammichpatch.herokuapp.com/)

## A brief origin story.
Have you ever been sat at your desk, at home? or at the office? Perhaps you were simply day dreaming or maybe even brainstorming your next 
big idea, when all of a sudden as if seemingly out of nowhere... THE CRAVING HITS! And as if by magic all your thoughts past, present and 
future are instantly replaced with and insatiable hunger that until quenched will not release you from its buns (excuse the pun).
In my case that craving was a sandwich. Not just any sandwich, but it had to be the perfect sandwich, with all the fixins, fillings
and just the right selection of cheese. That's when I knew that the answer to my MS4 project wasn't in my head but as with most of 
the important decisions I've undertaken in my short tenure as an adult, it was most definitely a gut feeling. 

And so the idea for SammichPatch was born. A web app that brings the experience of subway-esque sandwich making to the digital space
allowing our users to brave the crave and create their own perfect lunchtime snack, everytime. Our SammichPatch menu allows you to choose from
a diverse list of premium quality ingredients across a range of dietary requirements, offering something for everyone. Your creation can then be
paired with a choice of drink and side, rounding it out to a full lunchtime experience. The site allows for secure checkout using stripe, as well
as the ability for users to create accounts to save delivery information as well as view their past orders. Users may also edit their order and remove 
items from their bag. The site owner is provided with the ability to add, update or remove products from the site, as well as viewing the full order
customer order history, in the django admin. A lot of love and effort was put into the making of this app. I certainly hope it comes across to you.

# UX

### User Stories.	
- As a User, I want to be able to understand the site's purpose without forfeiting any information.
- As a User, I want to navigate the site easily and in the simplest most intuitive way possible.
- As a User, I want to use the main Form to build my sandwich and see my items added to the cart.
- As a User, I wan't the categories of that main form to give me an indication of whether or not I have selected a cretain category of ingredient when building my sandwich.
- As a User, I want a diverse list of ingredients to choose from 
- As a User, I want to sort my ingredients by dietry Requrement. If any.
- As a User, I want to see my order in a cart before purchase to change or delete any mistakes made.
- As a User, I want to have a selection of sides and drinks to round out my order.
- As a User, I want to be able to see my order total.
- As a User, I want to be able to checkout and pay securley.
- As a User, I want to have an account where I can save both my delivery info as well as see my past orders

### Site owner goals.

As the site owner who sees the value in my own creation I too feel as though I would want to be a user of this site.
So many of my choices as a site owner were made with the user purposefully in mind. 

Below are the main questions I asked myself throughout the development process:

- Is this obvious to the user? - specifically when dealing with the overal interactivity of the site and presentation of information,
  I.E. how easy is it to get from A to B? are the visual and navigational choices delightful? Does the site react in a way that is intuative to the user? Does it relate to/re-create a real life model or experience?
  more specifically - can I as a user recgonise where I am, how I got here and what options I have presented to me here on out?
- Is it pretty? - Does the overall UI look inviting? is there an obvious theme or color scheme? Is it attractive to my users, do they engage with the pictures and images used?
  Is the information displayed in a spaced out fashion? Is it distinguishible from other pieces of information? Is it pleasurable to the eye? Can it be retained at a glance? Will I need to remember where to go the next time I visit? 
- Is it interactive? - Does the site offer  visual queues to the user? Are the responses timely? Do they add to the understanding of the user? Do they add to the interactivity of the user and add weight to the users choices? Are their points where the site is susceptible to lag or inefficancy?
- Is it purposeful? - Am I building something enjoyable? Does it offer incentive to return? Is it a pleasure to use? Is it convenient?  Have I built the site in a way that helps the user fullfill the desired need?

Here are the site specific conclusions to the questions asked:

- As a Site Owner, I want my users to be able to securely and easily check out their products.
- As a Site Owner, I want to offer a visually appealing application that is gives my users confidence in the quality of my products.
- As a Site Owner, I want my users to understand how to correctly make use of my site from the landing page alone.
- As a Site Owner, I want to be able to edit and modify my site and its ingredients/items when required.
- As a Site Owner, I want to view an order history so as to track the performance of my business over time.


# Design & Colours

The approach here was a minimalist theme that took on adornments reminicent of those old 50's American diners, with the paper menus and double borders.
The logo itself was also designed to look rustic and classic in nature, and the choices of brown for the backgrounds of products and text coupled, 
with the light green borders for menus and forms were put in place with the hope of accenting the quality of the products and ingredients. In short 
I wanted the site to be reflective of finding ones-self at a diner or bakery or café.


### Colour Palette:
![colour palette](/media/colours.png)

### Icons

- All icons were sourced from SVGREPO (https://www.svgrepo.com/), 
as they provide an assorment of multicoloured icons that provided 
stark contrast to the otherwise minimal aesthetic I went for with
the colour palette.



### Typography

As Always the font choice needed to be specific. The all caps font Halva fit perfectly,
As it reminded me of those neon signs one would see at a classic restaurant or diner.
It felt instantly thematic and on brand and is used in both the bold and regular font weight
for titles and body text respectively. The font is available for download in the 
assets folder of this project. It is also deployed locally as google fonts don't seem to have
it freely available.

### Wireframes

For this project I used <a href= "https://www.figma.com/">figma</a> as a free online tool to complete my wireframes.
Its Easy to use navigation had me creating high fidelity wireframes and concepts within minutes.
I also used it as an editing tool to design my logo from scratch.
You can find all my wireframes here including the original concepts that were eventually refined to what the project looks like today.
![wireframe1](/media/wireframe1.png)
![wireframe2](/media/wireframe3.png)
![wireframe3](/media/wireframe2.png)

# Testing Credentials

 In order to test the site functionality, the following admin credentials can be used to log in as a superuser:
    - Username: Admin
    - Password: Admin1234!

# Features

### Menu

- The Sandwich Menu is split into 5 distinct categories offering the user a single choice of Bread, Filling, Cheese and Spread, With an unlimited amount of salad addons.

- The sandwich menu also prohibits the user from being allowed to make orders that don't make sense by placing limits on certain categories, like a sanwich with two types of breads for example or with every single type of meat.
Right now this feature limits the user to a single choice in the filling category but I would like to improve upon this feature in the future.

- The sandwich menu also allows you to remove ingredients from your sandwich as you make it as each category functions as a collapsible menu that can be re-opened to edit
an ingredient chosen by mistake.

- When an Ingredient is removed an info Message appears on the site in the form of a toast.

- The plus buttons are greyed out when an ingredient is added in cases where adding more of that ingredient will result in a nonsensical order. There must be order when it comes to sandwich making.

- Users can press upon each ingredients picture to get more information about that specific ingredient.

- Users can browse the full menu or filter the menu by category to see specific items

- Users can view a list of allergens for each item and click on individual allergens for a pop-up which shows descriptions of selected allergen.

- A success message is displayed to notify the user than an item has been added to the shopping cart
Individual menu items fade up onto the screen as the user scrolls on the page


### bag

- A summary of the user's order is displayed where the item names, and sub-totals can be seen

- Users may remove items from their order completely

- A warning message is displayed whenever a change to the order is made

- The user can navigate back to the menu or proceed to the Checkout from here.


### Drinks and sides

- The sides and drinks menu is very similar to the Sandwich menu it is split into two distinct categories wich can be accessed seperately from the navbar.

- Both categories are collapsible to allow for easier manouverability within the menu.

- At present This menu is somewhat simplified and allows for the removal of items only to take place within the bag.

- As the main effort went in to creating the logic for building the user's sandwhich this part of the website came later as an addition,
which is why going forward I would also like to implement the grouping of multiple products to be listed with their quantity rather as individual bag items
however due to time constraints, I had to settle on adding them individually.

- Full access to dietary requirements as well as item descriptions are displayed upon clicking the relative product.

### Checkout

- A summary of the user's order is displayed for inspection featuring item names, quantities and sub-totals for all order items
The user needs to fill in the payment form in order to proceed with the payment

- If they already have an account, the form will be populated with their information

- The user will be offered an opportunity to Sign In or Sign Up before proceeding with the payment

- A checkbox allows the form data to be saved to the user's account if they've already got one

- A secure test payment can be made using Stripe's testing details
The form will only be submitted once it has been validated

- A loading screen obscures that checkout page while the payment is being processed, while the payment form's submit button is also deactivated to prevent submitting the payment twice by accident

- A webhook is used to ensure that the order is processed even when the payment process gets interrupted

- If the user is successful, the user is directed to the Checkout Success page where they can view a summary of their order

- A confirmation email is also sent to the user upon successful completion of a payment
The user will see a success message wit their order number displayed as an additional measure to ensure they get confirmation of an order being processed successfully

### Profile
- Once the user has signed up to the site, they can access their profile where they can change their default delivery information and see their order history
Images


## Features to be implemented.

#### Sides and drinks
- As stated before I would love to add more functionality like allowing for the webite to show drinks by quantity rather than individual items.

- I would love to add dynamic remove buttons so that the user can remove an item from the page without editing it in their bag.

#### menu
- I would love to expand on the logic for the adding of ingredients. Give customers the option to order a selection of two fillings for example.

#### Mobile Nav
- I would love to add a bottom nav for mobile as its something I am yet to eperiment with! Due to time constraints I feel as though I havent been able to 
experiment with mobile layouts as much as I'd like to as the majority of time spent on this project was getting the logic right.

#### Profile 
- I want to add a feature whereby customers can favourite certain orders and re-order them, to speed up delivery process.

# Database
By default, Django works with SQL databases. During development on my local machine I worked with the standard sqlite3 database installed with Django.
Heroku provies a PostgreSQL database for deployment.

#### User Model

The standard Djando user model, `django.contrib.auth.models`, was used for this project.

#### Menu App

##### Category Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, blank=True, null=True | CharField


##### DietaryRequirements Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, blank=True, null=True | CharField


##### Ingredients Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category model
Name | name | max_length=254, blank=True, null=True | CharField
Description | description |  | TextField
Dietary Requiremnets | Dietary Requirements |  | ManyToManyfield
Price | price | max_digits=4, decimal_places=2 | DecimalField
Is Vegetarian | is_vegetarian | default=False | BooleanField
Image Url | image_url | max_length=1024, null=True, blank=True |URLField
Image | image | null=True, blank=True | ImageField

##### SidesAndDrinks Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey to Category model
Name | name | max_length=254, blank=True, null=True | CharField
Description | description |  | TextField
Dietary Requiremnets | Dietary Requirements |  | ManyToManyfield
Price | price | max_digits=4, decimal_places=2 | DecimalField
Is Vegetarian | is_vegetarian | default=False | BooleanField
Image Url | image_url | max_length=1024, null=True, blank=True |URLField
Image | image | null=True, blank=True | ImageField

   
#### Checkout App

##### Order Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to UserProfile
Full Name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
Postcode | postcode | max_length=20, null=True, blank=False | CharField
Town Or City | town_or_city | max_length=40, null=True, blank=False | CharField
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address2 | max_length=80, null=True, blank=True | CharField
County| County | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimefield
Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Original bag | original_bag | null=False, blank=False, default='' | TextField
Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

##### OrderItem Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems' | ForeignKey to Order
Product | product | Product, null=False, blank=False, on_delete=models.CASCADE | ForeignKey to Product
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Order Item Total | order_item_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | Decimalfield

##### OrderSideItem Model

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderSideitems' | ForeignKey to Order
Product | product | Product, null=False, blank=False, on_delete=models.CASCADE | ForeignKey to Product
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Order Side Item Total | order_side_item_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | Decimalfield

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
- [Python](https://www.python.org/about/)

### Frontend Frameworks
- [Bootstrap](https://getbootstrap.com/)
- [npm](https://www.npmjs.com/)
- [AOS](https://michalsnik.github.io/aos/)
- [JQUERY](https://jquery.com/)
- [Amazon AWS S3](https://aws.amazon.com/)


### Libraries, Frameworks

- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Gunicorn](https://gunicorn.org/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [boto3](https://pypi.org/project/boto3/)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)
- [Stripe](https://stripe.com/ie)
- [PostgreSQL](https://www.postgresql.org/)


### Tools

- [Font Awesome](https://fontawesome.com/)
- [Figma](https://www.figma.com/)
- [Git](https://git-scm.com/about)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)

Further details on all Python packages used on this project can be found in the requirements.txt file.
Each of these is outlined below (click below to expand the dropdown), with the package version and a brief description.


# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Firstly in order to run this project locally on your own system, you will need the following installed:

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [Microsoft Visual Studio Code](https://code.visualstudio.com) (or any suitable IDE) to develop your project.

To allow you to access all functionality, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Feel free to click on the links above to see the necessary documentation

## Next Instructions

- Clone this GitHub repository by either clicking the  "**Code**" button with the downward facing arrow to the left of it above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
    - `git clone https://github.com/Pipicallu/SammichPatch`

- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`

- Next A virtual environment is recommended for the Python interpreter, Python has one built-in. Enter the command:
    - `python -m .venv venv`

- Activate your virtual environment as follows:
    - `source venv/bin/activate`

- Install all requirements from the [requirements.txt](/requirements.txt) file using this command:
    - `pip3 -r requirements.txt`

- In the IDE terminal, use the following command to launch the Django project:
    - `python manage.py runserver` 

    - The `python` part of this command assumes you are using windows, you may need to alter if you are using a seperate operating system.

- The Django server should be running locally now on **http://127.0.0.1:8000**.
 If it doesn't automatically open, you can copy/paste it into your browser of choice.

- When you run the Django server for the first time, it should create a new *SQLite3* database file: **db.sqlite3**
- Set up the required environment variables

   - Setting up the required environment variables can be achieved in two ways.

   - If you have chosen Visual Studio Code as your IDE, this must be done in the `settings.json` file in the .vscode directory or open it for editing in Visual Studio Code by navigating to `File`, `Preferences`, `Settings` and searching for the `settings.json` file. Enter the environment variables as follows:

   ```json
       "terminal.integrated.env.linux": {
           "DEVELOPMENT": "True",
           "SECRET_KEY": "<your key here>",
           "STRIPE_PUBLIC_KEY": "<your key here>",
           "STRIPE_SECRET_KEY": "<your key here>",
           "STRIPE_WH_SECRET": "<your key here>",
           "AWS_ACCESS_KEY_ID": "<your key here>",
           "AWS_SECRET_ACCESS_KEY": "<your key here>",
           "AWS_STORAGE_BUCKET_NAME": "<your bucket name here>",
       }
   ```
- If this proves too complicated create a file called `env.py` in the root directory of your project and open it your IDE for editing
    - In the `env.py` file, set your environment variables as shown below:

        ```python
        import os
        os.environ["AWS_ACCESS_KEY_ID"] = "<your key here>"
        os.environ["AWS_S3_REGION_NAME"] = "<your AWS S3 region name here>
        os.environ["AWS_SECRET_ACCESS_KEY"] = "<your key here>"
        os.environ["AWS_STORAGE_BUCKET_NAME"] = "<your AWS S3 bucket name here>"
        os.environ["SECRET_KEY"] = "<your secret key here>"
        os.environ["STRIPE_PUBLIC_KEY"] = "<your key here>"
        os.environ["STRIPE_SECRET_KEY"] = "<your key here>"
        os.environ["STRIPE_WH_SECRET"] = "<your key here>"
        os.environ["DEVELOPMENT"] = "True"    ```


- Next, you'll need to make migrations to create the database schema:
    - `python manage.py makemigrations`
    - `python manage.py migrate`

- In order to access the Django *Admin Panel*, you must generate a superuser:
    - `python manage.py createsuperuser`

    - (assign an admin username, email, and secure password)

- All of the model entries in the Ingredients/Categories/DietaryRequirements and SidesAndDrinks models are saved in the file db.json
all that is required is for you to load the data to the database.

`python3 manage.py loaddata categories.json`,

`python3 manage.py loaddata DietaryRequirements.json`,

`python3 manage.py loaddata ingredients.json`,

`python3 manage.py loaddata sidesanddrinks.json`

- Once the program is running, go to the local link provided and add `/admin` to see the data has loaded correctly.


## Heroku Deployment

- Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
    - `pip3 freeze --local > requirements.txt`

- Create a `Procfile` with the terminal command
    - `echo web: python app.py > Procfile`.

- Sign up for a free Heroku account, 
    - create your project app by clicking on the **New** button, followed by **Create new app** in the dropdown menu.
    - click the **Deploy** tab, at which point you can **Connect GitHub** as the Deployment Method,
 and select **Enable Automatic Deployment**.

 - Perform a `git push` on github to also push the project to Heroku

 - You may also want to check the **Activity** tab to see the progress of your app uploading.

- In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
    - Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
EMAILJS_USER_ID | `<your secret key>`
HOSTNAME | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_CANCEL_URL | `<link to all-products page in your app>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`
STRIPE_SUCCESS_URL | `<link to checkout/confirm page in your app>`

- In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. 
Make sure to select the free Hobby level. 

This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab.
You'll need to update your **.env** file with your new **database-url** details.

- once done you can use the command below to load the information to the postgress db.
    `./manage.py loaddata db.json`

- You can now check back on your previous deployment. click the "View app" button provided to see the website live and running.

# Testing

Testing details can be found in the testing.md file [here](/testing.md)

# Credit

## Media

- [AOS](https://github.com/michalsnik/aos) (Animate On Scroll) - for the animations on both the index.html and about.html pages.
- [svgrepo](https://www.svgrepo.com/) - for all the Dietary Requirements emojis and other icons used.
- [Unsplash](https://unsplash.com/) & [BBCGoodFood](https://www.bbcgoodfood.com/)- For the hero image on the about page as well as the images for the ingredients page.
- [twinkl](https://www.twinkl.ae/) - For the hero image on the index page.
- [cocacola](https://www.coca-colacompany.com/) - for the pictures on the drinks page.
- [sprite](https://www.sprite.com/) - for the pictures on the drinks page.
- [fanta](https://www.fanta.com/) - for the pictures on the drinks page.


## Acknowledgments

- The fine tutors Of Code institute, who had plenty of patience with me when I got stuck on various bugs in my project.

- special thanks to my mentor Allen Thomas Varghese, who has always encouraged me, guided me and told me that my designs were fancy!

- My friend and trusted mentor MrJerB who has been my friend throughout childhoond, adulthood and beyond. He is an incredible Software developer who has always taken time out of his day to explain and teach me how to seek out the right ways to learn.

- Also special thanks to tutor Johann whose project, Burgersaurus rex gave me the inspiration to add dietary requirements to my site. 

- Massive Thanks to Alexander who works at student care and without whom I would not have met my deadline.

## Personal Reflections

My previous projects taught me a lot about time management and I knew I needed to be extra vigilant this time with in order to meet a meager 6 week deadline. I wanted to work on getting a minimum viable project done, quite the undertaking when I found that even after the fullstack module I still felt pretty green when it came to coordinating between apps and navigating django. But if I've learned anything from code institute the best remedy for feeling overwhelmed is to make a plan, break down the problems and dive in piece by piece. A mentality that I feel served me well as I undoubtedly ran into the various challenges in building my very own first fullstack site, an endeavour that only a year ago seemed so beyond me. I am insanely proud to have made through and all I can do now is remain eager and carry on learning , as I feel as although I have come so far, I have barely scratched the surface. My love for the front-end in particular has certainely matured and I will not waste any time as I plan to familiarise myself with typescript, React and vuejs. On a more personal note the past five months have been an incredibly challenging time in my personal life and although my mental health suffered, this course was a major part of what helped me keep my focus throughout. I know that in future it will remain a constant reminder of what I can achieve when I really believe in myself and set my mind to something that I am passionate about. Here's to hopeful and gainful Employment! Thanks code institute. 

# Disclaimer

This site is intended for educational purposes only, and is not intended for use in any other capacity.




