---
title: Browsers
---

# Browsers

## What is a Web Browser?

A **web browser** is a software application that allows you to access, retrieve, and display content from the World Wide Web. When you type a web address or click a link, your browser goes and fetches the content from a server and then displays it on your screen in a readable format.

:::tip Key Term
**Web Browser:** A software program that retrieves web pages from the internet and displays them on your screen. Examples include Google Chrome, Mozilla Firefox, Microsoft Edge, and Safari.
:::

Without a browser, you would see raw HTML code — a jumble of tags and text that means nothing to most people. The browser's job is to interpret that code and turn it into the beautiful, interactive pages you are used to seeing.

---

## Popular Web Browsers

There are many web browsers available, but a handful dominate the market. Here is an overview of the major ones:

### Google Chrome
Released in 2008 by Google, Chrome is the most popular browser in the world by a large margin. It is fast, has a huge library of extensions, and is tightly integrated with Google services like Gmail, Drive, and Search. It uses the **Blink** rendering engine.

### Mozilla Firefox
Firefox is developed by Mozilla, a non-profit organisation committed to an open internet. It is known for strong privacy features and is a favourite among developers. It uses the **Gecko** rendering engine.

### Microsoft Edge
Edge is Microsoft's modern browser, built into Windows 10 and 11. It replaced the old Internet Explorer and is now based on the same Chromium code as Chrome, so it uses the **Blink** engine. It has useful features like a built-in PDF reader and reading mode.

### Apple Safari
Safari is the default browser on iPhones, iPads, and Mac computers. It is optimised for Apple hardware and is known for being fast and energy-efficient on Apple devices. It uses the **WebKit** rendering engine. Safari is not available on Windows or Android.

### Opera
Opera is a long-running browser known for innovation. It introduced features like tabbed browsing and speed dial (now common in all browsers). It includes a built-in VPN and ad blocker. Opera uses the **Blink** engine.

### Brave
Brave is a newer browser focused heavily on privacy. It automatically blocks ads and trackers, which makes it fast and protects your privacy. Like Chrome and Edge, it is based on Chromium and uses the **Blink** engine.

---

## Browser Market Share

| Browser | Approximate Global Share (2024) | Rendering Engine | Made By |
|---------|--------------------------------|-----------------|---------|
| Chrome | ~65% | Blink | Google |
| Safari | ~19% | WebKit | Apple |
| Edge | ~5% | Blink | Microsoft |
| Firefox | ~3% | Gecko | Mozilla |
| Opera | ~2% | Blink | Opera Software |
| Brave | ~1% | Blink | Brave Software |
| Other | ~5% | Various | Various |

:::info Why Does Market Share Matter?
When web developers build websites, they need to test their sites in multiple browsers to make sure everything works correctly. A browser with a large market share must absolutely be supported — if your site breaks in Chrome, 65% of your visitors will have a bad experience.
:::

---

## How a Browser Works

When you type a URL into the address bar and press Enter, a lot happens very quickly. Here is the process, step by step:

### Step 1: You Enter a URL
You type `www.example.com` into the address bar (or click a link). The browser parses the URL to understand what you are asking for.

### Step 2: DNS Lookup
Your browser does not know where `www.example.com` actually is — it only knows domain names. So it contacts a **DNS (Domain Name System) server** to look up the **IP address** that corresponds to that domain name. Think of DNS as the internet's phone book.

### Step 3: The Browser Sends a Request
Once it has the IP address, the browser sends an **HTTP or HTTPS request** to the server at that address. This request says, in effect: "Please send me the web page at this URL."

### Step 4: The Server Responds
The web server receives the request and sends back the files needed to display the page: mainly an **HTML file**, plus links to any **CSS stylesheets** and **JavaScript files** the page needs.

### Step 5: The Browser Renders the Page
This is where the browser really earns its keep. It reads the HTML and builds the page structure. It downloads and applies the CSS styles. It downloads and runs the JavaScript. It fetches any images and other media. All of this happens simultaneously and very quickly.

### Step 6: The Page Appears on Screen
The finished, fully rendered page appears on your screen, usually within a second or two (depending on your internet speed and the complexity of the page).

