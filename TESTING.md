# **Quest Board - Testing** <!-- omit in toc -->

![Quest Board logo](quest_board/static/images/logo-alt.png)

![Quest Board displayed on miltiple devices]()

This is the testing documentation for the Quest Board website. [The full README is available here.](README.md)

[Click here to visit Quest Board]()

**By [Andrew Wright](https://github.com/AndyWright360)**

---

## **Contents** <!-- omit in toc -->

- [**Automated Testing**](#automated-testing)
  - [**W3C HTML Validation**](#w3c-html-validation)
  - [**W3C CSS Validation**](#w3c-css-validation)
    - [**Second Validation Test**](#second-validation-test)
  - [**JSHint JavaScript Validation**](#jshint-javascript-validation)
  - [**WCAG Colour Contrast Checker**](#wcag-colour-contrast-checker)
    - [**Page Content**](#page-content)
    - [**Score Display**](#score-display)
    - [**Buttons**](#buttons)
    - [**Footer Content**](#footer-content)
  - [**Lighthouse Testing**](#lighthouse-testing)
    - [**Desktop Results**](#desktop-results)
    - [**Mobile Results**](#mobile-results)
- [**Manual Testing**](#manual-testing)
  - [**Testing User Stories**](#testing-user-stories)
    - [**First Time Visitor Goals**](#first-time-visitor-goals)
    - [**Returning Visitor Goals**](#returning-visitor-goals)
    - [**Frequent User Goals**](#frequent-user-goals)
  - [**Full Testing**](#full-testing)

---

## **Automated Testing**

### **W3C HTML Validation**

[W3C](https://validator.w3.org/) was used to validate the HTML code.

- index.html - RESULT
- events.html - RESULT
- event.html - RESULT
- create_event.html - RESULT
- edit_event.html - RESULT
- sign_up.html - RESULT
- log_in.html - RESULT
- profile.html - RESULT
- 400.html - RESULT
- 403.html - RESULT
- 404.html - RESULT
- 500.html - RESULT

![W3C HTML validation results](documentation/testing/html-validation.jpg)

### **W3C CSS Validation**

[W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.

- style.css - RESULT
- map-style.css - RESULT

![W3C CSS validation errors]()

*Error*

![W3C CSS validation warnings]()

*Warnings*

Description of errors and warnings if they appeared.

#### **Second Validation Test**

The fix implemented. The results from the second validation were a pass.

![W3C CSS validation pass]()

*Pass*

### **JSHint JavaScript Validation**

[JSHint](https://jshint.com/) was used to validate the JavaScript code.

- script.js - RESULTS
- map.js - RESULTS
- filter.js - RESULTS

![JSHint JavaScript validation results]()

*Results*

Description of results and any steps needed to rectify them.

### **WCAG Colour Contrast Checker**

A considerable effort was made in creating a strong contrast in the website's colour scheme. With the font used throughout the site being a handwritten style. I felt it to be vital that the content was clear and as legible as possible to the user. Below, you'll find a detailed breakdown of the outcomes resulting from each combination of background and foreground colours used in this project.

#### **Red & White**

![Colour contrast results](documentation/testing/red-white.jpg)

This colour scheme serves as the primary navbar theme across the website. Additionally, it's employed for the "delete" button within user-created events.

#### **Green & White**

![Colour contrast results](documentation/testing/green-white.jpg)

Utilised as the secondary navbar colour, this scheme also extends to page content like the "Our Quest" section on the homepage. Similarly, the "edit" button in user-created events adopts this palette.

#### **Light Green & Brown**

![Colour contrast results](documentation/testing/lightgreen-brown.jpg)

Reserved for section headings on the homepage and profile page, this scheme accompanies large text elements due to its lower contrast.

#### **White & Brown**

![Colour contrast results](documentation/testing/white-brown.jpg)

Found primarily in form inputs on the create and edit event pages, as well as in the footer for copyright text.

#### **White & Light Brown**

![Colour contrast results](documentation/testing/white-lightbrown.jpg)
![Colour contrast results](documentation/testing/lightbrown-white.jpg)

Employed for user input labels and remaining buttons throughout the site.

#### **White & Mid Green**

![Colour contrast results](documentation/testing/white-midgreen.jpg)

Applied on the "Sign Up" and "Log In" pages, indicating navigation links to alternative pages. The font size was adjusted for clarity due to the lower contrast ratio.

#### **Yellow & Brown**

![Colour contrast results](documentation/testing/yellow-brown.jpg)

Designed for flash messages, this vibrant scheme ensures important notifications are eye-catching to users.

### **Lighthouse Testing**

Lighthouse within Chrome Developer Tools was used to assess the website's performance, accessibility, adherence to best practices, and SEO.

#### **Desktop Results**

| Page | Results |
| :--- | :--- |
| index.html | ![Lighthouse results for desktop]() |
| events.html | ![Lighthouse results for desktop]() |
| event.html | ![Lighthouse results for desktop]() |
| create_event.html | ![Lighthouse results for desktop]() |
| edit_event.html | ![Lighthouse results for desktop]() |
| sign_up.html | ![Lighthouse results for desktop]() |
| log_in.html | ![Lighthouse results for desktop]() |
| profile.html | ![Lighthouse results for desktop]() |
| 400.html | ![Lighthouse results for desktop]() |
| 403.html | ![Lighthouse results for desktop]() |
| 404.html | ![Lighthouse results for desktop]() |
| 500.html | ![Lighthouse results for desktop]() |

#### **Mobile Results**

| Page | Results |
| :--- | :--- |
| index.html | ![Lighthouse results for mobile]() |
| events.html | ![Lighthouse results for mobile]() |
| event.html | ![Lighthouse results for mobile]() |
| create_event.html | ![Lighthouse results for mobile]() |
| edit_event.html | ![Lighthouse results for mobile]() |
| sign_up.html | ![Lighthouse results for mobile]() |
| log_in.html | ![Lighthouse results for mobile]() |
| profile.html | ![Lighthouse results for mobile]() |
| 400.html | ![Lighthouse results for mobile]() |
| 403.html | ![Lighthouse results for mobile]() |
| 404.html | ![Lighthouse results for mobile]() |
| 500.html | ![Lighthouse results for mobile]() |

---