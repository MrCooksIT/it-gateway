---
title: HTML Tables
---

# HTML Tables

HTML tables are used to display **structured, tabular data** — information that naturally organises into rows and columns, like a timetable, price list, or comparison chart.

:::warning
Tables are for **data**, not for page layout. In the early web, tables were misused to position elements on pages. Modern web design uses CSS (Flexbox, Grid) for layout. Using tables for layout is bad practice.
:::

## Basic Table Structure

A table is built from nested elements:

```html
<table>
  <tr>
    <th>Name</th>
    <th>Grade</th>
    <th>Mark</th>
  </tr>
  <tr>
    <td>Sipho</td>
    <td>9</td>
    <td>78%</td>
  </tr>
  <tr>
    <td>Aisha</td>
    <td>9</td>
    <td>92%</td>
  </tr>
</table>
```

| Element | What it does |
|---------|-------------|
| `<table>` | Container for the entire table |
| `<tr>` | Table Row — wraps a row of cells |
| `<th>` | Table Header cell — displayed **bold and centred** by default |
| `<td>` | Table Data cell — regular content |

**Output** (no borders by default):

Name | Grade | Mark
-----|-------|-----
Sipho | 9 | 78%
Aisha | 9 | 92%

## Adding Visible Borders

By default, tables have no visible borders. The `border` attribute adds simple borders:

```html
<table border="1">
  ...
</table>
```

:::info
The `border` attribute is considered old-fashioned (deprecated in HTML5). For production websites, use CSS to style table borders. But for quick practice, `border="1"` is fine.
:::

## Table Caption

A caption gives the table a title, displayed above (or below) it:

```html
<table border="1">
  <caption>Class Test Results — June 2026</caption>
  <tr>
    <th>Name</th>
    <th>Mark</th>
  </tr>
  <tr>
    <td>Lerato</td>
    <td>85%</td>
  </tr>
</table>
```

## Semantic Grouping: `<thead>`, `<tbody>`, `<tfoot>`

For larger tables, you can group rows semantically:

```html
<table border="1">
  <caption>Hardware Prices</caption>
  <thead>
    <tr>
      <th>Component</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CPU</td>
      <td>R3 500</td>
    </tr>
    <tr>
      <td>RAM (16 GB)</td>
      <td>R1 200</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>R4 700</td>
    </tr>
  </tfoot>
</table>
```

- `<thead>` — header rows (column names)
- `<tbody>` — main data rows
- `<tfoot>` — footer rows (totals, summaries)

This is useful for screen readers and allows CSS to style each section independently.

## Spanning Cells: colspan and rowspan

### colspan — Merge Columns

`colspan` makes a cell span across multiple columns:

```html
<table border="1">
  <tr>
    <th colspan="3">School Timetable — Monday</th>
  </tr>
  <tr>
    <th>Period</th>
    <th>Subject</th>
    <th>Teacher</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Mathematics</td>
    <td>Mr Dlamini</td>
  </tr>
</table>
```

The first row has one `<th>` that spans all 3 columns — creating a merged header.

### rowspan — Merge Rows

`rowspan` makes a cell span down multiple rows:

```html
<table border="1">
  <tr>
    <th>Day</th>
    <th>Period</th>
    <th>Subject</th>
  </tr>
  <tr>
    <td rowspan="2">Monday</td>
    <td>1</td>
    <td>Maths</td>
  </tr>
  <tr>
    <!-- No <td> for Day — it's covered by the rowspan above -->
    <td>2</td>
    <td>Science</td>
  </tr>
</table>
```

:::warning
When using `rowspan`, remember that the rows it covers must have **one fewer `<td>`** — the rowspan cell takes up that space.
:::

## Complete Example: Hardware Comparison Table

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hardware Comparison</title>
</head>
<body>

  <h1>Computer Types Comparison</h1>

  <table border="1">
    <caption>Comparison of Computer Form Factors</caption>
    <thead>
      <tr>
        <th>Feature</th>
        <th>Desktop</th>
        <th>Laptop</th>
        <th>Tablet</th>
        <th>Smartphone</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>Portability</th>
        <td>None</td>
        <td>Good</td>
        <td>Excellent</td>
        <td>Excellent</td>
      </tr>
      <tr>
        <th>Processing Power</th>
        <td>Very High</td>
        <td>High</td>
        <td>Medium</td>
        <td>Medium</td>
      </tr>
      <tr>
        <th>Battery</th>
        <td>N/A (mains)</td>
        <td>4–12 hours</td>
        <td>8–15 hours</td>
        <td>12–24 hours</td>
      </tr>
      <tr>
        <th>Typical Cost (ZAR)</th>
        <td colspan="2">R6 000 – R30 000</td>
        <td>R4 000 – R20 000</td>
        <td>R3 000 – R25 000</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
```

## Check Your Understanding

1. Name the four main elements used to build a table and explain what each does.
2. What is the difference between `<th>` and `<td>`? How does the browser display them differently by default?
3. Write a table (with borders) showing a school timetable for one day with three periods, including the subject and teacher for each period.
4. What does `colspan="2"` do? In what situation would you use it?
5. The following table should have "Monday" appear only once in the first column, spanning the two periods. Fix the code:
   ```html
   <tr>
     <td>Monday</td>
     <td>1</td>
     <td>Maths</td>
   </tr>
   <tr>
     <td>Monday</td>
     <td>2</td>
     <td>Science</td>
   </tr>
   ```
6. What is `<caption>` used for? Add a caption to your timetable from question 3.
7. Why should tables NOT be used for page layout? What technology should be used for layout instead?
