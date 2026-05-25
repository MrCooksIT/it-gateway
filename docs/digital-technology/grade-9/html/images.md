---
title: Images in HTML
---

# Images in HTML

## Adding Images to Web Pages

We have all seen it — web pages have images. Images spice up a web page, give us something to look at, and help communicate information. It is very common for a web page to include images.

To add images to our web pages, we use the **`<img>` tag**.

---

## The `<img>` Tag

The `<img>` tag allows us to add images to our web pages.

```html
<img src="URL" alt="description">
```

There are two important things to note about the `<img>` tag:

1. **There is no closing tag.** Unlike most HTML tags, the `<img>` tag does not need a closing tag. This is because the image tag is not annotating or decorating text — it is simply fetching an image and placing it on the page. There is nothing to put inside an `<img>` tag and close, so it is just a single tag with attributes.

2. **The attributes are very important.** Without attributes, the image tag would not know what to display or how big to make it.

---

## The `src` Attribute

The **`src`** attribute (short for **source**) specifies **where to get the image from**. The value of `src` is the URL of the image.

```html
<img src="https://www.example.com/logo.png" alt="Example logo">
```

The `src` attribute is where the `<img>` tag looks to grab the image and insert it onto your web page.

:::tip
If you don't know the URL of an image by memory, you can right-click on any image in a web browser and choose **"Copy image address"**. This gives you the URL of that image, which you can then use as the value of your `src` attribute.
:::

---

## The `alt` Attribute

The **`alt`** attribute (short for **alternative**) defines text that the browser should display **in case the image is not found**.

```html
<img src="https://codehs.com/static/img/logo.png" alt="CodeHS logo">
```

If the URL in `src` is incorrect and the image cannot be loaded, the browser will display the alt text instead of the image. The alt text tells the user what the image was supposed to show.

---

## The `width` and `height` Attributes

The **`width`** and **`height`** attributes specify the **size of the image** in **pixels**.

:::tip Key Term
**Pixel:** The tiny, tiny little dots of colour on your computer screen. When put together, these dots of colour create the entire image you see on screen. Pixels are the unit of measurement used for image sizes.
:::

```html
<img src="logo.png" alt="Logo" width="100" height="100">
```

### Specifying Width Only

If you only specify **width** (and not height), the height will automatically scale to keep the image proportional — maintaining its original shape:

```html
<img src="logo.png" alt="Logo" width="100">
```

The image is resized to 100 pixels wide, and the height adjusts automatically to keep the correct proportions.

### Specifying Both Width and Height

If you specify **both** width and height, the image will be stretched to fit those exact dimensions — even if that distorts the image:

```html
<img src="logo.png" alt="Logo" width="100" height="600">
```

This would stretch the image to be very tall. Be careful when specifying both — only do this if you intentionally want to change the shape of the image.

---

## A Complete Image Example

Here is an example of a web page that uses images above links:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Links Page</title>
  </head>
  <body>
    <h1>Useful Websites</h1>

    <img src="https://codehs.com/static/img/logo.png" alt="CodeHS logo" width="100">
    <a href="https://codehs.com/info">CodeHS</a>

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png" alt="Wikipedia logo" width="200">
    <a href="https://wikipedia.org">Wikipedia</a>
  </body>
</html>
```

---

## Summary of `<img>` Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `src` | The URL of the image to display | `src="logo.png"` |
| `alt` | Text to show if the image cannot load | `alt="Company logo"` |
| `width` | The width of the image in pixels | `width="100"` |
| `height` | The height of the image in pixels | `height="200"` |

---

## Check Your Understanding

1. What is the purpose of the `<img>` tag? What does it do?

2. Why does the `<img>` tag not have a closing tag?

3. What does the `src` attribute do? What type of value does it hold?

4. What does the `alt` attribute do? When does the alt text get shown to the user?

5. What is a pixel? What unit do width and height use?

6. What happens if you specify only the `width` attribute and not the `height` attribute?

7. What happens if you specify both `width` and `height` attributes with different proportions than the original image?

8. Write the HTML code to display an image from `https://www.example.com/photo.jpg` with the alt text "A mountain view" and a width of 300 pixels.

9. How can you find the URL of an image you see on a web page without knowing it from memory?

10. **Extended question:** Why is the `alt` attribute useful even when the image loads correctly? Think about users who might have difficulty seeing images on screen.
