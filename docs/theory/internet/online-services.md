# Online Services

The internet has moved almost everything online — banking, shopping, collaboration, entertainment, and communication. Understanding what services exist, how they work, and what the trade-offs are is essential for both the theory exam and everyday digital life.

> [!NOTE] Grade 12
> Online services and applications (cloud storage, online apps, cookies, e-commerce) are primarily Grade 12 content, building on Grade 11 internet knowledge.

---

## Categories of Online Services

| Category | Description | Examples |
|---|---|---|
| **Email** | Electronic messaging | Gmail, Outlook |
| **Cloud storage** | Store and access files remotely | Google Drive, OneDrive, Dropbox |
| **Online productivity** | Web-based office tools | Google Docs, Microsoft 365 |
| **E-commerce** | Online shopping and payments | Amazon, Takealot, Woolworths |
| **Social media** | Share content, communicate | Facebook, Instagram, X |
| **Streaming** | Audio and video on demand | Netflix, YouTube, Spotify |
| **Online banking** | Manage finances online | FNB, Nedbank, Capitec |
| **Search engines** | Find information | Google, Bing |
| **Online learning** | Educational platforms | Khan Academy, Coursera |
| **Video conferencing** | Real-time video calls | Zoom, Teams, Google Meet |

---

## Cloud Storage

**Cloud storage** saves files on remote servers, accessible from any internet-connected device.

| Service | Provider | Free Storage |
|---|---|---|
| Google Drive | Google | 15 GB |
| OneDrive | Microsoft | 5 GB |
| Dropbox | Dropbox | 2 GB |
| iCloud | Apple | 5 GB |
| Amazon Drive | Amazon | 5 GB |

**Advantages of cloud storage:**
- Access files from any device, anywhere
- Automatic backup — files safe if device stolen/damaged
- Easy sharing and collaboration
- Scales — pay for more storage as needed
- No hardware to buy or maintain

**Disadvantages:**
- Internet required for access
- Ongoing subscription cost for large storage
- Privacy concerns — third party holds your data
- Vendor lock-in — difficult to switch providers
- Data sovereignty — your data may be stored in another country

---

## Online Applications vs Desktop Applications

| Feature | Online App (SaaS) | Desktop App |
|---|---|---|
| Installation | None — runs in browser | Must install on device |
| Updates | Automatic — always latest version | Manual or prompted |
| Access | Any device with browser | Only devices where installed |
| Internet required | Yes | Usually no |
| Storage | Cloud | Local |
| Collaboration | Real-time multi-user editing | Usually not |
| Offline use | Limited | Full |
| Examples | Google Docs, Canva, Figma | Microsoft Word, Photoshop |

**Google Docs vs Microsoft Word:**
| | Google Docs | Microsoft Word |
|---|---|---|
| Storage | Google Drive (cloud) | Local / OneDrive |
| Collaboration | Real-time, built-in | Requires OneDrive |
| Cost | Free (basic) | Subscription (Microsoft 365) |
| Internet needed | Yes | No (desktop) |
| Offline use | Limited | Full |

---

## E-Commerce

**E-commerce** (electronic commerce) is buying and selling goods and services over the internet.

### Types of E-Commerce

| Type | Description | Examples |
|---|---|---|
| **B2C** | Business to Consumer | Amazon, Takealot, Woolworths |
| **B2B** | Business to Business | Supplier ordering systems |
| **C2C** | Consumer to Consumer | eBay, Gumtree, Facebook Marketplace |
| **C2B** | Consumer to Business | Freelancers selling services |

### How Online Payments Work:

```
Customer → Checkout → Payment Gateway → Bank → Authorisation → Merchant
```

**Security in e-commerce:**
- HTTPS — all transactions encrypted
- PCI-DSS compliance — payment card security standard
- 3D Secure — additional bank authentication (OTP)
- SSL certificates — verify merchant identity

**Advantages of e-commerce:**
- Open 24/7
- Global reach — sell to anyone, anywhere
- Lower overheads than physical store
- Personalised recommendations

**Disadvantages:**
- Cannot see/touch product before purchase
- Returns process can be inconvenient
- Cybersecurity risks (phishing, card fraud)
- Relies on delivery infrastructure

---

## Online Banking

**Online banking** allows account holders to manage finances via a bank's website or app.