:::info What is "Rendering"?
**Rendering** is the process of turning the raw code files (HTML, CSS, JavaScript) into the visual page you see. The browser builds an internal model of the page called the **DOM (Document Object Model)** and uses it to paint pixels on your screen.
:::

---

## Parts of a Browser

Modern browsers have several key components that you interact with every day:

### Address Bar (Omnibox)
The bar at the top where you type URLs or search queries. In Chrome and Edge, it is called the **omnibox** because it also works as a search bar.

### Tabs
Tabs allow you to have multiple web pages open at once in a single browser window. You can switch between them by clicking on them at the top of the window.

### Bookmarks / Favourites
Bookmarks let you save the addresses of websites you visit frequently so you do not have to type them each time. Most browsers let you organise bookmarks into folders.

### History
Your browser keeps a record of every website you have visited. You can access it to find a page you visited recently but forgot to bookmark. You can also clear your history for privacy.

### Extensions / Add-ons
Extensions (also called add-ons or plug-ins) are small programs that add extra features to your browser. Examples include ad blockers, password managers, grammar checkers, and more.

### Developer Tools
Most browsers include powerful built-in tools for web developers. You can open them by pressing **F12** or right-clicking on any page and selecting "Inspect" or "Inspect Element". These tools let you see the HTML and CSS of any web page, monitor network traffic, and debug JavaScript.

---

## Rendering Engines

Behind the scenes, every browser has a **rendering engine** — the core software that interprets HTML and CSS and turns it into what you see on screen.

:::tip Key Term
**Rendering Engine:** The part of a browser that interprets HTML and CSS code and converts it into the visual display on your screen.
:::

| Engine | Used By | Made By |
|--------|---------|---------|
| **Blink** | Chrome, Edge, Opera, Brave, most Android browsers | Google (forked from WebKit) |
| **Gecko** | Firefox | Mozilla |
| **WebKit** | Safari | Apple |

Because Blink is used by so many browsers, a web page that works in Chrome will almost certainly work in Edge, Opera, and Brave too. Firefox (Gecko) and Safari (WebKit) can sometimes display pages slightly differently, which is why developers test in multiple browsers.

:::info Why Are There Different Rendering Engines?
Each engine was developed independently with different priorities. WebKit was developed for Apple devices. Gecko was developed to be open-source and standards-compliant. Blink started as a fork of WebKit developed by Google. Having multiple engines is good for the web because it prevents any one company from controlling how web standards are implemented.
:::

---

## Browser Settings

You can customise your browser in many ways through its settings menu:

- **Homepage:** The page that loads when you first open the browser
- **Default Search Engine:** Which search engine is used when you type in the address bar (Google, Bing, DuckDuckGo, etc.)
- **Cookies:** Small data files stored by websites — you can manage these in settings
- **Privacy Mode:** A special browsing mode that does not save history or cookies
- **Notifications:** Which websites are allowed to send you pop-up notifications
- **Permissions:** Camera, microphone, location — which sites can access these

---

## Browser Privacy and Security

### Private / Incognito Mode
Most browsers have a "private" or "incognito" mode (activated with **Ctrl+Shift+N** in Chrome or Edge, **Ctrl+Shift+P** in Firefox). When you browse in this mode:

**What incognito DOES:**
- Does not save your browsing history on your device
- Does not save cookies after the window is closed
- Does not save form data or passwords
- Opens without any of your existing cookies or login sessions

**What incognito DOES NOT do:**
- Hide your activity from your ISP (they can still see what you visit)
- Hide your activity from websites (they can still see your IP address)
- Hide your activity from your school or employer if they monitor the network
- Make you anonymous on the internet

:::warning Common Misconception
Many people think incognito mode makes them invisible or anonymous online. **It does not.** Incognito only prevents your browser from saving a local record on your device. Your ISP, your network administrator, and the websites you visit can still see what you are doing.
:::

### Browser Fingerprinting
Even without cookies, websites can identify you using a technique called **browser fingerprinting**. Your browser sends information about your system to every website you visit — your screen resolution, installed fonts, browser version, operating system, and more. This combination of details is often unique enough to identify you, even in private mode.

