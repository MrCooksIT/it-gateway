---
layout: page
title: Grade 10 Mid-Year Paper 1 Study Guide
parent: Paper 1 Preparation
grand_parent: Examination Preparation
nav_order: 3
---

# Grade 10 Mid-Year Paper 1 Study Guide

{: .text-blue-200 }

Your first steps into Delphi programming - master the basics!
{: .fs-6 .fw-300 }

---

## Paper Structure Overview

| Question       | Topic                           | Marks   |
| -------------- | ------------------------------- | ------- |
| **Question 1** | Basic Programming Concepts      | ~33     |
| **Question 2** | Conditional Programming         | ~35     |
| **Question 3** | Global Variables & Calculations | ~32     |
| **Total**      |                                 | **100** |

---

## Question 1: Basic Programming Concepts (33 marks)

### 1. Form Event Handling (OnShow)

Setting up your form when the program starts:

```pascal
// Example: Form OnShow event
procedure TfrmExample.FormShow(Sender: TObject);
begin
  // Set panel text
  pnlExample.Caption := 'Welcome to Grade 10 IT!';

  // Change font properties
  pnlExample.Font.Size := 15;
  pnlExample.Font.Name := 'Consolas';

  // Load and display an image
  imgExample.Picture.LoadFromFile('picture.jpg');
  imgExample.Stretch := true;  // Fit image to component size
end;
```

{: .note }
The OnShow event is perfect for setting initial values and loading resources!

### 2. Variable Declaration and Data Types

Understanding different data types:

```pascal
// Declaring variables
var
  age: integer;        // Whole numbers (-5, 0, 42)
  name: string;        // Text ("John", "Hello World")
  price: real;         // Decimal numbers (19.99, -3.14)
  isReady: boolean;    // True or False only
```

### 3. Getting Input from GUI Components

Extracting values from different components:

```pascal
var
  age: integer;
  name: string;
  checked: boolean;
begin
  // From spin edit (number selector)
  age := spnAge.Value;

  // From edit box (text input)
  name := edtName.Text;

  // From checkbox
  checked := chbOption.Checked;

  // From combo box (dropdown)
  weather := cmbWeather.Text;

  ShowMessage('Data captured successfully!');
end;
```

### 4. Basic Output Display

Showing results to users:

```pascal
// Display in panel
pnlResult.Caption := 'Hello ' + name;

// Display in label
lblOutput.Caption := 'Age: ' + IntToStr(age);

// Show message box
ShowMessage('Welcome to the program!');
```

### 5. Mathematical Calculations

Performing calculations with proper formatting:

```pascal
// Calculate total price with currency formatting
var
  price, total: real;
  quantity: integer;
begin
  price := StrToFloat(edtPrice.Text);
  quantity := spnQuantity.Value;

  // Calculate
  total := price * quantity;

  // Display with currency format
  lblResult.Caption := 'Price for ' + IntToStr(quantity) +
                       ' items is: ' +
                       FormatCurr('R #,##0.00', total);
end;
```

{: .tip }
**Currency Format**: `'R #,##0.00'` gives you R 1,234.56 format!

### 6. Using the Modulus (MOD) Operator

Checking divisibility and remainders:

```pascal
// Check if year is divisible by 4 (leap year check)
var
  year: integer;
begin
  year := StrToInt(edtYear.Text);

  if (year mod 4 = 0) then
    ShowMessage(IntToStr(year) + ' is divisible by 4')
  else
    ShowMessage(IntToStr(year) + ' is NOT divisible by 4');
end;

// MOD gives the remainder:
// 10 mod 3 = 1 (because 10 ÷ 3 = 3 remainder 1)
// 15 mod 5 = 0 (because 15 ÷ 5 = 3 remainder 0)
```

---

## Question 2: Conditional Programming (35 marks)

### 1. Basic IF Statements

Making decisions in your program:

```pascal
// Simple IF statement
if age >= 18 then
  ShowMessage('You are an adult');

// IF-THEN-ELSE statement
if age >= 18 then
  ShowMessage('You are an adult')
else
  ShowMessage('You are a minor');
```

### 2. Visual Feedback with Shapes

Changing component properties based on conditions:

```pascal
// Change shape color based on age
var
  age: integer;
begin
  age := spnAge.Value;

  if age >= 18 then
  begin
    shpIndicator.Brush.Color := clGreen;
    shpIndicator.Visible := true;
  end
  else
  begin
    shpIndicator.Brush.Color := clRed;
    shpIndicator.Visible := true;
  end;
end;
```

### 3. Complex Conditions with AND/OR

Combining multiple conditions:

```pascal
// Check multiple conditions
if (age >= 18) and (hasLicense = true) then
  ShowMessage('You can drive!')
else
  ShowMessage('You cannot drive yet');

// Using OR for alternatives
if (day = 'Saturday') or (day = 'Sunday') then
  ShowMessage('It''s the weekend!')
else
  ShowMessage('It''s a weekday');
```

### 4. Radio Group Selection

Using radio buttons for options:

```pascal
// Set radio group based on number
var
  number: real;
begin
  number := StrToFloat(edtNumber.Text);

  if number >= 0 then
    rdgResult.ItemIndex := 0  // First option (Positive)
  else
    rdgResult.ItemIndex := 1; // Second option (Negative)
end;
```

### 5. CASE Statements

Cleaner alternative to multiple IF statements:

```pascal
// Determine days in month using CASE
var
  month, days: integer;
begin
  month := spnMonth.Value;

  case month of
    1, 3, 5, 7, 8, 10, 12: days := 31;  // Long months
    4, 6, 9, 11: days := 30;             // Short months
    2: days := 28;                       // February
  else
    days := 0;  // Invalid month
  end;

  if days > 0 then
    ShowMessage('Month ' + IntToStr(month) + ' has ' +
                IntToStr(days) + ' days')
  else
    ShowMessage('Invalid month number!');
end;
```

### 6. String Comparison

Checking text input for validation:

```pascal
// Simple login system
var
  username, password: string;
begin
  username := edtUsername.Text;
  password := edtPassword.Text;

  if (username = 'admin') and (password = 'secret123') then
  begin
    imgSuccess.Visible := true;
    imgFail.Visible := false;
    ShowMessage('Login successful!');
  end
  else
  begin
    imgSuccess.Visible := false;
    imgFail.Visible := true;
    ShowMessage('Invalid credentials!');
  end;
end;
```

### 7. Percentage Calculations with Grading

Converting marks to percentages and grades:

```pascal
// Calculate percentage and determine grade
var
  mark: integer;
  percentage: real;
  grade: string;
begin
  mark := spnMark.Value;
  percentage := (mark / 40) * 100;  // Convert to percentage

  // Determine grade
  if percentage >= 80 then
    grade := 'A - Excellent!'
  else if percentage >= 70 then
    grade := 'B - Very Good'
  else if percentage >= 60 then
    grade := 'C - Good'
  else if percentage >= 50 then
    grade := 'D - Pass'
  else
    grade := 'F - Fail';

  // Display results
  memResult.Clear;
  memResult.Lines.Add('Mark: ' + IntToStr(mark) + '/40');
  memResult.Lines.Add('Percentage: ' +
                      FloatToStrF(percentage, ffFixed, 15, 1) + '%');
  memResult.Lines.Add('Grade: ' + grade);
end;
```

---

## Question 3: Global Variables & Calculations (32 marks)

### 1. Declaring Global Variables

Variables that can be used across all procedures:

```pascal
// Global variables (declare in VAR section at top)
var
  // Form variable (already there)
  frmMain: TfrmMain;

  // Your global variables
  sDriverName: string;
  iSets: integer;
  sType: string;
  iTotalItems: integer;
```

{: .important }
Global variables are declared OUTSIDE any procedure, at the top of your code!

### 2. Storing Data in Global Variables

Capturing GUI input into global variables:

```pascal
procedure TfrmExample.btnStoreClick(Sender: TObject);
begin
  // Store values from GUI components
  sDriverName := edtName.Text;
  iSets := spnSets.Value;

  // Get selected radio button text
  sType := rdgType.Items[rdgType.ItemIndex];

  // Confirmation
  ShowMessage('Data has been stored successfully');

  // Optional: Disable input components
  edtName.Enabled := false;
  spnSets.Enabled := false;
  rdgType.Enabled := false;
end;
```

### 3. Displaying Stored Information

Using global variables to show data:

```pascal
procedure TfrmExample.btnDisplayClick(Sender: TObject);
begin
  // Clear output
  redOutput.Clear;

  // Build display using global variables
  redOutput.Lines.Add('Driver Information');
  redOutput.Lines.Add('==================');
  redOutput.Lines.Add('Name: ' + sDriverName);
  redOutput.Lines.Add('Number of Sets: ' + IntToStr(iSets));
  redOutput.Lines.Add('Type Selected: ' + sType);
end;
```

### 4. Calculations with Global Variables

Performing calculations using stored values:

```pascal
procedure TfrmExample.btnCalculateClick(Sender: TObject);
begin
  // Calculate total items (4 items per set)
  iTotalItems := iSets * 4;

  // Display result
  redOutput.Lines.Add('');  // Blank line
  redOutput.Lines.Add('Calculation Results:');
  redOutput.Lines.Add('Total number of items: ' + IntToStr(iTotalItems));
end;
```

### 5. Complex Pricing with CASE and VAT

Using CASE for different pricing options:

```pascal
procedure TfrmExample.btnTotalCostClick(Sender: TObject);
var
  costPerItem, totalBeforeVAT, totalWithVAT: real;
begin
  // Determine price based on type using CASE
  case rdgType.ItemIndex of
    0: costPerItem := 2999.99;  // Type A - Basic
    1: costPerItem := 3599.99;  // Type B - Standard
    2: costPerItem := 4999.99;  // Type C - Premium
  else
    costPerItem := 0;
  end;

  // Calculate totals
  totalBeforeVAT := iTotalItems * costPerItem;
  totalWithVAT := totalBeforeVAT * 1.15;  // Add 15% VAT

  // Display formatted result
  redOutput.Lines.Add('');
  redOutput.Lines.Add('==== FINAL COSTING ====');
  redOutput.Lines.Add('Cost per item: ' +
                      FormatCurr('R #,##0.00', costPerItem));
  redOutput.Lines.Add('Total items: ' + IntToStr(iTotalItems));
  redOutput.Lines.Add('Subtotal: ' +
                      FormatCurr('R #,##0.00', totalBeforeVAT));
  redOutput.Lines.Add('VAT (15%): ' +
                      FormatCurr('R #,##0.00', totalWithVAT - totalBeforeVAT));
  redOutput.Lines.Add('------------------------');
  redOutput.Lines.Add('TOTAL WITH VAT: ' +
                      FormatCurr('R #,##0.00', totalWithVAT));
  redOutput.Lines.Add('========================');
end;
```

---

## Essential Programming Patterns

### Data Type Conversions

Know these by heart:

```pascal
// String to Number
integerValue := StrToInt(stringValue);
realValue := StrToFloat(stringValue);

// Number to String
stringValue := IntToStr(integerValue);
stringValue := FloatToStr(realValue);
stringValue := FloatToStrF(realValue, ffFixed, 15, 2);  // 2 decimals
```

### Common GUI Operations

```pascal
// Get values
text := edtExample.Text;              // Edit box
number := spnExample.Value;           // Spin edit
selected := cmbExample.Text;          // Combo box
checked := chbExample.Checked;        // Checkbox
index := rdgExample.ItemIndex;        // Radio group

// Set values
pnlExample.Caption := 'Text';         // Panel text
lblExample.Caption := 'Text';         // Label text
shpExample.Brush.Color := clGreen;    // Shape color
imgExample.Visible := true;           // Show/hide image
```

### Building Multi-line Output

```pascal
// Using memo or rich edit
redOutput.Clear;  // Clear first!
redOutput.Lines.Add('Line 1');
redOutput.Lines.Add('Line 2');
redOutput.Lines.Add('');  // Blank line

// Using #13 for new lines in strings
message := 'Line 1' + #13 + 'Line 2' + #13 + 'Line 3';
ShowMessage(message);
```

### Mathematical Operations Reference

```pascal
// Basic operations
sum := a + b;
difference := a - b;
product := a * b;
quotient := a / b;

// Special operations
remainder := a mod b;      // Modulus (remainder)
withVAT := amount * 1.15;  // Add 15% VAT
percentage := (part / whole) * 100;
```

---

## Exam Success Tips

{: .important }
**Time Management:**

- Read ALL questions first (5 minutes)
- Question 1: ~30 minutes
- Question 2: ~35 minutes
- Question 3: ~30 minutes
- Checking: 5 minutes

{: .tip }
**Common Grade 10 Mistakes:**

1. Forgetting `:=` for assignment (not just `=`)
2. Missing semicolons at end of lines
3. Not converting data types (StrToInt, IntToStr)
4. Case sensitivity in string comparisons
5. Using `=` instead of `:=` for assignment

{: .note }
**Quick Checklist:**

- ✓ All variables declared with correct types
- ✓ Data type conversions done properly
- ✓ Semicolons at the end of statements
- ✓ BEGIN-END blocks properly paired
- ✓ Global variables declared at the top

---

## Practice Exercises

### Exercise 1: Temperature Converter

Create a program that:

- Inputs temperature in Celsius
- Converts to Fahrenheit (F = C × 9/5 + 32)
- Shows "Hot" (>30°C), "Nice" (15-30°C), or "Cold" (<15°C)

### Exercise 2: Shop Calculator

Build a simple shop system:

- Input item price and quantity
- Apply discount if buying 5+ items (10% off)
- Add 15% VAT
- Display formatted total

### Exercise 3: Grade Calculator

Design a marks system:

- Input marks for 3 tests
- Calculate average
- Determine symbol (A, B, C, D, F)
- Use global variables to store results

Remember: Practice makes perfect! Type out these examples yourself rather than copying and pasting. Understanding comes from doing!

Good luck with your exam! 🎯
