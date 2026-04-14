---
layout: page
title: Online Applications and Storage
parent: Internet Technologies
nav_order: 2
---

# Online Applications and Storage

{: .note }
This topic is part of the Grade 12 CAPS curriculum and covers the technologies that enable modern web applications and how data is stored, processed, and presented online.

## Storing Data

Modern web applications use various methods to store data, both locally on the user's device and remotely on servers.

### Locally (Cookies)

Cookies are small text files stored on a user's device that contain data specific to a particular website or web application.

#### How Cookies Work

1. **Creation**: When visiting a website, the server sends a small text file to the browser
2. **Storage**: The browser saves this file on the user's device
3. **Identification**: On subsequent visits, the browser sends the cookie back to the server
4. **Recognition**: The server uses the cookie data to recognize the user or their preferences

![Cookie Mechanism](../../../assets/images/cookie-mechanism.png)
*Diagram needed: Visual showing how cookies are created, stored, and exchanged between browsers and servers*

#### Types of Cookies

- **Session cookies**: Temporary cookies that are deleted when the browser is closed
- **Persistent cookies**: Remain on the device for a specified period
- **First-party cookies**: Created by the website you're visiting
- **Third-party cookies**: Created by domains other than the one you're visiting
- **Supercookies**: More persistent tracking mechanisms that are harder to delete

#### Cookie Uses

- **Authentication**: Remembering login status
- **Personalization**: Storing user preferences
- **Shopping carts**: Tracking items selected for purchase
- **Tracking**: Monitoring user behavior across sites
- **Analytics**: Collecting data about site usage

#### Privacy and Security Considerations

- **Data collection**: What information is being stored
- **Consent requirements**: Legal obligations to inform users
- **Third-party tracking**: Cross-site monitoring of behavior
- **Cookie lifespans**: How long data persists
- **Security vulnerabilities**: Potential for cookie theft or manipulation

### Online (Databases)

Web applications typically store most of their data in online databases hosted on servers.

#### Types of Online Databases

- **Relational databases**: Structured data in tables with relationships (MySQL, PostgreSQL)
- **NoSQL databases**: Flexible schemas for unstructured data (MongoDB, Cassandra)
- **In-memory databases**: Data stored in RAM for faster access (Redis, Memcached)
- **Graph databases**: Optimized for highly connected data (Neo4j)
- **Time-series databases**: Optimized for time-based data (InfluxDB)

#### Advantages of Online Database Storage

- **Centralized management**: Data maintained in one location
- **Scalability**: Can grow to accommodate increasing data volumes
- **Backup and recovery**: Systematic protection against data loss
- **Concurrent access**: Multiple users can access simultaneously
- **Security controls**: Comprehensive protection mechanisms

#### Cloud Database Services

- **Database as a Service (DBaaS)**: Fully managed database solutions
- **Examples**: Amazon RDS, Google Cloud SQL, Azure SQL Database
- **Benefits**: Reduced administration, automatic scaling, high availability
- **Deployment models**: Public cloud, private cloud, hybrid approaches
- **Cost structure**: Pay-as-you-go pricing based on resources used

![Database Architecture](../../../assets/images/database-architecture.jpg)
*Image needed: Diagram showing typical web application database architecture with application servers and database servers*

## Role of SQL, Scripting Languages, and XML

Various technologies work together to create, manipulate, and exchange data in web applications.

### SQL (Structured Query Language)

SQL is the standard language for interacting with relational databases.

#### Common SQL Operations

- **SELECT**: Retrieving data from the database
- **INSERT**: Adding new records to tables
- **UPDATE**: Modifying existing records
- **DELETE**: Removing records from tables
- **JOIN**: Combining data from multiple tables

#### Example SQL Queries

```sql
-- Retrieve all products with price over 100
SELECT product_name, price FROM products WHERE price > 100;

-- Insert a new customer record
INSERT INTO customers (first_name, last_name, email) 
VALUES ('John', 'Smith', 'john.smith@example.com');

-- Update product prices
UPDATE products SET price = price * 1.1 WHERE category = 'Electronics';

-- Delete inactive users
DELETE FROM users WHERE last_login < '2020-01-01';
```

#### SQL in Web Applications

