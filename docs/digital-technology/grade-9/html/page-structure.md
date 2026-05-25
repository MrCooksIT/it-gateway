---
title: Structure of an HTML Page
---

# Structure of an HTML Page

## The Problem: Where Does the Text Go?

Suppose you have a simple web page. In the browser tab at the top, you want to show the title "My First Web Page". And on the actual page itself, you want to show the word "Hello".

You have two pieces of text:
- `My First Web Page`
- `Hello`

How do you tell the browser that one belongs in the tab and the other belongs on the page? Simply writing both pieces of text in a document is not enough — the browser needs structure to understand **where** to put each piece.

It turns out HTML has plenty of tags that help us tell the browser where we want text to go. These tags define the **structure** of the HTML page.

---

## The Basic HTML Skeleton

Here is the skeleton for a basic HTML page:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

There is a lot going on here. Let us break it down tag by tag.

---

## `<!DOCTYPE html>`

```html
<!DOCTYPE html>
```

The doctype tells the browser which **version of HTML** we are using. This declaration says we are using HTML5.

:::info
The doctype is not an actual HTML tag — it is a comment at the top of the file that tells the browser which version of HTML to use. You will need this at the top of all your HTML pages.
:::

---

## The `<html>` Tag

```html
<html>
  ...everything goes here...
</html>
```

The `<html>` tag says that everything between the opening and closing tag is our HTML page. It is the **container for all other tags** — our entire page goes inside the `<html>` tag.

---

## The `<head>` Tag

```html
<head>
  ...metadata here...
</head>
```

The `<head>` tag contains **important information about the document**. It contains **metadata** — data that describes data.

Think of the head as information *about* the page, not the page itself. The content in the head is not displayed on the actual web page. It is behind-the-scenes information about the page.

### The `<title>` Tag

```html
<title>My First Web Page</title>
```

The `<title>` tag defines the **title of the web page**. This is metadata — it is describing the page. The title is displayed in the browser tab at the top of the window. It is not shown in the body of the page itself.

---

## The `<body>` Tag

```html
<body>
  ...all page content here...
</body>
```

The `<body>` tag is where the **actual content** of the document goes. Text, images, links — everything that actually appears on your web page goes inside the body tag. Most of the time when you are building a web page, you will be writing code inside the body.

---

## Tags Inside Tags: Nesting

One of the most important things to notice is that **tags can go inside other tags**. This is called **nesting**.

- The `<head>` and `<body>` tags are both inside the `<html>` tag
- The `<title>` tag is inside the `<head>` tag
- The `<h1>` tag is inside the `<body>` tag

### Indentation Shows Structure

Every time we have a tag inside another tag, we **indent** those inner tags. Everything inside the `<html>` tag is indented one level. Everything inside the `<head>` tag is indented one level further.

This indentation helps us see the structure of the page — it shows which tags are inside which other tags.

---

## The Tree Structure

The structure of an HTML document can be described as a **tree**. At the very root of the tree is the `<html>` tag. The `<html>` tag has two children: `<head>` and `<body>`. Inside `<head>` we have `<title>`. Inside `<body>` we have our content tags like `<h1>`.

```
html
├── head
│   └── title
└── body
    └── h1
```

If we added more tags inside the body — like another `<h1>` — they would both appear at the same level of the tree.

---

## Putting it All Together

Going back to our original problem: we wanted "My First Web Page" to appear in the browser tab, and "Hello" to appear on the page.

- `My First Web Page` is **not** displayed on the actual page — it is metadata, information about the page. So it goes in the `<head>` inside a `<title>` tag.
- `Hello` is **displayed on the page** — it is actual content. So it goes in the `<body>`. We also need to tell the browser *how* to display it, so we wrap it in an `<h1>` tag to make it big and bold.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

The result: the browser tab shows "My First Web Page" as the title, and the page itself shows "Hello World" as a large heading.

---

## Key Points to Remember

:::tip Key Points
1. **Tags can go inside other tags** — this is called nesting.
2. **Use indentation** to show which tags are inside which other tags. This makes your code readable.
3. **The structure of an HTML document is like a tree** — with `<html>` at the root.
4. The `<head>` contains **metadata** (information about the page, not displayed to the user).
5. The `<body>` contains the **actual content** that appears on the page.
:::

---

## Complete Example

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

This is the basic structure you will use for every HTML page you create.

---

## Check Your Understanding

1. What is the purpose of `<!DOCTYPE html>`? Where does it go in an HTML file?

2. What does the `<html>` tag do? What does it contain?

3. What is the difference between the `<head>` and `<body>` sections? Give one example of what belongs in each.

4. What is metadata? Give an example of a tag that holds metadata.

5. Where does the `<title>` tag text appear? Is it displayed on the web page itself?

6. Write the complete HTML code for a page with a title of "About Me" and a heading on the page that says "Welcome to My Page".

7. Explain what nesting means in HTML. Give an example using the `<html>`, `<head>`, and `<body>` tags.

8. Why do we use indentation in HTML? Does it affect what the user sees in the browser?

9. Draw or describe the tree structure of this HTML:
   ```html
   <html>
     <head>
       <title>Example</title>
     </head>
     <body>
       <h1>Heading</h1>
     </body>
   </html>
   ```

10. What would happen if you put the `<title>` tag inside the `<body>` instead of the `<head>`?
