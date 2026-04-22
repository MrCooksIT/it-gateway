---
layout: page
title: Viewing Websites
parent: What is the Web? - Web Design
grand_parent: Grade 9 Digital Technology
nav_order: 4
---

# Viewing Websites
{: .text-blue-200 }

Discover the incredible behind-the-scenes process that happens every time you visit a website - from typing a URL to seeing the finished page on your screen.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Explain the step-by-step process of how browsers load and display web pages
- Understand what URLs are and how they work as addresses for web resources
- Describe how HTTP requests and responses work between browsers and servers
- Recognize the speed and complexity of modern web browsing
- Analyze different types of web resources and how they're delivered

---

## 🤔 The Big Question

**We know web pages are made with HTML and CSS code...**

But how do we let the world see the web pages we make? How exactly does a browser find and display a web page?

Every time you visit a website, an amazing process happens behind the scenes in **less than a second**. Let's break it down step by step!

---

## 🗺️ Step 1: The URL (Uniform Resource Locator)

### 🌐 What is a URL?

A **URL** is like a postal address for the Internet. It tells your browser exactly where to find a specific resource online.

**Example URL:** `www.example.com/homepage.html`

{: .key-concept }
**Think of it this way**: Just like your home has an address that helps people find you, every web page has a URL that helps browsers find it on the Internet!

### 📍 How do you use a URL?

You can trigger a web page request in several ways:

#### 🖱️ Direct Entry
- **Typing it in the browser** address bar: `www.example.com`
- **Clicking on a link** on another website
- **Clicking a bookmark** you've saved
- **Refreshing a page** you're already viewing

### 🧩 Breaking Down a URL

Let's analyze: `www.example.com/homepage.html`

#### 🌍 DOMAIN: `www.example.com`
**Where on the Internet you need to look for this resource**
- This is like the "street address" of the website
- Points to a specific server somewhere in the world
- Examples: `google.com`, `wikipedia.org`, `github.com`

#### 📂 PATH: `/homepage.html`
**What specific resource you are requesting**
- This is like the "apartment number" or specific room
- Points to a particular file on that server
- Could be an HTML page, image, video, or any other file

### 📁 Different Types of Resources

URLs can point to many different types of files:

#### 🌐 **HTML Files** (`.html`)
- Web pages with structure and content
- Example: `/about.html`, `/contact.html`

#### 🖼️ **Image Files** (`.jpg`, `.png`, `.gif`)
- Photos, graphics, logos, icons
- Example: `/images/logo.png`

#### 🎬 **Video Files** (`.mp4`, `.mov`)
- Videos embedded in websites
- Example: `/videos/tutorial.mp4`

#### 🎨 **Style Files** (`.css`)
- Styling instructions for web pages
- Example: `/styles/main.css`

#### ⚡ **Script Files** (`.js`)
- Interactive functionality for websites
- Example: `/scripts/animation.js`

{: .amazing-fact }
**Every single element** you see on a webpage - text, images, videos, styling - comes from a separate URL that your browser requests!

---

## 📤 Step 2: The Request

### 🗣️ Making the Request

Once you've provided a URL, your browser sends a request to the server:

**In simple terms:** *"Hey example.com! Can you send me your homepage.html file please?"*

### 🔧 The Technical Request

Behind the scenes, your browser sends a properly formatted **HTTP request**:

```
GET /homepage.html HTTP/1.1
Host: www.example.com
Content-Type: text/html
Content-Language: en
User-Agent: Mozilla/5.0 (Browser info)
Accept: text/html,application/xml
...
```

#### 📋 What this request includes:

- **GET**: The type of request (asking for a file)
- **`/homepage.html`**: The specific file being requested
- **Host**: Which server to contact
- **Content-Type**: What kind of file is expected
- **User-Agent**: Information about your browser
- **Accept**: What file types your browser can handle

### 🌐 HTTP Protocol

**HTTP** (HyperText Transfer Protocol) is the "language" browsers and servers use to communicate:
- **Standardized format** that all browsers and servers understand
- **Request-response system** for efficient communication
- **Stateless protocol** - each request is independent
- **Foundation of the World Wide Web**

{: .technical-note }
**HTTPS** is the secure version of HTTP - the 'S' stands for 'Secure' and means the communication is encrypted!

---

## 📥 Step 3: The Response

### 🤝 Server Response

The server at `www.example.com` receives your request and responds:

**In simple terms:** *"Yeah! Here you go!"*

### 📦 What Gets Sent Back

The server sends back the requested file(s):

```html
<html>
  <head>
    <title>Welcome to Example.com</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Hello World!</h1>
    <img src="logo.png" alt="Company Logo">
    <p>Welcome to our amazing website!</p>
  </body>
</html>
```

