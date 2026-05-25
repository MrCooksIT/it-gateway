---
title: Viewing Websites
---

# Viewing Websites

## Introduction

Every time you visit a website, an extraordinary chain of events takes place in a fraction of a second. Data travels across continents, computers exchange coded messages using agreed rules, and your browser assembles a complex document and paints it on your screen — all before you have finished blinking. In this chapter, we will trace every step of that journey and understand the technologies that make it possible.

---

## What Happens When You Visit a Website

Let us walk through the complete sequence of events when you visit a website. We will use the example of typing `https://www.school.co.za/subjects/it?grade=9#html` into your browser.

### Step 1: You Type a URL or Click a Link

You enter the address into your browser's address bar and press Enter (or click a link on a page). Your browser immediately begins to parse (analyse) the URL to understand what you are asking for.

### Step 2: Browser Checks DNS to Get the IP Address

Your browser knows the domain name (`www.school.co.za`) but not the actual network location of the server. It contacts a **DNS (Domain Name System) server** — a specialised server that works like a phone book for the internet — and asks: "What is the IP address for `www.school.co.za`?"

The DNS server looks up the domain and replies with an IP address, such as `196.22.133.10`. Now the browser knows where to send its request.

:::info DNS Caching
To speed things up, your browser caches (remembers) DNS lookups. If you visited the same site recently, your browser may already know the IP address and can skip the DNS step. Your operating system and your router also cache DNS results.
:::

### Step 3: Browser Sends an HTTP/HTTPS Request to the Server

Using the IP address, your browser opens a connection to the web server and sends an **HTTP request**. This request contains:
- The method (usually `GET` — "please give me this page")
- The specific path and resource being requested
- Information about your browser and what types of content it can accept
- Any cookies previously set by that website

### Step 4: Server Sends Back HTML, CSS, JavaScript Files

The web server receives the request, processes it, and sends back a **response**. The first file sent is the HTML document. The browser reads this HTML and discovers that it also needs CSS files, JavaScript files, images, and other resources. It sends additional requests for each of these files.

### Step 5: Browser Renders (Builds) the Page

The browser uses all the received files to construct the page:
- It reads the **HTML** to understand the structure and content
- It applies the **CSS** to control the visual appearance
- It runs the **JavaScript** to add interactive behaviour
- It downloads and displays all **images and media**

This construction process happens in the browser's memory and is called **rendering**.

### Step 6: The Page Appears on Screen

The fully rendered page is painted onto your screen. The whole process — from pressing Enter to seeing the page — typically takes between 0.5 and 3 seconds, depending on your internet connection, the complexity of the page, and the speed of the server.

---

## URLs in Detail

A **URL (Uniform Resource Locator)** is the complete address of a specific resource on the web. It looks simple, but each part carries important meaning.

:::tip Key Term
**URL (Uniform Resource Locator):** The complete address used to locate a specific page or resource on the internet. It tells the browser exactly what to retrieve and from where.
:::

### Anatomy of a URL

Let us break down this example URL:

```
https://www.school.co.za/subjects/it?grade=9#html
```

Here is each component labelled:

| Part | Value | Meaning |
|------|-------|---------|
| **Protocol** | `https://` | The communication method to use (secure HTTP) |
| **Subdomain** | `www` | A subdivision of the main domain |
| **Domain name** | `school.co.za` | The human-readable name of the server |
| **Path** | `/subjects/it` | The specific page or folder on the server |
| **Query string** | `?grade=9` | Extra data sent to the server (after the `?`) |
| **Fragment** | `#html` | A specific section on the page (after the `#`) |

### Visual Breakdown

```
 https  ://  www  .school.co.za  /subjects/it  ?grade=9  #html
   │          │         │              │             │        │
Protocol  Subdomain  Domain         Path         Query    Fragment
                      name                       string
```

### The Protocol
The protocol tells the browser how to communicate with the server.
- `http://` — HyperText Transfer Protocol (unencrypted)
- `https://` — HTTP Secure (encrypted with SSL/TLS)
- `ftp://` — File Transfer Protocol (for file downloads)
- `mailto:` — Opens an email client

### The Path
The path shows which specific page or file you want from the server. `/subjects/it` might correspond to a folder called `subjects` containing a file called `it.html` — or it might be a virtual path handled by the server's software.

### The Query String
After the `?`, you can pass additional parameters to the server. In `?grade=9`, the parameter name is `grade` and its value is `9`. Multiple parameters are separated by `&`: `?grade=9&subject=it`.

### The Fragment
After the `#`, the fragment tells the browser to scroll to a specific section of the page identified by an HTML `id` attribute. This part is only used by the browser — it is never sent to the server.

