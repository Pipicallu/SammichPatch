# Due to timing constraints Manual Testing had to be performed.

## HTML VALDATION

### Errors

- W3C HTML Validator - Unfortunately the W3C Validator for HTML does not understand the Django's templating syntax, so it therefore shows a lot of errors with regards to {{ variables }}, {% for %} {% endfor %}, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating. Also due to the Jinja templating, certain elements cannot be 'beautified' across multiple lines, and must remain on a single line.
other known "errors":
- Head element missing child element of title, which it isn't. Probably due to the Django templating language. Due to the first element on most pages extending the base template {% extends "base.html" %}↩{% load static %}↩↩{% block extra_css %}.
- Warning - Section lacks heading as some sections don't need one
- Warning - The type attribute is unnecessary for JavaScript resources.
- Warning ingredients page is showing inputs arent allowed a min attribute in convention - but this is necessary for the further expansion of work on quantities that I will implement as the next feature.

Any duplicate id's thrown up are in reference to the Jinja conditional logic statements that required me to repeat the same inputs

## CSS

- All the CSS for the site was tested using https://jigsaw.w3.org/css-validator/validator and returned no errors.

## JS

JS All the JavaScript for the site was tested using https://jshint.com/. Presently there are no errors save a few warnings. Which are of no concern as most modern browsers support ECMA 6.
As well as unidentified $ when it came to using Jquery for some of the bootstrap elements.

## Responsiveness

I used Am I Responsive and Responsinator to ensure that my app worked on multiple devices. The latter was expecially helpful when wanting to check out horizontal orientations on mobile devices.

As well as chrome developer tools, which has the provision to test on:

- Samsung Galaxy - Responsive
- Pixel 2 - Responsive
- Pixel 2 XL - Responsive
- iPhone 5s/Se/6/7/8/X - Responsive
- iPad 9.7" - Responsive
- iPad Pro - Responsive
- Surface Duo - Responsive
- Galaxy Fold - Responsive

- I also had a friend open it up on the latest 12 pro and 12 pro max iPhones.

## Compatibility

To ensure a broad range of users can successfully use this site, I tested it across the 6 major browsers in both desktop and mobile configuration.

Chrome - latest version
Edge - latest version
Firefox - latest version
Safari - latest version
Opera - latest version

## Links/Buttons
- All links work and are accounted for.

## Images
- All images render correctly, all image links work.

## Chrome Developer tools.

Together with [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) was the key tool used here for all aspects of testing my front-end and design. 
One of the largest bugs I had when sorting the front end was an issue interacting with the imported Animate on Scroll library
which kept breaking the layout on mobile devices due to the size and orientation of certain images. It was thanks to Dev tools I was able to realise that the issue didn't have anythign to do with the html, but the foreign package.

## Authentication
Every attempt has been made to secure the app by only allowing authenticated super users to access pages where CUD (create, update, delete) functionality needs to be performed.

## Menu App
A user has be logged in as a super user in order to Add, Update or Delete an ingredient or Drink/side. Should they try to access the related URLs by typing them directly in the browser,
they're informed of the need to be logged in with the proper credentials and redirected to the Home page. Furthermore, the buttons to Update and Delete products are only displayed on the Menu screen when a user is logged in as a super user.

## Testing
Below Please find a checklist I used to ensure all components of the site were working as well as so that users were able to navigate the site properly:

- **Nav Bar**, The main Tool for site navigation, it was necessary to design an instantly recognisable nav-layout for both mobile and desktop users.
It was key that this part of the website was not only appealing but also instantley familiar.
    
    - Click on navigation links to confirm correct redirection to the corresponding pages 
    - Make sure  of the colour transition of navigation links on hover 
    - Ensure that the logo also worked as a link to the home page 
    - Ensure the layout changed to accomodate smaller screens
    - Ensure that the Aesthetic of the navbar was minimal and didnt interfere with the user's ability to navigate the site.
    - Hamburger menu and subsequent drop down menu operational Y/N
    - Dropdown menus for Drinks/Sides and Account operations Y/N