### 🔄 Multiple Requests

Here's where it gets interesting! That single HTML file often references **many other resources**:

#### 🎯 Additional Automatic Requests:
1. **CSS file**: `styles.css` (for styling)
2. **Image file**: `logo.png` (for the logo)
3. **Font files**: Custom typography
4. **JavaScript files**: Interactive functionality
5. **More images**: Photos, icons, graphics

**Result**: Your browser automatically makes **additional requests** for each of these resources!

{: .mind-blown }
**Amazing reality**: Loading one "simple" webpage might actually involve 20-50 separate requests for different files - and your browser handles them all automatically!

---

## 🎨 Step 4: Rendering the Page

### 🔧 Browser Magic

Your browser takes all the received files and **renders** (creates) the visual web page:

#### 🏗️ The Rendering Process:

1. **Parse HTML** - Understand the page structure
2. **Request additional resources** - Images, CSS, JavaScript
3. **Parse CSS** - Understand styling instructions
4. **Build the DOM** - Create the Document Object Model
5. **Apply styles** - Make everything look right
6. **Load media** - Display images and videos
7. **Execute JavaScript** - Add interactive features
8. **Display final result** - Show you the complete webpage

### ⚡ Lightning Speed

**ALL OF THIS HAPPENS IN LESS THAN A SECOND!**

Think about what just occurred:
- Your browser contacted a server possibly thousands of miles away
- Downloaded multiple files (HTML, CSS, images, etc.)
- Interpreted and processed several programming languages
- Assembled everything into a beautiful, interactive web page
- Displayed it perfectly on your screen

{: .incredible-fact }
**Mind-blowing**: Modern browsers can handle hundreds of simultaneous requests, render complex layouts with animations, and display everything in under one second - while you're casually clicking a link!

---

## 🔍 Real-World Example Walkthrough

Let's follow a real website visit step by step:

### 📱 Scenario: Visiting a Social Media Site

**You type**: `www.instagram.com`

#### Step 1: URL Processing
- **Domain**: `www.instagram.com`
- **Path**: `/` (default homepage)
- **Your browser**: Prepares to make a request

#### Step 2: The Request
```
GET / HTTP/1.1
Host: www.instagram.com
User-Agent: Mozilla/5.0 (your browser info)
Accept: text/html,application/xml,image/*
```

#### Step 3: The Response
Instagram's server sends back:
- **HTML file**: Page structure and content
- **CSS files**: Styling for the Instagram look
- **JavaScript files**: Interactive features (like, comment, scroll)
- **Image files**: Profile pictures, posts, logos
- **Font files**: Custom Instagram typography

#### Step 4: Additional Requests
Your browser automatically requests:
- **Profile images**: Dozens of user profile pictures
- **Post images**: Photos and videos in your feed
- **Advertising content**: Sponsored posts and ads
- **API data**: Latest posts, comments, notifications

#### Step 5: Rendering
- **Layout calculation**: Positioning all elements
- **Image optimization**: Resizing for your screen
- **Interactive features**: Scroll behavior, buttons
- **Real-time updates**: New content loading

**Total files downloaded**: 100+ different resources
**Total time**: Less than 2 seconds for everything to appear!

---

## 🌍 Different Types of Websites

Understanding how websites are built helps you recognize different types:

### 📄 Static Websites

**What they are:**
- **Fixed content** that doesn't change unless manually updated
- **Simple structure** with basic HTML and CSS
- **Fast loading** because content is pre-made

**Examples:**
- Personal portfolios
- Company brochures
- Simple blogs
- Information sites

**How they work:**
1. Someone creates HTML/CSS files
2. Files are uploaded to a server
3. Browser requests and displays the exact files
4. Same content shown to everyone

### 🔄 Dynamic Websites

**What they are:**
- **Content that changes** based on user interactions
- **Database-driven** with content stored separately
- **Personalized experiences** for different users

**Examples:**
- Social media platforms (Facebook, Instagram)
- E-commerce sites (Amazon, eBay)
- News websites with constantly updating content
- Online banking and account management

**How they work:**
1. Browser makes a request
2. Server runs programs to generate HTML
3. Content is pulled from databases
4. Custom page is created and sent to browser
5. Different users see different content

### 🎮 Interactive Web Applications

**What they are:**
- **App-like experiences** running in your browser
- **Real-time functionality** with instant updates
- **Complex user interfaces** with advanced features

**Examples:**
- Google Docs (collaborative document editing)
- Spotify Web Player (music streaming)
- Online games
- Video conferencing (Zoom, Google Meet)

