---
title: Links in HTML
---

# Links in HTML

Links are what makes the web a *web* — without them, every page would be an island. The `<a>` (anchor) tag is one of the most important HTML elements you will use.

## The Anchor Tag

```html
<a href="URL">Link text</a>
```

- `<a>` is the anchor element
- `href` (HyperText REFerence) is the attribute that contains the destination URL
- The link text is what the user clicks on — it should describe where the link goes

```html
<p>Visit <a href="https://www.codehs.com">CodeHS</a> for coding activities.</p>
```

This displays as: Visit [CodeHS](https://www.codehs.com) for coding activities.

## Absolute vs Relative URLs

### Absolute URLs

An **absolute URL** includes the full address — protocol, domain, and path:

```html
<a href="https://www.example.com/about">About Us</a>
<a href="https://news24.com">News24</a>
```

Use absolute URLs when linking to **external websites** (pages on a different domain).

### Relative URLs

A **relative URL** gives a path *relative to the current page's location*:

```html
<a href="about.html">About Us</a>          <!-- Same folder -->
<a href="pages/contact.html">Contact</a>   <!-- In a subfolder -->
<a href="../index.html">Home</a>           <!-- Up one folder level -->
```

- `about.html` — file in the same directory as the current page
- `pages/contact.html` — file inside a `pages` subfolder
- `../index.html` — `..` means go up one folder level

Use relative URLs when linking to **pages within your own website**. If you move your website to a different domain, relative links still work — absolute links to your own site would all break.

**Example file structure:**
```
website/
  index.html
  about.html
  pages/
    contact.html
    gallery.html
```

From `index.html`: link to `about.html` → `href="about.html"`  
From `pages/contact.html`: link to `index.html` → `href="../index.html"`

## Opening Links in a New Tab

By default, links open in the same tab. To open in a new tab:

```html
<a href="https://www.example.com" target="_blank">Open in new tab</a>
```

:::warning Security note
When using `target="_blank"`, always add `rel="noopener noreferrer"`:

```html
<a href="https://www.example.com" target="_blank" rel="noopener noreferrer">Safe link</a>
```

Without `rel="noopener"`, the new page can access your page through JavaScript — a security vulnerability known as "reverse tabnabbing".
:::

## Email Links

```html
<a href="mailto:teacher@school.co.za">Email the teacher</a>
```

Clicking this link opens the user's default email client with the "To" field pre-filled.

You can also pre-fill the subject line:

```html
<a href="mailto:teacher@school.co.za?subject=Grade%209%20Question">Email about Grade 9</a>
```

(Spaces in URLs are encoded as `%20`)

## Phone Links

```html
<a href="tel:+27123456789">Call us: 012 345 6789</a>
```

On mobile devices, clicking a `tel:` link opens the phone app ready to dial.

## Linking to a Section on the Same Page

For long pages, you can create links that jump to a specific section. This requires two things:

**Step 1**: Give the target section an `id` attribute:
```html
<h2 id="history">History of the Internet</h2>
```

**Step 2**: Link to it using `#id`:
```html
<a href="#history">Jump to History section</a>
```

You can also link to a section on another page:
```html
<a href="about.html#team">Meet our team</a>
```

:::info
A list of section links at the top of a long page is called a **table of contents**. This technique is commonly used in Wikipedia articles.
:::

## Building a Navigation Menu

A navigation bar is typically an unordered list of links:

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="services.html">Services</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

The `<nav>` element is a semantic HTML5 element that indicates this is navigation. CSS is then used to style the list into a horizontal bar.

## Writing Good Link Text

:::warning
Avoid vague link text like "click here" or "read more". It is:
- Unhelpful to users who skim the page
- Inaccessible to screen reader users who navigate by links
- Bad for SEO (search engines use link text to understand context)
:::

**Bad:**
```html
To learn about cybersecurity, <a href="security.html">click here</a>.
```

**Good:**
```html
Learn more about <a href="security.html">cybersecurity basics</a>.
```

## A Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Links Demo</title>
</head>
<body>

  <h1>Useful Resources</h1>

  <!-- Table of contents -->
  <ul>
    <li><a href="#coding">Coding</a></li>
    <li><a href="#safety">Online Safety</a></li>
  </ul>

  <h2 id="coding">Coding Resources</h2>
  <p>Practice coding on <a href="https://www.codehs.com" target="_blank" rel="noopener noreferrer">CodeHS</a>.</p>

  <h2 id="safety">Online Safety</h2>
  <p>Report cybercrime to <a href="https://www.saps.gov.za">SAPS</a>.</p>

  <hr>
  <p>Questions? <a href="mailto:it@school.co.za">Email the IT department</a>.</p>

</body>
</html>
```

## Check Your Understanding

1. What does `href` stand for? Write the HTML for a link to `https://www.google.com` that displays as "Search Google".

2. Explain the difference between an absolute URL and a relative URL. When would you use each?

3. Consider this file structure:
   ```
   site/
     index.html
     contact.html
     blog/
       post1.html
   ```
   Write a relative link from `blog/post1.html` back to `index.html`.

4. Write a complete email link that opens an email to `admin@school.co.za` with the subject "Help needed".

5. A learner writes:
   ```html
   <a href="https://external-site.com" target="_blank">Visit this site</a>
   ```
   What security improvement should they make, and why?

6. How do you create a link that jumps to a section on the same page? Show both the target and the link in your answer.

7. Look at this link text: `For more info, <a href="info.html">click here</a>`. What is wrong with the link text and how would you improve it?
