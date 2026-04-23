# Web Scripting

Static HTML shows the same content to everyone. Web scripting languages make websites dynamic — generating personalised pages, handling login, processing forms, and connecting to databases. This is what separates a brochure site from online banking.

> [!NOTE] Grade 12
> Web scripting languages are a Grade 12 topic. You need to understand what each language does and where it runs (client-side vs server-side), not write code in the theory exam.

---

## Client-Side vs Server-Side

| | **Client-Side** | **Server-Side** |
|---|---|---|
| Where code runs | In the user's browser | On the web server |
| Who executes it | Browser (JavaScript engine) | Server software (PHP, Python) |
| User can see code | Yes (View Source) | No |
| Internet required to run | No (once loaded) | Yes |
| Access to database | No (directly) | Yes |
| Examples | JavaScript, HTML, CSS | PHP, Python, Node.js, Ruby |

---

## HTML, CSS, and JavaScript — The Three Layers

| Layer | Technology | Role |
|---|---|---|
| **Structure** | HTML | What content is on the page |
| **Presentation** | CSS | How the content looks |
| **Behaviour** | JavaScript | How the content acts (interactivity) |

These three always work together in a modern web page.

---

## JavaScript

**JavaScript** is the primary client-side scripting language — it runs in the browser.

**What JavaScript does:**
- Responds to user events (button clicks, mouse movements, keyboard input)
- Validates forms before submission
- Updates page content without reloading (AJAX)
- Animates elements
- Communicates with APIs

```html
<!-- Simple JavaScript example -->
<button onclick="greet()">Click me</button>
<script>
  function greet() {
    alert("Hello from JavaScript!");
  }
</script>
```

**JavaScript in web applications:**
- React, Vue, Angular — JavaScript frameworks for building complex apps
- Node.js — JavaScript running on the server (server-side)

---

## PHP — Hypertext Preprocessor

**PHP** is a server-side scripting language embedded in HTML, used to generate dynamic web pages.

**How PHP works:**
1. Browser requests a page (e.g. `profile.php?id=42`)
2. Server runs the PHP code
3. PHP queries the database for user 42's data
4. PHP generates HTML with that data inserted
5. Server sends the completed HTML to the browser

```php
<?php
  $name = "Finn";
  $grade = 12;
  echo "<h1>Welcome, $name!</h1>";
  echo "<p>You are in Grade $grade.</p>";
?>
```

**PHP is used for:**
- Login and authentication systems
- Dynamic content from databases
- Form processing
- E-commerce (WordPress, WooCommerce use PHP)
- APIs

---

## XML — Extensible Markup Language

**XML** is a markup language for storing and transporting data in a human and machine-readable format.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<students>
  <student>
    <name>Finn</name>
    <grade>12</grade>
    <mark>95</mark>
  </student>
  <student>
    <name>Jake</name>
    <grade>11</grade>
    <mark>88</mark>
  </student>
</students>
```

**XML vs HTML:**
| | XML | HTML |
|---|---|---|
| Purpose | Data storage/transport | Web page structure |
| Tags | User-defined | Predefined set |
| Strict? | Very strict (case-sensitive) | Lenient |
| Display data? | No | Yes |

**Uses:** RSS feeds, configuration files, data exchange between systems, SOAP web services

---

## AJAX — Asynchronous JavaScript and XML

**AJAX** allows a web page to update part of its content **without reloading the entire page**.

**Before AJAX:**
- Click a button → entire page reloads → slow, disruptive

**With AJAX:**
- Click a button → JavaScript sends request to server → only relevant data returned → page updates silently

```
User action → JavaScript sends HTTP request → Server processes → Returns data (JSON/XML) → JavaScript updates DOM
```

**Examples of AJAX in use:**
- Google search suggestions appearing as you type
- Facebook/Instagram feed loading more posts as you scroll
- Online maps loading new tiles as you pan
- Live sports score updates without page reload
- Form validation feedback (checking if username is taken)

---

## JSON — JavaScript Object Notation

**JSON** is the modern replacement for XML in data exchange — lighter, easier to read.

```json
{
  "students": [
    {"name": "Finn", "grade": 12, "mark": 95},
    {"name": "Jake", "grade": 11, "mark": 88}
  ]
}
```

**Why JSON over XML:**
- Less verbose — smaller file size
- Native JavaScript format — no parsing needed
- Human-readable
- APIs almost universally use JSON today

---

## CSS — Cascading Style Sheets

**CSS** controls the visual presentation of HTML elements.

```css
/* CSS Example */
h1 {
  color: #2563eb;
  font-size: 2rem;
  font-family: Arial, sans-serif;
}