**How they work:**
1. Initial page load brings the "app shell"
2. JavaScript takes over for app-like behavior
3. Continuous communication with servers
4. Real-time updates without page refreshes
5. Complex data synchronization

---

## 🚀 Website Performance Factors

Understanding how websites load helps you appreciate good web design:

### ⚡ What Makes Websites Load Fast?

#### 🗜️ Optimized Images
- **Compressed file sizes** without losing quality
- **Appropriate dimensions** for different devices
- **Modern formats** like WebP for better compression

#### 🎯 Efficient Code
- **Clean HTML** with proper structure
- **Optimized CSS** without unnecessary styles
- **Compressed JavaScript** for faster downloads

#### 🌍 Content Delivery Networks (CDNs)
- **Servers around the world** hosting copies of website files
- **Automatic routing** to the closest server
- **Faster delivery** regardless of user location

#### 📱 Responsive Design
- **Adaptive layouts** that work on any device
- **Mobile-first approach** for faster mobile loading
- **Progressive enhancement** for different capabilities

### 🐌 What Makes Websites Load Slowly?

#### 📸 Large, Unoptimized Images
- **Huge file sizes** taking forever to download
- **Too many images** loading at once
- **Wrong formats** for the content type

#### 💻 Poor Code Quality
- **Bloated HTML** with unnecessary elements
- **Inefficient CSS** with redundant styles
- **Heavy JavaScript** that blocks page rendering

#### 🌐 Bad Hosting
- **Slow servers** that take time to respond
- **Poor network infrastructure** causing delays
- **No content optimization** for faster delivery

{: .performance-tip }
**For web designers**: Always optimize your images, write clean code, and test your websites on different connection speeds!

---

## 🔐 Security and Privacy Considerations

When viewing websites, several security processes happen automatically:

### 🛡️ HTTPS Encryption

**What it does:**
- **Encrypts communication** between browser and server
- **Verifies server identity** to prevent impersonation
- **Protects sensitive data** like passwords and personal info

**How to recognize it:**
- **Lock icon** in the browser address bar
- **`https://`** instead of `http://`
- **Green indicators** in some browsers

### 🍪 Cookies and Tracking

**What happens:**
- **Websites store small files** (cookies) on your computer
- **Track your preferences** and login status
- **Remember your settings** for future visits
- **May track behavior** across multiple websites

**Privacy considerations:**
- **Some tracking is helpful** (remembering login)
- **Some tracking is invasive** (advertising profiles)
- **You can control cookies** in browser settings
- **Privacy laws** now require cookie consent notices

### 🔍 Data Collection

**What websites might collect:**
- **Pages you visit** and time spent
- **Links you click** and content you interact with
- **Device information** like screen size and browser type
- **Location data** if you grant permission

**Your control:**
- **Browser privacy settings** to limit tracking
- **Ad blockers** to prevent advertising tracking
- **Incognito/private browsing** for temporary sessions
- **VPN services** to hide your location

---

## 💻 Browser Developer Tools: See It Yourself!

You can actually watch this entire process happen in real-time!

### 🔧 How to Access Developer Tools

**In any browser:**
- **Right-click** on a webpage and select "Inspect" or "Inspect Element"
- **Keyboard shortcut**: F12 (Windows) or Cmd+Option+I (Mac)
- **Browser menu**: Look for "Developer Tools" or "Web Developer"

### 📊 Network Tab: Watch the Requests

#### 🎯 What you'll see:
1. **Open Developer Tools** and click the "Network" tab
2. **Refresh the page** (F5 or Ctrl+R)
3. **Watch the magic happen**: Every single file request appears in real-time!

#### 📈 Information displayed:
- **File names**: Every resource being downloaded
- **File sizes**: How much data each file contains
- **Load times**: How long each file takes to download
- **Request/response details**: The technical communication

#### 🕵️ Try this experiment:
1. Visit a news website like CNN.com or BBC.com
2. Open the Network tab and refresh
3. **Count the requests**: You'll likely see 100+ files!
4. **Notice the file types**: HTML, CSS, JS, images, fonts, ads
5. **Watch the timeline**: See how requests happen in parallel

{: .hands-on }
**Hands-on learning**: Spend 10 minutes exploring different websites with the Network tab open. You'll be amazed at how complex modern websites are!

---

## 🎨 Connection to Web Design

Understanding how websites are viewed affects how you should design them:

### 👥 User Experience Considerations

#### ⚡ Performance Impact
- **Large images slow down** your website for users
- **Too many requests** can cause delays
- **Mobile users** may have slower connections
- **International users** may be far from your server

#### 📱 Device Variations
- **Different screen sizes** need responsive design
- **Various browsers** interpret code slightly differently
- **Connection speeds** vary dramatically worldwide
- **Accessibility needs** require thoughtful design

