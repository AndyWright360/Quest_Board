# **Quest Board - Testing** <!-- omit in toc -->

![Quest Board logo](quest_board/static/images/logo-alt.webp)

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

| Page | Results |
| :--- | :--- |
| index.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| events.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| event.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| create_event.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| edit_event.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| sign_up.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| log_in.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| profile.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| 400.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| 403.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| 404.html | ![HTML Validation Result](documentation/testing/html-validation.png) |
| 500.html | ![HTML Validation Result](documentation/testing/html-validation.png) |

![HTML validation warning](documentation/testing/html-section-warning.jpg)

I encountered a warning across multiple pages regarding section elements lacking an associated heading. This issue primarily arose from wrapping flash messages in a section tag, which consequently made them accessible on every page. However, there were also a few instances where sections were used without a heading.

To address this, I refactored the section containers across all pages. Instead of using section tags, I wrapped the flash messages inside div elements. After implementing these changes, all pages passed the validation.

### **W3C CSS Validation**

[W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.

| Page | Results |
| :--- | :--- |
| style.css | ![CSS Validation Result](documentation/testing/css-validation.jpg) |
| map-style.css | ![CSS Validation Result](documentation/testing/css-validation.jpg) |

Several warnings were flagged, all related to the use of vendor extensions, which I opted to disregard.

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

## **Manual Testing**

### **Testing User Stories**

#### **First Time Visitor Goals**

| Goals | How are they achieved? |
| :--- | :--- |
| I want to create a profile so that I can start creating and joining events. |  |
| I want to filter events based on store location to find events in my preferred area. |  |
| I want to view the details of an event to ensure it aligns with my preferences and schedule. |  |

#### **Returning Visitor Goals**

| Goals | How are they achieved? |
| :--- | :--- |
| I want to log in to my account. |  |
| I want to join an event created by another user. |  |
| I want to edit the details of an event in case there are changes or updates. |  |

#### **Frequent User Goals**

| Goals | How are they achieved? |
| :--- | :--- |
| I want to check my profile page so I can easily monitor my created and joined events. |  |
| I want to leave an event if my plans change or I can no longer attend. |  |

#### **Administrator**

| Goals | How are they achieved? |
| :--- | :--- |
| I want to review and moderate user-created events to ensure they comply with community guidelines. |  |

### **Full Testing**

Full testing was performed on the following devices:

- Laptop:
  - MSI Thin GF63 15 inch screen
- Mobile Device:
  - iPhone XR

The following browsers were tested using each device:

- Laptop:
  - Google Chrome
  - Mozilla Firefox
- Mobile:
  - Safari

Friends and family also tested the website using a variety of devices. No issues were reported.

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
| Page Title | Redirect to the home page | Click page title | Redirected to home page | - |
| Home Link | Redirect to the home page | Click link | Redirected to home page | - |
| Events Link | Redirect to the events page | Click link | Redirected to events page | - |
| Sign Up Link | Redirect to the sign up page | Click link | Redirected to sign up page | - |
| Login Link | Redirect to the login page | Click link | Redirected to login page | - |
| Profile Link | Redirect to the profile page | Click link | Redirected to profile page | - |
| Burger Menu | Opens sidenav | Click icon | Sidenav opens | - |
| `Sidenav` |
| Home Link | Redirect to the home page | Click link | Redirected to home page | - |
| Events Link | Redirect to the events page | Click link | Redirected to events page | - |
| Sign Up Link | Redirect to the sign up page | Click link | Redirected to sign up page | - |
| Login Link | Redirect to the login page | Click link | Redirected to login page | - |
| Profile Link | Redirect to the profile page | Click link | Redirected to profile page | - |
| Close Sidenav | Close the sidenav bar | Click outside sidenav | Sidenav closed | - |
| `Footer` |
| Social Media Link (Facebook) | Opens Facebook link in a new tab | Clicked Facebook icon | New tab opened to Facebook | - |
| Social Media Link (YouTube) | Opens YouTube link in a new tab | Clicked YouTube icon | New tab opened to YouTube | - |
| Social Media Link (Twitter) | Opens Twitter link in a new tab | Clicked Twitter icon | New tab opened to Twitter | - |
| Icon Hover Effect | Icon size increases on mouse hover | Hover mouse over icon | Icon size increases | - |
| `Flash Messages` |
| Event Created | Message appear when event created | Create event | Message appeared | - |
| Event Deleted | Message appear when event deleted | Delete event | Message appeared | - |
| Join Event | Message appear when event joined | Join event | Message appeared | - |
| Leave Event | Message appear when leaveing event | Leave event | Message appeared | - |
| Welcome User | Message appear when user signs in | Sign In User | Message appeared | - |
| `Home Page` |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| Sign Up Button | Redirect to the sign up page | Click button | Redirected to sign up page | - |
| Open Map Marker (Checkmates) | Display store information window | Click marker | Store information window displayed | - |
| Close Map Marker (Checkmates) | Close store information window | Click information widow | Store information window closed | - |
| Open Map Marker (Dungeons & Dice) | Display store information window | Click marker | Store information window displayed | - |
| Close Map Marker (Dungeons & Dice) | Close store information window | Click information widow | Store information window closed | - |
| Open Map Marker (Castle Games) | Display store information window | Click marker | Store information window displayed | - |
| Close Map Marker (Castle Games) | Close store information window | Click information widow | Store information window closed | - |
| Open Map Marker (Boarderlands) | Display store information window | Click marker | Store information window displayed | - |
| Close Map Marker (Boarderlands) | Close store information window | Click information widow | Store information window closed | - |
| Display Next Gallery Image | Next sequential gallery image displays on screen | Drag gallery image to the left | Next gallery image displayed | - |
| Display Previous Gallery Image | Previous gallery image displays on screen | Drag gallery image to the right | Previous gallery image displayed | - |
| Select Gallery Indicator | Display the selected gallery image | Click gallery indicator | Selected gallery image displayed | - |
| `Events Page` |
| Fliter Dropdown (Open) | Open filter dropdown to display search options | Click filter | Filter dropdown opens | - |
| Fliter Dropdown (Close) | Close filter dropdown to remove search options | Click filter | Filter dropdown closes | - |
| Filter Checkbox (Cardiff) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Newport) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Swansea) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Bridgend) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (10am) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (12pm) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (2pm) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (4pm) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Beginner) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Everyone) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Filter Checkbox (Experienced) | Display events matching selected option | Click checkbox | Display corresponding events | - |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| Create Event Button | Redirect to the create event page | Click button | Redirected to create event page | - |
| Edit Button | Redirect to the edit event page | Click button | Redirected to edit event page | - |
| Delete Button | Open delete event modal | Click button | Delete event modal opened | - |
| Join Button | Increase party member display by one | Click button | Party member display increased by one | - |
| Leave Button | Decrease party member display by one | Click button | Party member display decreased by one | - |
| Full Event | Display "Full" stamp when party list reaches capacity | Fill party list | "Full" stamp displays on event | - |
| Event Stamp | Redirect to the selected event page | Click stamp | Redirected to selected event page | - |
| `Event Page` |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| Edit Button | Redirect to the edit event page | Click button | Redirected to edit event page | - |
| Delete Button | Open delete event modal | Click button | Delete event modal opened | - |
| Join Button | Add username to party member list | Click button | Username added to party list | - |
| Leave Button | Remove username from party member list | Click button | Username removed from party list | - |
| Full Event | Display "Full" stamp when party list reaches capacity | Fill party list | "Full" stamp displays on event | - |
| `Create Event Page` |
| Valid Input (Username) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Username) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Valid Input (Max Party Size) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Max Party Size) | Input border turns red and displays "max 10" text | Enter invalid input | Input border turned red and displayed "max 10" text | - |
| Valid Input (Description) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Description) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Character Counter (Username) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Character Counter (Description) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Select Dropdown (Location) | Display list of location options | Click input | Displays list of location options | - |
| Select Dropdown (Time) | Display list of time options | Click input | Displays list of time options | - |
| Date Picker | Open date picker modal | Click date input | Date picker modal opens | - |
| Required Inputs | Display message to user for unfilled input field | Submit form with empty inputs | Message displayed notifying of empty input field | - |
| Radio Input (Beginner) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Radio Input (Everyone) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Radio Input (Experienced) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Popover Message (Beginner) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| Popover Message (Everyone) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| Popover Message (Experienced) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| `Edit Event Page` |
| Valid Input (Event Name) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Event Name) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Valid Input (Max Party Size) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Max Party Size) | Input border turns red and displays "max 10" text | Enter invalid input | Input border turned red and displayed "max 10" text | - |
| Valid Input (Description) | Input border turns green | Enter valid input | Input border turned green | - |
| Invalid Input (Description) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Character Counter (Username) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Character Counter (Description) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Select Dropdown (Location) | Display list of location options | Click input | Displays list of location options | - |
| Select Dropdown (Time) | Display list of time options | Click input | Displays list of time options | - |
| Date Picker | Open date picker modal | Click date input | Date picker modal opens | - |
| Required Inputs | Display message to user for unfilled input field | Submit form with empty inputs | Message displayed notifying of empty input field | - |
| Radio Input (Beginner) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Radio Input (Everyone) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Radio Input (Experienced) | Radio button highligted when input selected | Select input | Radio button highlighted | - |
| Popover Message (Beginner) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| Popover Message (Everyone) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| Popover Message (Experienced) | Display popover message when hovering over question mark icon | Hover over icon | Corresponding popover message displayed | - |
| `Delete Event Modal` |
| Button Hover Effect | Button colour darkens on mouse hover | Hover mouse over button | Button colour darkens | - |
| Cancel Button | Close delete modal | Click button | Modal closed | - |
| Delete Button | Delete event data and redirect to events page | Click button | Redirected to events page and event deleted | - |
| Close Modal (Click outside modal window) | Close modal by clicking outside window | Click outside modal window | Modal closed | - |
| `Sign Up Page` |
| Valid Input (Username) | Input border turns green and displays "valid" text | Enter valid input | Input border turned green and displayed "valid" text | - |
| Invalid Input (Username) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Valid Input (Password) | Input border turns green and displays "valid" text | Enter valid input | Input border turned green and displayed "valid" text | - |
| Invalid Input (Password) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Character Counter (Username) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Character Counter (Password) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Required Inputs | Display message to user for unfilled input field | Submit form with empty inputs | Message displayed notifying of empty input field | - |
| Input Pattern Recognition | Display message to user if keys outside the pattern requirements are entered | Submit form with invalid inputs | Message displayed notifying of incorrect input type | - |
| Link Hover Effect | Text underlines on mouse hover | Hover over link text | Link text underlined | - |
| Log In Link | Redirect to login page | Click button | Redirected to login page | - |
| Successful Sign Up | Redirect to profile page | Submit valid sign up details | Redirected to profile page | - |
| `Login Page` |
| Valid Input (Username) | Input border turns green and displays "valid" text | Enter valid input | Input border turned green and displayed "valid" text | - |
| Invalid Input (Username) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Valid Input (Password) | Input border turns green and displays "valid" text | Enter valid input | Input border turned green and displayed "valid" text | - |
| Invalid Input (Password) | Input border turns red and displays "invalid entry" text | Enter invalid input | Input border turned red and displayed "invalid entry" text | - |
| Character Counter (Username) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Character Counter (Password) | Dynamically display character number as input is entered | Enter input data | Counter displays current character number | - |
| Required Inputs | Display message to user for unfilled input field | Submit form with empty inputs | Message displayed notifying of empty input field | - |
| Input Pattern Recognition | Display message to user if keys outside the pattern requirements are entered | Submit form with invalid inputs | Message displayed notifying of incorrect input type | - |
| Link Hover Effect | Text underlines on mouse hover | Hover over link text | Link text underlined | - |
| Sign Up Link | Redirect to sign up page | Click button | Redirected to sign up page | - |
| Invalid Username | Display message notifying of invalid username or password | Submit incorrect username | Message displayed notifying of invalid username or password | - |
| Invalid Password | Display message notifying of invalid username or password | Submit incorrect password | Message displayed notifying of invalid username or password | - |
| Successful Login | Redirect to profile page | Submit valid login details | Redirected to profile page | - |
| `Profile Page` |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| Create Event Button | Redirect to the create event page | Click button | Redirected to create event page | - |
| Edit Button | Redirect to the edit event page | Click button | Redirected to edit event page | - |
| Delete Button | Open delete event modal | Click button | Delete event modal opened | - |
| Leave Button | Remove event from joined event list | Click button | Event removed from joined events list | - |
| Event Stamp | Redirect to the selected event page | Click stamp | Redirected to selected event page | - |
| No Events Message | Display message if no created events exist | Enter page with no created events | Message displayed notifying of no events | - |
| No Joined Events Message | Display message if no joined events exist | Enter page with no joined events | Message displayed notifying of no joined events | - |
| `400 Error Page` |
| Return Home Button | Redirect to the home page | Click button | Redirected to home page | - |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| `403 Error Page` |
| Return Home Button | Redirect to the home page | Click button | Redirected to home page | - |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| `404 Error Page` |
| Return Home Button | Redirect to the home page | Click button | Redirected to home page | - |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |
| `500 Error Page` |
| Return Home Button | Redirect to the home page | Click button | Redirected to home page | - |
| Button Hover Effect | Button scale increase on mouse hover | Hover mouse over button | Button scale increases | - |
| Button Click Animation | Button scale decreases on click | Click button | Button scale decreases | - |

