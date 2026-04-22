---
layout: page
title: The Internet
parent: What is the Web? - Web Design
grand_parent: Grade 9 Digital Technology
nav_order: 2
---

# The Internet
{: .text-blue-200 }

Explore the incredible global network that makes websites, communication, and digital collaboration possible.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Define what the Internet is and explain its core principles
- Understand how data travels across networks from point A to point B
- Analyze the impact of the Internet on communication, business, and society
- Recognize both the benefits and challenges of global connectivity
- Explain why open protocols and accessibility are important for the Internet

---

## 🌐 What is the Internet?

### 🤔 Big Questions to Consider:
- **What is the Internet?**
- **Why is it important?**
- **How has it changed our world?**

### 📡 Core Definition

The Internet is fundamentally **three things**:

#### 🧠 A Philosophy
**Making information and knowledge open and accessible to ALL**
- Based on the principle that information should be freely shared
- Designed to connect people regardless of location, background, or resources
- Built on the idea that collaboration and open access benefit everyone

#### 🔗 A Network of Networks
**A massive interconnected system of smaller networks**
- Not owned by any single organization or government
- Made up of thousands of individual networks connected together
- Allows any device on any network to communicate with devices on other networks

#### 📋 Built on Open Protocols
**Agreed-upon standards that allow different systems to work together**
- Common "languages" that all Internet-connected devices understand
- Open standards that anyone can use and improve
- Protocols like HTTP, TCP/IP, and others that make communication possible

{: .key-concept }
**Essential Idea**: The Internet enables **any machine to communicate with any other machine**, and therefore **any human to communicate with any other human**, anywhere in the world.

---

## 📊 The Internet by the Numbers (2023)

Understanding the massive scale and impact of the Internet:

### 🌍 Global Internet Usage
- **5.16 billion total Internet users** worldwide
- **64.4% of the world's population** uses the Internet
- **+1.9% growth** year-over-year (+98 million new users)
- **6 hours 37 minutes** average daily time spent online per user

### 📱 How People Access the Internet
- **92.3% access via mobile devices** (smartphones, tablets)
- **65.6% access via computers and tablets**
- Mobile has become the primary way people connect to the Internet

### 👥 Demographics
- **61.6% of Internet users are female**
- **67.2% of Internet users are male**
- **78.3% of urban populations** use the Internet
- **45.8% of rural populations** use the Internet

{: .impact }
**Think about it**: Over 5 billion people are connected to the same global network - that's unprecedented in human history!

---

## 🔧 How the Internet Actually Works

### 🧠 Protocols: The Universal Language

#### 📋 What is a Protocol?
A **protocol** is a widely agreed-upon set of rules that standardize communication between machines.

#### 💻 Binary Foundation
- **Computers represent all information using binary** - everything is built up using 0s and 1s
- Example: `110100` might represent the letter "A", while `110101` represents "B"
- **A protocol is adopted** to ensure that all computers interpret the 0s and 1s in the same way

#### 🌐 Internet Protocols
The Internet lays out a series of protocols that **ALL devices connected to the Internet must adopt**.
That way ALL devices can communicate, no matter what type or when it was made.

{: .key-concept }
**Universal Communication**: Because everyone follows the same protocols, a smartphone made in 2025 can communicate with a server built in 2010, and they'll understand each other perfectly!

### 🔌 The Internet is a Wire

Contrary to popular belief about "the cloud," **the Internet is literally physical infrastructure**:

#### 🌍 Physical Infrastructure
- **In the ground**: Fiber optic cables run under streets and across continents
- **In the oceans**: Massive underwater cables span the entire globe
- **Not in the cloud**: It's actual, physical wires and cables everywhere

#### ⚡ Different Ways to Send Information

The Internet uses various methods to transmit data as 0s and 1s:

**Electrical Signals:**
- **High voltage = 1**
- **Low voltage = 0**

**Light Signals (Fiber Optic):**
- **Light on = 1**
- **Light off = 0**

**Radio Waves (Wireless):**
- **Short wave = 1**
- **Long wave = 0**

