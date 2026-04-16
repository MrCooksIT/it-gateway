# Network Hardware

Every network needs physical components to make communication possible. From the cable in the wall to the router blinking in your lounge, each piece of hardware plays a specific role in getting data from one device to another.

> [!NOTE] Grade 11
> Network hardware is primarily a Grade 11 topic. Understanding the role and function of each device is essential for Paper 2.

---

## Overview of Network Hardware

| Device | Purpose | Layer |
|---|---|---|
| **NIC** | Connects device to network | Physical |
| **Hub** | Broadcasts data to all ports | Physical |
| **Switch** | Sends data to correct device only | Data Link |
| **Router** | Connects different networks; routes data | Network |
| **Modem** | Converts digital ↔ analogue signals | Physical |
| **WAP** | Provides wireless access to a LAN | Data Link |
| **Repeater** | Amplifies signal over long distances | Physical |
| **Bridge** | Connects two network segments | Data Link |
| **Firewall** | Filters traffic based on security rules | Network |

---

## NIC — Network Interface Card

A **NIC** (Network Interface Card) is the hardware component that physically connects a device to a network.

- Every networked device has a NIC (built-in or expansion card)
- Assigned a unique **MAC address** (Media Access Control) — 48-bit hardware address
- Can be wired (Ethernet port) or wireless (Wi-Fi)
- Operates at 100 Mbps, 1 Gbps, or 10 Gbps depending on standard

**MAC address format:** `00:1A:2B:3C:4D:5E` (6 pairs of hexadecimal digits)

---

## Hub

A **hub** is a basic network device that connects multiple devices in a LAN.

**How it works:**
- Receives data on one port
- Broadcasts it to **all** other ports
- All devices receive every packet (even if not addressed to them)

**Problems:**
- Creates unnecessary network traffic (**collisions**)
- Security risk — all devices see all data
- Largely replaced by switches

> [!WARNING] Hubs are obsolete
> Hubs are rarely used in modern networks. Switches are far more efficient. You may still see hubs in exam questions — know that they broadcast to all ports.

---

## Switch

A **switch** is an intelligent network device that connects multiple devices and sends data **only to the intended recipient**.

**How it works:**
- Maintains a **MAC address table** — maps port numbers to MAC addresses
- When a frame arrives, it checks the destination MAC and sends it to the correct port only
- Reduces collisions, improves efficiency

**Types:**
- **Unmanaged switch** — plug and play, no configuration
- **Managed switch** — configurable (VLANs, QoS, monitoring)

| Hub vs Switch | Hub | Switch |
|---|---|---|
| Data delivery | Broadcast to all ports | Only to destination port |
| Collisions | Many | Minimal |
| Security | Low | Better |
| Speed | Shared | Dedicated per connection |
| Used today | Rarely | Universally |

---

## Router

A **router** connects different networks together and **routes data packets** between them using IP addresses.

**Functions:**
- Connects your LAN to the internet (WAN)
- Assigns IP addresses via DHCP
- Acts as a gateway between networks
- Provides NAT (Network Address Translation) — one public IP for many devices
- Most home routers include a built-in switch and WAP

**Routing process:**
1. Packet arrives at router with destination IP address
2. Router checks its **routing table**
3. Forwards packet to the next hop toward the destination
4. Process repeats until packet reaches destination

**Home router vs Enterprise router:**
- Home router: simple, consumer-grade, all-in-one (router + switch + WAP + modem)
- Enterprise router: high-performance, complex routing protocols, handles thousands of connections

---

## Modem

A **modem** (MOdulator-DEModulator) converts signals between digital (computer format) and analogue (telephone line format).

**Why needed:**
- Phone lines and cable TV lines carry analogue signals
- Computers use digital signals
- Modem converts digital → analogue for sending; analogue → digital for receiving

**Types:**
| Type | Technology | Speed |
|---|---|---|
| ADSL modem | Phone line | Up to 24 Mbps |
| Cable modem | Coaxial (TV cable) | Up to 1 Gbps |
| Fibre ONT | Fibre optic | Up to 1 Gbps+ |
| 4G/LTE modem | Mobile network | Up to 150 Mbps |