- **Database connectivity**: Libraries and drivers for connecting to databases
- **Query building**: Constructing SQL queries based on user input
- **Result processing**: Converting database results to application objects
- **Prepared statements**: Preventing SQL injection attacks
- **ORM (Object-Relational Mapping)**: Abstracting database operations

### Scripting Languages

Scripting languages enable dynamic functionality in web applications, both on the server and client sides.

#### Server-Side Scripting

Code executed on the web server before sending content to the user:

- **PHP**: Widely used language embedded in HTML
- **Python**: Versatile language with frameworks like Django and Flask
- **Node.js**: JavaScript running on the server
- **Ruby**: Object-oriented language with Ruby on Rails framework
- **C#/ASP.NET**: Microsoft's server-side technology

**Server-side responsibilities**:
- Processing form submissions
- Database interactions
- Authentication and authorization
- Business logic implementation
- Dynamic page generation

#### Client-Side Scripting

Code executed in the user's browser:

- **JavaScript**: Primary language for browser-based interactivity
- **TypeScript**: Typed superset of JavaScript
- **Frameworks**: React, Angular, Vue.js
- **Libraries**: jQuery, D3.js
- **WebAssembly**: Binary format for high-performance applications

**Client-side responsibilities**:
- User interface interactivity
- Form validation
- Dynamic content updates
- Client-side data processing
- Visual effects and animations

#### AJAX (Asynchronous JavaScript and XML)

Technology for updating parts of a webpage without reloading:
- Allows asynchronous communication with the server
- Enables more responsive user interfaces
- Updates content dynamically
- Originally used XML but now often uses JSON
- Core technology for single-page applications

![Client-Server Architecture](../../../assets/images/client-server-scripting.png)
*Diagram needed: Visual showing the relationship between client-side and server-side scripting in web applications*

### XML (Extensible Markup Language)

XML is a markup language that defines rules for encoding documents in a format that is both human-readable and machine-readable.

#### XML Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<students>
  <student id="1">
    <firstName>John</firstName>
    <lastName>Smith</lastName>
    <grade>11</grade>
    <subjects>
      <subject>Mathematics</subject>
      <subject>Physics</subject>
      <subject>Computer Science</subject>
    </subjects>
  </student>
  <student id="2">
    <firstName>Sarah</firstName>
    <lastName>Johnson</lastName>
    <grade>12</grade>
    <subjects>
      <subject>History</subject>
      <subject>English</subject>
      <subject>Biology</subject>
    </subjects>
  </student>
</students>
```

#### Uses of XML in Web Applications

- **Data exchange**: Format for sharing data between systems
- **Configuration files**: Storing application settings
- **Web services**: SOAP API communication
- **Content management**: Structured document storage
- **RSS/Atom feeds**: Syndicating regularly updated content

#### XML Technologies

- **XPath**: Language for navigating XML documents
- **XSLT**: Transforming XML into other formats
- **XML Schema**: Defining structure of XML documents
- **DOM/SAX**: APIs for processing XML
- **XML Namespaces**: Avoiding name conflicts in documents

#### JSON vs. XML

While XML was once the dominant data exchange format, JSON (JavaScript Object Notation) has become more popular in modern web applications:

| Aspect | JSON | XML |
|--------|------|-----|
| Syntax | Lighter, less verbose | More verbose with tags |
| Parsing | Native in JavaScript | Requires specific parsers |
| Data types | Supports common types | Text-based, requires conversion |
| Readability | Simple for basic data | Better for complex documents |
| Validation | Requires separate schema | Built-in validation options |

## Running Instructions

Web applications execute code both on the server and in the browser, each with different characteristics and purposes.

### Locally (Scripts, AJAX)

Modern websites rely heavily on code running in the user's browser to create interactive experiences.

#### JavaScript Execution

- **Loading**: Scripts loaded from server into browser
- **Parsing**: Browser converts code to executable format
- **Execution**: Code runs in browser's JavaScript engine
- **DOM manipulation**: Scripts modify webpage content and structure
- **Event handling**: Code responds to user interactions

#### JavaScript Capabilities

- **DOM manipulation**: Changing page content and structure
- **Event handling**: Responding to user actions
- **Form validation**: Checking input before submission
- **Data processing**: Manipulating information locally
- **Animation**: Creating visual effects and transitions
- **API communication**: Requesting data from servers

#### AJAX Implementation

AJAX (Asynchronous JavaScript and XML) allows webpages to update dynamically by exchanging data with a server in the background:

```javascript
// Modern AJAX implementation using Fetch API
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    console.log('Data received:', data);
    document.getElementById('result').innerHTML = data.message;
  })
  .catch(error => console.error('Error:', error));