---

## Domain Names

A **domain name** is the human-readable address of a website (like `school.co.za`). Domain names are much easier to remember than IP addresses like `196.22.133.10`.

:::tip Key Term
**Domain Name:** A human-readable address that identifies a website. Domain names are registered and mapped to IP addresses through the Domain Name System (DNS).
:::

### Top-Level Domains (TLDs)

The last part of a domain name is called the **Top-Level Domain (TLD)**. It gives a hint about the type or origin of the website.

| TLD | Meaning | Example |
|-----|---------|---------|
| `.com` | Commercial (international) | google.com |
| `.org` | Non-profit organisations | wikipedia.org |
| `.net` | Network-related organisations | speedtest.net |
| `.edu` | Educational institutions (USA) | mit.edu |
| `.gov` | Government (USA) | nasa.gov |
| `.co.za` | Commercial companies in South Africa | takealot.co.za |
| `.gov.za` | South African government | sars.gov.za |
| `.ac.za` | Academic institutions in South Africa | uct.ac.za |
| `.school.za` | Schools in South Africa | (school websites) |
| `.io` | Originally Indian Ocean territory, now popular for tech companies | github.io |

### Subdomains
A **subdomain** is a prefix added before the main domain name, separated by a dot.
- `www.example.com` — the `www` part is a subdomain (very common, but not required)
- `mail.google.com` — Google's mail service
- `maps.google.com` — Google Maps
- `blog.example.com` — a blog section of a website

Any domain owner can create as many subdomains as they like on their own domain.

---

## DNS: The Internet's Phone Book

The **Domain Name System (DNS)** is a distributed system of servers that translates domain names into IP addresses. It is one of the most important pieces of infrastructure on the internet.

:::tip Key Term
**DNS (Domain Name System):** A global system that acts like a phone book for the internet, translating human-readable domain names (like `www.google.com`) into machine-readable IP addresses (like `142.250.80.46`).
:::

### How DNS Works

1. You type `www.google.com` in your browser
2. Your browser checks its **local DNS cache** — has it looked this up recently?
3. If not cached, it asks your operating system's cache
4. If not there, it asks your **ISP's DNS server** (or a public DNS server like Google's `8.8.8.8`)
5. The DNS server works through a hierarchy of servers to find the answer
6. The IP address is returned to your browser
7. The result is cached so future lookups are instant

The whole process takes milliseconds. You can change which DNS server your device uses — some people use public DNS servers like **Google (8.8.8.8)** or **Cloudflare (1.1.1.1)** which are sometimes faster or provide extra privacy.

---

## HTTP vs HTTPS

### HTTP
**HTTP (HyperText Transfer Protocol)** is the set of rules used to transfer web pages between servers and browsers. It was the original protocol of the web.

The problem with HTTP is that the data is sent in **plain text** — if anyone intercepts the communication between your browser and the server (for example, on a public Wi-Fi network), they can read everything: your passwords, your personal information, everything.

### HTTPS
**HTTPS (HTTP Secure)** is HTTP with an added layer of encryption. The **S** stands for **Secure**.

When you use HTTPS, your connection to the server is encrypted using a technology called **SSL/TLS (Secure Sockets Layer / Transport Layer Security)**. This means:
- All data travelling between your browser and the server is scrambled
- An interceptor cannot read your data
- Your browser verifies that you are actually talking to the real server (not a fake impersonator)

:::tip Key Term
**HTTPS:** A secure version of HTTP that encrypts all data sent between your browser and the server. Identified by `https://` in the URL and a padlock icon in the browser.
:::

### The Padlock Symbol
When you visit an HTTPS site, your browser shows a **padlock icon** in the address bar. Clicking on it shows information about the site's security certificate.

:::warning HTTPS Does Not Mean Safe Content
The padlock means the **connection** is encrypted — it does not mean the website itself is trustworthy or safe. A scam website can still have HTTPS. Always check the actual domain name, not just the padlock.
:::

### SSL/TLS Certificates
For a site to use HTTPS, its owner must obtain an **SSL/TLS certificate** from a trusted **Certificate Authority (CA)**. This certificate proves that the domain owner is who they claim to be. Certificates can be obtained for free from services like **Let's Encrypt**, or purchased for higher levels of verification.

If a site's certificate has expired or is invalid, your browser will show a warning before letting you proceed.

---

## HTTP Status Codes

When a browser requests a page, the server always sends back a **status code** indicating whether the request succeeded and why (or why not). These three-digit codes are grouped by their first digit.

:::tip Key Term
**HTTP Status Code:** A three-digit number sent by a web server in response to a browser's request, indicating whether the request was successful or describing what went wrong.
:::

### Common Status Codes

