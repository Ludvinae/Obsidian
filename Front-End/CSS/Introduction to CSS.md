# Tags
- [[CSS]]
# CSS Intro
- **Date:** 2024-12-09
- Beginner's Guide to CSS with Sample Code

# What do we talk about ?
- An brief intro to CSS, covering the basics of styling web pages and the essential properties for beginners.

## What is CSS?
- CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of an HTML document.
- It controls the layout, colors, fonts, and overall visual appearance of web pages.
- CSS can be applied in three ways:
    1. Inline: Within the HTML element using the `style` attribute.
    2. Internal: Using the `<style>` tag in the `<head>` section.
    3. External: Linking an external CSS file using `<link>`. This is the format to use most of the time. It's cleaner and more understandable.
- Example using an external file:
    ```
    <!DOCTYPE html>
    <html>
      <head>
        <link rel="stylesheet" href="styles.css">
      </head>
      <body>
        <h1>Hello, CSS!</h1>
        <p>This is a styled paragraph.</p>
      </body>
    </html>
    ```
    
    ```
    /* styles.css */
    body {
      background-color: lightblue;
    }
    h1 {
      color: navy;
    }
    ```

## Basic CSS Syntax
- A CSS rule is made up of a selector and a declaration block:
    ```
    selector {
      property: value;
    }
    ```
- Example with explanation:
    ```
    p {
      color: red; /* Changes the text color to red */
      font-size: 16px; /* Sets the font size to 16 pixels */
    }
    ```
    - **Selectors**: Target the HTML elements you want to style. For instance:
    - Explore and practice selectors at [CSS Diner](https://flukeout.github.io/).
        - `p`: Targets all paragraph elements.
        - `.classname`: Targets all elements with the specified class.
        - `#id`: Targets the element with the specific ID.
    - **Properties**: Define what aspect of the element you want to style, such as text color, size, spacing, or layout.
    - **Values**: Specify the settings for the properties, like `red`, `16px`, or `bold`.

## Essential CSS Properties
- **Text Styling**:
    - `color`: Sets the text color.
    - `font-family`: Specifies the font.
    - `font-size`: Defines the size of the text.
    - Example with explanation:
        ```
        h1 {
          color: blue; /* Makes the text blue */
          font-family: Arial, sans-serif; /* Uses Arial or a default sans-serif font */
          font-size: 24px; /* Sets the text size to 24 pixels */
        }
        ```
- **Box Model**:
    - Every element is a rectangular box styled using properties like `margin`, `border`, `padding`, and `width`.
    - Example with explanation:
        ```
        div {
          width: 300px; /* Sets the width of the box */
          padding: 10px; /* Adds space inside the box around the content */
          border: 2px solid black; /* Adds a 2-pixel black border */
          margin: 20px; /* Adds space outside the box */
        }
        ```
- **Background**:
    - `background-color`: Sets the background color.
    - `background-image`: Adds a background image.
    - Example with explanation:
        ```
        body {
          background-color: #f0f0f0; /* Sets a light gray background color */
          background-image: url('background.jpg'); /* Uses the specified image as background */
        }
        ```
- **Positioning**:
    - `position`: Defines the positioning scheme (`static`, `relative`, `absolute`, `fixed`).
    - Example with explanation:
        ```
        .box {
          position: absolute; /* Positions the box relative to its nearest positioned ancestor */
          top: 50px; /* Moves the box 50 pixels down */
          left: 100px; /* Moves the box 100 pixels to the right */
        }
        ```

## Flexbox
- Flexbox is a CSS layout model that makes it easier to design flexible and responsive layout structures.
- Learn and practice Flexbox interactively at [Flexbox Froggy](https://flexboxfroggy.com/#fr).
- Key properties:
    - `display: flex;`: Defines a flex container.
    - `flex-direction`: Determines the direction of the flex items (`row`, `column`, etc.).
    - `justify-content`: Aligns items along the main axis.
    - `align-items`: Aligns items along the cross axis.
- Example:
    ```
    <!DOCTYPE html>
    <html>
      <head>
        <link rel="stylesheet" href="styles.css">
      </head>
      <body>
        <div class="flex-container">
          <div class="item">1</div>
          <div class="item">2</div>
          <div class="item">3</div>
        </div>
      </body>
    </html>
    ```
    
    ```
    /* styles.css */
    .flex-container {
      display: flex; /* Makes the container a flex container */
      flex-direction: row; /* Items are placed in a row */
      justify-content: space-around; /* Spreads items evenly */
      align-items: center; /* Centers items along the cross axis */
    }
    .item {
      background-color: lightcoral; /* Adds background to items */
      padding: 20px; /* Adds space inside items */
      border: 1px solid black; /* Adds a border around items */
    }
    ```

# Resume
- Resume, what's important ?
    - CSS enhances the appearance of web pages and works hand-in-hand with HTML.
    - Master the basic syntax: selectors, properties, and values.
    - Focus on essential properties like text styling, the box model, backgrounds, and positioning.
    - Flexbox is a powerful tool for creating responsive layouts.
    - Practice creating visually appealing web pages by experimenting with styles.

# Metadata
- Status : In progress
- Sources :
    - /
- Author :
    - Cédric BRASSEUR

# References
- Links
    - /