---
title: Introduction to HTML
---

# Introduction to HTML

## Have You Ever Wondered How Web Pages Are Made?

You probably visit several websites every day on the internet. But have you ever wondered what goes into making those web pages — what is happening behind the scenes?

The answer is **HTML**.

HTML is the language used to build web pages. Once you understand HTML, you will understand how every single page on the internet is made. Facebook, Google, Wikipedia — every web page you have ever visited was built with HTML, and it was built by people who had to learn it first. No one started off knowing HTML. That is what we are going to do: learn HTML so we can start building our own web pages.

---

## Why Learn HTML?

HTML lets us build our own web pages. When we build our own web pages, we can:

- Easily **share our ideas** and creations with the entire world
- **Spread information** about topics we care about
- Create a **space for our art** or work
- **Organise** groups and communities

Web pages have become an incredibly valuable resource in our society. They are the new way information is shared between people.

Furthermore, what is incredible about HTML is that once you make a single HTML document, **any browser on any device** is able to take that document and display a beautiful web page from it. It does not matter whether someone is on a phone, a tablet, or a computer. It does not matter whether they use Chrome or Firefox. Every browser can view your web page.

---

## What is HTML?

**HTML** stands for **HyperText Markup Language**. That is a lot of words — let us break them down one by one.

### HyperText

**Hypertext** simply means text that is displayed on a computer and has links to other hypertext documents. These links are called **hyperlinks**.

This is an incredible part of HTML: an HTML document is not a standalone document like a page from a book. Instead, HTML documents are **interconnected** — you can easily travel between them by clicking hyperlinks. In the past, if you were reading a document and wanted more information, you had to track down the right book, find the right chapter, and locate the right paragraph. With HTML, you can just **click a link** and go straight to that information.

For example, clicking a hyperlink might take you to the Wikipedia page for a topic, where you can read more — without having to search for it yourself. Links truly make the World Wide Web a "web" of connected pages.

### Markup Language

A **markup language** is a language that lets you annotate (mark up) normal text to define how it should be displayed. Markup language marks up standard text to provide further information about it — telling the browser how that text should look.

### Putting it Together

So HTML is a language that:
- Works with **hypertext** (text that links to other documents)
- Uses **markup** (special codes called tags) to tell the browser how to display text

---

## HTML Tags

HTML uses **tags** to mark up the text of a document. Tags tell the browser how that text should be displayed. At its core, HTML is really just **normal text plus markup tags**.

:::tip Key Term
**HTML Tag:** A keyword enclosed in angle brackets that tells the browser how to display the text around it. Tags are not displayed on the resulting web page — they are only found in the HTML code.
:::

Tags have the following properties:
- They are enclosed in **angle brackets**: `< >`
- They are **not displayed** on the resulting web page — they only appear in the HTML code
- They **inform the browser** about how certain text should be displayed

### Opening and Closing Tags

When we use HTML tags, we usually need both an **opening tag** and a **closing tag**:

```html
<h1>Hello</h1>
```

- The **opening tag** is `<h1>` — marks the start
- The **closing tag** is `</h1>` — marks the end (note the forward slash)
- The **content** between the tags (`Hello`) is what actually appears on the web page

The content between the opening and closing tag is **affected by** (decorated by) the tag.

---

## Your First HTML Tag: `<h1>`

The `<h1>` tag is a **heading tag**. It tells the browser to display the text between the tags as a large, bold heading.

```html
<h1>Hello</h1>
```

The name of the tag is `h1` — it goes between the angle brackets. When the browser sees this, it displays "Hello" as a big, bold heading at the top of the page.

If you simply write the word `Hello` without any tags, it appears as plain, small text. But when you wrap it in `<h1>` tags, you are **marking it up** — decorating it to tell the browser: "Display this big and bold."

---

## A Browser is Your HTML Viewer

A **browser** is simply an application on a computer that can take an HTML document and display it as a web page.

When you write HTML code and open it in a browser, the browser reads your code and renders (builds) the visual web page from it. The code is the instruction; the browser carries out those instructions.

---

## Summary

| Term | Meaning |
|------|---------|
| **HTML** | HyperText Markup Language — the language used to build web pages |
| **HyperText** | Text that links to other documents via hyperlinks |
| **Markup Language** | A language that annotates text with tags to define how it is displayed |
| **Tag** | A keyword in angle brackets that tells the browser how to display content |
| **`<h1>`** | A heading tag — displays text as a large, bold heading |
| **Browser** | An application that reads HTML code and displays it as a web page |

---

## Check Your Understanding

1. What does HTML stand for? What does each word in the name mean?

2. In your own words, explain what a hyperlink is. How do hyperlinks make the web different from a book?

3. What is a markup language? What does it mean to "mark up" text?

4. What are HTML tags? Give TWO properties of tags.

5. What is the difference between an opening tag and a closing tag? Show an example of each.

6. What does the `<h1>` tag do? Write the HTML code to display the heading "My First Web Page".

7. What is the role of a browser? How does it relate to HTML?

8. Why is it said that "all web pages are built with HTML"? What does this mean for your ability to learn web development?
