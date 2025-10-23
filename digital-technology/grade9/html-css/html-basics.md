---
layout: page
title: HTML Basics
parent: HTML & CSS Fundamentals
grand_parent: Grade 9 Digital Technology
nav_order: 1
---

# HTML Basics
{: .text-blue-200 }

Learn the fundamental building blocks of web pages using HTML (HyperText Markup Language).

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Understand the basic structure of an HTML document
- Create properly formatted HTML pages with essential elements
- Use heading levels to organize content hierarchically
- Format text with paragraphs and other basic elements
- Create hyperlinks to connect web pages
- Build ordered and unordered lists
- Construct tables to display data
- Add interactive button elements

---

## 📄 What is HTML?

**HTML** (HyperText Markup Language) is the standard language used to create web pages. It provides the **structure and content** of every website you visit.

### 🏗️ HTML as the Structure

Think of building a house:
- **HTML** = The frame, walls, and rooms (structure)
- **CSS** = The paint, decorations, and furniture (styling)
- **JavaScript** = The electricity, plumbing, and smart features (functionality)

{: .key-concept }
**HTML provides the skeleton of a web page** - it defines what content appears and how it's organized, but not how it looks visually (that's CSS's job).

---
## 💻 Interactive Examples

Throughout this lesson, you'll find **"Try It Yourself"** interactive examples. These let you:
- See the code running live in your browser
- Edit the code and see changes immediately
- Experiment without breaking anything
- Learn by doing!

{: .tip }
**How to use interactive examples**: Click "Run Pen" to load the example, then edit the code in the editor. Your changes appear instantly in the preview!

---

## 🏛️ Basic HTML Document Structure

Every HTML page follows the same basic structure:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Welcome to My Website</h1>
    <p>This is my first paragraph.</p>
  </body>
</html>
```

### 📋 Breaking Down Each Part:

#### `<!DOCTYPE html>`
**Tells the browser this is an HTML5 document**
- Must be the very first line of your HTML file
- Not technically an HTML tag, but a declaration
- Ensures the browser displays your page correctly

#### `<html>` ... `</html>`
**The root element that contains all other HTML elements**
- Opening tag: `<html>`
- Closing tag: `</html>`
- Everything else goes between these tags

#### `<head>` ... `</head>`
**Contains information about the document (metadata)**
- Not displayed on the page itself
- Includes the page title, links to CSS files, and other meta information
- Example: `<title>My Page</title>` sets the browser tab text

#### `<body>` ... `</body>`
**Contains all the visible content of the page**
- Everything you see on a web page goes here
- Headings, paragraphs, images, links, etc.
- This is where you'll spend most of your time writing HTML

{: .structure-note }
**Remember**: Every HTML tag that opens must also close! Opening tag: `<tagname>`, Closing tag: `</tagname>`

### 💡 Try It Yourself: Basic HTML Structure

Let's see a complete HTML page in action. Click "Run Pen" below to load the interactive example:

<p class="codepen" data-height="400" data-theme-id="light" data-default-tab="html,result" data-slug-hash="preview" data-preview="true" data-user="yourusername" style="height: 400px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/pen/">Basic HTML Structure</a> - Try editing the title or adding a new paragraph!</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

**Challenge**: 
1. Change the title in the `<head>` section
2. Add another paragraph in the `<body>`
3. Watch the result update automatically!

---

## 📝 Headings: Creating Content Hierarchy

HTML provides six levels of headings, from most important (h1) to least important (h6).

### 🔢 The Six Heading Levels
```html
<h1>Main Page Title - Largest and Most Important</h1>
<h2>Major Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Sub-subsection Heading</h4>
<h5>Minor Heading</h5>
<h6>Smallest Heading</h6>
```

### 📊 Visual Representation

**How They Look:**
- **h1**: Largest - typically used once per page for the main title
- **h2**: Large - major sections of content
- **h3**: Medium - subsections within h2 sections
- **h4**: Smaller - further subdivisions
- **h5**: Very small - rarely used, minor details
- **h6**: Smallest - rarely used, most minor headings

### ✅ Best Practices for Headings

#### ✓ DO:
- **Use h1 once per page** for the main title
- **Use headings in order** (don't skip from h1 to h4)
- **Use headings to create logical structure** (like an outline)
- **Make headings descriptive** of the content that follows

#### ✗ DON'T:
- **Don't use headings just to make text bigger** (use CSS for that)
- **Don't skip heading levels** (h1 → h3 without an h2)
- **Don't use multiple h1 tags** on the same page
- **Don't make headings too long** (keep them concise)

### 💡 Example of Good Heading Structure
```html
<h1>South African Wildlife Guide</h1>
  
  <h2>Big Five Animals</h2>
    <h3>African Lion</h3>
    <h3>African Elephant</h3>
    <h3>African Leopard</h3>
  
  <h2>Conservation Efforts</h2>
    <h3>National Parks</h3>
    <h3>Wildlife Reserves</h3>
