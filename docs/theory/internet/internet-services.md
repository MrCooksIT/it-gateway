# Internet Services

The internet is more than just websites. Email, file transfer, streaming, voice calls, and real-time communication all run on the same network infrastructure but use different protocols and services designed for each purpose.

> [!NOTE] Grade 11
> Internet services and protocols (HTTP/S, FTP, VoIP, RSS, SEO) are Grade 11 content. Grade 12 extends with scripting and online applications.

---

## Overview of Internet Services

| Service | Protocol | Port | Purpose |
|---|---|---|---|
| Web browsing | HTTP | 80 | Transfer web pages (unencrypted) |
| Secure web browsing | HTTPS | 443 | Transfer web pages (TLS encrypted) |
| Email sending | SMTP | 25 / 587 | Send email messages |
| Email retrieval | POP3 | 110 | Download email to device |
| Email access | IMAP | 143 | Access email on server |
| File transfer | FTP | 20/21 | Transfer files between computers |
| Secure file transfer | SFTP / FTPS | 22 / 990 | Encrypted file transfer |
| Voice/video calls | VoIP | Varies | Internet-based calls |
| Domain name resolution | DNS | 53 | Convert domain names to IP addresses |
| IP address assignment | DHCP | 67/68 | Assign IP addresses automatically |
| News feeds | RSS | — | Subscribe to content updates |

---

## HTTP and HTTPS

**HTTP** (Hypertext Transfer Protocol) is the foundation of data exchange on the web. Every time you visit a website, your browser uses HTTP to request pages from the server.

### HTTP Request-Response Cycle:
```
Browser → GET /index.html HTTP/1.1 → Web Server
Web Server → 200 OK + HTML content → Browser
```

**Common HTTP status codes:**
| Code | Meaning |
|---|---|
| 200 | OK — request successful |
| 301 | Moved Permanently — redirect |
| 403 | Forbidden — no permission |
| 404 | Not Found — page doesn't exist |
| 500 | Internal Server Error |

**HTTPS** = HTTP + **TLS encryption**
- All data encrypted before sending
- Certificate verifies server identity
- Port 443 (HTTP uses port 80)

---

## FTP — File Transfer Protocol

**FTP** is used to transfer files between a client and a server over a network.

| Feature | FTP | SFTP |
|---|---|---|
| Encryption | None | Yes (SSH) |
| Port | 20 (data), 21 (control) | 22 |
| Security | Credentials sent in plaintext | Credentials encrypted |
| Use case | Legacy systems | Modern secure transfers |

**Uses:**
- Web developers uploading files to web server
- Downloading large files from servers
- Transferring files between companies

---

## DNS — Domain Name System

**DNS** translates human-readable domain names into IP addresses.

```
www.google.com → 142.250.185.78
```