{: .innovation }
**Continuous Innovation**: We are continually finding better and better ways to send information, but the layout of the information remains the same! Every computer uses the same protocols.

### 🔗 From Simple to Complex Networks

#### 🏠 Simple Networks: The Scalability Problem

**What is a Network?**
A group of 2 or more computer systems linked together.

**The Problem with Direct Connections:**
If you tried to connect every computer directly to every other computer:
- With just 4 computers, you need 6 cables
- With 8 computers, you need 28 cables
- With 100 computers, you need 4,950 cables!

**Result: NOT SCALABLE!**

#### 🔄 Network Solutions: Switches

**The Switch Solution:**
Instead of connecting every computer to every other computer, connect them all to a central **"Switch"**:
- All computers connect to one central device
- The switch routes messages between computers
- Much more efficient and manageable

#### 🌐 Complex Networks: Routers

**Connecting Networks Together:**
To connect multiple networks (each with their own switches), we use **"Routers"**:
- Routers connect different networks together
- They figure out the best path for data to travel
- They can handle communication between networks in different locations

**The Problem of Scale:**
Even with routers, connecting every network to every other network becomes "Too much!" - not practical for global scale.

#### 🌍 The Internet: Network of Networks

**The Solution: The Internet**
The Internet solves the scalability problem by creating **a network connecting individual networks**:
- Local networks connect to regional networks
- Regional networks connect to national networks
- National networks connect to international networks
- This creates a hierarchical structure that can scale globally

### 📍 Internet Addresses: Finding Destinations

#### 🏠 IP Addresses
**Every device on the Internet has a unique address**, called an **Internet Protocol (IP) address**.