```

{: .accessibility-note }
**Accessibility Tip**: Screen readers use heading structure to help visually impaired users navigate pages. Proper heading hierarchy makes your website more accessible!

### 💡 Try It Yourself: Heading Levels

Experiment with different heading levels and see how they look:

<p class="codepen" data-height="450" data-theme-id="light" data-default-tab="html,result" data-slug-hash="preview" data-preview="true" data-user="yourusername" style="height: 450px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/pen/">Heading Hierarchy</a> - Try changing the heading levels!</span>
</p>

**Challenge**: 
1. Change some of the heading numbers (e.g., change h3 to h2)
2. Add a new subsection with appropriate heading levels
3. Notice how the size changes with each level!

---

## 📝 Paragraphs: The Building Blocks of Content

The `<p>` tag defines a paragraph of text.

### 📖 Basic Paragraph Syntax
```html
<p>This is a paragraph of text. It can contain multiple sentences and will automatically wrap to fit the width of the browser window.</p>

<p>Each paragraph tag creates a new block of text with spacing before and after it automatically.</p>
```

### 🎨 How Paragraphs Behave

**Automatic Features:**
- **Line breaks**: Text wraps automatically at the browser edge
- **Spacing**: Browsers add space above and below paragraphs automatically
- **Block element**: Each paragraph starts on a new line

### 💡 Paragraph Examples
```html
<h2>About Our School</h2>

<p>Welcome to our school website! We are a vibrant learning community dedicated to providing excellent education to all our learners.</p>

<p>Our school was founded in 1995 and has been serving the community for over 25 years. We pride ourselves on our commitment to academic excellence and character development.</p>

<p>Our facilities include modern classrooms, a library, computer lab, and sports fields. We offer a wide range of extracurricular activities to support holistic student development.</p>
```

### ⚠️ Common Mistakes

#### ❌ Wrong: Using `<br>` for spacing
```html
<p>First paragraph</p>
<br><br><br>
<p>Second paragraph</p>
```

#### ✅ Correct: Using CSS for spacing
```html
<p>First paragraph</p>
<p>Second paragraph</p>
<!-- Control spacing with CSS margin properties -->
```

{: .tip }
**Tip**: Never use multiple `<br>` tags to create space between paragraphs. Use CSS to control spacing instead!

---

## 🔗 Links: Connecting Web Pages

The `<a>` (anchor) tag creates hyperlinks that let users navigate between pages.

### 🌐 Basic Link Syntax
```html
<a href="https://www.example.com">Click here to visit Example.com</a>
```

**Components:**
- `<a>` = Anchor tag (creates the link)
- `href` = "Hypertext Reference" - where the link goes
- `Click here...` = The visible, clickable text
- `</a>` = Closing anchor tag

### 📋 Types of Links

#### 🌍 External Links (to other websites)
```html
<a href="https://www.google.com">Visit Google</a>
<a href="https://www.wikipedia.org">Read Wikipedia</a>
```

#### 📁 Internal Links (to other pages on your site)
```html
<a href="about.html">About Us</a>
<a href="contact.html">Contact</a>
<a href="../index.html">Back to Home</a>
```

#### 📧 Email Links
```html
<a href="mailto:info@example.com">Email Us</a>
```

#### 📞 Phone Links (especially useful on mobile)
```html
<a href="tel:+27123456789">Call: 012 345 6789</a>
```

### 🎯 Link Attributes

#### Opening Links in New Tabs
```html
<a href="https://www.example.com" target="_blank">
  Open in New Tab