```

#### Single-Page Applications (SPAs)

Modern web applications that load a single HTML page and dynamically update content:
- Rely heavily on client-side JavaScript
- Provide app-like user experience
- Reduce server round-trips
- Frameworks: React, Angular, Vue.js
- Examples: Gmail, Google Maps, Twitter

### Online (Server Side, Scripts and Code)

Server-side code executes on the web server before content is sent to the browser.

#### Server-Side Execution Process

1. **Request**: Browser sends HTTP request to server
2. **Processing**: Server executes code based on request
3. **Database interaction**: Code retrieves or updates data
4. **Response generation**: Dynamic content created
5. **Response**: HTML/CSS/JavaScript sent to browser

#### Server-Side Capabilities

- **Database operations**: Reading and writing data
- **Authentication**: Verifying user identities
- **Authorization**: Controlling access to resources
- **Business logic**: Implementing application rules
- **Integration**: Connecting with other systems and APIs
- **File operations**: Managing uploads and downloads

#### Example: PHP Server-Side Code

```php
<?php
// Connect to database
$conn = new mysqli("localhost", "username", "password", "database");

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Query database
$sql = "SELECT id, name, email FROM users WHERE active = 1";
$result = $conn->query($sql);

// Generate HTML dynamically
if ($result->num_rows > 0) {
  echo "<ul>";
  while($row = $result->fetch_assoc()) {
    echo "<li>Name: " . $row["name"] . " - Email: " . $row["email"] . "</li>";
  }
  echo "</ul>";
} else {
  echo "No users found";
}
$conn->close();
?>
```

#### Client-Server Communication

- **HTTP/HTTPS requests**: Primary communication protocol
- **API endpoints**: Specific URLs for accessing functionality
- **Request methods**: GET, POST, PUT, DELETE, etc.
- **Response formats**: JSON, XML, HTML, binary data
- **WebSockets**: Persistent connections for real-time communication

![Client-Server Flow](../../../assets/images/client-server-flow.jpg)
*Image needed: Diagram showing the flow of data between client and server in a typical web application*

## Formatting Output

Web applications use various technologies to present information visually to users.

### CSS (Cascading Style Sheets)

CSS is the standard technology for styling web pages and controlling their visual presentation.

#### CSS Functionality

- **Layout control**: Positioning elements on the page
- **Visual styling**: Colors, fonts, borders, backgrounds
- **Responsive design**: Adapting to different screen sizes
- **Animations**: Creating motion and transitions
- **Print styling**: Controlling appearance for printing

#### CSS Implementation Methods

- **Inline styles**: Applied directly to HTML elements
- **Internal stylesheets**: Defined within HTML document
- **External stylesheets**: Separate CSS files linked to HTML
- **CSS preprocessors**: Extended syntaxes like SASS, LESS
- **CSS frameworks**: Pre-built systems like Bootstrap, Tailwind

#### CSS Example

```css
/* Styling a navigation menu */
.nav-menu {
  display: flex;
  justify-content: space-between;
  background-color: #333;
  padding: 1rem;
}

.nav-menu a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-menu a:hover {
  background-color: #555;
}

