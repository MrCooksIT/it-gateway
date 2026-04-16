# Cloud Computing & Virtualisation

Your files are on your phone, your laptop, and accessible from any computer in the world — that's the cloud. Behind the scenes, physical servers run dozens of virtual machines simultaneously. These two technologies — cloud and virtualisation — have reshaped how businesses and individuals use computing.

> [!NOTE] Grade 11–12
> Cloud computing is introduced at Grade 11. Virtualisation and deeper cloud architecture are Grade 12 content.

---

## What is Cloud Computing?

**Cloud computing** is the delivery of computing services (servers, storage, software, databases, networking) over the internet ("the cloud"), provided by a third-party company.

Instead of owning hardware and software, you pay to use resources hosted elsewhere.

```
Traditional model: Buy server → Install software → Maintain it yourself
Cloud model:       Connect to internet → Access service → Pay for what you use
```

---

## Cloud Service Models

| Model | Full Name | What you get | You manage | Examples |
|---|---|---|---|---|
| **IaaS** | Infrastructure as a Service | Virtual hardware (CPU, storage, networking) | OS, apps, data | AWS EC2, Microsoft Azure, Google Cloud |
| **PaaS** | Platform as a Service | Development environment + runtime | Apps and data | Google App Engine, Heroku |
| **SaaS** | Software as a Service | Ready-to-use software via browser | Only your data | Gmail, Microsoft 365, Netflix, Dropbox |

> [!TIP] Memory Aid
> Think of it as a pizza analogy:
> - **IaaS** = you get a kitchen (you cook everything)
> - **PaaS** = you get pizza dough (you add toppings)
> - **SaaS** = you get a delivered pizza (just eat it)

---

## Cloud Deployment Models

| Model | Who uses it | Description |
|---|---|---|
| **Public cloud** | Anyone | Shared infrastructure owned by provider (AWS, Azure, Google) |
| **Private cloud** | One organisation | Dedicated infrastructure, greater control, higher cost |
| **Hybrid cloud** | Mixed | Combination of public and private — sensitive data on private, other services on public |
| **Community cloud** | Shared organisations | Shared by organisations with similar needs (e.g. government departments) |

---

## Advantages of Cloud Computing

| Advantage | Explanation |
|---|---|
| **Accessibility** | Access files and apps from any device, anywhere with internet |
| **Automatic backups** | Data backed up automatically by the provider |
| **Scalability** | Scale resources up or down as needed — no upfront hardware purchase |
| **Cost savings** | No capital expense on hardware; pay-as-you-go model |
| **Automatic updates** | Software updates handled by provider — always latest version |
| **Collaboration** | Multiple users can work on the same document simultaneously |
| **Disaster recovery** | Data survives local hardware failure |

---

## Disadvantages of Cloud Computing

| Disadvantage | Explanation |
|---|---|
| **Internet dependency** | No internet = no access to cloud services |
| **Privacy and security** | Data stored on third-party servers — risk of breach |
| **Ongoing cost** | Subscription costs accumulate over time — may exceed owning hardware |
| **Vendor lock-in** | Difficult to switch providers once data is stored in one ecosystem |
| **Limited control** | Cannot customise the underlying infrastructure |
| **Latency** | Network delays may slow access to data vs local storage |
| **Compliance concerns** | Data stored in other countries may face different legal jurisdictions |

---

## Cloud Storage vs Local Storage

| Feature | Cloud Storage | Local Storage (HDD/SSD) |
|---|---|---|
| Access | Anywhere with internet | Only at that device |
| Backup | Automatic | Manual |
| Cost | Ongoing subscription | Once-off purchase |
| Speed | Limited by internet | Fast (local bus speed) |
| Privacy | Third-party holds data | Full control |
| Capacity | Scalable | Fixed |
| Risk | Provider outage | Drive failure |

---

## Popular Cloud Services

