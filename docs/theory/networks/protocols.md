# Network Protocols

A protocol is a set of rules that governs communication between devices. Without protocols, a Windows laptop, an Android phone, a Linux server, and a Mac could not exchange a single byte. Protocols make interoperability possible.

> [!NOTE] Grade 11+
> Network protocols are introduced in Grade 11. SSL/TLS and network security protocols extend into Grade 12.

---

## What is a Protocol?

A **network protocol** is a set of standardised rules that define:
- The **format** of data packets (how data is structured)
- The **sequence** of messages (who sends first, how errors are acknowledged)
- **Error detection** and correction methods
- **Speed** and flow control

**Analogy:** A protocol is like a language. Two people can only communicate if they use the same language and follow the same grammar rules.

---

## The TCP/IP Model

The **TCP/IP model** is the fundamental protocol suite of the internet. It organises protocols into four layers:

| Layer | Protocols | Function |
|---|---|---|
| **Application** | HTTP, HTTPS, FTP, SMTP, DNS, DHCP | What the application does with data |
| **Transport** | TCP, UDP | End-to-end delivery, error correction |
| **Internet** | IP | Addressing and routing between networks |
| **Network Access** | Ethernet, Wi-Fi | Physical transmission of data |

---

## Core Protocols — Table

| Protocol | Full Name | Port | Purpose |
|---|---|---|---|
| **HTTP** | HyperText Transfer Protocol | 80 | Transfers web pages (unencrypted) |
| **HTTPS** | HTTP Secure | 443 | Encrypted HTTP using SSL/TLS |
| **FTP** | File Transfer Protocol | 20, 21 | Transfers files between computers |
| **SFTP** | SSH File Transfer Protocol | 22 | Encrypted file transfer |
| **SMTP** | Simple Mail Transfer Protocol | 25 | Sends email from client to server |
| **POP3** | Post Office Protocol v3 | 110 | Downloads email to local device (removes from server) |
| **IMAP** | Internet Message Access Protocol | 143 | Access email on server (stays on server) |
| **DNS** | Domain Name System | 53 | Translates domain names to IP addresses |
| **DHCP** | Dynamic Host Configuration Protocol | 67/68 | Automatically assigns IP addresses |
| **TCP** | Transmission Control Protocol | — | Reliable, ordered data delivery |
| **UDP** | User Datagram Protocol | — | Fast but unreliable delivery (no error correction) |
| **VoIP** | Voice over IP | various | Voice calls over internet (e.g. Skype, WhatsApp calls) |
| **SSH** | Secure Shell | 22 | Encrypted remote terminal access |
| **Telnet** | — | 23 | Remote terminal access (unencrypted — obsolete) |

---

## Key Protocols Explained

### HTTP and HTTPS

**HTTP (HyperText Transfer Protocol)**
- Governs how web browsers request and receive web pages
- Stateless — each request is independent
- Unencrypted — data can be intercepted

**HTTPS (HTTP Secure)**
- HTTP with SSL/TLS encryption
- All data between browser and server is encrypted
- URL begins with `https://` and shows a padlock icon
- Required for any sensitive data (login, banking, purchases)

---

### DNS — Domain Name System

**The internet's phonebook:** converts human-readable domain names into IP addresses.

```
www.google.com  →  DNS lookup  →  142.250.80.100
```

**How DNS works:**
1. User types `www.school.co.za` in browser
2. Computer checks local DNS cache
3. If not cached, asks ISP's DNS server
4. DNS server finds the IP address
5. Computer connects to that IP address

**DNS record types:**
- **A record**: Domain → IPv4 address
- **AAAA record**: Domain → IPv6 address
- **MX record**: Mail exchange — where to send email for this domain
- **CNAME**: Alias — one domain points to another

---

### DHCP — Dynamic Host Configuration Protocol

Automatically assigns IP configuration to devices joining a network:
- IP address
- Subnet mask
- Default gateway (router address)
- DNS server address

Without DHCP, every device needs a manually configured static IP address.

---

### TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| **Reliability** | Guaranteed delivery — acknowledgements | No guarantee — "fire and forget" |
| **Order** | Packets arrive in order | May arrive out of order |
| **Error correction** | Yes — retransmits lost packets | No |
| **Speed** | Slower (overhead from acknowledgements) | Faster |
| **Connection** | Connection-oriented (handshake first) | Connectionless |
| **Use cases** | Web browsing, email, file transfer | Video streaming, gaming, VoIP |