| Code | Name | Meaning |
|------|------|---------|
| **200** | OK | The request was successful — the page was found and sent |
| **301** | Moved Permanently | The page has permanently moved to a new URL |
| **302** | Found (Redirect) | The page has temporarily moved to a different URL |
| **400** | Bad Request | The browser sent a request the server could not understand |
| **401** | Unauthorised | You need to log in to access this page |
| **403** | Forbidden | You do not have permission to access this page |
| **404** | Not Found | The page does not exist at this URL |
| **500** | Internal Server Error | Something went wrong on the server |
| **503** | Service Unavailable | The server is temporarily down or overloaded |

You have certainly encountered a 404 error before — that is what you see when you click a broken link or mistype a URL. The 500 error means the server had a problem processing your request. 200 is what you want — it means everything worked.

:::info Status Code Groups
- **1xx** — Informational
- **2xx** — Success (200 OK is the most common)
- **3xx** — Redirection (browser is sent elsewhere)
- **4xx** — Client error (you did something wrong or the page does not exist)
- **5xx** — Server error (the server had a problem)
:::

---

## Web Servers

A **web server** is a computer (or software running on a computer) that stores website files and serves them to browsers that request them. Web servers are designed to:

- Run **24 hours a day, 7 days a week** without stopping
- Handle thousands or millions of requests simultaneously
- Respond to incoming HTTP/HTTPS requests from anywhere in the world
- Store and organise web files (HTML, CSS, JavaScript, images, databases)

:::tip Key Term
**Web Server:** A computer (or the software on it) that stores website files and responds to requests from browsers, sending back the files needed to display web pages.
:::

The most popular web server software includes:
- **Apache** — the most widely used, open-source, runs on Linux
- **Nginx** (pronounced "engine-X") — fast, efficient, widely used for high-traffic sites
- **IIS (Internet Information Services)** — Microsoft's web server software for Windows

A simple personal website might run on a single modest server. A site like Google or Netflix runs on **hundreds of thousands** of servers distributed across data centres on every continent.

---

## Viewing a Page's Source Code

One of the most powerful things you can do as a web student is look at the actual HTML code behind any web page. This is entirely legal and free to do — all the HTML that makes up the visible web is sent to your browser, so you already have it.

### Method 1: View Page Source
Right-click anywhere on a web page and choose **"View Page Source"** (or press **Ctrl+U** in most browsers). This opens a new tab showing the raw HTML of the page exactly as it was sent by the server.

### Method 2: Developer Tools
Press **F12** (or right-click and choose **"Inspect"** or **"Inspect Element"**). This opens the browser's developer tools panel, which shows:
- The **Elements** tab: HTML structure, with the ability to see how each element appears
- The **Network** tab: All the files downloaded to display the page
- The **Console** tab: JavaScript errors and output
- The **Sources** tab: All the files that make up the page

Developer Tools is an incredibly powerful learning resource — you can click on any element on a page and immediately see its HTML code.

:::info Learning from Real Websites
One of the best ways to learn web design and HTML is to look at how real websites are built. Use View Page Source on websites you admire and study how they are structured. Developers do this all the time.
:::

---

## Check Your Understanding

1. List the SIX steps that happen when you visit a website. Write each step in your own words.

2. Break down the following URL and explain what each part means:
   `https://blog.example.org/articles/2024?category=tech#introduction`

3. What is a domain name? What is the difference between the domain name `school.co.za` and the subdomain `www.school.co.za`?

4. What do the following TLDs indicate about a website?
   a) `.gov.za`
   b) `.ac.za`
   c) `.org`
   d) `.com`

5. Explain what DNS does. Use the analogy of a phone book in your answer.

6. What is the difference between HTTP and HTTPS? Why does HTTPS matter, especially when using public Wi-Fi?

7. You see a padlock in your browser's address bar. A friend says "That means this website is completely safe and trustworthy." Is your friend correct? Explain your answer fully.

8. Match each HTTP status code to its meaning:
   - 200, 404, 403, 500, 301
   - OK, Not Found, Forbidden, Internal Server Error, Moved Permanently

9. What is a web server? How is it different from an ordinary personal computer?

10. What is an SSL/TLS certificate? Why do websites need one to use HTTPS?

11. You click a link and see a "404 Not Found" error. Give TWO possible reasons why this might happen.

12. **Practical task:** Open your browser, visit any website, and press Ctrl+U to view the page source. Can you find the `<title>` tag? What text is in it? Can you find any links (look for `<a href=...>`)? Write down what you found.

13. **Extended question:** Explain why DNS is described as a "distributed" system. Why is it better to have thousands of DNS servers around the world rather than one central DNS server?
