# Network Topologies

The arrangement of devices in a network — how they connect to each other physically and logically — is called the **topology**. The choice of topology affects cost, performance, reliability, and how easy it is to add or remove devices.

> [!NOTE] Grade 11
> Network topologies are a Grade 11 topic. You need to know the diagram, advantages, and disadvantages of each topology for Paper 2.

---

## What is a Topology?

**Physical topology** — the actual layout of cables and devices.  
**Logical topology** — how data flows through the network (may differ from physical).

The four main topologies you need to know:

| Topology | Shape | Key feature |
|---|---|---|
| **Star** | Devices connect to central switch/hub | Most common; central failure = total failure |
| **Bus** | All devices on one shared cable | Simple; cable break = network fails |
| **Ring** | Devices in a circle; data travels one way | Each device regenerates signal; one break = network fails |
| **Mesh** | Every device connects to every other | Most reliable; very expensive |

---

## Star Topology

All devices connect to a **central switch or hub**. No direct connection between end devices.

```
    PC1       PC2
      \       /
       SWITCH
      /   |   \
   PC3   PC4   PC5
```

### Advantages
- If one cable fails, only that device is affected — rest of network continues
- Easy to add or remove devices without disrupting network
- Easier to detect faults and isolate problems
- High performance — dedicated connection per device (with switch)
- Most commonly used topology in modern LANs

### Disadvantages
- Central switch/hub is a **single point of failure** — if it fails, entire network fails
- Requires more cable than bus topology
- Higher cost — central device must handle all connections

---

## Bus Topology

All devices connect to a single **shared backbone cable**. Data travels along the cable and all devices see every packet.

```
PC1 --- PC2 --- PC3 --- PC4 --- PC5
|_______________________________|
         Backbone cable
        (terminated at both ends)
```

A **terminator** is placed at each end of the cable to prevent signal bounce.

### Advantages
- Simple and inexpensive to set up
- Less cable used than star or mesh
- Easy to extend (add devices to the cable)
- Suitable for small networks

### Disadvantages
- A break anywhere in the backbone cable = **entire network fails**
- All devices share bandwidth → performance degrades as more devices are added
- Data collisions are common (all devices transmit on the same medium)
- Difficult to isolate faults — entire cable must be checked
- Not suitable for large networks

---

## Ring Topology

Devices are connected in a **closed loop** (ring). Data travels in one direction around the ring, passing through each device until it reaches its destination.

```
     PC1
    /    \
  PC4    PC2
    \    /
     PC3
```

Each device acts as a **repeater**, boosting the signal as it passes through.

**Token Ring** (older technology): a "token" passes around the ring; only the device holding the token can transmit.

### Advantages
- No data collisions (only one device transmits at a time)
- Each device regenerates the signal — performs well over longer distances
- Equal access for all devices

### Disadvantages
- A single break in the ring = **entire network fails**
- Difficult to add or remove devices without disrupting the network
- Slower than star topology in modern implementations
- Largely replaced by star topology using Ethernet switches

---

## Mesh Topology

Every device connects directly to every other device. Two types:

- **Full mesh**: every device has a direct link to every other device
- **Partial mesh**: some devices have multiple connections, not all

```
PC1 ——— PC2
 |  \  / |
 |   \/  |
 |   /\  |
 |  /  \ |
PC3 ——— PC4
```

Full mesh with 5 devices requires: n(n-1)/2 = 10 connections.

### Advantages
- **Highly redundant** — multiple paths between devices; network continues if a link fails
- No single point of failure
- High performance — dedicated links between pairs of devices
- Used in critical infrastructure (internet backbone, military networks)

### Advantages (summary)
| Feature | Result |
|---|---|
| Redundancy | If one link fails, data takes another path |
| No congestion | Dedicated links between pairs |
| Reliability | Most reliable of all topologies |

### Disadvantages
- **Very expensive** — number of cables grows rapidly with more devices
- Complex to install and manage
- Impractical for large LANs

---

## Topology Comparison

| Feature | Star | Bus | Ring | Mesh |
|---|---|---|---|---|
| Central device | Switch/Hub | None | None | None |
| Cable used | Moderate | Least | Moderate | Most |
| Cost | Moderate | Low | Moderate | Very high |
| Reliability | Medium (single point of failure) | Low | Low | Very high |
| Failure impact | One device loses connection | Whole network | Whole network | Minimal |
| Modern use | Very common | Rare | Rare | Internet backbone |
| Fault detection | Easy | Difficult | Difficult | Easy |

---

## Key Terms

| Term | Definition |
|---|---|
| **Topology** | The arrangement/layout of devices in a network |
| **Physical topology** | Actual physical layout of cables and devices |
| **Logical topology** | How data logically flows through the network |
| **Star topology** | All devices connect to a central switch |
| **Bus topology** | All devices on a single shared backbone cable |
| **Ring topology** | Devices form a closed loop; data travels in one direction |
| **Mesh topology** | Every device connects to every other device |
| **Terminator** | Device placed at ends of a bus cable to prevent signal bounce |
| **Single point of failure** | One component whose failure brings down the whole system |
| **Token** | Control signal passed around a ring; device holding it can transmit |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Give TWO advantages of a star topology"** — failure of one cable only affects that device; easy to add/remove devices; easy fault detection
>
> 2. **"Give TWO disadvantages of a star topology"** — central switch is a single point of failure; requires more cable than bus; higher cost
>
> 3. **"Which topology is most reliable? Explain why."** — Mesh; multiple paths exist between devices so if one link fails, data takes an alternative route
>
> 4. **"What happens if the backbone cable in a bus topology breaks?"** — The entire network fails because all devices share the same cable
>
> 5. **"Why is a ring topology rarely used in modern networks?"** — A single break fails the entire network; star topology with switches is faster and easier to manage