**Features:**
- View balances and transactions
- Transfer money between accounts
- Pay bills and recipients
- Apply for loans and credit
- View statements

**Security measures used:**
- HTTPS (TLS encryption)
- Two-factor authentication (OTP to phone)
- Session timeouts
- Fraud detection algorithms
- Automatic logout on inactivity

---

## Cookies (in depth)

**Cookies** are small text files stored on a user's device by websites they visit.

### Cookie Types

| Type | Lifespan | Purpose |
|---|---|---|
| **Session cookie** | Browser session | Login state, shopping cart |
| **Persistent cookie** | Days to years | Preferences, saved login |
| **First-party cookie** | Site's own | Site functionality |
| **Third-party cookie** | Advertiser's | Cross-site tracking for ads |

### What cookies store:
- Login session token (keep you logged in)
- Shopping cart contents
- Language and display preferences
- Anonymised tracking ID (for analytics)
- Advertising targeting data

### Privacy and legislation:
- **GDPR** (EU) — must obtain informed consent for non-essential cookies
- **POPIA** (SA) — must protect personal information; consent required
- Websites must show a cookie consent banner
- Users can clear, block, or manage cookies in browser settings

### How advertisers use cookies:
1. Visit website A — advertiser sets cookie with your ID
2. Visit website B — same advertiser reads cookie
3. Advertiser knows you visited both sites → shows relevant ads
4. **Retargeting**: shows you ads for products you viewed

---

## Search Engines

**Search engines** index the web and return relevant results for queries.

### How Google works:
1. **Crawling** — Googlebot follows links, discovers new pages
2. **Indexing** — pages analysed and added to database
3. **Ranking** — algorithm scores pages on ~200 factors:
   - Relevance to query
   - Page authority (backlinks)
   - Content quality
   - Page speed
   - Mobile-friendliness
   - HTTPS

**Personalised search:**
- Google uses your search history, location, and preferences
- Two people searching the same term may see different results

---

## Social Media

**Social media** platforms allow users to create profiles, share content, and interact.

| Platform | Type | Main content |
|---|---|---|
| Facebook | Social network | Posts, photos, video, groups |
| Instagram | Visual | Photos, short videos (Reels) |
| X (Twitter) | Microblogging | Short text posts, news |
| TikTok | Short video | 15-second to 10-minute videos |
| YouTube | Video | Long-form video |
| LinkedIn | Professional | Career networking, job listings |

**Business use of social media:**
- Marketing and advertising (paid ads target specific demographics)
- Customer service
- Brand building
- Influencer partnerships

**Risks:**
- Privacy — data used for profiling
- Misinformation spreads rapidly
- Cyberbullying
- Mental health impacts (comparison, addiction by design)
- Data breaches

---

## Key Terms

| Term | Definition |
|---|---|
| **Cloud storage** | Storing files on remote servers accessible over the internet |
| **SaaS** | Software as a Service — software delivered via browser |
| **E-commerce** | Buying and selling goods online |
| **B2C** | Business to Consumer online commerce |
| **Cookie** | Small text file stored by a website on your device |
| **Session cookie** | Temporary cookie — expires when browser closes |
| **Third-party cookie** | Cookie set by advertiser, not the site you're visiting |
| **HTTPS** | HTTP with TLS encryption — essential for secure transactions |
| **Retargeting** | Showing ads based on sites previously visited |
| **GDPR** | EU data protection regulation requiring cookie consent |
| **POPIA** | SA Protection of Personal Information Act |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Give TWO advantages of using online applications (SaaS) over desktop applications"** — no installation needed; automatically updated; accessible from any device; real-time collaboration
>
> 2. **"What is a cookie? Give TWO uses."** — small text file stored by a website; uses: keep user logged in; remember preferences; track browsing for advertising; shopping cart contents
>
> 3. **"Give TWO security measures used in online banking"** — HTTPS (TLS encryption); two-factor authentication (OTP); session timeout; fraud detection
>
> 4. **"What is e-commerce? Give ONE advantage and ONE disadvantage"** — buying/selling online; advantage: open 24/7, global reach; disadvantage: cannot see product before buying, security risks
>
> 5. **"What is the difference between a first-party cookie and a third-party cookie?"** — First-party: set by the site you're visiting (login, preferences); Third-party: set by an advertiser to track you across multiple websites
