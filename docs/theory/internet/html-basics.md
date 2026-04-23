# HTML Basics

Every web page you visit is built on HTML. Behind the images, buttons, and layouts is a plain text file with tags telling the browser what each piece of content means. Understanding HTML is understanding the language of the web.

> [!NOTE] Grade 10
> HTML basics are a Grade 10 theory topic. You need to understand the structure, common tags, and their purpose — not write full websites from scratch in the theory exam.

---

## What is HTML?

**HTML** (HyperText Markup Language) is the standard language used to structure content on the web.

- **HyperText**: text with links to other documents
- **Markup**: tags that annotate/describe the content
- **Language**: a set of rules browsers can interpret

HTML describes **what** content is (a heading, a paragraph, a link) — not **how it looks** (that's CSS).

---

## Basic HTML Document Structure

Every valid HTML page follows this structure:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Page Title</title>
  </head>
  <body>
    <h1>Welcome to my page</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

| Part | Purpose |
|---|---|
| `<!DOCTYPE html>` | Declares this is an HTML5 document |
| `<html>` | Root element — wraps all content |
| `<head>` | Metadata — not visible on page (title, charset, links) |
| `<meta charset="UTF-8">` | Character encoding — handles international characters |
| `<title>` | Text shown in browser tab |
| `<body>` | All visible page content goes here |

---

## HTML Tags

Tags are written in angle brackets: `<tagname>content</tagname>`

- **Opening tag**: `<p>`
- **Closing tag**: `</p>`
- **Self-closing tag**: `<img src="photo.jpg" alt="A photo">` (no closing tag needed)

---

## Heading Tags

Six levels of headings — `<h1>` is most important (page title), `<h6>` is least.

```html
<h1>Main Page Title</h1>
<h2>Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Sub-subsection</h4>
```

> [!TIP] SEO and headings
> Search engines use heading structure to understand your page. Only one `<h1>` per page — it's the main topic.

---

## Common HTML Tags

| Tag | Purpose | Example |
|---|---|---|
| `<h1>–<h6>` | Headings (6 levels) | `<h1>Title</h1>` |
| `<p>` | Paragraph | `<p>Text here.</p>` |
| `<a href="">` | Hyperlink | `<a href="https://example.com">Click me</a>` |
| `<img src="" alt="">` | Image | `<img src="logo.png" alt="Company logo">` |
| `<br>` | Line break (self-closing) | `Line 1<br>Line 2` |
| `<hr>` | Horizontal rule / divider | `<hr>` |
| `<strong>` | Bold (semantic importance) | `<strong>Important</strong>` |
| `<em>` | Italic (emphasis) | `<em>stressed word</em>` |
| `<ul>` | Unordered list (bullets) | see below |
| `<ol>` | Ordered list (numbers) | see below |
| `<li>` | List item | `<li>Item</li>` |
| `<div>` | Block-level container | `<div>Section content</div>` |
| `<span>` | Inline container | `<span style="color:red">red text</span>` |
| `<table>` | Table | see below |
| `<form>` | Input form | see below |

---

## Lists

```html
<!-- Unordered list -->
<ul>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Oranges</li>
</ul>

<!-- Ordered list -->
<ol>
  <li>First step</li>
  <li>Second step</li>
  <li>Third step</li>
</ol>
```

---

## Links

```html
<!-- Link to external website -->
<a href="https://www.google.com">Visit Google</a>

<!-- Link to another page on the same site -->
<a href="about.html">About Us</a>

<!-- Link that opens in new tab -->
<a href="https://example.com" target="_blank">Open in new tab</a>

<!-- Email link -->
<a href="mailto:teacher@school.co.za">Email the teacher</a>
```

**`href`** = hypertext reference — the URL or file path to link to

---

## Images

```html
<img src="photo.jpg" alt="A photo of the school">
```

| Attribute | Purpose |
|---|---|
| `src` | Source — path or URL of the image file |
| `alt` | Alternative text — shown if image fails; read by screen readers |
| `width` | Width in pixels or percentage |
| `height` | Height in pixels or percentage |

> [!WARNING] Always include alt text
> Missing alt text fails accessibility standards and harms SEO.

---

## Tables

```html
<table border="1">
  <tr>
    <th>Name</th>
    <th>Mark</th>
  </tr>
  <tr>
    <td>Finn</td>
    <td>95</td>
  </tr>
  <tr>
    <td>Jake</td>
    <td>88</td>
  </tr>
</table>
```

| Tag | Purpose |
|---|---|
| `<table>` | Defines the table |
| `<tr>` | Table row |
| `<th>` | Table header cell (bold, centred by default) |
| `<td>` | Table data cell |

---

## Forms

Forms collect user input and send it to a server.

```html
<form action="submit.php" method="post">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Enter your name">
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  
  <label for="age">Age:</label>
  <input type="number" id="age" name="age" min="10" max="100">
  
  <input type="submit" value="Submit">
</form>
```

**Form attributes:**
| Attribute | Purpose |
|---|---|
| `action` | URL to send form data to |
| `method` | HTTP method: `get` (data in URL) or `post` (data in request body) |

**Common input types:**
| Type | Purpose |
|---|---|
| `text` | Single-line text input |
| `email` | Email address (validated) |
| `password` | Hidden text input |
| `number` | Numeric input |
| `checkbox` | Tick box |
| `radio` | One option from a group |
| `submit` | Submit button |
| `file` | File upload |

---

## HTML Attributes

Attributes provide additional information about elements. They go inside the opening tag.

```html
<tagname attribute="value">content</tagname>
```

| Attribute | Used on | Purpose |
|---|---|---|
| `href` | `<a>` | Hyperlink URL |
| `src` | `<img>`, `<script>` | Source file |
| `alt` | `<img>` | Alternative text |
| `id` | Any | Unique identifier |
| `class` | Any | CSS class for styling |
| `style` | Any | Inline CSS |
| `target` | `<a>` | Where to open link (`_blank` = new tab) |
| `placeholder` | `<input>` | Hint text in empty field |
| `required` | `<input>` | Field cannot be left empty |

---

## HTML vs CSS vs JavaScript

| Language | Role | Example |
|---|---|---|
| **HTML** | Structure — what content is | `<h1>Title</h1>` |
| **CSS** | Presentation — how it looks | `h1 { color: blue; font-size: 32px; }` |
| **JavaScript** | Behaviour — what it does | `document.getElementById('btn').onclick = ...` |

---

## Key Terms

| Term | Definition |
|---|---|
| **HTML** | HyperText Markup Language — structure of web pages |
| **Tag** | HTML element written in angle brackets `<tagname>` |
| **Attribute** | Property of an HTML element written in the opening tag |
| **`href`** | Attribute specifying the URL of a hyperlink |
| **`src`** | Attribute specifying the source of an image or script |
| **`alt`** | Alternative text for images |
| **`<head>`** | Section containing metadata (not visible) |
| **`<body>`** | Section containing all visible content |
| **`<div>`** | Block-level container element |
| **`<span>`** | Inline container element |
| **Form** | HTML structure for collecting user input |
| **CSS** | Cascading Style Sheets — controls appearance of HTML |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Write the HTML tag to create a link to www.google.com with the text 'Visit Google'"** — `<a href="https://www.google.com">Visit Google</a>`
>
> 2. **"Write the HTML tag to display an image called 'logo.png' with alt text 'School logo'"** — `<img src="logo.png" alt="School logo">`
>
> 3. **"What is the purpose of the `alt` attribute on an image tag?"** — Displays alternative text if image fails to load; read by screen readers for accessibility; used by search engines
>
> 4. **"What is the difference between `<th>` and `<td>`?"** — `<th>` is a table header cell (displayed bold and centred); `<td>` is a regular table data cell
>
> 5. **"Explain the difference between HTML and CSS"** — HTML defines the structure and content (what elements are on the page); CSS controls the presentation (how they look — colours, fonts, layout)