</a>
```

#### Adding Title Tooltips
```html
<a href="about.html" title="Learn more about our company">
  About Us
</a>
```

### 💡 Link Best Practices

#### ✓ DO:
- **Use descriptive link text** that tells users where they're going
- **Make links visually distinct** (usually underlined and colored)
- **Test all links** to ensure they work
- **Use relative paths** for internal site links

#### ✗ DON'T:
- **Don't use "click here"** as link text (not descriptive)
- **Don't link to broken pages** (404 errors)
- **Don't overuse `target="_blank"`** (can be annoying)
- **Don't forget the `https://`** for external links

### 📝 Example: Navigation Menu
```html
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="services.html">Services</a>
  <a href="contact.html">Contact</a>
</nav>
```

---

## 📋 Lists: Organizing Information

HTML provides two main types of lists for organizing information.

### 🔢 Ordered Lists (Numbered)

Use `<ol>` when the **order matters** (steps, rankings, sequences).
```html
<h3>Steps to Make Tea</h3>
<ol>
  <li>Boil water</li>
  <li>Put tea bag in cup</li>
  <li>Pour hot water into cup</li>
  <li>Let it steep for 3-5 minutes</li>
  <li>Remove tea bag and enjoy</li>
</ol>
```

**Output:**
1. Boil water
2. Put tea bag in cup
3. Pour hot water into cup
4. Let it steep for 3-5 minutes
5. Remove tea bag and enjoy

### 🔹 Unordered Lists (Bullet Points)

Use `<ul>` when the **order doesn't matter** (features, lists, collections).
```html
<h3>Required School Supplies</h3>
<ul>
  <li>Notebooks</li>
  <li>Pens and pencils</li>
  <li>Calculator</li>
  <li>Ruler</li>
  <li>Textbooks</li>
</ul>
```

**Output:**
- Notebooks
- Pens and pencils
- Calculator
- Ruler
- Textbooks

### 🎯 List Structure Explained

**Components:**
- `<ol>` or `<ul>` = Container for the list
- `<li>` = List Item - each individual item in the list
- Each `<li>` must be inside an `<ol>` or `<ul>`

### 📦 Nested Lists (Lists within Lists)
```html
<h3>School Departments</h3>
<ul>
  <li>Mathematics
    <ul>
      <li>Pure Mathematics</li>
      <li>Mathematical Literacy</li>
    </ul>
  </li>
  <li>Sciences
    <ul>
      <li>Physical Science</li>
      <li>Life Sciences</li>
    </ul>
  </li>
  <li>Languages
    <ul>
      <li>English</li>
      <li>Afrikaans</li>
      <li>isiZulu</li>
    </ul>
  </li>
</ul>
```

### 💡 When to Use Which List Type

| Use Ordered List `<ol>` | Use Unordered List `<ul>` |
|-------------------------|---------------------------|
| Step-by-step instructions | Features or benefits |
| Rankings or ratings | Shopping lists |
| Sequences that must be followed | Menu items |
| Table of contents | Collections of items |
| Chronological events | Team members |

### 💡 Try It Yourself: Creating Lists

Practice making both types of lists:

<p class="codepen" data-height="500" data-theme-id="light" data-default-tab="html,result" data-slug-hash="preview" data-preview="true" data-user="yourusername" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/pen/">HTML Lists Practice</a> - Try adding your own list items!</span>
</p>

**Challenge**: 
1. Add more items to the shopping list
2. Create your own "Top 5" list using `<ol>`
3. Try creating a nested list (list inside a list)!

---

## 📊 Tables: Displaying Data

Tables are used to display data in rows and columns.

