---
title: HTML Styling
---

# HTML Styling

A plain HTML page works — but it looks like a plain text document from the 1990s. CSS (Cascading Style Sheets) is what makes web pages look good. In this chapter you'll learn three ways to add CSS to HTML and the essential CSS properties every web developer knows.

## Separation of Concerns

:::tip Key Term
**Separation of concerns** is a design principle that says each technology should handle one responsibility:
- **HTML** → structure and content
- **CSS** → appearance and layout
- **JavaScript** → behaviour and interactivity
:::

Keeping these separate makes code easier to maintain. One CSS file can style an entire website of hundreds of pages.

## Three Ways to Add CSS

### Method 1: Inline Styles

CSS written directly on an element using the `style` attribute:

```html
<h1 style="color: blue; font-size: 36px;">Welcome</h1>
<p style="background-color: yellow;">This is highlighted.</p>
```

**When to use**: Quick tests, one-off styling, email templates.

**Disadvantages**:
- Cannot be reused — must be repeated on every element
- Mixes structure and style (against best practice)
- Hard to maintain on large sites

### Method 2: Internal Styles

CSS placed inside a `<style>` element in the `<head>`:

```html
<head>
  <meta charset="UTF-8">
  <title>My Page</title>
  <style>
    h1 {
      color: blue;
      font-size: 36px;
    }
    p {
      font-family: Arial, sans-serif;
      line-height: 1.6;
    }
  </style>
</head>
```

**When to use**: Single-page websites, quick prototypes.

**Disadvantages**: The styles only apply to that one page — not reusable across multiple pages.

### Method 3: External Stylesheet (Best Practice)

CSS in a separate `.css` file, linked from the HTML `<head>`:

**HTML file (index.html):**
```html
<head>
  <meta charset="UTF-8">
  <title>My Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
```

**CSS file (styles.css):**
```css
h1 {
  color: navy;
  font-size: 36px;
}

p {
  font-family: Arial, sans-serif;
  line-height: 1.6;
}
```

**Advantages**:
- One CSS file styles the entire website
- Change the CSS file → all pages update instantly
- Browser caches the CSS — pages load faster
- Clean separation of HTML and CSS

## CSS Syntax

A CSS rule has this structure:

```css
selector {
  property: value;
  property: value;
}
```

- **Selector**: which element(s) to style
- **Property**: what aspect to change (colour, size, font, etc.)
- **Value**: what to change it to
- Each declaration ends with a semicolon `;`

## CSS Selectors

| Selector | Syntax | What it selects |
|----------|--------|----------------|
| Element | `p { }` | All `<p>` elements |
| Class | `.intro { }` | All elements with `class="intro"` |
| ID | `#header { }` | The element with `id="header"` |
| All | `* { }` | Every element on the page |

```html
<!-- HTML -->
<h1 class="title">Hello</h1>
<p class="intro">First paragraph</p>
<p>Second paragraph</p>
<footer id="main-footer">Footer text</footer>
```

```css
/* CSS */
h1 { color: navy; }           /* styles all h1 elements */
.intro { font-weight: bold; } /* styles elements with class="intro" */
#main-footer { color: grey; } /* styles element with id="main-footer" */
```

:::warning
Use `id` selectors sparingly — each `id` should be unique on a page. Use `class` for styling multiple elements with the same style.
:::

## Essential CSS Properties

### Colour

```css
p {
  color: red;               /* Text colour */
  background-color: yellow; /* Background colour */
}
```

**Colour values:**

| Format | Example | Notes |
|--------|---------|-------|
| Named colour | `red`, `navy`, `forestgreen` | ~140 named colours available |
| Hex code | `#ff0000` | 6 hex digits: #RRGGBB |
| Short hex | `#f00` | 3 digit shorthand when digits repeat |
| RGB | `rgb(255, 0, 0)` | Red, Green, Blue values 0–255 |
| RGBA | `rgba(255, 0, 0, 0.5)` | RGB + Alpha (transparency 0–1) |

```css
h1 { color: #2c3e50; }             /* Dark blue-grey hex */
nav { background-color: rgb(0, 128, 0); }  /* Green RGB */
.overlay { background-color: rgba(0, 0, 0, 0.7); } /* Semi-transparent black */
```

### Typography

```css
p {
  font-family: Arial, Helvetica, sans-serif; /* Font stack */
  font-size: 16px;                           /* Text size */
  font-weight: bold;                         /* bold or normal */
  font-style: italic;                        /* italic or normal */
  text-align: center;                        /* left, center, right, justify */
  text-decoration: underline;                /* underline, line-through, none */
  line-height: 1.6;                          /* Space between lines */
  letter-spacing: 2px;                       /* Space between letters */
}
```

**Font stacks**: List multiple fonts in case the first isn't installed. End with a generic family:

```css
font-family: "Georgia", "Times New Roman", serif;
font-family: "Arial", "Helvetica", sans-serif;
font-family: "Courier New", "Courier", monospace;
```

### Box Model: Spacing

Every element is a rectangular box. CSS controls spacing:

```css
div {
  margin: 20px;     /* Space OUTSIDE the element */
  padding: 15px;    /* Space INSIDE the element, between border and content */
  border: 2px solid black; /* Border around the element */
}
```

You can set each side individually:

```css
p {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;
}

/* Shorthand: top, right, bottom, left (clockwise) */
p { margin: 10px 20px 10px 20px; }

/* Same on all sides */
p { margin: 10px; }
```

### Dimensions

```css
div {
  width: 400px;           /* Fixed width in pixels */
  width: 80%;             /* Width as percentage of parent */
  max-width: 800px;       /* Maximum width */
  height: 200px;          /* Fixed height */
}
```

## A Complete Styled Example

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Styled Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header>
    <h1>Digital Technology Notes</h1>
    <nav>
      <ul>
        <li><a href="#html">HTML</a></li>
        <li><a href="#css">CSS</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h2 id="html">What is HTML?</h2>
    <p class="intro">HTML is the foundation of every web page.</p>
    <p>It uses tags to structure content.</p>

    <h2 id="css">What is CSS?</h2>
    <p class="intro">CSS controls how HTML elements look.</p>
  </main>

</body>
</html>
```

**styles.css:**
```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  color: #333333;
}

header {
  background-color: #2c3e50;
  color: white;
  padding: 20px;
  margin-bottom: 30px;
}

h1 {
  font-size: 28px;
  margin: 0;
}

h2 {
  color: #2c3e50;
  border-bottom: 2px solid #2c3e50;
  padding-bottom: 5px;
}

.intro {
  font-weight: bold;
  color: #555555;
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 20px;
}

nav a {
  color: white;
  text-decoration: none;
}
```

## Check Your Understanding

1. Explain the three ways to add CSS to HTML. Which is best practice for a multi-page website and why?
2. Write the CSS rule to make all `<h1>` elements display in dark blue (`#003366`) with a font size of 32 pixels.
3. What is the difference between `margin` and `padding`? Draw a simple sketch or describe in words.
4. A student has `class="highlight"` on several `<p>` tags. Write the CSS selector and rule to give these paragraphs a yellow background.
5. What is a font stack? Write a CSS font-family declaration for a sans-serif style with three fallback fonts.
6. Write complete HTML and CSS for a page about your favourite food that includes:
   - A styled heading (colour and size of your choice)
   - Two paragraphs with readable line height
   - A coloured background for the page
7. What does `margin: 0 auto` do when applied to a block element with a set width? Why is this technique useful?