> [!TIP] Most home devices are a modem + router + switch + WAP combined
> ISPs provide a single unit that does all four jobs. The term "modem" is commonly used even when the device is technically a "residential gateway."

---

## WAP — Wireless Access Point

A **WAP** (Wireless Access Point) connects wireless devices to a wired LAN.

- Transmits and receives Wi-Fi signals (IEEE 802.11)
- Connected to the switch/router via Ethernet cable
- Extends the reach of a LAN wirelessly
- Each WAP has an **SSID** (Service Set Identifier) — the visible Wi-Fi network name

**WAP vs Router:**
- A WAP only provides wireless connectivity — it does not route between networks
- A router can include a WAP, but they are separate functions

**Enterprise WAPs:**
- Ceiling-mounted, manage dozens of simultaneous connections
- Managed centrally by a **wireless LAN controller**
- Used in schools, hospitals, shopping centres

---

## Repeater

A **repeater** amplifies and regenerates a network signal to extend its range.

- Signals weaken over long cable runs (attenuation)
- A repeater boosts the signal so it can travel further
- Does not filter or manage traffic — purely amplifies
- Wireless repeaters extend Wi-Fi range (also called "Wi-Fi extenders" or "range extenders")

---

## Firewall

A **firewall** is a security device (hardware or software) that monitors and controls incoming and outgoing network traffic based on predefined security rules.

**What it does:**
- Blocks unauthorised access to the network
- Allows legitimate traffic through
- Can filter by IP address, port number, protocol

**Types:**
| Type | Description |
|---|---|
| Software firewall | Installed on a device (Windows Defender Firewall) |
| Hardware firewall | Dedicated device between network and internet |
| Packet filtering | Checks source/destination IP and port |
| Stateful inspection | Tracks connection state; smarter filtering |

---

## Cables and Connectors

| Cable Type | Description | Max Speed | Max Distance |
|---|---|---|---|
| **Cat5e** (UTP) | Twisted-pair copper | 1 Gbps | 100 m |
| **Cat6** (UTP) | Twisted-pair copper | 10 Gbps | 55 m |
| **Cat6a** (UTP) | Twisted-pair copper | 10 Gbps | 100 m |
| **Coaxial** | Thick copper with shielding | Varies | 500 m |
| **Fibre optic** | Light through glass/plastic | Up to Tbps | Kilometres |

**RJ-45 connector** — standard plug for Ethernet cables (looks like a large phone plug)

**Fibre optic advantages:**
- Much faster — light travels faster than electrical signals
- Not affected by electromagnetic interference (EMI)
- More secure — cannot be easily tapped
- Higher cost, more fragile

---

## Key Terms

| Term | Definition |
|---|---|
| **NIC** | Network Interface Card — hardware connecting device to network |
| **MAC address** | Unique hardware address of a NIC (48-bit hex) |
| **Hub** | Network device that broadcasts to all ports |
| **Switch** | Network device that sends data only to the destination port |
| **Router** | Connects networks; routes packets using IP addresses |
| **Modem** | Converts digital ↔ analogue signals for transmission |
| **WAP** | Wireless Access Point — provides Wi-Fi access to a LAN |
| **Firewall** | Security device filtering network traffic |
| **SSID** | Wi-Fi network name broadcast by a WAP |
| **Repeater** | Amplifies network signal to extend range |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between a hub and a switch?"** — Hub broadcasts to all ports (collisions, less efficient); switch sends only to the correct device using MAC address table (more efficient, more secure)
>
> 2. **"What is the function of a router?"** — Routes data packets between different networks; connects LAN to internet; assigns IP addresses via DHCP
>
> 3. **"What is a MAC address? Where is it stored?"** — Unique 48-bit hardware address assigned to every NIC; stored on the NIC itself
>
> 4. **"What is the purpose of a modem?"** — Converts digital signals from a computer to analogue signals for transmission over phone/cable lines, and vice versa
>
> 5. **"Give ONE advantage of fibre optic cable over UTP cable"** — Much faster data transmission; not affected by electromagnetic interference; can transmit over much longer distances