### 🏗️ Basic Table Structure
```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Grade</th>
  </tr>
  <tr>
    <td>Sarah</td>
    <td>15</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Michael</td>
    <td>14</td>
    <td>9</td>
  </tr>
</table>
```

### 📋 Table Elements Explained

#### `<table>` ... `</table>`
**The container for the entire table**
- Wraps all table content
- Only contains `<tr>` elements directly

#### `<tr>` ... `</tr>` 
**Table Row - creates a horizontal row**
- Each row contains cells (`<th>` or `<td>`)
- Stack rows vertically to build the table

#### `<th>` ... `</th>`
**Table Header - labels for columns or rows**
- Usually in the first row
- Automatically bold and centered
- Helps users understand what each column represents

#### `<td>` ... `</td>`
**Table Data - regular data cells**
- Contains the actual information
- One `<td>` per piece of data

### 📊 Complete Table Example
```html
<h2>Class Schedule</h2>
<table>
  <tr>
    <th>Time</th>
    <th>Monday</th>
    <th>Tuesday</th>
    <th>Wednesday</th>
  </tr>
  <tr>
    <td>08:00 - 09:00</td>
    <td>Mathematics</td>
    <td>English</td>
    <td>Science</td>
  </tr>
  <tr>
    <td>09:00 - 10:00</td>
    <td>Life Orientation</td>
    <td>History</td>
    <td>Mathematics</td>
  </tr>
  <tr>
    <td>10:00 - 11:00</td>
    <td>English</td>
    <td>Afrikaans</td>
    <td>Geography</td>
  </tr>
</table>
```

### 🎯 Table Best Practices

#### ✓ DO:
- **Always include header rows** with `<th>` tags
- **Keep tables simple** and easy to read
- **Use tables for tabular data** (schedules, statistics, comparisons)
- **Make sure all rows have the same number of cells**

#### ✗ DON'T:
- **Don't use tables for page layout** (use CSS instead)
- **Don't create overly complex tables** (split into multiple tables if needed)
- **Don't forget closing tags** for rows and cells
- **Don't mix up `<th>` and `<td>`** - headers are different from data

### 🔧 Common Table Patterns

#### Data Comparison Table
```html
<table>
  <tr>
    <th>Feature</th>
    <th>Basic Plan</th>
    <th>Premium Plan</th>
  </tr>
  <tr>
    <td>Storage</td>
    <td>10GB</td>
    <td>100GB</td>
  </tr>
  <tr>
    <td>Price</td>
    <td>R50/month</td>
    <td>R150/month</td>
  </tr>
</table>
```

#### Contact Information Table
```html
<table>
  <tr>
    <th>Department</th>
    <th>Contact Person</th>
    <th>Phone</th>
  </tr>
  <tr>
    <td>Admissions</td>
    <td>Mrs. Smith</td>
    <td>012 345 6789</td>
  </tr>
  <tr>
    <td>IT Support</td>
    <td>Mr. Jones</td>
    <td>012 345 6790</td>
  </tr>
</table>
```

{: .styling-note }
**Styling Tables**: Tables by default look plain. We'll use CSS to add borders, colors, and spacing to make them look professional!

### 💡 Try It Yourself: Building Tables

Create and modify your own data table:

<p class="codepen" data-height="500" data-theme-id="light" data-default-tab="html,result" data-slug-hash="preview" data-preview="true" data-user="yourusername" style="height: 500px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/pen/">HTML Table Builder</a> - Try adding more rows and columns!</span>
</p>

**Challenge**: 
1. Add another row to the table
2. Add a new column (remember to add a `<th>` and `<td>` in each row)
3. Create your own table showing something you're interested in!

---

## 🔘 Buttons: Interactive Elements

Buttons are interactive elements that users can click.

### 🎯 Basic Button Syntax
```html
<button>Click Me</button>
<button>Submit Form</button>
<button>Learn More</button>
```

### 📋 Types of Buttons

#### Standard Button
```html
<button>Standard Button</button>
```

#### Button with Type Attribute
```html
<button type="button">Action Button</button>
<button type="submit">Submit Button</button>
<button type="reset">Reset Button</button>
```