---

## Browser Extensions: Useful and Risky

Extensions can be very useful:
- **uBlock Origin:** Blocks ads and trackers
- **Bitwarden / LastPass:** Password managers
- **Grammarly:** Grammar and spell checking
- **Google Translate:** Translate web pages
- **Dark Reader:** Makes websites dark mode

However, extensions carry risks:
- They can access everything you do in the browser, including passwords and payment details
- Malicious extensions have been used to steal data
- Extensions can slow down your browser

:::warning Extension Safety Rules
1. Only install extensions from the official browser store (Chrome Web Store, Firefox Add-ons)
2. Check the permissions an extension requests — does a notes extension really need to read all your browsing data?
3. Only install extensions from developers you trust
4. Regularly review and remove extensions you no longer use
:::

---

## Cookies

A **cookie** is a small text file that a website saves to your computer through your browser. Cookies are used to remember information about you.

:::tip Key Term
**Cookie:** A small file stored in your browser by a website, used to remember information such as your login status, preferences, or shopping cart contents.
:::

### Types of Cookies

**Session Cookies:**
These exist only while your browser is open. They are deleted automatically when you close the browser. They are used for things like keeping you logged in while you browse a site or maintaining a shopping cart.

**Persistent Cookies:**
These are saved to your device and remain after you close the browser. They are used to remember your preferences (like language or dark mode), keep you logged in across sessions ("Remember me"), and track your browsing habits across multiple sessions.

**Third-Party Cookies:**
These are set by domains other than the one you are visiting — mainly used by advertisers to track your behaviour across many different websites. Many browsers are phasing out third-party cookies due to privacy concerns.

:::info Why Do Websites Ask About Cookies?
Under South Africa's **Protection of Personal Information Act (POPIA)** and Europe's **GDPR**, websites are legally required to inform users about cookies and obtain consent before storing tracking cookies. This is why almost every website now shows a cookie consent banner.
:::

---

## Caching

**Caching** is the process of saving copies of files locally so they do not have to be downloaded again.

:::tip Key Term
**Cache:** A temporary storage area where the browser saves copies of web page files (images, CSS, JavaScript) so they load faster on subsequent visits.
:::

When you visit a website for the first time, your browser downloads all the files needed to display it — HTML, CSS, JavaScript, images, etc. When you visit the same page again, the browser checks its cache. If it has a saved copy of a file that has not changed, it uses the local copy instead of downloading it again. This makes pages load much faster.

### Why Clear Your Cache?
Sometimes the cached version of a page is outdated — the website has been updated but your browser is showing you the old version. Clearing the cache forces the browser to download fresh copies of everything.

You can clear your browser's cache in the settings menu, or use **Ctrl+Shift+Delete** in most browsers to open the clear browsing data panel.

---

## Check Your Understanding

1. In your own words, explain what a web browser does. Why do we need a browser — what would happen without one?

2. Name FOUR popular web browsers. For each one, state the company that makes it and the rendering engine it uses.

3. According to the market share table, which browser is the most popular? What percentage of internet users use it?

4. Describe what happens when you type a URL into your browser and press Enter. Include at least FOUR steps in your answer.

5. What is a rendering engine? Name the three main rendering engines discussed in this chapter.

6. What does "private" or "incognito" mode do? List TWO things it does and TWO things it does NOT do.

7. Explain what a cookie is. What is the difference between a session cookie and a persistent cookie?

8. What is browser caching? Explain why it makes websites load faster, and in what situation you might want to clear your cache.

9. Give ONE example of a useful browser extension and explain what it does.

10. Why can browser extensions be risky? What precautions should you take before installing an extension?

11. **Critical thinking:** Safari holds about 19% of the global browser market — yet among iPhone users, its share is much higher (nearly 90%). Why do you think this is? What does this suggest about how device makers influence software choices?

12. **Practical task:** Open your browser and press F12 (or right-click and choose "Inspect"). What do you see? Can you identify where the HTML code for the page is shown? Write a brief description of what the developer tools panel looks like.