**Why use UDP if it's unreliable?**  
In live video or gaming, a slightly corrupted frame or late packet is better than stopping to retransmit. Speed matters more than perfection.

---

### FTP — File Transfer Protocol

Used to transfer files between a client and server:
- `FTP`: unencrypted
- `SFTP`: encrypted (uses SSH)
- `FTPS`: FTP with SSL/TLS encryption

FTP is still used for web hosting and large file transfers, but SFTP is preferred for security.

---

### Email Protocols

| Protocol | Direction | Server-Side | Notes |
|---|---|---|---|
| **SMTP** | Sending | Outgoing mail server | All email clients use SMTP to send |
| **POP3** | Receiving | Downloads to device | Removes email from server; local storage |
| **IMAP** | Receiving | Stays on server | Access from any device; sync across devices |

> [!TIP] POP3 vs IMAP
> POP3 downloads and deletes from server — better for one device only. IMAP keeps mail on server — better for accessing email from phone, laptop, and tablet simultaneously.

---

## SSL/TLS — Encryption for Web

> [!IMPORTANT] Grade 12 Focus
> SSL/TLS and public/private key encryption are Grade 12 content.

**SSL (Secure Sockets Layer)** and its successor **TLS (Transport Layer Security)** provide:
- **Encryption**: Data is scrambled — unreadable to interceptors
- **Authentication**: Certificates verify the server's identity
- **Integrity**: Data cannot be tampered with in transit

### How HTTPS/TLS Works (Simplified)

1. Browser connects to `https://bank.co.za`
2. Server sends its **digital certificate** (contains public key)
3. Browser verifies the certificate (signed by a trusted Certificate Authority)
4. Browser generates a session key, encrypts it with the server's public key
5. Server decrypts it with its **private key**
6. All further communication is encrypted with the session key

### Public Key vs Private Key

| Key | What it is | What it does |
|---|---|---|
| **Public key** | Shared openly — anyone can see it | Encrypts data (only the private key can decrypt) |
| **Private key** | Kept secret by the owner | Decrypts data encrypted with the matching public key |

---

## Wi-Fi Standards (IEEE 802.11)

| Standard | Nickname | Max Speed | Frequency |
|---|---|---|---|
| 802.11g | Wi-Fi 3 | 54 Mbps | 2.4 GHz |
| 802.11n | Wi-Fi 4 | 600 Mbps | 2.4/5 GHz |
| 802.11ac | Wi-Fi 5 | 3.5 Gbps | 5 GHz |
| 802.11ax | Wi-Fi 6 | 9.6 Gbps | 2.4/5/6 GHz |

**2.4 GHz vs 5 GHz:**
- 2.4 GHz: longer range, lower speed, more interference (used by microwaves, Bluetooth)
- 5 GHz: shorter range, faster speed, less interference

---

## Key Terms

| Term | Definition |
|---|---|
| **Protocol** | Standardised rules governing network communication |
| **HTTP** | Protocol for transferring web pages (unencrypted) |
| **HTTPS** | HTTP with SSL/TLS encryption |
| **DNS** | System translating domain names to IP addresses |
| **DHCP** | Protocol automatically assigning IP addresses on a network |
| **TCP** | Reliable, ordered data transmission protocol |
| **UDP** | Fast, unreliable data transmission — no error correction |
| **FTP** | Protocol for transferring files between client and server |
| **SMTP** | Protocol for sending email |
| **POP3** | Downloads email to device; removes from server |
| **IMAP** | Accesses email on server; synchronises across devices |
| **SSL/TLS** | Encryption protocols securing internet communications |
| **VoIP** | Voice over IP — telephone calls via internet |
| **Public key** | Encryption key shared openly |
| **Private key** | Decryption key kept secret by the owner |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the purpose of DNS?"** — translates human-readable domain names into IP addresses
>
> 2. **"Explain the difference between TCP and UDP. When would you use each?"** — TCP: reliable, ordered, error correction; used for web/email. UDP: fast, no error correction; used for streaming/gaming
>
> 3. **"What is the difference between POP3 and IMAP?"** — POP3 downloads and removes from server; IMAP keeps on server and syncs across devices
>
> 4. **"Explain how HTTPS is more secure than HTTP"** — HTTPS uses SSL/TLS encryption; data is encrypted in transit; certificate verifies server identity
>
> 5. **"What is DHCP and why is it useful?"** — automatically assigns IP address, subnet mask, gateway, DNS to devices; without it, every device needs manual IP configuration
