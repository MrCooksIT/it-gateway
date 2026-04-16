# Network Types

Not all networks are the same size. The network in your bedroom connecting your phone to your laptop is nothing like the network connecting offices across continents. Networks are classified by their geographic scope, ownership, and purpose.

> [!NOTE] Grade 10–11
> Network types (PAN, LAN, WAN) are introduced at Grade 10. Grade 11 adds MAN, HAN, and more detailed comparisons.

---

## Overview: Network Classification by Size

| Network Type | Full Name | Typical Range | Who uses it |
|---|---|---|---|
| **PAN** | Personal Area Network | < 10 metres | Individual (Bluetooth devices) |
| **HAN** | Home Area Network | Single home | Household (smart home devices) |
| **LAN** | Local Area Network | Single building/campus | School, office, home |
| **MAN** | Metropolitan Area Network | City / town | ISP, municipality, large organisation |
| **WAN** | Wide Area Network | Countries / worldwide | Businesses, internet |

---

## PAN — Personal Area Network

A **PAN** connects devices for personal use, typically within a few metres of a single person.

**Characteristics:**
- Range: up to 10 metres
- Technologies: Bluetooth, USB, infrared (IrDA), NFC
- Low speed, low power
- No infrastructure required

**Examples:**
- Wireless earphones connected to a phone
- Smartwatch syncing to a smartphone
- Laptop connected to a wireless mouse and keyboard
- Transferring files between two phones via Bluetooth

---

## HAN — Home Area Network

A **HAN** connects devices within a home, often managed by a home router.

**Characteristics:**
- Range: single dwelling
- Technologies: Wi-Fi, Ethernet, Powerline networking
- Managed by consumer-grade router
- Often includes smart home devices (IoT)

**Examples:**
- Home Wi-Fi network connecting phones, TVs, and laptops
- Smart home hub controlling lights, thermostat, and security cameras
- Gaming consoles connected to the internet via home router

---

## LAN — Local Area Network

A **LAN** is a network within a single building or campus, owned and managed by that organisation.

**Characteristics:**
- Range: single building or campus (up to ~1 km)
- High speed: 100 Mbps to 10 Gbps (Gigabit Ethernet)
- Low latency
- Owned by the organisation
- Technologies: Ethernet (wired), Wi-Fi (wireless)

**Examples:**
- School computer lab network
- Office network sharing a printer and file server
- University campus network

**Wired LAN (Ethernet):**
- Uses Cat5e, Cat6 cables
- Faster and more secure than Wi-Fi
- Devices connected to a switch

**Wireless LAN (WLAN / Wi-Fi):**
- Uses wireless access points (WAPs)
- More flexible — no cables
- Slightly slower, more interference-prone

---

## MAN — Metropolitan Area Network

A **MAN** covers a city or large town, connecting multiple LANs.

**Characteristics:**
- Range: up to 50 km (city-wide)
- Faster than WAN, but more limited than LAN
- Often owned by ISPs, municipalities, or large organisations
- Technologies: fibre optic cable, WiMAX

**Examples:**
- City-wide Wi-Fi network provided by municipality
- Network connecting multiple branches of a bank across a city
- ISP infrastructure connecting suburbs to a city exchange

---

## WAN — Wide Area Network

A **WAN** spans large geographic areas — countries or globally. The internet is the world's largest WAN.

**Characteristics:**
- Range: unlimited — can be global
- Slower than LAN (limited by physical distance and infrastructure)
- Usually uses leased lines or public infrastructure
- Technologies: fibre optic cables, satellite, DSL, mobile (4G/5G)

**Examples:**
- The internet
- A company's private network connecting offices in Johannesburg, Cape Town, and London
- ATM banking network
- Video streaming from servers in the USA to South Africa

---

## LAN vs WAN Comparison

| Feature | LAN | WAN |
|---|---|---|
| Geographic range | Single building/campus | Countries or global |
| Speed | Very fast (up to 10 Gbps) | Slower (limited by distance) |
| Ownership | Private (organisation) | Typically leased or public |
| Cost | Lower | Higher |
| Security | Easier to secure | More difficult to secure |
| Error rate | Low | Higher (longer distance) |
| Examples | School network, office | Internet, corporate WAN |

---

## Client-Server vs Peer-to-Peer Networks

### Client-Server

- **Dedicated server** manages resources, authentication, and storage
- Clients (workstations) request services from the server
- Centralised control → easier management and security
- Used in: businesses, schools, organisations

| Advantage | Disadvantage |
|---|---|
| Centralised data management | Expensive server hardware required |
| Easier to apply security policies | Server is single point of failure |
| Easy to back up centrally | Requires IT staff to administer |
| Scales well | Server downtime affects all users |

### Peer-to-Peer (P2P)

- Each device is equal — any can be a client or server
- No central server — devices share directly
- Simpler, cheaper to set up
- Used in: small home networks, file sharing

| Advantage | Disadvantage |
|---|---|
| No expensive server required | No central security management |
| Easy to set up | Files scattered across devices |
| No single point of failure | Harder to back up |
| Suitable for small networks | Slows as network grows |

---

## Key Terms

| Term | Definition |
|---|---|
| **PAN** | Personal Area Network — connects personal devices within ~10 metres |
| **HAN** | Home Area Network — devices within a home |
| **LAN** | Local Area Network — network within a single building or campus |
| **MAN** | Metropolitan Area Network — city-scale network |
| **WAN** | Wide Area Network — spans large geographic areas |
| **Client** | Device that requests services from a server |
| **Server** | Dedicated device providing services (files, printing, authentication) |
| **Peer-to-peer** | Network where all devices are equal — no dedicated server |
| **Ethernet** | Wired LAN technology using twisted-pair cables |
| **WLAN** | Wireless LAN — uses Wi-Fi (IEEE 802.11 standards) |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between a LAN and a WAN?"** — LAN: single building/campus, high speed, privately owned; WAN: spans large distances/countries, slower, uses leased/public infrastructure
>
> 2. **"Give ONE example of each: PAN, LAN, WAN"** — PAN: Bluetooth earphones; LAN: school computer lab; WAN: the internet
>
> 3. **"Give TWO advantages of a client-server network over a P2P network"** — centralised data management; easier to enforce security policies; central backup; scales well
>
> 4. **"Give TWO disadvantages of a client-server network"** — expensive server hardware; server is single point of failure; requires trained IT staff
>
> 5. **"What type of network would be most suitable for connecting two branches of a company in different cities? Motivate."** — WAN; it spans large geographic distances connecting separate locations across cities or countries
