# Networks & Internet — Quick Summary

No prose. Tables and key facts only.

---

## Network Types

| Type | Range | Example |
|---|---|---|
| PAN | ~10m | Bluetooth headset ↔ phone |
| HAN | One home | Home Wi-Fi |
| LAN | Building | School computer lab |
| MAN | City | City-wide Wi-Fi |
| WAN | Country/continent | Bank branch network |
| Internet | Global | The internet |

---

## Network Models

| | Client-Server | Peer-to-Peer |
|---|---|---|
| Dedicated server? | Yes | No |
| Cost | High | Low |
| Security | Centralised, high | Decentralised, low |
| Scale | Many computers | Best < 10 |
| Admin | One place | Each computer |
| Used in | Schools, businesses | Home networks |

---

## Topologies

| Topology | Shape | Single point of failure? | Cable? |
|---|---|---|---|
| Star | Central switch + cables to each device | Switch | More |
| Bus | One cable, devices tap in | Main cable | Less |
| Ring | Circle | Any break | Moderate |
| Mesh | Everything connected to everything | No | Most |

**Modern choice:** Star (switch-based)

---

## Network Hardware

| Device | Function |
|---|---|
| NIC | Hardware enabling device to connect to network |
| Switch | Connects devices on SAME network; sends to specific device |
| Hub | Like switch but broadcasts to ALL (less efficient) |
| Router | Connects DIFFERENT networks; assigns IP (DHCP) |
| Modem | Converts digital ↔ analogue for phone line |
| WAP | Wireless Access Point — extends Wi-Fi coverage |
| Firewall | Filters network traffic for security |
| Repeater | Extends signal distance |

---

## Key Protocols

| Protocol | Port | Purpose |
|---|---|---|
| HTTP | 80 | Web pages (unencrypted) |
| HTTPS | 443 | Web pages (SSL/TLS encrypted) |
| FTP | 20/21 | File transfer |
| SMTP | 25 | Send email |
| POP3 | 110 | Download email (removes from server) |
| IMAP | 143 | Access email (stays on server) |
| DNS | 53 | Domain name → IP address |
| DHCP | 67/68 | Automatic IP address assignment |
| SSH | 22 | Secure remote access |

---

## TCP vs UDP

| | TCP | UDP |
|---|---|---|
| Reliable? | Yes — acknowledgements | No |
| Ordered? | Yes | No |
| Speed | Slower | Faster |
| Use for | Web, email, FTP | Streaming, gaming, VoIP |

---

## Wi-Fi Standards

| Standard | Name | Max Speed |
|---|---|---|
| 802.11g | Wi-Fi 3 | 54 Mbps |
| 802.11n | Wi-Fi 4 | 600 Mbps |
| 802.11ac | Wi-Fi 5 | 3.5 Gbps |
| 802.11ax | Wi-Fi 6 | 9.6 Gbps |

2.4 GHz = longer range, slower, more interference  
5 GHz = shorter range, faster, less interference

---

## Intranet / Extranet / Internet

| | Who accesses | Security |
|---|---|---|
| Intranet | Internal only | Inside firewall |
| Extranet | Internal + authorised external | Controlled |
| Internet | Anyone | Public |

---

## Internet Concepts

| Term | Definition |
|---|---|
| IP address | Unique identifier for device on network |
| IPv4 | 32-bit address (x.x.x.x) ~4.3B addresses |
| IPv6 | 128-bit address (hex groups) — virtually unlimited |
| Domain name | Human-readable address (www.google.com) |
| DNS | Translates domain names to IP addresses |
| ISP | Internet Service Provider |
| URL | Full web address (protocol + domain + path) |
| TLD | Top Level Domain (.com, .co.za, .org) |

---

## Web Evolution

| | Web 1.0 | Web 2.0 | Web 3.0 |
|---|---|---|---|
| Type | Read only | Read-Write | Semantic/AI |
| Content creator | Website owner | Anyone (UGC) | Machine + user |
| Interaction | None | Social, comments, sharing | Personalised, decentralised |
| Example | Early websites | Facebook, YouTube | AI assistants, IoT |

---

## SSL/TLS Encryption

1. Browser connects to HTTPS site
2. Server sends **certificate** (with public key)
3. Browser verifies certificate (Certificate Authority)
4. Browser encrypts session key with server's **public key**
5. Server decrypts with **private key**
6. All traffic encrypted with session key

Public key = shared openly → encrypts  
Private key = kept secret → decrypts

---

## Email Security Threats

| Threat | Description |
|---|---|
| Spam | Unsolicited bulk email |
| Phishing | Fake email to steal credentials |
| Spear phishing | Targeted phishing using personal info |
| Spoofing | Faking sender identity |
| Malware attachment | Virus/trojan in email attachment |

---

## Cloud Service Models

| Model | What you get | Example |
|---|---|---|
| IaaS | Virtual hardware (servers, storage) | AWS, Azure |
| PaaS | Development platform | Google App Engine |
| SaaS | Software via internet | MS 365, Gmail, Netflix |