#### Button in a Link
```html
<a href="contact.html">
  <button>Contact Us</button>
</a>
```

### 💡 Button Best Practices

#### ✓ DO:
- **Use clear, action-oriented text** (e.g., "Download PDF", "Send Message")
- **Make buttons look clickable** with proper CSS styling
- **Use buttons for actions** that do something
- **Keep button text short** and descriptive

#### ✗ DON'T:
- **Don't use vague text** like "Click Here" or "Button"
- **Don't make buttons too small** to click easily
- **Don't overuse buttons** - not everything needs to be a button
- **Don't forget to style buttons** - plain buttons look unprofessional

### 🎨 Button Examples
```html
<h2>Download Our Resources</h2>
<button>Download Brochure</button>
<button>Download Application Form</button>

<h2>Contact Options</h2>
<button>Email Us</button>
<button>Call Us</button>
<button>Visit Our Office</button>

<h2>Emergency Actions</h2>
<button>Call Emergency Services</button>
<button>View Safety Information</button>
```

{: .interaction-note }
**Note**: Buttons alone don't do anything - they need JavaScript or to be part of a form to have functionality. We'll learn to style them with CSS to make them look great!

---

## 🎯 Putting It All Together

Let's combine all these elements into a complete, well-structured HTML page:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>School Emergency Procedures</title>
  </head>
  <body>
    <h1>School Emergency Procedures</h1>
    
    <h2>Emergency Contacts</h2>
    <table>
      <tr>
        <th>Service</th>
        <th>Number</th>
      </tr>
      <tr>
        <td>Police</td>
        <td>10111</td>
      </tr>
      <tr>
        <td>Ambulance</td>
        <td>10177</td>
      </tr>
      <tr>
        <td>Fire Department</td>
        <td>10111</td>
      </tr>
    </table>
    
    <h2>Fire Evacuation Steps</h2>
    <ol>
      <li>Stay calm and don't panic</li>
      <li>Leave belongings behind</li>
      <li>Walk quickly to the nearest exit</li>
      <li>Do not use elevators</li>
      <li>Gather at the assembly point</li>
    </ol>
    
    <h2>Assembly Points</h2>
    <ul>
      <li>Sports Field - Main building evacuation</li>
      <li>Front Parking Lot - Science block evacuation</li>
      <li>Back Field - Hostels evacuation</li>
    </ul>
    
    <h2>Report an Emergency</h2>
    <p>If you notice any emergency situation, please report it immediately to a teacher or use one of the emergency phones located throughout the campus.</p>
    
    <button>Call Emergency Services</button>
    <button>View Full Safety Manual</button>
    
    <p>For more information, visit our <a href="safety.html">complete safety guide</a>.</p>
  </body>
