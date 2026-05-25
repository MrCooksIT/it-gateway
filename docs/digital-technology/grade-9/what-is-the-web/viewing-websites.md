---
title: Viewing Websites
---

# Viewing Websites

## Introduction

We know that web pages are made with HTML and CSS code. But how does a browser actually find and display a web page? And how do we let the world see the web pages we make? In this chapter, we will trace every step of the journey — from typing a web address to seeing the finished page on your screen.

---

## Step 1: The URL

Everything starts with a **URL** (Uniform Resource Locator). A URL is the address of a specific page or file on the internet. You enter a URL in one of three ways:

- Typing it directly into the browser's address bar
- Clicking on a link
- Refreshing a page you are already on

:::tip Key Term
**URL (Uniform Resource Locator):** The address of a specific resource on the internet. When you type a URL, you are telling the browser exactly what to go and find.
:::

A URL like `www.example.com/homepage.html` has two important parts:

| Part | Example | What it means |
|------|---------|--------------|
| **Domain** | `www.example.com` | **Where** in the internet to look for this resource |
| **Path** | `/homepage.html` | **What** resource you are requesting |

The path tells the server which specific file you want. The file could be a web page (`.html`), an image (`.jpg`), a video (`.mp4`), or any other type of file.

---

## Step 2: The Request

Once the browser knows the URL, it sends a **request** to the server.

Think of it like a phone call: the browser is saying, "Hey, example.com! Can you send me your `homepage.html` file please?"

More technically, the browser sends a message that looks something like this:

```
GET /homepage.html HTTP/1.1
Host: www.example.com
Content-Type: text/html
Content-Language: en
...
```

The key part here is **HTTP** — HyperText Transfer Protocol. HTTP is the agreed-upon protocol that browsers and servers use to communicate with each other. It defines the format of requests and responses.

The request travels through the internet (across routers and networks) until it reaches the server at `www.example.com`.

---

## Step 3: The Response

The server at `www.example.com` receives the request. If everything is in order, it responds: "Yeah! Here you go!" — and sends back the HTML file for `homepage.html`.

The response travels back through the internet to your browser.

---

## Step 4: Rendering the Page

The browser now has the HTML code. It reads through the code and **renders** the page — building the visual web page that you see on your screen.

:::info
All four of these steps — the URL, the request, the response, and rendering — happen in **less than a second**.
:::

---

## Hosting Our Own Website

Now that we understand how viewing a website works, we can understand what it means to **host** a website — to make your web pages available for the rest of the world to view.

To host a website, you need three things:

1. **Register a domain** — choose and register a name for your website (like `mysite.com`)
2. **Have a server listen for requests** — a computer that is connected to the internet and waiting to receive requests for your domain
3. **Give the server files to respond with** — the actual HTML files that the server will send to visitors (like `homepage.html`)

In this course, the first two steps are taken care of for you. **Your job is to create the files** — the HTML and CSS that make up your web pages.

---

## Summary of the Steps

| Step | What happens |
|------|-------------|
| 1. The URL | You type or click a URL — the address tells the browser what to look for and where |
| 2. The Request | The browser sends a request across the internet to the server |
| 3. The Response | The server sends back the HTML file |
| 4. Rendering | The browser reads the HTML and builds the visual web page on your screen |

---

## Check Your Understanding

1. What does URL stand for? What are the two main parts of a URL and what does each part tell the browser?

2. Describe what happens during Step 2 (The Request). What is HTTP and why is it important?

3. What does the server do when it receives a request from a browser?

4. What does "rendering" a web page mean?

5. How long does the entire process from URL to displayed page take?

6. List the three things you need to host a website. In this course, which of these are you responsible for?

7. Explain the URL `www.school.com/about.html` — what is the domain and what is the path?

8. **Extended question:** In your own words, describe the full journey of what happens when you type a web address and press Enter. Use all four steps in your answer.
