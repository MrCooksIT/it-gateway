---
title: Privacy & Security
---

# Privacy & Security

## Introduction

Think about your bedroom. You probably feel entitled to some privacy in there — to have a space that is yours, where you can keep your personal things without everyone having access to them. You would not leave your front door open and invite strangers to walk through your house whenever they felt like it.

Your digital life is the same, but in many ways it is even more exposed. Every device you use, every app you download, and every website you visit is, by default, collecting data about you. The question is not whether data is being collected — it is whether you understand what is being collected, and whether you are taking steps to protect yourself.

This chapter covers two closely related concepts: **privacy** (your right to control your personal information) and **security** (the tools and habits that protect your data and devices from unauthorised access).

---

## Privacy vs Security: What's the Difference?

These two words are often used together, but they mean different things.

:::tip Key Term
**Privacy** is your right to control who has access to your personal information — to decide what you share, with whom, and when.
:::

:::tip Key Term
**Cybersecurity** (or digital security) is the set of practices, tools, and systems used to protect devices, networks, and data from unauthorised access, damage, or attack.
:::

A useful analogy: imagine a diary. **Privacy** is your decision about who you want to read it — maybe nobody, maybe just your best friend. **Security** is the lock you put on the diary to enforce that decision. You need both: privacy tells you what to protect, and security gives you the means to protect it.

---

## Creating Strong Passwords

Passwords are the first line of defence for almost every account you have. Despite this, weak passwords remain one of the most common causes of account compromise. Every year, analysis of leaked passwords shows that millions of people use passwords like `123456`, `password`, or their own first name.

### What Makes a Password Strong?

:::tip Key Term
A **strong password** is one that would be extremely difficult for a person or a computer program to guess. It is long, uses a variety of characters, does not contain personal information, and is used for only one account.
:::

