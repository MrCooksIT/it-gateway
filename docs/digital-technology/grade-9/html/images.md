---
title: Images in HTML
---

# Images in HTML

Images make web pages visually engaging. The `<img>` tag is used to embed images into HTML — it is a **self-closing tag** with no content between tags.

## The `<img>` Tag

```html
<img src="path/to/image.jpg" alt="Description of the image">
```

The two most important attributes:
- `src` (source) — the path or URL to the image file
- `alt` (alternative text) — a description of the image

:::warning
The `alt` attribute is **required**. Never omit it. If the image fails to load, the alt text is displayed instead. Screen readers also read the alt text aloud for visually impaired users.
:::

## The `src` Attribute

Just like the `href` attribute in links, `src` can be a relative path or an absolute URL:

```html
<!-- Image in the same folder -->
<img src="photo.jpg" alt="A mountain">

<!-- Image in an images subfolder -->
<img src="images/logo.png" alt="Company logo">

<!-- Image from another website (external) -->
<img src="https://www.example.com/photo.jpg" alt="External image">
```

:::warning
Linking directly to images on other websites (hotlinking) uses their bandwidth without permission. For your own projects, download and host images locally.
:::

## Writing Good Alt Text

| Situation | Good alt text | Poor alt text |
|-----------|--------------|---------------|
| A photo of a cat sleeping | `alt="An orange cat sleeping on a sofa"` | `alt="cat"` |
| A company logo | `alt="IT Gateway logo"` | `alt="logo"` |
| A decorative divider line | `alt=""` (empty — tell screen reader to ignore it) | `alt="decorative image"` |
| A graph showing sales data | `alt="Bar chart showing sales increase of 30% from 2023 to 2024"` | `alt="chart"` |

:::info
If an image is purely decorative (background pattern, decorative border), use an empty `alt=""`. This tells screen readers to skip it, reducing unnecessary noise for visually impaired users.
:::

## Sizing Images

You can set the width and height directly in HTML:

```html
<img src="photo.jpg" alt="Mountain" width="400" height="300">
```

- Values are in pixels by default
- Specifying both maintains the aspect ratio in the browser's rendering calculations (reduces layout shift as the page loads)

:::warning
While setting dimensions in HTML is acceptable, it is better practice to control image sizes using CSS. Over-specifying in HTML can override CSS styling.
:::

## Image File Formats

Choosing the right format affects file size, quality, and transparency support:

| Format | Best for | Supports transparency? | Lossy/Lossless |
|--------|---------|----------------------|----------------|
| **JPEG / JPG** | Photographs, complex images with many colours | No | Lossy (quality decreases with compression) |
| **PNG** | Screenshots, graphics, logos, images needing transparency | Yes (alpha channel) | Lossless |
| **GIF** | Simple animations, limited colours | Yes (binary — fully transparent or not) | Lossless (limited to 256 colours) |
| **SVG** | Icons, logos, illustrations | Yes | Vector (scales without pixelating) |
| **WebP** | Modern replacement for JPEG/PNG — better compression | Yes | Both modes available |

:::tip Key Term
**Lossy compression** reduces file size by permanently discarding some image data. Each time you save a JPEG, quality decreases slightly. **Lossless compression** reduces file size without losing any data — quality is always perfect.
:::

:::tip Key Term
**Vector graphics** (SVG) are defined by mathematical formulas, not pixels. They scale to any size without becoming blurry or pixelated — unlike raster/bitmap images (JPEG, PNG, GIF).
:::

## Image Optimisation

Large image files slow down web pages. For fast-loading sites:
- Use JPEG for photographs (compress to 70–80% quality)
- Use PNG only when transparency is needed
- Use WebP for modern browsers (best compression)
- Resize images to the maximum size they'll be displayed before uploading
- Use free tools like Squoosh.app or TinyPNG.com to compress images

:::info
A single unoptimised photograph can be 5–10 MB. On a 4G connection, this could take several seconds to load. Optimised for the web, the same photo might be 200–400 KB.
:::

## Copyright and Images

:::warning
Just because you find an image on Google does not mean you can use it. Most images are protected by copyright. Using them without permission is copyright infringement.
:::

**Where to find free-to-use images:**
- [Unsplash](https://unsplash.com) — free high-quality photos (CC0 or similar)
- [Pexels](https://pexels.com) — free photos and videos
- [Pixabay](https://pixabay.com) — free photos, illustrations, vectors

**For Google Images**, filter by licence:
- Tools → Usage Rights → "Creative Commons licences"

Always read the specific licence — some require attribution even if free to use.

## The `<figure>` and `<figcaption>` Elements

For images with captions, use the semantic `<figure>` element:

```html
<figure>
  <img src="computer.jpg" alt="A modern desktop computer">
  <figcaption>A typical desktop computer setup in 2024.</figcaption>
</figure>
```

- `<figure>` wraps the image and its caption as a self-contained unit
- `<figcaption>` provides the visible caption shown below the image
- This is semantically better than just placing a `<p>` beneath an `<img>`

## A Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Images Demo</title>
</head>
<body>

  <h1>Computer Hardware</h1>

  <p>Below are examples of common computer components.</p>

  <figure>
    <img src="images/cpu.jpg" alt="An Intel CPU chip on a motherboard" width="400">
    <figcaption>A modern CPU — the brain of the computer.</figcaption>
  </figure>

  <figure>
    <img src="images/monitor.jpg" alt="A widescreen LCD monitor displaying a desktop" width="400">
    <figcaption>An output device: the monitor.</figcaption>
  </figure>

  <p>For more information, visit
  <a href="https://www.howstuffworks.com" target="_blank" rel="noopener noreferrer">HowStuffWorks</a>.
  </p>

</body>
</html>
```

## Check Your Understanding

1. Write the HTML to display an image called `school.png` stored in an `images/` subfolder, with appropriate alt text.

2. Why is the `alt` attribute required? Give two separate reasons.

3. A designer creates a company logo. Should they save it as JPEG, PNG, or SVG? Explain your choice.

4. An image of a person's face is 8 MB in size. Why is this a problem for a website, and what should be done about it?

5. What is the difference between a raster image (JPEG/PNG) and a vector image (SVG)?

6. A student right-clicks an image on Google Images and uses "Copy image address" to link to it directly in their HTML. What is this practice called and why is it a problem?

7. Write the HTML to display an image `sunset.jpg` with:
   - Alt text describing a sunset over the ocean
   - A width of 600 pixels
   - A caption that reads "Cape Town sunset, 2024"
