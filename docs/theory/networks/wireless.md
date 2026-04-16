# Wireless Networking

Cut the cable — wireless networking has made it possible to connect devices without a single wire. From the Wi-Fi in your home to 5G on your phone to Bluetooth in your earphones, wireless technology covers a wide range of standards, speeds, and distances.

> [!NOTE] Grade 11
> Wireless networking is a Grade 11 topic. Know the different wireless technologies, their ranges, speeds, and use cases.

---

## Why Wireless?

| Advantage | Explanation |
|---|---|
| **Mobility** | Move freely within range — no physical connection needed |
| **Easy installation** | No cables to run through walls |
| **Scalability** | Add devices without adding cable infrastructure |
| **Accessibility** | Connect in places where cabling is impractical |

| Disadvantage | Explanation |
|---|---|
| **Security** | Signals can be intercepted — encryption is essential |
| **Interference** | Other wireless devices, walls, appliances reduce signal |
| **Speed** | Generally slower than wired equivalents |
| **Range** | Signal weakens with distance |
| **Reliability** | Susceptible to environmental factors |

---

## Wi-Fi (IEEE 802.11)

**Wi-Fi** is a wireless LAN technology based on the IEEE 802.11 family of standards. It connects devices to a local network (and through it, to the internet) via a Wireless Access Point (WAP) or router.

### Wi-Fi Standards

| Standard | Common Name | Max Speed | Frequency | Year |
|---|---|---|---|---|
| 802.11g | Wi-Fi 3 | 54 Mbps | 2.4 GHz | 2003 |
| 802.11n | Wi-Fi 4 | 600 Mbps | 2.4 / 5 GHz | 2009 |
| 802.11ac | Wi-Fi 5 | 3.5 Gbps | 5 GHz | 2013 |
| 802.11ax | Wi-Fi 6 | 9.6 Gbps | 2.4 / 5 / 6 GHz | 2019 |

### 2.4 GHz vs 5 GHz

| | 2.4 GHz | 5 GHz |
|---|---|---|
| Range | Longer (through walls better) | Shorter |
| Speed | Slower | Faster |
| Interference | More crowded | Less crowded |
| Best for | Devices far from router | Devices near router, streaming |

### Wi-Fi Security Protocols

| Protocol | Year | Security Level | Notes |
|---|---|---|---|
| WEP | 1999 | Weak | Easily cracked — obsolete |
| WPA | 2003 | Moderate | Improved over WEP |
| WPA2 | 2004 | Strong | AES encryption — current standard |
| WPA3 | 2018 | Very strong | Latest — protects against dictionary attacks |

> [!WARNING] Always use WPA2 or WPA3
> WEP and WPA are no longer secure. Networks using WEP can be cracked in minutes with freely available tools.

---

## Bluetooth

**Bluetooth** is a short-range wireless technology for connecting personal devices.

| Feature | Detail |
|---|---|
| Standard | IEEE 802.15 |
| Range | ~10 m (Class 2), up to 100 m (Class 1) |
| Speed | Up to 3 Mbps (classic), 2 Mbps (BLE) |
| Frequency | 2.4 GHz |
| Power | Very low (especially Bluetooth Low Energy / BLE) |

**Uses:** wireless earphones, keyboards, mice, smartwatches, speakers, file transfer between phones, car audio systems

**Bluetooth Low Energy (BLE):**
- Used in IoT devices, fitness trackers, medical devices
- Battery lasts months on a single cell

---

## WiMAX

**WiMAX** (Worldwide Interoperability for Microwave Access) is a long-range wireless technology providing broadband internet over large areas.

| Feature | Detail |
|---|---|
| Standard | IEEE 802.16 |
| Range | Up to 50 km |
| Speed | Up to 70 Mbps |
| Use case | Providing internet to rural areas; MAN |

**Purpose:** Delivers internet access where fibre or cable infrastructure doesn't exist — rural areas, developing regions.

Now largely superseded by 4G LTE for mobile coverage, but still used in some deployments.

---

## Mobile Data Networks (Cellular)

Cellular networks provide internet and communication via a network of base stations (towers).