p {
  line-height: 1.6;
  max-width: 800px;
}

/* Responsive design */
@media (max-width: 768px) {
  h1 {
    font-size: 1.5rem;
  }
}
```

**CSS concepts:**
| Concept | Description |
|---|---|
| **Selector** | What to style (`h1`, `.class`, `#id`) |
| **Property** | What aspect to change (`color`, `font-size`) |
| **Value** | What to set it to (`blue`, `16px`) |
| **Media query** | Apply different styles at different screen sizes |
| **Cascade** | Rules applied in order of specificity |

**Why "Cascading"?**
Multiple CSS rules can apply to one element — the "cascade" determines which rule wins (specificity, order, importance).

---

## Web Application Architecture

### How a dynamic website works:

```
Browser
  ↓ HTTP request (GET /profile.php?id=5)
Web Server (Apache, Nginx)
  ↓ runs PHP
PHP Script
  ↓ SQL query
Database (MySQL)
  ↓ returns data
PHP Script
  ↓ generates HTML
Web Server
  ↓ HTTP response (HTML page)
Browser
  ↓ renders HTML + CSS + JavaScript
```

**Common technology stacks:**
| Stack | Technologies |
|---|---|
| **LAMP** | Linux + Apache + MySQL + PHP |
| **WAMP** | Windows + Apache + MySQL + PHP |
| **MEAN** | MongoDB + Express + Angular + Node.js |
| **JAMstack** | JavaScript + APIs + Markup |

---

## APIs — Application Programming Interfaces

An **API** allows different software systems to communicate and share data.

**Web APIs:**
- Server exposes endpoints (URLs) that return data
- Client (browser or app) calls the API to get data
- Data returned in JSON format

**Examples:**
- Google Maps API — embed maps in any website
- Payment gateway API (PayFast, PayPal) — process payments
- Weather API — retrieve real-time weather data
- Social login API — "Login with Google/Facebook"

---

## Key Terms

| Term | Definition |
|---|---|
| **Client-side** | Code runs in the user's browser |
| **Server-side** | Code runs on the web server |
| **JavaScript** | Client-side scripting language for web interactivity |
| **PHP** | Server-side scripting language for dynamic pages |
| **XML** | Markup language for storing and transporting data |
| **AJAX** | Updating web page content without full reload |
| **JSON** | Lightweight data format for API responses |
| **CSS** | Cascading Style Sheets — controls visual presentation |
| **API** | Interface allowing software systems to communicate |
| **DOM** | Document Object Model — browser's representation of the page |
| **Framework** | Pre-built set of tools for building applications (React, Vue) |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between client-side and server-side scripting?"** — Client-side: runs in the browser (JavaScript); user can see code; no database access. Server-side: runs on the server (PHP); user cannot see code; can access databases
>
> 2. **"What is AJAX? Give ONE example of its use."** — Allows a web page to update content without reloading the entire page; example: Google search suggestions appearing as you type
>
> 3. **"What is the purpose of PHP?"** — Server-side scripting language that generates dynamic web pages; processes form data; queries databases; handles authentication
>
> 4. **"What is the difference between XML and HTML?"** — XML stores and transports data using user-defined tags; HTML displays content using predefined tags
>
> 5. **"What does CSS do? Give TWO examples of CSS properties."** — Controls the visual presentation of HTML elements; examples: `color`, `font-size`, `background-color`, `margin`, `padding`
