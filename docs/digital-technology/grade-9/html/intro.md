---
title: Introduction to HTML
---

# Introduction to HTML

## What Is HTML?

:::tip Key Term
**HTML** stands for **HyperText Markup Language**. It is the standard language used to create and structure content on the web.
:::

- **HyperText** refers to text that contains links to other text — what makes the web a *web* of connected documents
- **Markup** means adding special codes (tags) to plain text to give it structure and meaning
- **Language** — though importantly, HTML is **not a programming language**. It cannot make calculations or decisions. It is a *description* language that tells a browser how to display content.

## A Brief History of HTML

- **1989**: Tim Berners-Lee (working at CERN in Switzerland) proposes a system of linked documents
- **1991**: First version of HTML published
- **1994**: HTML 2.0 standardised; the World Wide Web begins to grow rapidly
- **1999**: HTML 4.01 — the version that defined the web for many years
- **2014**: **HTML5** becomes the official standard — the version used today

HTML5 added major improvements: video and audio without plugins, semantic elements, canvas for drawing, and better mobile support.

## HTML vs CSS vs JavaScript

| Language | What it does | Analogy |
|----------|-------------|---------|
| **HTML** | Defines the structure and content | The skeleton / walls of a building |
| **CSS** | Controls the appearance and layout | The paint, furniture, decoration |
| **JavaScript** | Adds interactivity and behaviour | The electricity and moving parts |

A web page can work with just HTML. But it will look very plain — like a typed document with no formatting.

## How HTML Works: Tags

HTML uses **tags** to mark up content. A tag is a keyword surrounded by angle brackets:

```html
<tagname>content goes here</tagname>
```

Most tags come in pairs:
- **Opening tag**: `<tagname>` — marks the start
- **Closing tag**: `</tagname>` — marks the end (note the forward slash)
- The content between them is called the **element**

**Example:**
```html
<h1>Welcome to my website</h1>
<p>This is a paragraph of text.</p>
```

This tells the browser: display "Welcome to my website" as a level-1 heading, and display the next text as a paragraph.

## Self-Closing Tags

Some elements have no content and don't need a closing tag:

```html
<br>       <!-- Line break -->
<hr>       <!-- Horizontal rule (divider line) -->
<img src="photo.jpg" alt="A photo">   <!-- Image -->
<meta charset="UTF-8">                <!-- Page metadata -->
```

In HTML5, these can also be written with a trailing slash: `<br />` — both forms are acceptable.

## Attributes

Tags can have **attributes** that provide extra information or configuration:

```html
<tagname attribute="value">content</tagname>
```

**Examples:**
```html
<a href="https://www.example.com">Click here</a>
<img src="logo.png" alt="Company logo" width="200">
<p class="intro">This is a special paragraph.</p>
```

- `href`, `src`, `alt`, `width`, `class` are all attribute names
- The value is always in quotation marks
- Attributes go inside the opening tag only

## Case Sensitivity

HTML is **not case-sensitive** — `<P>` and `<p>` mean the same thing. However, **convention is to use lowercase** for all tags and attributes. This is the HTML5 standard style.

## Whitespace in HTML

HTML ignores extra spaces, tabs, and blank lines in your code. These two examples produce identical output:

```html
<p>Hello world</p>

<p>Hello      world</p>
```

To force a space, you use `&nbsp;` (non-breaking space). To force a line break within a paragraph, use `<br>`.

## Your First HTML File

To create an HTML file:
1. Open a text editor (Notepad, VS Code, etc.)
2. Type your HTML code
3. Save the file with a `.html` extension (e.g. `index.html`)
4. Open the file in a web browser (double-click it, or drag it into the browser)

## Viewing HTML Source

In any web browser, you can view the HTML of any web page:
- **Right-click** on the page → **View Page Source** (shows the complete HTML)
- **Right-click** on an element → **Inspect** (opens Developer Tools showing the HTML and CSS)

This is a great way to learn — look at how real websites are built.

:::info
Pressing **F12** in most browsers opens the Developer Tools panel, which shows the HTML, CSS, and JavaScript of the current page. Professional web developers use this constantly.
:::

## Check Your Understanding

1. What does HTML stand for? What does each word in the name mean?
2. Explain the difference between HTML, CSS, and JavaScript. Use an analogy in your answer.
3. Is HTML a programming language? Justify your answer.
4. What is the difference between an opening tag and a closing tag? Give an example of each.
5. What is an attribute? Give an example of a tag with two attributes.
6. Write the HTML for a level-2 heading that says "About Me" and a paragraph that says "I am a Grade 9 learner."
7. How would you view the HTML code of a web page you are visiting? Why might this be useful when learning HTML?