### 🛠️ Design Best Practices

#### 🎯 Optimize for Speed
- **Compress images** before using them
- **Write efficient HTML and CSS** code
- **Minimize HTTP requests** by combining files when possible
- **Test on slow connections** to ensure good user experience

#### 🌍 Design for Everyone
- **Responsive layouts** that work on all devices
- **Progressive enhancement** so basic functionality works everywhere
- **Accessibility features** for users with disabilities
- **International considerations** for global audiences

#### 🔄 Plan for Dynamic Content
- **Flexible layouts** that adapt to different content lengths
- **Loading states** to show users that content is coming
- **Error handling** when resources fail to load
- **Graceful degradation** when features aren't supported

---

## 🤔 Critical Thinking Questions

Consider these questions to deepen your understanding:

### 🌐 Technical Understanding
1. **Performance**: Why might a website load slowly on your phone but quickly on your computer?
2. **Resources**: If a webpage has 50 images, does the browser make 50 separate requests? Why or why not?
3. **Caching**: Why do websites often load faster the second time you visit them?

### 👥 User Experience
1. **Accessibility**: How might slow loading times affect users with disabilities or older devices?
2. **Global Access**: What challenges do users in developing countries face when accessing websites?
3. **Mobile First**: Why is it important to design websites that work well on mobile devices?

### 🎨 Design Implications
1. **Visual Hierarchy**: How can understanding the loading process help you design better websites?
2. **Content Strategy**: How should the technical loading process influence what content you prioritize?
3. **Progressive Enhancement**: How can you ensure your website works even if some resources fail to load?

---

## 📚 Key Takeaways

### 🎯 Essential Understanding
1. **URLs are addresses** that help browsers locate specific resources on the Internet
2. **HTTP requests and responses** enable communication between browsers and servers
3. **Modern web pages** typically involve dozens of separate file requests
4. **The entire process** happens in less than a second despite incredible complexity
5. **Different website types** (static, dynamic, interactive) work in different ways

### ⚡ Performance Awareness
- **Optimized resources** load faster and provide better user experiences
- **Multiple requests** happen automatically when loading a single webpage
- **Network conditions** greatly affect how users experience your websites
- **Browser capabilities** vary, requiring responsive and accessible design

### 🛠️ Design Implications
- **Understanding the technical process** helps you make better design decisions
- **Performance considerations** should influence your choice of images, code, and features
- **User diversity** in devices, connections, and abilities requires thoughtful design
- **Security and privacy** are built into the web browsing experience

---

## 🔗 Connection to Other Lessons

This lesson connects everything you've learned:

### 🔄 Building on Previous Knowledge
- **Web Design vs Development (2.1)**: Now you understand the technical process developers optimize
- **The Internet (2.2)**: This is how your local device connects to servers worldwide
- **Browsers (2.3)**: Now you understand exactly what browsers do with the code they receive

### 🚀 Preparing for Creation
- **HTML/CSS Learning**: You'll create the files that go through this process
- **Web Hosting**: You'll learn how to make your websites available at URLs
- **Performance Optimization**: You'll learn to make your websites load quickly
- **User Experience Design**: You'll design with this technical reality in mind

---

## 💡 Looking Ahead: Your Role as a Web Creator

### 🎨 As a Web Designer
You'll create the **visual experiences** that users see after this entire technical process completes. Your design decisions directly impact:
- **How quickly** pages load for users
- **How well** websites work on different devices
- **How accessible** websites are to all users
- **How secure** user interactions remain

### 💻 As a Web Developer
You'll write the **HTML and CSS code** that travels through this process. You'll need to consider:
- **File optimization** for faster loading
- **Code efficiency** for better performance
- **Responsive design** for multiple devices
- **Error handling** when things go wrong

### 🌍 As a Digital Citizen
You'll be a more informed user of websites, understanding:
- **Why some websites** load faster than others
- **How your data** is being collected and transmitted
- **What security indicators** to look for
- **How to troubleshoot** common browsing issues

---

**Next Up**: We'll start creating our own web content with **HTML fundamentals** - writing the code that will travel through this amazing process to reach users around the world!

---

## 💭 Final Reflection

Every time you click a link or type a URL, you're triggering an incredible technological symphony. Servers respond, networks route data across continents, browsers interpret code, and pixels light up on your screen to create the web experience you see.

As you begin creating websites, remember that you're not just writing code - you're contributing to this global system that connects people, shares knowledge, and enables creativity on an unprecedented scale.

**Your websites will become part of this amazing process. What will you create to contribute to the World Wide Web?**

The web is not just technology - it's human creativity made accessible to the entire world through this incredible delivery system. You're about to become part of that creative community!