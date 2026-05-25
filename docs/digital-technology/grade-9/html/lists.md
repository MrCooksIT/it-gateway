---
title: HTML Lists
---

# HTML Lists

Lists are one of the most commonly used HTML structures. They organise information clearly and are also the building block for navigation menus.

## Unordered Lists

An **unordered list** is used when the order of items doesn't matter — such as a shopping list or list of features. Items are displayed with bullet points by default.

```html
<ul>
  <li>Keyboard</li>
  <li>Mouse</li>
  <li>Monitor</li>
  <li>Speakers</li>
</ul>
```

**Output:**
- Keyboard
- Mouse
- Monitor
- Speakers

- `<ul>` = unordered list container
- `<li>` = list item (used inside both `<ul>` and `<ol>`)

## Ordered Lists

An **ordered list** is used when the sequence matters — such as steps in a process or a ranking.

```html
<ol>
  <li>Open your text editor</li>
  <li>Type your HTML code</li>
  <li>Save the file as index.html</li>
  <li>Open it in a browser</li>
</ol>
```

**Output:**
1. Open your text editor
2. Type your HTML code
3. Save the file as index.html
4. Open it in a browser

### Ordered List Variations

The `type` attribute changes the numbering/lettering style:

| Attribute | Style | Example |
|-----------|-------|---------|
| `type="1"` | Decimal numbers (default) | 1, 2, 3 |
| `type="A"` | Uppercase letters | A, B, C |
| `type="a"` | Lowercase letters | a, b, c |
| `type="I"` | Uppercase Roman numerals | I, II, III |
| `type="i"` | Lowercase Roman numerals | i, ii, iii |

```html
<ol type="A">
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

**Output:** A. First item, B. Second item, C. Third item

The `start` attribute changes where numbering begins:

```html
<ol start="5">
  <li>Fifth item</li>
  <li>Sixth item</li>
</ol>
```

The `reversed` attribute counts down:

```html
<ol reversed>
  <li>Gold medal</li>
  <li>Silver medal</li>
  <li>Bronze medal</li>
</ol>
```
**Output:** 3. Gold medal, 2. Silver medal, 1. Bronze medal

## Nested Lists

Lists can be placed inside other lists to create **nested lists** — useful for outlines, submenus, and hierarchical information.

```html
<ul>
  <li>Hardware
    <ul>
      <li>Input devices
        <ul>
          <li>Keyboard</li>
          <li>Mouse</li>
        </ul>
      </li>
      <li>Output devices
        <ul>
          <li>Monitor</li>
          <li>Printer</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Software
    <ul>
      <li>System software</li>
      <li>Application software</li>
    </ul>
  </li>
</ul>
```

:::warning
When nesting, place the nested `<ul>` or `<ol>` **inside** the `<li>` element — not after it:

```html
<!-- CORRECT -->
<li>Hardware
  <ul>
    <li>CPU</li>
  </ul>
</li>

<!-- WRONG — nested list is outside the li -->
<li>Hardware</li>
<ul>
  <li>CPU</li>
</ul>
```
:::

## Description Lists

A **description list** is used for terms and their definitions — like a glossary.

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language — the standard language for creating web pages.</dd>

  <dt>CSS</dt>
  <dd>Cascading Style Sheets — used to control the appearance of HTML elements.</dd>

  <dt>JavaScript</dt>
  <dd>A programming language that adds interactivity to web pages.</dd>
</dl>
```

- `<dl>` = description list container
- `<dt>` = description term (the word or phrase being defined)
- `<dd>` = description details (the definition or explanation)

By default, `<dt>` appears bold and `<dd>` is indented.

## Lists for Navigation Menus

Navigation bars are built with lists. A horizontal menu is an unordered list styled with CSS:

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

Without CSS this displays as a vertical bullet list. CSS transforms it into a horizontal menu bar by changing the list items to `display: inline` or `display: flex`.

## A Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lists Demo</title>
</head>
<body>

  <h1>Computer Components</h1>

  <h2>Types of Hardware</h2>
  <ul>
    <li>Input Devices
      <ul>
        <li>Keyboard</li>
        <li>Mouse</li>
        <li>Scanner</li>
      </ul>
    </li>
    <li>Processing
      <ul>
        <li>CPU</li>
        <li>GPU</li>
      </ul>
    </li>
    <li>Output Devices
      <ul>
        <li>Monitor</li>
        <li>Printer</li>
      </ul>
    </li>
  </ul>

  <h2>Steps to Create a Website</h2>
  <ol>
    <li>Plan your content and structure</li>
    <li>Write the HTML</li>
    <li>Add CSS styling</li>
    <li>Test in multiple browsers</li>
    <li>Publish your website</li>
  </ol>

  <h2>Key Terms</h2>
  <dl>
    <dt>Browser</dt>
    <dd>Software used to access and view websites.</dd>

    <dt>URL</dt>
    <dd>Uniform Resource Locator — the address of a web page.</dd>
  </dl>

</body>
</html>
```

## Check Your Understanding

1. What is the difference between `<ul>` and `<ol>`? Give an example of when you would use each.
2. Write the HTML for an ordered list of the steps to boil an egg (at least 4 steps).
3. Write an unordered list about your favourite subject with at least two sub-topics nested under each item.
4. What does the `type="A"` attribute do to an `<ol>`? Write an example.
5. What is a `<dl>` and when would you use it? Write a description list with three programming terms and their definitions.
6. A learner creates a navigation bar using three separate `<p>` tags instead of a list. What would be a better approach and why?
7. What is wrong with the following HTML?
   ```html
   <ul>
   <li>Fruit</li>
   <ul>
     <li>Apple</li>
     <li>Banana</li>
   </ul>
   <li>Vegetables</li>
   </ul>
   ```
