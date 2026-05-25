---
title: HTML Lists
---

# HTML Lists

## Why Use Lists?

Lists show up everywhere on the internet. We see articles like "Six quotes from an author", rankings, instructions, and countless other lists every day. There are good reasons for this — lists are a valuable tool:

- Lists make it very easy to **organise information**
- They have a very **simple structure**
- They are very **easy to read** and write
- We can use numbers or letters to **arrange things in order** — from most important to least important
- Lists can be about **anything**

Because lists are so common on web pages, HTML provides built-in tags specifically for creating them.

---

## Two Types of Lists in HTML

There are two main types of lists in HTML:

| Type | When to use | Appearance |
|------|-------------|-----------|
| **Unordered list** | When there is no specific order to the items — just bullet points | Bullet points (•) |
| **Ordered list** | When order matters — first, second, third | Numbers (1, 2, 3) |

---

## Unordered Lists

To make an **unordered list**, we use the **`<ul>` tag** (short for **u**nordered **l**ist). Inside the `<ul>` tag, each item in the list gets its own **`<li>` tag** (short for **l**ist **i**tem).

```html
<ul>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Milk</li>
  <li>Bread</li>
</ul>
```

The result is a bulleted list:
- Apples
- Bananas
- Milk
- Bread

### Tags Used

- `<ul>` — defines the unordered list (the container)
- `<li>` — defines each individual list item inside the list

---

## Ordered Lists

For an **ordered list**, we use the **`<ol>` tag** (short for **o**rdered **l**ist). Can you guess? `ul` for unordered, `ol` for ordered.

Just like with `<ul>`, we use an `<li>` tag for each item inside the list. The `<li>` tag simply defines a list item — it does not care whether it is part of an ordered or unordered list.

```html
<ol>
  <li>Apples</li>
  <li>Cookies</li>
  <li>Milk</li>
  <li>Bread</li>
</ol>
```

The result is a numbered list:
1. Apples
2. Cookies
3. Milk
4. Bread

Instead of bullet points, we now have 1, 2, 3, 4 — the items are numbered automatically by the browser.

---

## Nested Lists

You might be wondering: what if a list item could contain its own smaller list? It can! We can put lists inside of lists. This is called **nesting lists**.

For example, suppose I have a grocery list with apples, cookies, and milk. But I want to give more detail about exactly which cookies I am buying. I can put a list inside the `cookies` list item to list out the types:

```html
<ul>
  <li>Apples</li>
  <li>Cookies
    <ul>
      <li>Chocolate chip</li>
      <li>Peanut butter</li>
    </ul>
  </li>
  <li>Milk</li>
</ul>
```

Notice that the nested `<ul>` goes **inside** the `<li>` for "Cookies" — not after it. The entire cookies item (including its sub-list) is one list item in the outer list.

We can even go a level deeper. If I want to be more specific about what kind of chocolate chips:

```html
<ul>
  <li>Apples</li>
  <li>Cookies
    <ul>
      <li>Chocolate chip
        <ol>
          <li>White chocolate chip</li>
          <li>Dark chocolate chip</li>
        </ol>
      </li>
      <li>Peanut butter</li>
    </ul>
  </li>
  <li>Milk</li>
</ul>
```

Notice that every time we nest a list, we **indent** it over. The indentation shows the nesting structure — which items belong to which list.

You can also mix ordered and unordered lists. The outer list is unordered (bullet points), but the inner list for the types of chocolate chips is ordered (numbered).

---

## Building a Grocery List

Here is a complete example — a simple grocery list web page:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Grocery List</title>
  </head>
  <body>
    <h1>My Grocery List</h1>
    <ul>
      <li>Apples</li>
      <li>Milk</li>
      <li>Cookies
        <ol>
          <li>Chocolate chip</li>
          <li>Peanut butter</li>
          <li>Oatmeal raisin</li>
        </ol>
      </li>
      <li>Bread</li>
    </ul>
  </body>
</html>
```

The grocery list is unordered (the overall items have no specific order), but the cookie types are ordered (perhaps we want them in priority order).

---

## Summary

| Tag | Full Name | Purpose |
|-----|-----------|---------|
| `<ul>` | Unordered List | Container for a bulleted list |
| `<ol>` | Ordered List | Container for a numbered list |
| `<li>` | List Item | Each individual item in either type of list |

:::tip
The `<li>` tag is used regardless of whether you are inside a `<ul>` or an `<ol>`. It simply means "this is one item in the list."
:::

---

## Check Your Understanding

1. What is the difference between an unordered list and an ordered list? Give an example of when you would use each.

2. What do the tags `<ul>`, `<ol>`, and `<li>` stand for?

3. Write the HTML for an unordered list with four items: Apples, Bananas, Milk, and Bread.

4. Write the HTML for an ordered list showing the steps to make toast (at least 3 steps).

5. What is a nested list? In your own words, explain how to create one.

6. Write a nested list with "Fruit" and "Vegetables" as the outer items, and at least two items nested inside each.

7. When nesting a list, where exactly does the inner `<ul>` or `<ol>` go — inside the `<li>` or after it? Why does this matter?

8. Can you mix ordered and unordered lists when nesting? Give an example of when this might be useful.