- **Landing page**,  Here I wanted to make sure that my users primarily understood the purpose of the site,
how to interact with it as well as how to use the page before them to reach the menu and sides pages using soley the links available on the page
Rather than the navbar.

    - The link in the Hero image working correctly Y/N
    - All Animations on scroll working correctly Y/N
    - Are Users able to understand how to use the site based on the information displayed on the how to section? Y/N
    - Is the layout still intact on mobile devices? Y/N


- **Ingredients page (Sandwiches)**, This page is where the majority of the work took place on this page I wanted figure out if my users understood the work flow of the app and whether or not the process came naturally to them.
also whether they were able to use the various sorting functions to manipulate the menu for their specific dietary requrements.

    - Verify the user is able to recognise the menu as titled Y/N
    - Verify the user is able to sort by price Y/N
    - Verify the user is able  to show the vegetarian menu Y/N
    - Verify the user is able to understand how to sort by dietary Requirements Y/N
    - Can the user able to click on the images to find out more? Y/N
    - Can the user select the dietary requirements to find out more? Y/N
    - Can the user Identify each category? Y/N
    - Can the user make use of the collapsibles in the case of navigating the menu? Y/N
    - Can the user add an ingredient? Y/N
    - Can the user make use of the collapsibles in the case of reopening the menu to remove an incorrect ingredient? Y/N
    - Can the user remove an ingredient? Y/N
    - Can the user see the toast informing the that said ingredient has been removed? Y/N
    - Can the user identify when the ingredient has been added to bag? Y/N
    - Can the user identify when the Sandwich has been added to bag? Y/N
    - can the user see the individual cost of each ingredient added? Y/N
    - can the user see the subtotal cost of the combined sandwich? Y/N

- **Drinks and Sides**, although a simplified version of the ingredients page it was key that this part of the site worked correctly for our users to be able to round out their order.
Alot of the session logic was re-worked here alongside seperate views being added.

    - Verify the user is able to recognise the menu as titled Y/N
    - Verify the user is able to sort by price Y/N
    - Can the user able to click on the images to find out more? Y/N
    - Can the user select the dietary requirements to find out more? Y/N
    - Can the user Identify each category? Y/N
    - Can the user make use of the collapsibles in the case of navigating the menu? Y/N
    - Can the user add an item? Y/N
    - Can the user identify when the item has been added to bag? Y/N
    - can the user see the subtotal cost of the combined sandwich? Y/N
   

- **Bag Page**, I wanted this page to act as a staging ground for the checkout pages so that users were able to correctly finalise their order.
    
    - Verify that the page heading displays correctly Y/N
    - Verify that Each product is displayed with the correct icon representation. Y/N
    - Verify that the price of each item as well as the subtotal is displayed correctly Y/N
    - In the case of a Sandwich Verify that each ingredient attributing to the subtotal is displayed Y/N
    - Verify that bag items can be removed from the bag Y/N
    - Confirm that the Order total, appropriate Delivery Charge and Grand Total are displayed correctly Y/N
    - confirm the keep shopping and secure checkout buttons are working correctly Y/N

- **checkout** page, One of if not the key feature of the site allowing my userbase to checkout items securely and safely. Ensuring this was my goal.
    
    - Verify that the page heading displays correctly 
    - Confirm that the Details section of the payment form displays correctly with all inputs present and placeholders displaying Y/N
    - Confirm that the Delivery section of the payment form displays correctly with all inputs present and placeholders displaying Y/N
    - Confirm that the Payment section of the payment form displays correctly with all inputs present and placeholders displaying Y/N
    - Is there a checkbox is displayed for logged-in users to save their information to their profile Y/N
    - Verify that the form data is saved to a logged-in user's profile if the checkbox is checked Y/N
    - Confirm that buttons to register or sign in are displayed instead of the checkbox for users not logged into the site Y/N
    - Confirm that the register and sign in buttons direct the user to the appropriate page when clicked Y/N
    - Verify that an error message is displayed below the Payment section when invalid card details are entered Y/N
    - Verify that an loading spinner is displayed when the Checkout button is clicked Y/N
    - Verify that the Checkout button is disabled when the Checkout button is clicked Y/N
    - Are the order summary and relevant totals being displayed correctly in all formats ? Y/N

