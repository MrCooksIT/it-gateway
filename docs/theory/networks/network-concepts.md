# Network Concepts

Standalone computers are powerful — networked computers are transformational. A network lets computers share resources, communicate, and access the internet. Understanding networks is foundational to every topic in the communication and internet sections of Paper 2.

> [!NOTE] Grade 10+
> Basic network concepts (what is a network, advantages, types) are introduced in Grade 10. Hardware, topologies, protocols, and security extend through Grade 11 and 12.

---

## What is a Computer Network?

A **computer network** is two or more computers connected together to share resources and communicate.

**Resources that can be shared:**
- Files and data
- Printers and scanners
- Internet connection
- Software applications
- Storage space

---

## Why Use a Network?

| Advantage | Explanation |
|---|---|
| **Resource sharing** | One printer or internet connection serves many computers |
| **Data sharing** | Files can be accessed from any computer on the network |
| **Communication** | Email, messaging, video calls between users |
| **Centralised management** | IT can update software and manage all computers from one place |
| **Backup** | Data can be backed up automatically to a central server |
| **Cost efficiency** | Shared resources reduce the need for individual peripherals |

**Disadvantages:**
- Security risks — one compromised device can affect all
- Setup and maintenance costs
- If the server fails, the whole network is affected
- Requires technical expertise to manage

---

## Network Models

### Client-Server Network

A **dedicated server** provides services to client computers.

```
Client 1 ──┐
Client 2 ──┤── Server (file, print, web, email)
Client 3 ──┘
```

| Feature | Detail |
|---|---|
| **Server** | Powerful computer dedicated to network services |
| **Clients** | Workstations that request services from the server |
| **Control** | Centralised — IT admin controls access from one place |
| **Security** | High — centralised authentication |
| **Scalability** | Can add more clients easily |
| **Dependency** | If server fails, clients lose network access |
| **Cost** | High — server hardware + network OS + maintenance |
| **Used in** | Schools, offices, businesses, data centres |

### Peer-to-Peer (P2P) Network

All computers are **equal** — any device can be both client and server.

```
Computer A ── Computer B ── Computer C
     └──────────────────────────┘
```

| Feature | Detail |
|---|---|
| **No dedicated server** | All computers share resources directly |
| **Control** | Decentralised — each user controls their own computer |
| **Security** | Lower — harder to enforce consistent security |
| **Scalability** | Not suitable for large networks (slow and complex) |
| **Cost** | Low — no server needed |
| **Used in** | Home networks, small offices (under 10 computers) |

---

## Network Types by Size

| Type | Full Name | Range | Example |
|---|---|---|---|
| **PAN** | Personal Area Network | ~1–10 metres | Bluetooth headset ↔ phone |
| **LAN** | Local Area Network | Building or campus | School computer lab |
| **MAN** | Metropolitan Area Network | City or town | City-wide Wi-Fi system |
| **WAN** | Wide Area Network | Country or continent | Bank branches linked nationally |
| **Internet** | Global WAN | Worldwide | The internet |
| **HAN** | Home Area Network | One home | Home router network |

### LAN Characteristics

- High speed (100 Mbps to 10 Gbps)
- Low cost — short cable distances
- Private — owned and managed by the organisation
- Can be wired (Ethernet) or wireless (Wi-Fi)

### WAN Characteristics

- Connects geographically distant networks
- Lower speed and higher cost than LAN
- Typically uses public infrastructure (leased lines, internet, satellite)
- Managed by ISPs (Internet Service Providers)

---

## Wired vs Wireless Networks

| Feature | Wired (Ethernet) | Wireless (Wi-Fi) |
|---|---|---|
| Speed | Up to 10 Gbps | Up to 9.6 Gbps (Wi-Fi 6) |
| Reliability | Very high — no interference | Lower — can drop, interference possible |
| Security | Higher — physical access needed | Lower — signals travel through walls |
| Installation | Cables must be run | No cables needed |
| Mobility | Fixed — cable length limits movement | Full mobility within coverage area |
| Cost | Cable + ports + installation | WAP + no cable installation |
| Best for | Servers, labs, desktop PCs | Laptops, phones, tablets |

---

## Network Hardware Summary

