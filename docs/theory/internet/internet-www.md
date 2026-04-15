# Internet & the World Wide Web

The internet and the web are not the same thing. The internet is the infrastructure — billions of computers connected by cables, fibre, and wireless links. The web is one service that runs on top of it. Understanding both is core Paper 2 knowledge.

> [!NOTE] Grade 10+
> Internet basics (IP, domain names, ISPs, WWW) are introduced in Grade 10. Web evolution (1.0/2.0/3.0), HTML, and internet services extend into Grade 11 and 12.

---

## Internet vs World Wide Web

| | Internet | World Wide Web |
|---|---|---|
| **Definition** | Global network of interconnected computers | System of web pages and resources accessible via the internet using HTTP/HTTPS |
| **Type** | Physical + logical infrastructure | A service/application that runs ON the internet |
| **Protocol** | TCP/IP | HTTP / HTTPS |
| **Access** | Many services (email, FTP, streaming, gaming) | Web pages viewed in browsers |
| **Invented** | 1969 (ARPANET) | 1991 (Tim Berners-Lee) |

> The internet is the road. The web is one of many vehicles on it.  
> Other "vehicles" (services on the internet): email, FTP, VoIP, online gaming, cloud storage.

---

## How the Internet Works

### IP Addresses

Every device on the internet has an **IP address** — a unique numerical label that identifies it.

**IPv4:** 32-bit address — written as four groups of numbers 0–255  
Example: `196.22.145.100`  
Total addresses: ~4.3 billion (running out)

**IPv6:** 128-bit address — written in hexadecimal groups  
Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`  
Total addresses: 340 undecillion (essentially unlimited)

### Domain Names

IP addresses are hard to remember. **Domain names** are human-readable addresses:

```
www.google.com
 |      |    |
www   google  com
|       |      |
subdomain  domain  TLD
```

**TLD = Top Level Domain:**

| TLD | Use |
|---|---|
| `.com` | Commercial organisations |
| `.org` | Non-profit organisations |
| `.gov` | Government |
| `.edu` / `.ac` | Educational institutions |
| `.co.za` | South African commercial |
| `.za` | South Africa (country code) |
| `.net` | Network services |

### DNS Resolution

When you type `www.school.co.za`:
1. Your device checks its local **DNS cache**
2. Asks your router → ISP's DNS server
3. DNS server returns the IP address: `196.22.145.100`
4. Your browser connects to that IP address

### ISP — Internet Service Provider

An **ISP** is a company that provides internet access — Telkom, Vodacom, MTN, Afrihost, etc.

The ISP:
- Connects your network to the internet backbone
- Assigns IP addresses (via DHCP)
- Provides DNS servers
- Manages your bandwidth

---

## Web Technologies

### URL — Uniform Resource Locator

A URL is the complete address of a resource on the web:

```
https://www.school.co.za:443/it/notes.html?topic=binary#section1
  |         |            |    |      |           |          |
protocol  domain       port  path  file       query     anchor
```

| Part | Example | Purpose |
|---|---|---|
| Protocol | `https://` | How to retrieve the resource |
| Domain | `www.school.co.za` | Which server |
| Port | `:443` | Which service on the server (optional — defaults apply) |
| Path | `/it/` | Folder/directory on the server |
| File | `notes.html` | Specific resource |
| Query | `?topic=binary` | Parameters passed to the server |
| Anchor | `#section1` | Jump to section within the page |

### Web Browser

A **web browser** is the application that retrieves and displays web content:
- Google Chrome, Firefox, Safari, Microsoft Edge
- Interprets HTML, CSS, JavaScript
- Communicates using HTTP/HTTPS

### Web Server

A **web server** is a computer that stores and serves web pages:
- Runs server software (Apache, Nginx, IIS)
- Listens on port 80 (HTTP) or 443 (HTTPS)
- Receives browser requests and returns HTML/CSS/JS files

---

## Web Evolution

> [!TIP] Grade 11 — Extension
> Web 1.0/2.0/3.0 classification extended in Grade 11.

### Web 1.0 — Read Only (mid-1990s – early 2000s)

- Static HTML pages
- Content created only by website owners
- No user interaction or accounts
- Users read but don't contribute
- Examples: first business websites, early news sites