**Examples of IP addresses:**
- `192.168.1.1` (your home router)
- `8.8.8.8` (Google's DNS server)
- `172.217.16.142` (might be Google's main website)

**How it works:**
Information is sent to and from these unique addresses, like postal addresses for digital communication.

#### 🖥️ Servers
**Websites are hosted on servers** - special computers that:
- **Sit at particular IP addresses** on the Internet
- **Listen for requests** from browsers and other clients
- **Respond with HTML/CSS code** that makes up the requested website

**Example:**
- CodeHS might be hosted at `122.21.44.100`
- Wikipedia might be hosted at `45.56.232.100`

#### 🌐 Domain Names: Human-Friendly Addresses

**The Problem:** IP addresses like `122.21.44.100` are hard for humans to remember.

**The Solution:** **Domain names** let you register a nice, readable name to associate with your IP address:
- `codehs.com` → `122.21.44.100`
- `wikipedia.org` → `45.56.232.100`

When you type `google.com`, your computer automatically looks up the IP address and connects to the right server.

### 📦 Sending and Receiving Information: Packets

#### 🎁 Breaking Information into Packets

**Information is broken down into manageable pieces** when sent through the Internet. These pieces are called **packets**.

**Why use packets?**
- Large files are too big to send all at once
- Networks can be more efficient with smaller pieces
- If one packet gets lost, only that piece needs to be resent

#### 🛤️ Packet Journey

**Amazing Packet Behavior:**
When you request a website from `codehs.com` (`122.21.44.100`), here's what happens:

1. **Your request is broken into packets**
2. **Each packet is labeled:** 
   - `To: 122.21.44.100` (codehs.com)
   - `From: 5.2.6.2` (your computer)

3. **Packets take different paths** through the network of routers
4. **Packets can arrive at different times**, even out of order
5. **Packets are reassembled** at the destination to recreate the original message

#### 🗺️ Multiple Routes

**Network Resilience:**
The beauty of packet switching is that:
- **Multiple paths exist** between any two points on the Internet
- **If one route is blocked** or busy, packets automatically find another route
- **Network failures** don't stop communication - traffic just finds a different path
- **Load balancing** happens automatically as packets spread across available routes

{: .amazing-fact }
**Mind-blowing reality**: When you load a webpage, dozens of packets might travel through completely different countries, some going through undersea cables, others through satellite links, all to deliver one webpage to your screen in milliseconds!

---

## 💥 Why the Internet is Important

The Internet has **completely changed** the way we live, work, and interact:

### 💬 Communication Revolution
- **Instant messaging** across any distance
- **Video calls** connecting families and friends globally
- **Social media** creating new forms of community
- **Email** replacing traditional mail for most purposes

### 📚 Access to Information
- **Search engines** putting all human knowledge at our fingertips
- **Online education** making learning accessible to anyone
- **Real-time news** from around the world
- **Research databases** available to students and professionals

### 🗺️ Navigation and Location Services
- **GPS and mapping** helping people find their way
- **Real-time traffic** information improving travel
- **Location-based services** connecting people to nearby resources

### 🤝 Global Collaboration
- **Remote work** enabling people to work from anywhere
- **Collaborative tools** allowing teams to work together across distances
- **Open source projects** where people worldwide contribute to shared goals
- **Crowdsourcing** solutions to complex problems

### 💼 Business Transformation
- **E-commerce** enabling global marketplaces
- **Digital marketing** reaching targeted audiences
- **Online banking** and financial services
- **Supply chain management** coordinating global operations

### 🎮 Entertainment and Media
- **Streaming services** for music, movies, and games
- **User-generated content** platforms
- **Online gaming** connecting players worldwide
- **Digital art and creativity** platforms

---

## 🤔 Personal Reflection: How Has the Internet Impacted YOUR Life?

Consider these areas of your daily life:
- How do you communicate with friends and family?
- Where do you go for information when you need to learn something?
- How do you discover new music, movies, or entertainment?
- What would a typical day be like without Internet access?
- How has the Internet affected your education and learning?

---

## 🌟 Positive Impact Examples

### 🏥 Community Supported Causes
**Example: #match4lara Campaign**
- Used social media to **diversify the bone marrow registry**
- Connected people globally to support a specific medical need
- Demonstrated how the Internet can mobilize communities for social good
- Shows the power of **hashtag activism** and viral campaigns

### 🧬 Collaborative Problem Solving
**Example: Foldit - Citizen Science Game**
- **Online game** where players solve protein folding puzzles
- Players produced an **accurate model of an AIDS-causing virus in 10 days**
- Problem had been **unsolved by computer simulations and researchers for 15 years**
- Demonstrates how **crowdsourcing** can solve complex scientific problems

### 🛒 E-commerce Revolution
**Benefits of Online Shopping:**
- **Buy directly from retailers** without geographic limitations
- **Support small businesses** that couldn't afford physical stores
- **Find the best products at the lowest prices** through comparison shopping
- **Access global markets** rather than being limited by location
- **Customer reviews** help make informed purchasing decisions

### 💰 Crowdfunding Innovation
**Platforms like Kickstarter, Indiegogo, and Tilt enable:**
- **Community funding** for creative projects
- **Alternative to traditional banks** and investors
- **Direct connection** between creators and supporters
- **Innovation** in products and services that might not get traditional funding

---

## ⚠️ Complications and Challenges

While the Internet brings many benefits, it also creates new challenges:

### 📚 Access to Copyrighted Material
**The Challenge:**
- **Peer-to-peer networks** make it easy to share content
- **Shared content** is often not owned by the people sharing it
- **Distribution of copyrighted material** is easier than ever before

**Why This Matters:**
- **Creators lose income** when their work is shared without permission
- **Legal consequences** for people who download or share copyrighted content
- **Difficulty enforcing** copyright across global networks

{: .ethics-connection }
**Connection to Digital Citizenship**: Remember our lesson on Creative Credit & Copyright - these principles apply especially to Internet sharing!

### 🎭 Anonymity Debate
**The Dilemma:**
Should Internet users be identifiable or anonymous?

#### 🌟 Benefits of Anonymity:
- **Equality on the Internet** - users won't be discriminated against based on identity
- **Protection for whistleblowers** and people reporting wrongdoing
- **Freedom of expression** in oppressive regimes
- **Privacy protection** from corporations and governments

#### ⚠️ Risks of Anonymity:
- **Cyberbullying** becomes easier when people aren't accountable
- **Trolling and harassment** without consequences
- **Spread of misinformation** without accountability
- **Criminal activity** becomes harder to investigate

### 🚫 Censorship Concerns
**Complex Questions:**
- Should search engines display **explicit or illegal content**?
- Should governments be able to **filter what their citizens see** online?
- Who decides what content is **appropriate or inappropriate**?
- How do we balance **free speech** with **protecting people from harm**?

#### 🌍 Global Variations:
- Different countries have **different standards** for Internet content
- Some governments **block access** to certain websites or services
- **Corporate policies** also determine what content is allowed on platforms
- **Cultural differences** affect what is considered acceptable

---

## 🧠 Critical Thinking Questions

Consider these complex issues:

### 🤔 Access and Equality:
1. **Digital Divide**: How does unequal Internet access affect opportunities for education and employment?
2. **Global Perspective**: Should Internet access be considered a human right?
3. **Economic Impact**: How does the Internet affect traditional businesses and employment?

### ⚖️ Ethics and Responsibility:
1. **Information Quality**: Who is responsible for ensuring information on the Internet is accurate?
2. **Platform Responsibility**: Should social media companies be responsible for content their users post?
3. **Government Role**: What should be the role of governments in regulating Internet content?

### 🔮 Future Considerations:
1. **Emerging Technologies**: How might artificial intelligence change how we use the Internet?
2. **Privacy Evolution**: How will privacy expectations change as Internet use grows?
3. **Global Cooperation**: How can countries work together to address Internet challenges?

---

## 🔗 Connection to Web Design

Understanding the Internet helps you become a better web designer and developer:

### 🌐 Technical Understanding:
- **How websites are delivered** from servers to users' browsers
- **Why page loading speed** matters for user experience
- **How global audiences** access your websites differently

### 👥 User Considerations:
- **Accessibility** for users with different Internet speeds
- **Mobile-first design** since most users access via mobile devices
- **Cross-cultural design** for global audiences

### 📊 Data and Analytics:
- **Understanding user behavior** through web analytics
- **Optimizing websites** for different types of Internet connections
- **Responsive design** for various devices and screen sizes

---

## 📚 Key Takeaways

### 🎯 Essential Understanding:
1. **The Internet is a network of networks** that enables global communication
2. **Open protocols and standards** make the Internet accessible to everyone
3. **Data travels through multiple routes** making the Internet resilient and efficient
4. **5+ billion people** are connected, creating unprecedented opportunities for collaboration
5. **The Internet has transformed** virtually every aspect of modern life

### ⚖️ Balanced Perspective:
- **Amazing benefits** in communication, education, business, and creativity
- **Real challenges** around copyright, privacy, anonymity, and censorship
- **Ongoing evolution** as technology and society adapt to digital connectivity
- **Personal responsibility** in how we use and contribute to the Internet

### 🚀 Looking Forward:
- **Web design and development** are ways to contribute positively to the Internet
- **Digital citizenship skills** help navigate Internet challenges responsibly
- **Understanding the infrastructure** helps you build better websites
- **Global perspective** is essential for creating inclusive web experiences

---

## 🔗 Connection to Other Lessons

This lesson builds on and connects to other important concepts:

- **Digital Citizenship (Module 1)**: All those skills apply to Internet use and creation
- **Web Design & Development (2.1)**: Now you understand the platform your websites will use
- **Browsers (2.3)**: Next, we'll explore how browsers interpret and display Internet content
- **Future Programming**: Understanding networks helps you build better web applications

---

**Next Lesson**: We'll explore **Browsers** - the software applications that interpret web code and display websites on your screen, making the Internet accessible and user-friendly.

---

## 💭 Final Reflection

The Internet represents one of humanity's greatest collaborative achievements - a global network that connects billions of people and enables instant sharing of information, creativity, and resources.

As you begin learning web design and development, remember that you're not just learning technical skills - you're learning to contribute to this incredible global platform that has the power to connect, educate, and inspire people around the world.

**Your websites will become part of this amazing network. What will you create?**