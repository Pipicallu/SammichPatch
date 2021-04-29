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