### Web 2.0 — Read-Write (2004 – present)

- Dynamic, interactive content
- User-generated content
- Social media, comments, wikis, sharing
- Examples: Facebook, YouTube, Wikipedia, Twitter, Google Docs

**Key features:**
- AJAX (update parts of page without full reload)
- APIs (applications communicate with each other)
- Blogs, podcasts, user reviews
- Cloud computing

### Web 3.0 — Semantic Web (emerging)

- Intelligent, personalised, context-aware content
- Machine-readable data — computers understand meaning, not just words
- Decentralised (blockchain-based)
- Personalised search based on understanding your context and preferences
- Examples: AI assistants, personalised recommendations, IoT integration

---

## Static vs Dynamic Websites

| | Static | Dynamic |
|---|---|---|
| **Content** | Fixed HTML files — same for everyone | Generated per request — customised per user |
| **Server** | Just serves files | Runs server-side code (PHP, Python, Node.js) |
| **Database** | Not used | Usually used |
| **Update** | Developer edits HTML files | CMS or user input changes database |
| **Examples** | Simple brochure sites | Facebook, Gmail, online banking |

---

## Intranet vs Extranet vs Internet

| | Intranet | Extranet | Internet |
|---|---|---|---|
| **Who can access** | Internal users only | Authorised external parties | Anyone |
| **Security** | Inside company firewall | Controlled external access | Public |
| **Example** | Company internal portal | Supplier order system | www |

---

## Cloud Computing

> [!IMPORTANT] Grade 12 — Mastery
> Cloud computing and online services are a Grade 12 focus.

**Cloud computing** = accessing computing resources (storage, software, processing) over the internet instead of locally.

**Service models:**

| Model | What you get | Example |
|---|---|---|
| **IaaS** (Infrastructure as a Service) | Rent hardware — virtual servers, storage | Amazon AWS, Microsoft Azure |
| **PaaS** (Platform as a Service) | Rent a development platform | Google App Engine |
| **SaaS** (Software as a Service) | Rent software — pay per use | Microsoft 365, Google Workspace, Netflix |

**Advantages of cloud:**
- Access from any device, anywhere
- Automatic backups and updates
- Scale up/down without hardware purchases
- Pay only for what you use

**Disadvantages of cloud:**
- Requires internet connectivity
- Data security and privacy concerns
- Ongoing subscription costs
- Vendor lock-in (dependency on one provider)

---

## Key Terms

| Term | Definition |
|---|---|
| **Internet** | Global network of interconnected computers |
| **WWW** | World Wide Web — web pages accessible via HTTP/HTTPS |
| **IP address** | Unique numerical identifier for a device on a network |
| **IPv4/IPv6** | Version 4 (32-bit) / Version 6 (128-bit) IP address formats |
| **Domain name** | Human-readable address (www.google.com) |
| **TLD** | Top Level Domain — the last part of a domain (.com, .za) |
| **DNS** | System translating domain names to IP addresses |
| **URL** | Full address of a resource on the web |
| **ISP** | Internet Service Provider — company providing internet access |
| **Browser** | Application that retrieves and displays web content |
| **Web server** | Computer storing and serving web pages |
| **Static website** | Fixed HTML — same for all visitors |
| **Dynamic website** | Server-generated — customised per user/request |
| **Cloud computing** | Computing resources delivered over the internet |
| **SaaS** | Software as a Service — software accessed via internet |
| **Web 2.0** | Interactive, user-generated content web |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Explain the difference between the Internet and the World Wide Web"** — internet = infrastructure; web = service running on internet using HTTP to access web pages
>
> 2. **"What is an IP address? What is the purpose of DNS?"** — unique device identifier; DNS translates domain names to IP addresses
>
> 3. **"Explain the difference between Web 1.0 and Web 2.0"** — 1.0 = static, read-only; 2.0 = interactive, user-generated content, social media
>
> 4. **"Give TWO advantages of cloud computing"** — access anywhere, automatic backups, scalable, no hardware to buy/maintain
>
> 5. **"What is the difference between an intranet and the internet?"** — intranet: private internal network; internet: public global network