### **Bugs & Fixes**

#### **Button Scale Bug**

![Button Scale Bug](documentation/testing/button-scale-bug.gif)

I noticed that the text within buttons moved as the scale increased on mouse hover. Upon searching online I was able to find a resolution on Stack Overflow contributed by Chris W (please see credits section below). The fix incorporated additional CSS classes to create a seamless transition during scaling.

![Button Scale Fix](documentation/testing/button-scale-fix.gif)

#### **Horizontal Scroll Bug**

![Horizontal Scroll Bug](documentation/testing/horizontal-scroll-bug.gif)

After including the popover messages to the Create Event page, I encountered this bug. After the size of the page window had been reduced, the width of the body exceeded the display width, creating horizontal page scroll. This occurred even though no content on the page was being pushed outside the display. 

As far as I could tell, the page wasn't resizing the popover content correctly. Upon reloading the page, the horizontal scroll would disappear. The fix I implemented to was to apply `overflow-x: hidden` to the body element.

#### **Navbar Link Bug**

![Navbar Link Bug](documentation/testing/navbar-bug.gif)

This issue occurred after I changed the "id" attribute to a "class" attribute for the board trim on the events page. The reason behind this change was to address a situation where both sets of boards were being displayed simultaneously on the profile page. Instead of using unique IDs to target each side of the trim and corner plates, I opted for class names. However, one of these class names inadvertently matched a Materialize class associated with navbar links. Consequently, the CSS styling intended for the board trim was also affecting the position of the navbar links. To resolve this, I assigned alternative class names to the board trim and corner plates.