- **Stripe**
    
    - verify in stripe that payment is fullfilled correctly Y/N
    - verify in stripe that webhooks are working and endpoints are correct Y/N

- **Profile Page**, Here is where the user should be able to see their saved credentials as well as order history. 
    
    - Verify the user is able to identify the page from the header Y/N
    - Verify the user is able to see their information saved if any Y/N
    - can the user add and save their information on the page? Y/N
    - are the inputs clearly marked so as to indicate to the user where to place the correct information? Y/N
    - Does the update information button work as intended? Y/N
    - Can the orders sort through their order history? Y/N
    - Can they correctly identify the order total and date the order was made? Y/N
    - Can they select the truncated order number to be directed to the Checkout success page ? Y/N
    - is the order table clear and identifiable under the correct subheading? Y/N

## SuperUser Testing

- **Add an Ingredient** **Add a drink/side**

   - Verify that the page heading displays correctly Y/N
   - Confirm that the Category dropdown features all categories Y/N
   - Verify that all input fields are displayed Y/N
   - Verify that required fields need an input for the form to be validated Y/N
   - Confirm that all Dietary requirements are displayed in the allergen multiple select dropdown Y/N
   - Verify that the Back To Menu button redirects the user back to the menu Y/N
   - Verify that clicking the Add button with a valid form add the product to the menu Y/N
   - Confirm that a success message is displayed notifying the user that item was added successfully Y/N
   - Confirm that the user is redirected to the correct page Y/N

- **Edit an Ingredient** **Edit a drink/side**
    - Verify that the page heading displays correctly Y/N
    - confirm that an alert message is displayed notifying the user of which item is being edited Y/N 
    - Confirm that the Category dropdown features all categories and that the item's existing category is selected Y/N
    - Verify all existing product information is displayed in the relevant inputs Y/N
    - Verify that the cancel button redirects the user back to the menu Y/N
    - Verify that clicking the Edit item/ingredient button with a valid form edits the product's values Y/N
    - Confirm that the user is then redirected to the appropriate page Y/N
    - Confirm that a success message is displayed notifying the user that the product has been edited successfully Y/N

- **Remove**
    - Verify the shop owner can distinguish the delete button. Y/N
    - Verify it removes the correct item Y/N


## Bugs I ran into during development

- Massive rework was done on the add to bag view as it was originally adding sandwiches based on the length of items in the session, This got incredibly complicated, when the user was signed in as the amount of items in the session would change.
    - Solution was to call all seperate variables pertaining to each of the prime categories as the sandwich was being constructed, such as BREAD_ADDED and then set the values to true.
    - Result way less code and an optimal solution 

- Due to items being named numerically based on the length of the bag there seemed to be duplicate names being created after an item was removed. This resulted in items being replaced rather than added.
    - solution as displayed below 
    ` if f'item_{str(itemNo)}' not in request.session['bag']:
            bag[f'item_{str(itemNo)}'] = sandwich
        else:
            bag[f'item_{str(itemNo)}_replacement'] = sandwich `
    - Result, No chance of overlap.

- Merely an observation but some of the hardest bugs or rather issues I came across were resolved not due to incorrect logic, but incorrect indentation.
Python is notorious for this and I will be sure to revise my indentation as it is a weak point in my coding ability.


## Known minor bugs/fixes
    
Due to time contraints I wasn't able to get to these minor bugs before submission. However they do not inhibit the user's use of the site. (They are next on the list I promise <3)

 - Certain product images need to be resized to be consistent primarily on the drinks page , 
 - because of a bug when using the display block class in boostrap 2 of the categories dropdown arrow dissapeared after the site was deployed this has been identified and will be dealt with,
 - I noticed that in the url when sorting several commas remain. This looks untidy but a quick fix none the less,
 - some success toasts still have the bag total displayed unnecessarily. 
 