</html>
```

---

---

## 💻 Try It Yourself: Complete HTML Page

Here's a complete example using everything we've learned. Try editing any part of it:

<p class="codepen" data-height="600" data-theme-id="light" data-default-tab="html,result" data-slug-hash="preview" data-preview="true" data-user="yourusername" style="height: 600px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/pen/">Complete HTML Example</a> - A full page using all HTML basics!</span>
</p>

**Your Turn**: 
1. Change the page topic from "Emergency Procedures" to something you choose
2. Modify the table data to fit your new topic
3. Update the lists with relevant information
4. Add your own content sections!

{: .practice }
**Practice Tip**: Fork this pen to your own CodePen account to save your work! Just click "Fork" in the bottom right of the CodePen editor.

---

## 💻 Practice Exercises

Now that you've seen interactive examples, here are some exercises:

### Exercise 1: Personal Page
Create an HTML page about yourself that includes:
- Your name as an h1
- A paragraph describing your hobbies
- An unordered list of your favorite subjects
- A table of your weekly schedule

### Exercise 2: School Information Page
Create a page about your school with:
- School name as main heading
- Sections for History, Facilities, and Contact
- Ordered list of steps to apply
- Contact information table
- Links to other pages

### Exercise 3: Recipe Page
Create a recipe page with:
- Recipe name as h1
- Ingredients as unordered list
- Instructions as ordered list
- Nutrition facts as table

{: .practice }
**Practice Tip**: Use an online HTML editor like CodePen, JSFiddle, or W3Schools' "Try it Yourself" feature to test your code as you learn!

---

## ✅ HTML Basics Checklist

Before moving on to CSS, make sure you can:

### Document Structure
- [ ] Write a complete HTML document with DOCTYPE, html, head, and body
- [ ] Add a title to the head section
- [ ] Understand what goes in head vs. body

### Content Elements
- [ ] Create all six heading levels (h1-h6)
- [ ] Use headings in proper hierarchy
- [ ] Write paragraphs with the `<p>` tag
- [ ] Understand when to use each heading level

### Links and Navigation
- [ ] Create links to external websites
- [ ] Create links to other pages on your site
- [ ] Make email and phone links
- [ ] Write descriptive link text

### Lists
- [ ] Create ordered lists for numbered sequences
- [ ] Create unordered lists for bullet points
- [ ] Nest lists inside other lists
- [ ] Choose the right list type for your content

### Tables
- [ ] Build a basic table structure
- [ ] Use `<th>` tags for headers
- [ ] Use `<td>` tags for data cells
- [ ] Ensure all rows have equal cells
- [ ] Create meaningful table layouts

### Interactive Elements
- [ ] Add button elements
- [ ] Write clear button text
- [ ] Understand where buttons are appropriate

### General Skills
- [ ] Always close your tags properly
- [ ] Nest elements correctly (no overlapping tags)
- [ ] Write clean, readable HTML code
- [ ] Test your HTML in a browser preview

---

## 🐛 Common Mistakes to Avoid

### ❌ Forgetting to Close Tags
```html
<!-- Wrong -->
<p>This paragraph is not closed

<p>This causes problems
```
```html
<!-- Correct -->
<p>This paragraph is properly closed</p>

<p>Each paragraph has an opening and closing tag</p>
```

### ❌ Incorrect Nesting
```html
<!-- Wrong -->
<p>This is <strong>bold and <em>italic</p></em></strong>
```
```html
<!-- Correct -->
<p>This is <strong>bold and <em>italic</em></strong></p>
```

### ❌ Missing Required Attributes
```html
<!-- Wrong -->
<a>Click here</a>
```
```html
<!-- Correct -->
<a href="page.html">Click here</a>
```

### ❌ Using Wrong Element Types
```html
<!-- Wrong - using headings for styling -->
<h1>Big text</h1>
<h6>Small text</h6>
```
```html
<!-- Correct - using headings for structure -->
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
  <p>Regular paragraph text</p>
```

---

## 📚 Key Takeaways

### Essential HTML Concepts:
1. **HTML provides structure** - it organizes content, not style
2. **Every tag must close** - opening and closing tags are required
3. **Proper nesting matters** - tags must be properly nested inside each other
4. **Semantic HTML is important** - use elements for their intended purpose
5. **Heading hierarchy creates organization** - use h1-h6 in logical order

### Document Structure:
- **DOCTYPE** declares HTML5
- **html** tag contains everything
- **head** contains metadata
- **body** contains visible content

### Content Organization:
- **Headings** create document structure
- **Paragraphs** contain text content
- **Links** connect pages together
- **Lists** organize related items
- **Tables** display structured data
- **Buttons** create interactive elements

---

## 🚀 Next Steps

Now that you understand HTML basics, you're ready to:
- **Learn about Classes and IDs** to target specific elements
- **Add CSS** to style your HTML elements
- **Create complete web pages** with proper structure
- **Build responsive layouts** that work on all devices

{: .success }
**Congratulations!** You now know the fundamental building blocks of web pages. Everything you see on the Internet starts with HTML like this!

---

## 💡 Additional Resources

- **W3Schools HTML Tutorial**: Interactive examples and "Try it Yourself" editor
- **MDN Web Docs**: Comprehensive HTML reference
- **CodePen**: Practice HTML in your browser
- **HTML Validator**: Check your code for errors

Ready to move on? Next lesson: **HTML Classes and IDs**!