| Generation | Speed | Latency | Key Uses |
|---|---|---|---|
| **2G (GSM)** | ~0.1 Mbps | High | Voice calls, SMS |
| **3G (UMTS)** | 2–42 Mbps | ~100 ms | Mobile internet, video calls |
| **4G LTE** | 10–150 Mbps | 30–50 ms | HD streaming, mobile apps, hotspots |
| **5G** | 100 Mbps–10 Gbps | <10 ms | IoT, autonomous vehicles, AR/VR, smart cities |

### 4G vs 5G

| Feature | 4G LTE | 5G |
|---|---|---|
| Max speed | ~150 Mbps | ~10 Gbps |
| Latency | 30–50 ms | <1 ms |
| Device density | Moderate | Very high (IoT) |
| Coverage | Widespread globally | Still expanding |
| Infrastructure | Existing towers | New towers required (mmWave) |
| Main benefit | Fast mobile internet | Ultra-low latency + massive IoT |

---

## NFC — Near Field Communication

**NFC** enables very short-range (< 4 cm) wireless communication between devices.

| Feature | Detail |
|---|---|
| Range | < 4 cm |
| Speed | ~400 Kbps |
| Use case | Contactless payment, tap-to-pair, access cards |

**Examples:** Apple Pay, Google Pay, tap-to-pay bank cards, hotel room key cards, tap-to-connect Bluetooth speakers

---

## RFID — Radio Frequency Identification

**RFID** uses radio waves to read data from passive or active tags without physical contact.

| Feature | Detail |
|---|---|
| Range | cm to several metres (depends on frequency) |
| Power | Passive (no battery) or active (battery) |
| Use case | Inventory tracking, library books, access control, toll gates, livestock tracking |

**Passive RFID:** the reader powers the tag via radio waves — no battery needed in the tag.

---

## Wireless Technology Comparison

| Technology | Range | Speed | Use Case |
|---|---|---|---|
| Bluetooth | < 10 m | Low | Personal devices |
| NFC | < 4 cm | Very low | Payments, pairing |
| Wi-Fi (802.11ac) | ~50 m indoors | Up to 3.5 Gbps | LAN wireless |
| 4G LTE | City-wide | 10–150 Mbps | Mobile internet |
| 5G | City-wide | Up to 10 Gbps | IoT, ultra-low latency |
| WiMAX | Up to 50 km | Up to 70 Mbps | Rural broadband |
| RFID | cm–metres | Very low | Tracking, access |

---

## Key Terms

| Term | Definition |
|---|---|
| **Wi-Fi** | Wireless LAN technology (IEEE 802.11) |
| **WAP** | Wireless Access Point — connects wireless devices to a wired LAN |
| **SSID** | Name of a Wi-Fi network broadcast by a WAP |
| **WPA2** | Wi-Fi security protocol using AES encryption |
| **Bluetooth** | Short-range wireless standard for personal devices |
| **BLE** | Bluetooth Low Energy — for IoT and wearable devices |
| **WiMAX** | Long-range wireless broadband (IEEE 802.16) |
| **4G LTE** | 4th generation mobile network — fast mobile internet |
| **5G** | 5th generation network — ultra-fast, ultra-low latency |
| **NFC** | Near Field Communication — < 4 cm range, used for payments |
| **RFID** | Radio Frequency Identification — tracking via radio tags |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between 4G and 5G?"** — 5G is much faster (up to 10 Gbps vs 150 Mbps); 5G has lower latency (<1 ms vs 30–50 ms); 5G supports higher device density for IoT; 4G has wider coverage currently
>
> 2. **"Give TWO advantages of wireless networking over wired"** — no cables needed (easy installation, mobility); can connect in locations where cabling is impractical
>
> 3. **"Give TWO disadvantages of wireless networking"** — security risk (signals can be intercepted); interference from walls and other devices; generally slower than wired
>
> 4. **"What is WPA2? Why is WEP no longer recommended?"** — WPA2 is a Wi-Fi security protocol using AES encryption; WEP is easily cracked with freely available tools
>
> 5. **"Give ONE use of Bluetooth and ONE use of NFC"** — Bluetooth: wireless earphones / keyboard; NFC: contactless payment (Apple Pay/Google Pay) / tap to pair