/* Responsive design */
@media (max-width: 768px) {
  .nav-menu {
    flex-direction: column;
  }
}
```

#### Modern CSS Capabilities

- **CSS Grid**: Two-dimensional layout system
- **Flexbox**: One-dimensional layout control
- **Custom properties (variables)**: Reusable values
- **Media queries**: Responsive design rules
- **Animations and transitions**: Motion effects
- **Dark mode support**: Color scheme preferences

### HTML Templates and Frameworks

Modern web development often uses templating systems and frameworks to structure and generate HTML.

#### Server-Side Templates

- **PHP templates**: Built-in templating in PHP
- **Jinja2/Django templates**: Python-based templating
- **EJS/Handlebars**: JavaScript templating engines
- **Razor**: C#/ASP.NET templating
- **ERB/Haml**: Ruby templating

**Example: Jinja2 Template**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>Welcome, {{ user.name }}!</h1>
    <ul>
    {% for item in items %}
        <li>{{ item.name }} - ${{ item.price }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

#### Client-Side Templates

- **React JSX**: JavaScript XML syntax for component-based UIs
- **Vue templates**: Vue.js templating system
- **Angular templates**: HTML with Angular directives
- **Mustache/Handlebars**: Logic-less templating
- **Lit-html**: HTML templating library for Web Components

**Example: React JSX**
```jsx
function ProductList({ products }) {
  return (
    <div className="product-list">
      <h2>Our Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>${product.price}</p>
            <button>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### Frontend Frameworks

Modern web development often uses comprehensive frameworks that combine templating, styling, and interactivity.

#### Popular Frontend Frameworks

- **React**: Component-based library for building user interfaces
- **Angular**: Complete framework with extensive features
- **Vue.js**: Progressive framework for building UIs
- **Svelte**: Compiler-based approach to building interfaces
- **Ember.js**: Opinionated framework for ambitious applications

#### Advantages of Using Frameworks

- **Component reusability**: Building blocks that can be reused
- **State management**: Tools for managing application data
- **Performance optimization**: Efficient rendering techniques
- **Developer tools**: Debugging and development assistance
- **Community and ecosystems**: Libraries and extensions

### Responsive Web Design

Modern websites need to work well on devices of all sizes, from smartphones to desktops.

#### Core Techniques

- **Fluid layouts**: Using percentages instead of fixed widths
- **Flexible images**: Images that scale with their containers
- **Media queries**: CSS rules that apply based on device characteristics
- **Mobile-first approach**: Designing for small screens first
- **Viewport settings**: Controlling how pages display on different devices

**Example: Responsive Layout with Media Queries**
```css
/* Base styles for mobile */
.container {
  width: 100%;
  padding: 15px;
}

.column {
  width: 100%;
  margin-bottom: 20px;
}

/* Tablet styles */
@media (min-width: 768px) {
  .container {
    max-width: 750px;
    margin: 0 auto;
  }
  
  .column {
    width: 48%;
    float: left;
    margin-right: 4%;
  }
  
  .column:nth-child(2n) {
    margin-right: 0;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .container {
    max-width: 1000px;
  }
  
  .column {
    width: 30%;
    margin-right: 5%;
  }
  
  .column:nth-child(2n) {
    margin-right: 5%;
  }
  
  .column:nth-child(3n) {
    margin-right: 0;
  }
}
```

## Paper 2 Connection

In Paper 2 examinations, expect questions that require you to:
- Explain how data is stored locally and online in web applications
- Describe the role of cookies and their privacy implications
- Explain how client-side and server-side scripting work together
- Analyze the advantages and disadvantages of different data formats
- Describe how CSS is used to format web content
- Compare different approaches to creating responsive web designs

{: .highlight }
When answering questions about online applications, be sure to explain both the technical aspects and the practical implications. For example, when discussing cookies, mention both how they work technically and their privacy considerations.

## Practice Questions

1. Explain the difference between client-side and server-side scripting in web applications. Provide an example of each and describe when each would be most appropriate.

2. Describe how cookies are used to store data locally in web browsers. Discuss two benefits and two privacy concerns associated with cookies.

3. Compare JSON and XML as data exchange formats. Explain why JSON has become more popular for modern web applications.

4. Explain how CSS is used to format web content. Provide examples of three different ways CSS can be applied to HTML documents and discuss the advantages of each approach.

5. A company is developing a web application that needs to work well on both desktop computers and mobile devices. Describe the key principles of responsive web design they should follow and explain how media queries contribute to this approach.

## Self-Assessment

Check your understanding:

- [ ] I can explain how cookies work and their privacy implications
- [ ] I understand how databases are used to store information online
- [ ] I can describe the role of SQL in web applications
- [ ] I understand the differences between client-side and server-side scripting
- [ ] I can explain how XML and JSON are used for data exchange
- [ ] I understand how CSS is used to format web content
- [ ] I can describe the principles of responsive web design