| Service | Provider | Category |
|---|---|---|
| Google Drive | Google | Storage + SaaS |
| Microsoft OneDrive | Microsoft | Storage + SaaS |
| iCloud | Apple | Storage + SaaS |
| Dropbox | Dropbox | Storage |
| AWS | Amazon | IaaS + PaaS |
| Microsoft Azure | Microsoft | IaaS + PaaS + SaaS |
| Google Workspace | Google | SaaS |
| Microsoft 365 | Microsoft | SaaS |
| Netflix | Netflix | SaaS (streaming) |

---

## Virtualisation

**Virtualisation** is the process of creating a virtual (software-based) version of a physical resource — such as a server, storage device, or operating system.

A single physical computer can run multiple **virtual machines (VMs)** simultaneously, each with its own OS and applications.

```
Physical Server (1 machine)
├── Virtual Machine 1 — Windows Server 2022
├── Virtual Machine 2 — Ubuntu Linux
└── Virtual Machine 3 — Windows 10
```

---

## Hypervisors

A **hypervisor** (Virtual Machine Monitor) is software that manages and runs virtual machines on a host computer.

| Type | Description | Examples |
|---|---|---|
| **Type 1 (Bare-metal)** | Runs directly on hardware — no host OS | VMware ESXi, Microsoft Hyper-V, Xen |
| **Type 2 (Hosted)** | Runs on top of an existing OS | VirtualBox, VMware Workstation, Parallels |

**Type 1** is faster and used in enterprise data centres.  
**Type 2** is used on personal computers for testing and development.

---

## Benefits of Virtualisation

| Benefit | Explanation |
|---|---|
| **Better hardware utilisation** | One server running many VMs = less wasted capacity |
| **Cost reduction** | Fewer physical servers needed → lower hardware and energy costs |
| **Isolation** | If one VM crashes, others are unaffected |
| **Snapshots** | Save the state of a VM at a point in time — restore instantly if needed |
| **Portability** | VMs can be moved between physical hosts |
| **Quick provisioning** | Spin up a new server in minutes — no hardware ordering needed |
| **Testing environments** | Test software on different OS versions without multiple physical machines |

---

## Cloud and Virtualisation Together

Most cloud services are built on virtualisation:
- AWS, Azure, and Google Cloud all use hypervisors to create thousands of VMs
- When you launch a cloud server, you're starting a VM on their physical hardware
- This allows cloud providers to sell "virtual servers" to many customers on the same physical machine

---

## Key Terms

| Term | Definition |
|---|---|
| **Cloud computing** | Delivery of computing services over the internet |
| **IaaS** | Cloud model providing virtual hardware |
| **PaaS** | Cloud model providing development platform |
| **SaaS** | Cloud model providing ready-to-use software |
| **Virtualisation** | Creating software-based versions of physical resources |
| **Virtual machine (VM)** | Software-based computer running on a physical host |
| **Hypervisor** | Software that creates and manages virtual machines |
| **Snapshot** | Saved state of a virtual machine at a point in time |
| **Scalability** | Ability to increase or decrease resources on demand |
| **Vendor lock-in** | Difficulty of switching from one cloud provider to another |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Explain the difference between IaaS, PaaS, and SaaS. Give ONE example of each."** — IaaS: virtual hardware (AWS); PaaS: dev platform (Heroku); SaaS: software via browser (Gmail, Microsoft 365)
>
> 2. **"Give THREE advantages of cloud computing"** — accessibility from anywhere, automatic backups, scalability, cost savings, automatic updates — always explain each
>
> 3. **"Give TWO disadvantages of cloud computing"** — internet dependency (no internet = no access); privacy concerns (data stored on third-party servers); ongoing subscription cost; vendor lock-in
>
> 4. **"What is virtualisation? How does it benefit a business?"** — creating software-based versions of resources; benefits: better utilisation of hardware, cost reduction, isolation between VMs, snapshots for recovery
>
> 5. **"Explain the difference between Type 1 and Type 2 hypervisors"** — Type 1 runs directly on hardware (enterprise use, faster); Type 2 runs on host OS (personal computers, VirtualBox)
