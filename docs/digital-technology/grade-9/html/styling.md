---
title: HTML Inline Styling
---

# HTML Inline Styling

## Making Pages More Stylish

So far our web pages have been looking pretty good — we have got headers, formatted text, links, images, lists, and tables. But we can make our pages look even more stylish by adding colour, changing font sizes, and adjusting text alignment.

The way we do this is by introducing the **`style` attribute**.

---

## The `style` Attribute

The **`style` attribute** is an attribute that we can add to **any HTML tag**. It lets us add several different types of visual styles to that tag.

```html
<tagname style="property: value; property: value;">content</tagname>
```

The `style` attribute works like this:
- Inside the double quotes, we define **style properties**
- Each property has a **name** and a **value**, separated by a colon `:`
- Each property declaration ends with a semicolon `;`
- We can have **multiple styles on one tag** by separating them with semicolons

For example:

```html
<p style="color: blue;">Hello</p>
```

This paragraph will display with blue text.

```html
<h1 style="color: blue; font-size: 60px;">Hello</h1>
```

This heading will display in blue with a font size of 60 pixels.

---

## Adding Multiple Styles

We can stack as many style properties as we like on a single tag, as long as we separate them with semicolons and keep everything inside the double quotes:

```html
<p style="color: blue; background-color: yellow; font-size: 60px;">Hello</p>
```

This paragraph would display with:
- Blue text
- A yellow background (highlighted)
- Text that is 60 pixels tall

---

## Style Properties

Here are the key style properties you can use:

### `color`

The `color` property defines the **text colour** for the tag. All text inside that tag — including text in any nested tags — will have that colour.

```html
<p style="color: red;">This text is red.</p>
<h1 style="color: navy;">This heading is navy blue.</h1>
```

### `background-color`

The `background-color` property sets the **background colour** for the entire tag area — like a highlighter effect.

```html
<p style="background-color: yellow;">This is highlighted yellow.</p>
<ul style="background-color: navy; color: white;">...</ul>
```

### `font-size`

The `font-size` property controls how large the text is. We specify the size in **pixels**.

```html
<p style="font-size: 12px;">Small text</p>
<p style="font-size: 30px;">Medium text</p>
<p style="font-size: 60px;">Large text</p>
```

### `text-align`

The `text-align` property controls the **alignment** of the text within the tag. Options include:

| Value | Effect |
|-------|--------|
| `left` | Aligns text to the left (default) |
| `center` | Centres the text |
| `right` | Aligns text to the right |

```html
<h1 style="text-align: center;">Centred Heading</h1>
<p style="text-align: right;">Right-aligned text</p>
```

### `list-style-type`

For lists, we can change the type of bullet or marker used with the `list-style-type` property:

```html
<ul style="list-style-type: square;">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

For ordered lists, we can change from numbers to letters:

```html
<ol style="list-style-type: lower-alpha;">
  <li>First item</li>
  <li>Second item</li>
</ol>
```

`lower-alpha` gives us lowercase letters (a, b, c) instead of numbers.

---

## HTML Colour Names

You may be wondering: what colours can I use? It turns out there are **140 colours that have names in HTML**. You have your standard colours like red, blue, and green, but there are also some unusual ones — like `cyan`, `blanchedalmond`, and `darkgoldenrod`.

Some examples:

```html
<p style="color: red;">Red text</p>
<p style="color: navy;">Navy text</p>
<p style="color: olive;">Olive text</p>
<p style="color: darkgoldenrod;">Dark golden rod text</p>
<p style="color: chocolate;">Chocolate text</p>
```

:::tip
You can find a full list of all 140 HTML colour names at **w3schools.com**. Simply search for "HTML color names" to see the complete list and what each colour looks like.
:::

---

## Styling Individual List Items

We can apply different styles to individual `<li>` tags:

```html
<ol style="list-style-type: lower-alpha; font-size: 18px;">
  <li style="color: chocolate;">Chocolate chip</li>
  <li style="color: darkgoldenrod;">Oatmeal raisin</li>
  <li style="color: brown;">Peanut butter</li>
</ol>
```

Each cookie type gets its own colour, making the list visually distinct.

---

## A Complete Styled Example

Here is a complete example that styles a heading and a list:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Styled Page</title>
  </head>
  <body>
    <h1 style="color: olive; font-size: 50px;">My Grocery List</h1>
    <ul style="list-style-type: square; font-size: 20px; color: navy;">
      <li>Apples</li>
      <li>Milk</li>
      <li>Cookies
        <ol style="list-style-type: lower-alpha; font-size: 18px;">
          <li style="color: chocolate;">Chocolate chip</li>
          <li style="color: darkgoldenrod;">Oatmeal raisin</li>
          <li style="color: brown;">Peanut butter</li>
        </ol>
      </li>
      <li>Bread</li>
    </ul>
  </body>
</html>
```

---

## Summary of Style Properties

| Property | What it changes | Example value |
|----------|----------------|--------------|
| `color` | Text colour | `red`, `navy`, `olive` |
| `background-color` | Background colour behind the element | `yellow`, `blue` |
| `font-size` | Size of the text | `20px`, `60px` |
| `text-align` | Alignment of text | `left`, `center`, `right` |
| `list-style-type` | Bullet/marker type for lists | `square`, `lower-alpha` |

---

## Check Your Understanding

1. What is the `style` attribute? Which HTML tags can it be added to?

2. What is the format of a style declaration inside the `style` attribute? Describe both the syntax and give an example.

3. Write the HTML for a paragraph that displays the text "Welcome!" in red with a font size of 30 pixels.

4. Write the HTML for a heading that is centred, has an olive colour, and a font size of 50 pixels.

5. How can you add multiple style properties to a single tag? Write an example with at least three properties.

6. What does the `background-color` property do? How is it different from the `color` property?

7. Write the HTML for an unordered list that uses square bullets, has a navy text colour, and a font size of 20 pixels. Include at least three items.

8. How many named colours does HTML provide? Where can you find the full list?

9. Write the HTML for an ordered list that uses lowercase letters (a, b, c) instead of numbers, with at least three items.

10. **Extended question:** Look at this style attribute: `style="color: blue; background-color: yellow; font-size: 60px;"` — what will the element look like? Describe it in words, and explain what each of the three properties is doing.
