---
title: Links in HTML
---

# Links in HTML

## What are Hyperlinks?

**Links** — also known as **hyperlinks** — connect web pages together. A hyperlink points to another hypertext document (which is what web pages are), and allows viewers to click from page to page when browsing the internet.

For example, a link on a page might take you to the Google search results for a particular topic. Every one of those search results is itself a link to another page. Clicking any one of them takes you to that page. From there, you might see more links to related topics — each one taking you somewhere new.

This is what makes hyperlinks so powerful: they link together relevant web pages and make it very easy for users to find more information about whatever they are looking at — without having to search for each page manually.

---

## The `<a>` Tag

To make a hyperlink in HTML, we use the **`<a>` tag** (short for **anchor**). The `<a>` tag allows us to define a hyperlink.

The basic structure of a link is:

```html
<a href="URL">Link text</a>
```

- The **link text** (what appears inside the tags) is what the user sees and clicks on
- The **`href` attribute** specifies the address that the link actually takes you to

---

## HTML Attributes

This introduces something new: **attributes**. Tags can have attributes that give us more information about what the tag is doing.

:::tip Key Term
**Attribute:** Extra information added inside an HTML opening tag. Attributes have a **name** and a **value**, written as `name="value"`.
:::

Attributes go inside the **opening tag**, after the tag name. The format is:

```html
<tagname attribute="value">content</tagname>
```

For the `<a>` tag, the attribute we need is called **`href`** (short for **HyperText REFerence**). The value of `href` is the URL that the link points to.

```html
<a href="https://www.google.com">Click me</a>
```

- The text `Click me` is what the user sees on the page
- The `href` tells the browser: when the user clicks this link, take them to `https://www.google.com`

Just putting an `<a>` tag around text is not enough — that would create a link with no destination. You must include the `href` attribute to tell the browser **where** the link should take the user.

---

## A Complete Link Example

Let us say we have a web page with a heading and some text about CodeHS, and we want to add a link to the CodeHS information page:

```html
<h1>Welcome to CodeHS</h1>
<a href="https://codehs.com/info">Learn more about CodeHS</a>
```

When the user clicks "Learn more about CodeHS", they are taken to `https://codehs.com/info`.

We can add multiple links on the same page:

```html
<a href="https://codehs.com/info">CodeHS</a>
<a href="https://wikipedia.org">Wikipedia</a>
```

Now the page has two links — one takes the user to CodeHS, and the other takes them to Wikipedia.

---

## Links in Practice

Links really make the World Wide Web go round. They make it very easy for users to browse the web and get more information without having to manually search for every page they want to visit.

Here is a more complete example of a web page with links:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Useful Links</title>
  </head>
  <body>
    <h1>Welcome to CodeHS</h1>
    <p>CodeHS is a platform for learning to code.</p>
    <a href="https://codehs.com/info">Learn more about CodeHS</a>

    <a href="https://wikipedia.org">Wikipedia</a>
  </body>
</html>
```

---

## Summary of the `<a>` Tag

| Part | Example | Purpose |
|------|---------|---------|
| Opening tag | `<a` | Starts the anchor element |
| `href` attribute | `href="https://google.com"` | Sets the destination URL |
| Closing `>` of opening tag | `>` | Ends the opening tag |
| Link text | `Click me` | The text the user sees and clicks |
| Closing tag | `</a>` | Ends the anchor element |

---

## Check Your Understanding

1. What is a hyperlink? What makes hyperlinks important for the World Wide Web?

2. What does the `<a>` tag stand for? What is its purpose?

3. What is an HTML attribute? Describe the format of an attribute (name and value).

4. What does `href` stand for? What information does it provide?

5. Write the HTML code to create a link that displays the text "Visit Google" and takes the user to `https://www.google.com`.

6. A student writes `<a>Click here</a>` without an `href` attribute. What is wrong with this? How would you fix it?

7. Write the HTML code to create TWO links on the same page: one to `https://www.codehs.com` (displayed as "CodeHS") and one to `https://www.wikipedia.org` (displayed as "Wikipedia").

8. **Extended question:** Think about a web page you use frequently. How many hyperlinks does it probably have? Why do you think links are described as what makes the World Wide Web a "web"?