| Feature | Why It Matters | Example |
|---|---|---|
| **Length (12+ characters)** | Every extra character multiplies the time needed to crack it | `Th!sIsLong3r` |
| **Uppercase letters** | Increases complexity | `MixingCases` |
| **Lowercase letters** | Standard base | `mixingcases` |
| **Numbers** | Adds variety | `m1x1ngc4s3s` |
| **Special characters (!@#$%^&*)** | Greatly increases difficulty | `m1x!ngC@s3s` |
| **No personal information** | Prevents guessing from social media | Not your name, birthday, or pet's name |
| **Unique per account** | Limits damage if one account is compromised | Different for every site |

### The Passphrase Method

One of the most effective techniques for creating a strong, memorable password is the **passphrase** — a sequence of random, unrelated words.

For example: `CorrectHorseBatteryStaple49!`

This password is:
- Very long (28 characters)
- Completely random in the combination of words
- Memorable (you can picture each word)
- Difficult to crack (even for a computer)

### What to Avoid

:::danger Weak Password Patterns
- Using your name, birth date, school name, or pet's name
- Using `password`, `123456`, or `qwerty`
- Using the same password across multiple accounts
- Making small variations like adding "1" to your old password (`OldPassword1`)
- Sharing passwords with friends, even your closest ones
:::

---

## Password Managers

If every account needs a different, strong, 12+ character password, how is anyone expected to remember them all? The answer is: you don't need to. A password manager does it for you.

:::tip Key Term
A **password manager** is a secure application that stores all your passwords in an encrypted vault. You only need to remember one master password to unlock it. The manager can also generate strong passwords for you automatically.
:::

### How a Password Manager Works

1. You create one strong master password to access the manager itself.
2. When you create a new account, the manager generates a unique, complex password for it.
3. The manager saves that password in your encrypted vault.
4. Next time you visit that site, the manager fills in your password automatically.
5. Your passwords are synced across your devices so you always have access.

### Popular Password Managers

| Manager | Cost | Notes |
|---|---|---|
| **Bitwarden** | Free (basic) | Open source, highly trusted |
| **Google Password Manager** | Free | Built into Chrome/Android |
| **Apple Keychain** | Free | Built into iOS/macOS |
| **1Password** | Paid | Popular for families and teams |

:::info
Your school may have a recommended password manager. Ask your IT department or teacher.
:::

---

## Two-Factor Authentication (2FA)

Even a strong password can be stolen — through phishing, data breaches, or someone watching over your shoulder. **Two-factor authentication** adds a second layer of protection so that a stolen password alone is not enough to access your account.

:::tip Key Term
**Two-factor authentication (2FA)**, also called two-step verification, is a security process where you must provide two different forms of proof of identity before being granted access to an account.
:::

### How 2FA Works

When you enable 2FA on an account:

1. You log in with your username and password (factor 1: something you **know**).
2. The service sends a unique code to your phone number or authentication app (factor 2: something you **have**).
3. You enter that code within a short time window.
4. Only then are you logged in.

Even if a hacker has your password, they cannot get into your account without also having access to your phone.

### Types of 2FA

| Method | How It Works | Security Level |
|---|---|---|
| **SMS code** | A code is sent to your phone via text message | Basic — can be intercepted |
| **Authenticator app** | An app (like Google Authenticator) generates a time-based code | Better — codes are local to your device |
| **Email code** | A code is sent to your email address | Moderate — only as secure as your email |
| **Biometric** | Uses your fingerprint or face scan | Strong — unique to you |
| **Physical security key** | A USB device that must be plugged in | Very strong — used by high-security accounts |

:::info Recommendation
Enable 2FA on every account that supports it — especially your email, social media, and any account linked to financial information. An authenticator app (like Google Authenticator or Authy) is more secure than SMS codes.
:::

---

## Privacy Settings on Social Media, Apps, and Devices

Privacy settings are controls that allow you to limit who can see your information and what data apps are allowed to access. Most services are configured to collect as much data as possible by default — it is up to you to change that.

### Social Media Privacy Settings

| Setting | What It Controls | Recommended Setting |
|---|---|---|
| **Profile visibility** | Who can see your profile | Private/Friends only |
| **Post visibility** | Who can see your posts | Friends only |
| **Location tagging** | Whether your location is attached to posts | Disabled |
| **Story visibility** | Who can see your Stories | Friends only |
| **Searchability** | Whether strangers can find you by name/email | Limited or off |
| **Who can message you** | Who can send you direct messages | Friends only |
| **Tagged photos** | Whether others can tag you in photos | Requires your approval |

### App Permissions on Your Phone

When you install an app, it requests access to various features of your phone — your camera, microphone, contacts, location, and more. Many apps request far more access than they actually need to function.

:::warning Check Your App Permissions
- Does a flashlight app need access to your contacts? **No.**
- Does a recipe app need access to your microphone? **No.**
- Does a social media app need to track your location even when you're not using it? **Probably not.**

Review your app permissions regularly: **Settings > Privacy > Permissions** (on most Android and iOS devices).
:::

### Device Settings

| Setting | Why It Matters |
|---|---|
| **Screen lock / PIN / Biometric** | Prevents physical access to your device if lost or stolen |
| **Automatic OS updates** | Updates patch security vulnerabilities |
| **"Find my device"** | Allows you to locate, lock, or wipe a lost device |
| **Disable Bluetooth when not in use** | Open Bluetooth can be a security vulnerability |
| **Review connected devices** | Revoke access from old/unused devices |

---

## What Data Websites Collect

Every time you visit a website, data about you is collected. Understanding what is collected and how it is used is a key part of digital privacy.

### A Worked Example: Visiting a Website

Here is what happens in the background when you visit a typical website:

**Step 1: Your IP address is logged.**
Your IP address is a number that identifies your internet connection and can be used to determine your approximate location. Every website you visit logs your IP address.

**Step 2: Cookies are placed on your device.**
The website places small text files (cookies) on your device. These record information like:
- Whether you are logged in
- Items in your shopping cart
- Your preferences and settings
- How many times you have visited

**Step 3: Tracking pixels activate.**
Many websites embed a tiny, invisible image (one pixel) that, when loaded, sends data to third parties (like Facebook or Google) about which page you visited and when — even if you don't have those platforms open.

**Step 4: Analytics tools record your behaviour.**
Tools like Google Analytics record which pages you visited, how long you spent, what you clicked, how far you scrolled, and which device and browser you used.

**Step 5: Advertising networks build a profile.**
Advertising networks aggregate data about your browsing across many different websites to build a detailed profile of your interests, which they then use to target you with specific advertisements.

:::info Did You Know?
When you search for something on Google or browse a type of product online, you often start seeing adverts for that product everywhere — on other websites, on YouTube, on Instagram. This is not a coincidence. It is the result of tracking and behavioural advertising.
:::

### Types of Cookies

| Cookie Type | Purpose |
|---|---|
| **Necessary/Essential** | Required for the website to function (e.g. keeping you logged in) |
| **Preferences/Functional** | Remembers your settings and choices |
| **Analytics** | Tracks how you use the site to improve it |
| **Marketing/Advertising** | Tracks you across sites to serve targeted ads |

You can choose to reject marketing and analytics cookies when websites ask (the pop-up that appears when you first visit). Choosing "necessary only" reduces the data collected about you.

---

## Identity Theft

:::tip Key Term
**Identity theft** is when someone obtains your personal information and uses it to impersonate you — typically for financial gain, such as opening accounts, making purchases, or taking out loans in your name.
:::

### How Identity Theft Happens

- **Data breaches:** A company's database is hacked and your information is stolen
- **Phishing:** You are tricked into providing your details to a fake website
- **Social engineering:** Someone manipulates you into revealing information over the phone or online
- **Physical theft:** Someone steals a wallet, ID document, or device containing personal information
- **Public Wi-Fi snooping:** On unsecured networks, data can be intercepted

### Consequences of Identity Theft

- Fraudulent bank accounts or loans in your name
- Criminal records created under your identity
- Damage to your credit record that can affect you for years
- Significant time and effort required to resolve

### Prevention

| Action | Why It Helps |
|---|---|
| Use unique, strong passwords | Limits damage from any single breach |
| Enable 2FA | Makes stolen passwords insufficient |
| Never share personal info online | Reduces the data available to attackers |
| Check your accounts regularly | Spot unusual activity early |
| Shred documents with personal information | Prevents physical theft of data |
| Monitor your credit record | Detect fraud early (adults can do this through credit bureaus) |

---

## Data Breaches

:::tip Key Term
A **data breach** is an incident where sensitive, confidential, or private information is accessed, disclosed, or stolen without authorisation. Breaches can affect millions of people at once when a company's systems are compromised.
:::

You may have had your data exposed in a breach without knowing it. Companies including major social media platforms, banks, and retailers have all experienced significant data breaches.

### What to Do If Your Data Is Leaked

1. **Check if you were affected.** Visit **haveibeenpwned.com** (a free, legitimate service) and enter your email address. It will tell you if your email has appeared in any known data breaches.
2. **Change your password** for the affected account immediately — and for any other account where you used the same password.
3. **Enable 2FA** if you haven't already.
4. **Watch for phishing.** Attackers who obtain your email from a breach may try to follow up with targeted phishing attempts.
5. **Contact your bank** if financial information was compromised.

:::info Have I Been Pwned?
The website **haveibeenpwned.com** was created by a security researcher and is widely trusted. It shows you which data breaches have included your email address and what type of data was exposed. Checking it regularly is a good security habit.
:::

---

## Keeping Devices Secure

Your smartphone and computer contain enormous amounts of personal data. Keeping them physically and digitally secure is essential.

### Checklist: Securing Your Device

- [ ] Use a strong PIN, password, or biometric lock — not `0000` or `1234`
- [ ] Enable automatic screen lock after a short period of inactivity
- [ ] Keep your operating system and apps updated
- [ ] Only install apps from official stores (Google Play, Apple App Store)
- [ ] Review app permissions and revoke unnecessary access
- [ ] Enable "Find My Phone" / "Find My Device"
- [ ] Back up your data regularly
- [ ] Be careful about charging via USB in public places (data can be transferred via charging cables in a practice called "juice jacking")

### Operating System Updates

:::warning Do Not Ignore Updates
Software updates are not just about new features. A large portion of every update involves **security patches** — fixes for vulnerabilities that have been discovered. Ignoring updates leaves known security holes in your system that attackers can exploit. Enable automatic updates where possible.
:::

---

## Scenario: The Data Trail of One Afternoon Online

Follow Thandi through an ordinary afternoon online and notice all the data being collected.

> **3:30pm** — Thandi gets home and opens Chrome. She searches "Converse sneakers cheap South Africa." Google logs the search query, her IP address, and the time.

> **3:32pm** — She clicks on an online shoe shop. The shop logs her IP address, places several cookies on her device (including advertising cookies), and fires a Facebook Pixel that sends her visit to Facebook's servers.

> **3:40pm** — She opens Instagram. Instagram shows her adverts for sneakers. Her browsing has already been matched to her profile.

> **3:45pm** — She watches a YouTube video about sneaker reviews. YouTube logs her watch history and serves her related recommendations — and more shoe adverts.

> **4:00pm** — She fills in a competition entry form: name, email, phone number. This information is sold to a marketing company.

> **4:15pm** — She gets an email to her Gmail inbox saying "Your account has been compromised, click here to verify." She almost clicks it before noticing the sender's address is `googIe-support@mail.ru`. It is a phishing email.

In less than one hour, Thandi's data was collected by at least six different companies, she was tracked across multiple platforms, and she nearly fell for a phishing attempt.

---

## Summary

| Concept | Key Point |
|---|---|
| Privacy | Your right to control your personal information |
| Security | Tools and habits to protect data from unauthorised access |
| Strong passwords | Long, complex, unique, and no personal info |
| Password managers | Store all passwords securely; you remember only one |
| Two-factor authentication | Second layer of proof; makes stolen passwords useless alone |
| Data collection | Websites collect IP addresses, cookies, and behavioural data |
| Identity theft | Using someone else's information to impersonate them |
| Data breaches | Check haveibeenpwned.com; change passwords immediately |
| Device security | Update, lock, review permissions |

---

## Check Your Understanding

1. Explain the difference between privacy and cybersecurity using an analogy of your own.
2. List **five** features of a strong password and explain why each one matters.
3. Create an example of a strong passphrase (do not use the one in this chapter) and explain why it is better than a simple password like `Zara2010`.
4. What is two-factor authentication? Describe how it works using a step-by-step example.
5. Why is receiving a 2FA code via an authenticator app more secure than receiving one via SMS?
6. Describe **three** types of data that a website collects when you visit it. Explain what each type is used for.
7. What is identity theft? Describe two ways it can happen and two steps you can take to prevent it.
8. A friend says, "I don't need to bother with security updates — they just slow my phone down." Write a response explaining why this attitude is risky.
9. What is a data breach? Describe the steps you should take if you discover that your data has been leaked.
10. Read the following scenario and answer the questions:
    > Siphamandla uses the same password — `soccer2011` — for his Gmail, Instagram, and school portal. His Gmail is hacked in a data breach and his password is exposed.
    - (a) Why is using the same password across multiple accounts particularly dangerous?
    - (b) What does `soccer2011` score on the strong password checklist? Identify its weaknesses.
    - (c) List the steps Siphamandla should take immediately.
    - (d) What could he have done beforehand to protect himself?
