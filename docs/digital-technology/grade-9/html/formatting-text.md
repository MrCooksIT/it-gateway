---
title: Formatting Text in HTML
---

# Formatting Text in HTML

Text is the foundation of most web pages. HTML provides a rich set of tags for structuring and formatting text — from large headings to tiny subscripts.

## Headings

HTML has six levels of headings, from `<h1>` (largest, most important) to `<h6>` (smallest, least important):

```html
<h1>This is a Level 1 Heading</h1>
<h2>This is a Level 2 Heading</h2>
<h3>This is a Level 3 Heading</h3>
<h4>This is a Level 4 Heading</h4>
<h5>This is a Level 5 Heading</h5>
<h6>This is a Level 6 Heading</h6>
```

**How they display** (default browser styling, decreasing in size from h1 to h6):

> # H1 Heading
> ## H2 Heading
> ### H3 Heading

### Important rules for headings:

:::warning
- Use only **one `<h1>` per page** — it represents the main title of the page
- Use headings in order (don't jump from h1 to h4)
- Use headings for structure, not for making text bigger — use CSS for size
- Search engines give extra weight to h1 and h2 content
:::

## Paragraphs

```html
<p>This is a paragraph. It can contain as much text as you like.</p>

<p>This is a second paragraph. The browser automatically adds space between paragraphs.</p>
```

- Each `<p>` element creates a block of text with automatic spacing above and below
- Blank lines in your HTML code do NOT create blank lines on the page — use `<p>` for that

## Bold and Italic

### Semantic vs Presentational Tags

HTML has two ways to make text bold and two ways to make it italic:

| Tag | Meaning | When to use |
|-----|---------|------------|
| `<strong>` | **Semantically important** text | The browser shows it bold, but it also means "this is important content" |
| `<b>` | **Visually bold** only | Bold for stylistic reasons, not because content is important |
| `<em>` | **Emphasised** text | Shown in italic; means this word is spoken with emphasis |
| `<i>` | **Visually italic** only | Italic for stylistic reasons (e.g. foreign words, titles of books) |

```html
<p>This is <strong>very important</strong> information.</p>
<p>The book is called <i>To Kill a Mockingbird</i>.</p>
<p>You must <em>never</em> share your password.</p>
<p>The <b>Submit</b> button is at the bottom of the form.</p>
```

:::info
Screen readers (used by visually impaired users) give extra emphasis when reading `<strong>` and `<em>` elements — another reason to use semantically meaningful tags.
:::

## Other Text Formatting Tags

### Underline

```html
<p>This text is <u>underlined</u>.</p>
```

:::warning
Use `<u>` sparingly on web pages. Users expect underlined text to be a hyperlink. Underlined text that isn't a link is confusing.
:::

### Strikethrough

```html
<p>The original price was <s>R599</s> R399.</p>
<p>The item was <del>deleted</del> from the list.</p>
```

`<s>` = strikethrough for stylistic reasons; `<del>` = strikethrough to indicate deleted/removed content (semantic).

### Superscript and Subscript

```html
<p>Water is H<sub>2</sub>O.</p>
<p>Einstein's equation: E = mc<sup>2</sup></p>
<p>Today is 1<sup>st</sup> June 2026.</p>
```

### Line Break

```html
<p>123 Main Street<br>
Cape Town<br>
8001</p>
```

- `<br>` inserts a line break within the flow of text
- Use for addresses, poems, song lyrics — where line breaks are meaningful
- Do NOT use `<br><br>` to create spacing between paragraphs — use separate `<p>` elements instead

### Horizontal Rule

```html
<h2>Chapter 1</h2>
<p>Content here...</p>
<hr>
<h2>Chapter 2</h2>
```

`<hr>` draws a horizontal line across the page — used as a visual separator between sections.

### Blockquote

```html
<blockquote>
  "The best way to predict the future is to invent it."
  — Alan Kay
</blockquote>
```

Used for longer quotations. Browsers typically indent blockquote content.

### Preformatted Text

```html
<pre>
  This text        preserves
    all  spacing
      and line breaks exactly.
</pre>
```

`<pre>` displays text in a monospace font and preserves all whitespace — useful for displaying code or ASCII art.

### Inline Code

```html
<p>Use the <code>print()</code> function to display output.</p>
```

`<code>` marks inline code snippets, displayed in a monospace font.

### Small Text

```html
<p>This product comes with a warranty. <small>Terms and conditions apply.</small></p>
```

## A Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Text Formatting Demo</title>
</head>
<body>

  <h1>The History of the Internet</h1>

  <h2>Origins</h2>
  <p>The internet began as <strong>ARPANET</strong> in <em>1969</em>.
  It was originally a military communications network.</p>

  <h2>The World Wide Web</h2>
  <p>In <strong>1991</strong>, Tim Berners-Lee published the
  first website. His quote on the matter was:</p>

  <blockquote>
    "The web is more a social creation than a technical one."
    — Tim Berners-Lee
  </blockquote>

  <h2>Data Sizes</h2>
  <p>1 Megabyte = 1024<sup>2</sup> bytes</p>
  <p>Water has the formula H<sub>2</sub>O.</p>

  <hr>

  <p><small>Last updated: June 2026</small></p>

</body>
</html>
```

## Check Your Understanding

1. Write the HTML for a page about your favourite sport with:
   - An `<h1>` for the sport name
   - An `<h2>` for "Rules"
   - A paragraph with the word "important" in bold using the semantic tag
   - Another `<h2>` for "Famous Players"
   - A paragraph with a player's name in italics using the semantic tag

2. What is the difference between `<strong>` and `<b>`? When would you choose one over the other?

3. Write HTML to display the following address on separate lines (without using multiple paragraphs):
   ```
   Marist Brothers School
   Rivonia Boulevard
   Sandton, 2128
   ```

4. What does `<sup>` do? Write the HTML to display "x squared" correctly (x²).

5. Why should you be careful when using the `<u>` tag?

6. A learner writes:
   ```html
   <h1>Welcome</h1>
   <br><br><br>
   <h2>About Me</h2>
   ```
   What is wrong with their approach to creating space between sections?

7. What is the difference between `<s>` and `<del>`? Give an example where `<del>` is more appropriate than `<s>`.
