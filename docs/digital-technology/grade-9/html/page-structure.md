---
title: Structure of an HTML Page
---

# Structure of an HTML Page

Every HTML page — from a simple school project to a complex website — follows the same basic structure. Understanding this skeleton is essential before adding any content.

## The Minimal HTML5 Page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My First Page</title>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is my first web page.</p>
</body>
</html>
```

Let's break down every line.

## `<!DOCTYPE html>`

```html
<!DOCTYPE html>
```

- This is a **declaration**, not a tag
- It tells the browser: "This is an HTML5 document"
- Must be the very first line — before anything else
- Not case-sensitive, but convention is uppercase `DOCTYPE`

Without it, browsers may enter "quirks mode" and render the page differently.

## The `<html>` Element

```html
<html lang="en">
  ...all content goes here...
</html>
```

- The **root element** — everything else is inside it
- The `lang` attribute tells browsers and screen readers what language the page is in (`en` for English, `af` for Afrikaans, `zu` for Zulu)
- Has exactly two children: `<head>` and `<body>`

## The `<head>` Element

```html
<head>
  ...metadata here...
</head>
```

The `<head>` contains **metadata** — information about the page that is not displayed to the user. Think of it as behind-the-scenes instructions.

### `<meta charset="UTF-8">`

```html
<meta charset="UTF-8">
```

- Sets the **character encoding** — how the browser interprets text characters
- UTF-8 supports virtually all characters and languages in the world
- Without this, special characters (é, ü, ñ, © etc.) may display incorrectly
- Should always be the first thing in `<head>`

### `<title>`

```html
<title>My First Page</title>
```

- Sets the text shown in the **browser tab** and in bookmark names
- Used by search engines as the title in search results
- Should be descriptive: "About Us | Marist School" rather than just "Page"

### Other Common `<head>` Elements

```html
<meta name="description" content="A brief description of this page for search engines">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="styles.css">
```

| Tag | Purpose |
|-----|---------|
| `<meta name="description">` | Page summary for search engines |
| `<meta name="viewport">` | Controls layout on mobile devices (essential for responsive design) |
| `<link rel="stylesheet">` | Links an external CSS file |
| `<link rel="icon">` | Sets the small icon in the browser tab (favicon) |

:::info
None of the content in `<head>` appears on the web page itself. It's all instructions for the browser, search engines, and other tools.
:::

## The `<body>` Element

```html
<body>
  ...everything the user sees...
</body>
```

Everything inside `<body>` is displayed on the screen: headings, text, images, links, tables, forms — everything.

## Nesting: The Tree Structure

HTML elements can be **nested** inside each other — meaning one element can contain another. This creates a tree-like structure:

```html
<body>
  <h1>My Website</h1>
  <p>Welcome to <strong>my</strong> page.</p>
</body>
```

In this example:
- `<body>` contains `<h1>` and `<p>`
- `<p>` contains `<strong>`
- `<strong>` is a **child** of `<p>`; `<p>` is the **parent**

**Critical rule**: elements must be properly nested — they cannot overlap.

```html
<!-- CORRECT: properly nested -->
<p>This is <strong>bold text</strong>.</p>

<!-- WRONG: overlapping tags -->
<p>This is <strong>bold text</p></strong>
```

## Indentation

HTML does not require indentation — the browser ignores whitespace. But indentation makes your code **readable** for humans.

**Convention**: Indent each nested level by 2 spaces (or a tab).

```html
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Heading</h1>
    <p>Paragraph.</p>
  </body>
</html>
```

Good indentation habits now will save you hours of debugging later.

## HTML Comments

```html
<!-- This is a comment — the browser ignores it -->
```

Comments are notes in your code that are not displayed on the page. Use them to:
- Explain complex code
- Temporarily "disable" a section of code
- Leave reminders for yourself or collaborators

```html
<!-- Navigation section -->
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
</nav>

<!-- TODO: add a contact form here -->
```

## A Complete Example with Explanation

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="My personal school project page">
  <title>My School Project | Grade 9</title>
</head>
<body>

  <h1>My Technology Project</h1>

  <p>This website is about the <strong>history of computers</strong>.</p>

  <h2>Introduction</h2>
  <p>The first computers were room-sized machines that used
  vacuum tubes to perform calculations.</p>

  <!-- Add more content below this line -->

</body>
</html>
```

## Check Your Understanding

1. What is `<!DOCTYPE html>` and why must it be the first line in an HTML file?
2. What is the difference between the `<head>` and `<body>` sections? Give two examples of what belongs in each.
3. Why is `<meta charset="UTF-8">` important? What could happen if you leave it out?
4. Write the HTML code for a page with:
   - A proper DOCTYPE and `<html>` element with the language set to English
   - A `<head>` containing a title of "My Hobby" and the UTF-8 charset meta tag
   - A `<body>` containing an `<h1>` with your hobby name and two sentences about it in a `<p>`
5. Explain what nesting means in HTML. Why does it matter that tags are properly nested?
6. What are HTML comments? Show the syntax and give one situation where you would use one.
7. Does indentation in HTML affect what the user sees in the browser? Why do we use it anyway?