| Device | Function |
|---|---|
| **NIC (Network Interface Card)** | Hardware in each computer enabling network connection |
| **Router** | Connects networks together; directs data between networks; provides IP addresses (DHCP) |
| **Switch** | Connects devices on the SAME network; sends data only to intended device |
| **Hub** | Like a switch but broadcasts to all devices — less efficient (mostly outdated) |
| **Modem** | Converts digital to analogue for phone-line transmission (and back) |
| **Wireless Access Point (WAP)** | Extends wireless coverage; connects wireless devices to wired network |
| **Repeater / Range extender** | Boosts signal to extend coverage distance |
| **Bridge** | Connects two network segments |
| **Firewall** | Hardware or software filtering incoming/outgoing network traffic for security |

---

## Intranet vs Extranet vs Internet

| | Intranet | Extranet | Internet |
|---|---|---|---|
| **Access** | Internal users only | Internal + authorised external users | Anyone |
| **Example** | Company internal website | Supplier accessing company inventory system | World Wide Web |
| **Security** | High — inside firewall | Medium — controlled external access | Lower — public |

---

## Network Topologies

The **topology** is the physical or logical arrangement of computers and cables in a network.

### Star Topology

```
      PC
      |
PC ─ Switch ─ PC
      |
      PC
```

- All devices connect to a **central switch or hub**
- **Most common in modern networks**

| Advantage | Disadvantage |
|---|---|
| If one cable fails, only that device is affected | If the central switch fails, the whole network fails |
| Easy to add new devices | More cable required |
| Easy to troubleshoot | Central switch is a single point of failure |

### Bus Topology

```
PC ─── PC ─── PC ─── PC ─── PC
│                             │
Terminator                  Terminator
```

- All devices connect to a single cable (the bus)
- **Largely obsolete**

| Advantage | Disadvantage |
|---|---|
| Less cable needed | If the main cable breaks, the whole network fails |
| Easy and cheap to set up | Performance degrades as more devices added |

### Ring Topology

```
    PC
   /  \
 PC    PC
   \  /
    PC
```

- Devices form a closed loop; data travels in one direction

| Advantage | Disadvantage |
|---|---|
| Equal access for all devices | One break brings down the whole network |
| Data flows in one direction (no collisions) | Difficult to troubleshoot |

### Mesh Topology

Every device connects to every other device:

| Advantage | Disadvantage |
|---|---|
| Very reliable — multiple paths for data | Very expensive — many cables |
| Used in WANs and internet backbone | Complex to manage |

> [!TIP] Exam Tip
> Know **two advantages AND two disadvantages** of star, bus, and ring. Star is almost always the correct choice for a modern LAN — be able to explain why.

---

## Client-Server vs P2P — Summary

| Criterion | Client-Server | Peer-to-Peer |
|---|---|---|
| Number of computers | Many (enterprise) | Few (<10 for practicality) |
| Dedicated server needed? | Yes | No |
| Cost | High | Low |
| Security | Centralised, high | Decentralised, low |
| Performance | Consistent | Degrades as more added |
| Administration | From one server | Each user manages own PC |

---

## Key Terms

| Term | Definition |
|---|---|
| **Network** | Two or more computers connected to share resources |
| **LAN** | Local Area Network — within a building or campus |
| **WAN** | Wide Area Network — across cities, countries |
| **Client** | Computer that requests services from a server |
| **Server** | Dedicated computer providing network services |
| **P2P** | Peer-to-Peer — all computers are equal with no dedicated server |
| **Topology** | Physical or logical arrangement of network devices |
| **Star topology** | All devices connect to a central switch |
| **Bus topology** | All devices share one cable |
| **Router** | Connects networks; directs data between them |
| **Switch** | Connects devices on the same network efficiently |
| **Intranet** | Private internal network using web technologies |
| **Extranet** | Intranet with controlled access for external authorised users |
| **Firewall** | Security device/software that filters network traffic |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Give TWO advantages of a LAN"** — resource sharing, communication, centralised management, cost saving
>
> 2. **"Compare client-server and P2P networks"** — dedicate at least two criteria: cost, security, scalability, server dependency
>
> 3. **"Draw and describe the star topology. Give one advantage and one disadvantage."** — can draw a simple diagram; central switch; advantage: one cable failure doesn't down whole network; disadvantage: switch failure takes out all
>
> 4. **"What is the difference between a router and a switch?"** — router connects networks and routes data between them; switch connects devices on the same network
>
> 5. **"Give ONE example of an intranet use in a school"** — school's internal website with timetables, notices, and results accessible only from school computers
