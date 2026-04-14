---
layout: page
title: How to Use This Resource
permalink: /how-to-use/
nav_order: 2
---

# How to Use This Resource

IT Gateway covers both Digital Technology (Grades 8-9) and Information Technology (Grades 10-12). The Grade 10-12 content is organised by **CAPS IT concept**, not by grade — each topic page shows how it builds from Grade 10 through to Grade 12 in one place.

## Navigation

- **Side menu** — shows all sections including Grade 8-9, the six CAPS topics, and Exam Prep
- **Search bar** — type any keyword to find content quickly
- **Links within pages** — concepts link to related topics

## For Grade 8 and 9 learners

Go to [Digital Technology](/digital-technology/) for your full curriculum content including Karel coding, digital citizenship, and web design.

## For Grade 10-12 learners

- Use the side menu to find the CAPS topic you are studying
- Each topic page explains what is covered at Grade 10, 11, and 12
- Look for the **Practice Questions** section at the bottom of each page
- Use the [Exam Preparation](/exam-prep/) section before tests and exams

## Using with Google Classroom

This resource works alongside Google Classroom:
- Your teacher will link specific pages to assignments
- Submit your work through Google Classroom as usual

---

## Markdown quick reference

*For adding or editing content — learners don't need this section.*

### Basic formatting

```
**Bold text**
_Italic text_
~~Strikethrough~~
```

### Headings

```
# Heading 1 (page title)
## Heading 2 (main section)
### Heading 3 (sub-section)
```

### Lists

```
- Bullet item
- Another item

1. Numbered item
2. Another item
```

### Tables

```
| Column 1 | Column 2 |
|---|---|
| Row 1 data | More data |
| Row 2 data | More data |
```

### Code blocks

Use triple backticks with the language name:

````
```sql
SELECT * FROM Students WHERE Grade = 12;
```
````

````
```pascal
writeln('Hello World');
```
````

### Note and highlight callouts

```
{: .note }
This appears as a blue note box.

{: .highlight }
This appears as a yellow highlight box.
```

### Links

```
[Link text](./relative-page)
[Link text](/absolute-path/page)
```

### Adding a new page

1. Copy `_templates/concept-page.md` or `_templates/exam-prep-page.md`
2. Rename the file (use lowercase, hyphens instead of spaces: `my-new-topic.md`)
3. Put it in the correct topic folder
4. Update the `title:` and `parent:` in the frontmatter at the top
5. Write your content below the `---` line