### DNS Resolution Process:
1. You type `www.example.com` in browser
2. Browser checks local **DNS cache** — if not found:
3. Queries **Recursive resolver** (your ISP's DNS server)
4. Resolver queries **Root nameserver** → directs to TLD nameserver (.com, .co.za)
5. TLD nameserver directs to **Authoritative nameserver** for example.com
6. Authoritative nameserver returns the IP address
7. Browser connects to that IP address

**DNS record types:**
| Record | Purpose |
|---|---|
| A | Maps domain to IPv4 address |
| AAAA | Maps domain to IPv6 address |
| MX | Mail server for the domain |
| CNAME | Alias — one domain points to another |
| TXT | Text information (used for email security) |

---

## Search Engines and SEO

### How Search Engines Work:
1. **Crawling** — bots follow links across the web, discovering pages
2. **Indexing** — discovered pages are analysed and added to the index
3. **Ranking** — when a user searches, the algorithm ranks relevant results

**Major search engines:** Google, Bing, DuckDuckGo, Baidu

### SEO — Search Engine Optimisation

**SEO** is the process of improving a website to rank higher in search engine results pages (SERPs).

| SEO Technique | Description |
|---|---|
| **Relevant keywords** | Include search terms users actually use |
| **Page title and meta description** | Descriptive HTML tags help search engines understand content |
| **Quality content** | Original, useful, well-written content ranks better |
| **Backlinks** | Links from other reputable sites improve authority |
| **Mobile-friendly design** | Google ranks mobile-friendly sites higher |
| **Page load speed** | Faster sites rank better |
| **HTTPS** | Secure sites get a ranking boost |
| **Alt text on images** | Describes images for search engines and accessibility |

**White-hat SEO** — legitimate techniques following search engine guidelines  
**Black-hat SEO** — manipulative techniques (keyword stuffing, link farms) — penalised

---

## Cloud Services

**Cloud computing** delivers computing services over the internet — storage, software, processing.

| Model | What you get | Examples |
|---|---|---|
| **SaaS** | Ready-to-use software | Gmail, Microsoft 365, Netflix |
| **PaaS** | Development platform | Google App Engine, Heroku |
| **IaaS** | Virtual hardware | AWS, Microsoft Azure |

### Online Storage Services

| Service | Provider | Free Storage |
|---|---|---|
| Google Drive | Google | 15 GB |
| OneDrive | Microsoft | 5 GB |
| Dropbox | Dropbox | 2 GB |
| iCloud | Apple | 5 GB |

---

## Cookies

**Cookies** are small text files stored on your device by websites you visit.

**Types:**
| Type | Purpose |
|---|---|
| **Session cookie** | Temporary — expires when browser closes; keeps you logged in during visit |
| **Persistent cookie** | Stored longer — remembers preferences, login details |
| **Third-party cookie** | Set by advertisers tracking you across multiple websites |

**What cookies do:**
- Keep you logged in
- Remember shopping cart contents
- Store user preferences (language, theme)
- Track browsing behaviour for targeted advertising
- Maintain session state

**Privacy considerations:**
- GDPR (EU) and POPIA (SA) require consent before non-essential cookies
- Users can clear cookies or block third-party cookies in browser settings

---

## Streaming

**Streaming** delivers audio and video as a continuous real-time flow rather than requiring a complete download first.

| Feature | Download | Streaming |
|---|---|---|
| Wait time | Full download before playback | Starts almost immediately |
| Storage | Saves file locally | No local file (unless downloaded) |
| Internet needed during playback | No (after download) | Yes (constant) |
| Buffering | No | Yes (if connection drops) |

**Adaptive bitrate streaming:** Video quality automatically adjusts based on connection speed (YouTube, Netflix).

**Compression used in streaming:**
- Video: H.264, H.265 (HEVC), AV1
- Audio: MP3, AAC, FLAC
- Lossless vs lossy depending on content

---

## Online Applications vs Desktop Applications

| Feature | Online App (SaaS) | Desktop App |
|---|---|---|
| Installation | None — runs in browser | Must be installed |
| Updates | Automatic | Manual |
| Access | Any device with browser | Only installed devices |
| Internet required | Yes | Usually no |
| Storage | Cloud | Local |
| Examples | Google Docs, Canva | Microsoft Word, Photoshop |

---

## Key Terms

| Term | Definition |
|---|---|
| **HTTP** | Protocol for transferring web pages |
| **HTTPS** | HTTP with TLS encryption |
| **FTP** | Protocol for transferring files between computers |
| **DNS** | Translates domain names to IP addresses |
| **SEO** | Optimising a website to rank higher in search results |
| **Cookie** | Small file stored in browser recording visit/preference data |
| **Streaming** | Delivering media in real-time without full download |
| **Cloud computing** | Delivery of computing services over the internet |
| **SaaS** | Software delivered via internet (no installation) |
| **RSS** | Format for subscribing to content updates from websites |
| **Adaptive bitrate** | Streaming that adjusts quality based on connection speed |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between HTTP and HTTPS?"** — HTTP transmits data unencrypted (port 80); HTTPS uses TLS to encrypt data and verify server identity (port 443)
>
> 2. **"What is a cookie? Give TWO uses."** — small text file stored by a website; uses: keep user logged in; remember preferences; track browsing for advertising; store shopping cart
>
> 3. **"Explain what DNS does"** — translates human-readable domain names (www.google.com) into IP addresses so browsers can connect to the correct server
>
> 4. **"What is SEO? Give THREE techniques."** — Search Engine Optimisation; techniques: relevant keywords; quality content; backlinks from reputable sites; fast loading; HTTPS; mobile-friendly
>
> 5. **"Give TWO advantages of streaming over downloading"** — playback starts immediately (no wait for full download); no local storage space needed