#### **Materialize Select Validation Bug**

![Select Validation Bug](documentation/testing/select-validation-bug.gif)

This bug involved the use of JavaScript to replicate the Materialize validate class for form inputs. This class provides visual feedback to the user for valid and invalid inputs by dynamically altering the colour of the input border. The bug resulted in the border colour changing to red whenever the input lost focus, regardless of its validity. This only affected the select inputs on the create event page and functioned as intended on the edit event page. I also tested this on multiple devices and found it only to be present on my laptop, despite the same browser being used on other tests.

As I was unable to find a method to add the validate class to the date and textarea inputs. I opted to remove this class from the event form inputs altogether. As this validation method wasn't consistent across all inputs on the form, I felt it wasn't offering the user experience I intended. And with no known fix for the bug, I wanted to avoid the possibility of users being provided incorrect feedback.

#### **Materialize Select Input Mobile Bug**

I encountered this issue while testing the site on an iPhone. The Materialize select dropdown menu doesn't function effectively on touchscreen devices. Often, the input would populate with a different option than the one selected, resulting in a frustrating user experience as it becomes challenging to select the intended option.

Upon researching online, I discovered that this issue is widely documented and found a solution on Stack Overflow.

### **Known Bugs**

#### **Section Pixel Bug**

![Section Pixel Bug](documentation/testing/section-pixel-bug.jpg)

Despite thorough research, I couldn't find a definitive solution to this issue. It occurs when two sections with the same background color connect, resulting in occasional misalignment and a 1 or 2-pixel white line gap between them. The size of this gap varies based on the width of the display screen. To mitigate this, I adjusted the height of the header section, which removed it from the range of display widths that the site can be viewed. However, I'm unsure if this would fix the issue across all browsers.