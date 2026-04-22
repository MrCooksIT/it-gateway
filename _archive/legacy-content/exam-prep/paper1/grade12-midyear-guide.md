---
layout: page
title: Grade 12 Mid-Year Paper 1 Study Guide
parent: Paper 1 Preparation
grand_parent: Examination Preparation
nav_order: 1
---

# Grade 12 Mid-Year Paper 1 Study Guide


Complete preparation guide for the Grade 12 practical programming mid-year exam
{: .fs-6 .fw-300 }

---

## Paper Structure Overview

| Section       | Topic                       | Marks   |
| ------------- | --------------------------- | ------- |
| **Section A** | General Programming Skills  | ~40     |
| **Section B** | Database & SQL              | ~40     |
| **Section C** | Object-Oriented Programming | ~40     |
| **Section D** | Problem-Solving Programming | ~30     |
| **Total**     |                             | **150** |

---

## Section A: General Programming Skills

### 1. GUI Component Properties

Setting visual properties of interface components programmatically:

```pascal
// Example: Formatting a panel
pnlExample.Height := 100;
pnlExample.Width := 500;
pnlExample.Font.Name := 'Arial';
pnlExample.Font.Size := 14;
```

{: .note }
Remember to access properties using the dot notation: `ComponentName.PropertyName`

### 2. Built-in Mathematical Functions

Common math functions you should know:

```pascal
// Floor function - rounds down to nearest integer
edtFloor.Text := IntToStr(Floor(5.7));  // Result: 5

// Power function - raises to a power
edtPower.Text := FloatToStrF(Power(2, 3), ffFixed, 15, 2);  // Result: 8.00

// Other useful functions:
// Ceil(x)     - rounds up
// Round(x)    - rounds to nearest integer
// Trunc(x)    - removes decimal part
// Sqrt(x)     - square root
// Sqr(x)      - square (x²)
```

### 3. Conditional Logic

Making decisions based on user input:

```pascal
// Example: Age and checkbox validation
if (spnAge.Value >= 18) and (chkLicense.Checked) then
  ShowMessage('You can apply now!')
else
  ShowMessage('Requirements not met');

// Multiple conditions
if (condition1) and (condition2) or (condition3) then
  // code here
```

### 4. Message Dialogs

Displaying information to users:

```pascal
// Simple message
ShowMessage('Success message');

// Message with variable
ShowMessage('Welcome ' + sName + '!');

// Multi-line message
ShowMessage('Line 1' + #13 + 'Line 2');
```

### 5. Loop Structures

Creating patterns using nested loops:

```pascal
// Example: Star triangle pattern
for i := 1 to rows do
begin
  for j := 1 to i do
    redOutput.Text := redOutput.Text + '*';
  redOutput.Text := redOutput.Text + #13;  // New line
end;

// Result:
// *
// **
// ***
// ****
```

### 6. File I/O Operations

Reading and displaying file contents:

```pascal
// Reading a text file
var
  txtFile: TextFile;
  line: string;
begin
  AssignFile(txtFile, 'data.txt');
  Reset(txtFile);  // Open for reading

  while not EOF(txtFile) do
  begin
    ReadLn(txtFile, line);
    redDisplay.Lines.Add(line);
  end;

  CloseFile(txtFile);
end;
```

---

## Section B: Database & SQL

### 1. SQL Query Fundamentals

Key SQL concepts to master:

#### SELECT DISTINCT

```sql
-- Get unique values from a column
SELECT DISTINCT City FROM Customers;
```

#### WHERE Clauses

```sql
-- Basic comparison
SELECT * FROM Products WHERE Price > 20;

-- Multiple conditions
SELECT * FROM Orders
WHERE OrderDate >= '2024-01-01'
  AND Status = 'Completed';
```

#### GROUP BY with COUNT

```sql
-- Count items per category
SELECT Category, COUNT(*) as Total
FROM Products
GROUP BY Category;
```

#### DELETE Statements

```sql
-- Delete specific records
DELETE FROM Orders WHERE OrderID = 123;

-- Delete with condition
DELETE FROM Products WHERE Stock = 0;
```

#### Dual Table Queries (Joins)

```sql
-- Link tables using WHERE clause
SELECT c.CustomerName, o.OrderDate, o.Total
FROM Customers c, Orders o
WHERE c.CustomerID = o.CustomerID;

-- With additional conditions
SELECT p.ProductName, s.Quantity
FROM Products p, Sales s
WHERE p.ProductID = s.ProductID
  AND s.SaleDate = '2024-06-15';
```

### 2. Database Navigation with Delphi

Working with database tables in code:

```pascal
// Loop through all records
tblExample.First;
while not tblExample.EOF do
begin
  // Process current record
  displayText := tblExample['fieldName'];
  redOutput.Lines.Add(displayText);

  // Move to next record
  tblExample.Next;
end;

// Navigate to specific positions
tblExample.First;    // Go to first record
tblExample.Last;     // Go to last record
tblExample.Prior;    // Go to previous record
tblExample.Next;     // Go to next record
```

---

## Section C: Object-Oriented Programming (42 marks)

### Class Structure Template

```pascal
type
  TExampleClass = class
  private
    fAttribute1: string;     // Private attributes start with 'f'
    fAttribute2: real;
  public
    constructor Create(param1: string; param2: real);

    // Getters (return private values)
    function getAttribute1: string;
    function getAttribute2: real;

    // Setters/Mutators (change private values)
    procedure setAttribute1(value: string);
    procedure setAttribute2(value: real);

    // Other methods
    function calculateSomething: real;
    function toString: string;
  end;
```

### Constructor Implementation

```pascal
constructor TExampleClass.Create(param1: string; param2: real);
begin
  fAttribute1 := param1;
  fAttribute2 := param2;
end;
```

### Getter Methods

```pascal
function TExampleClass.getAttribute1: string;
begin
  Result := fAttribute1;
end;

function TExampleClass.getAttribute2: real;
begin
  Result := fAttribute2;
end;
```

### Setter/Mutator Methods

```pascal
procedure TExampleClass.setAttribute1(value: string);
begin
  fAttribute1 := value;
end;

procedure TExampleClass.setAttribute2(value: real);
begin
  if value >= 0 then  // Validation example
    fAttribute2 := value;
end;
```

### Calculation Methods

```pascal
function TExampleClass.calculateSomething: real;
begin
  Result := fAttribute2 / 10.5;  // Example calculation
end;
```

### Conditional Methods with Parameters

```pascal
function TExampleClass.getCategory(level: integer): integer;
begin
  case level of
    0: Result := 5;
    1: Result := 10;
    2: Result := 15;
  else
    Result := 20;
  end;
  Result := Trunc(fAttribute2 / Result);  // Truncate to integer
end;
```

### toString Method

```pascal
function TExampleClass.toString: string;
begin
  Result := 'Name: ' + fAttribute1 + #13 +
            'Value: ' + FloatToStr(fAttribute2) + #13 +
            'Calculated: ' + FloatToStrF(calculateSomething, ffFixed, 15, 3);
end;
```

### Using Objects in Main Program

```pascal
var
  objExample: TExampleClass;
begin
  // Create object
  objExample := TExampleClass.Create('Test Name', 25.5);

  // Use getter
  edtDisplay.Text := objExample.getAttribute1;

  // Use setter
  objExample.setAttribute1('New Name');

  // Use calculation method
  pnlResult.Caption := FloatToStrF(objExample.calculateSomething, ffFixed, 15, 3);

  // Use toString
  redOutput.Text := objExample.toString;

  // Don't forget to free the object when done!
  objExample.Free;
end;
```

---

## Section D: Problem-Solving Programming (30 marks)

### 1. Array Display Operations

Showing array contents in formatted columns:

```pascal
// Display with tab alignment
for i := 1 to arraySize do
begin
  redOutput.Lines.Add(arrNames[i] + #9 +
                      FloatToStrF(arrValues[i], ffFixed, 10, 2));
end;
```

{: .tip }
**Key formatting characters:**

- `#9` = Tab character (for column alignment)
- `#13` = Carriage return (new line)

### 2. Mathematical Computations

Calculating averages and totals:

```pascal
// Calculate average
total := 0;
for i := 1 to arraySize do
  total := total + arrValues[i];

average := total / arraySize;
edtAverage.Text := FloatToStrF(average, ffFixed, 15, 2);
```

### 3. Sorting Algorithms

Simple bubble sort implementation:

```pascal
// Sort two parallel arrays (bubble sort)
for i := 1 to arraySize - 1 do
  for j := 1 to arraySize - i do
    if arrValues[j] < arrValues[j + 1] then  // Descending order
    begin
      // Swap values
      tempValue := arrValues[j];
      arrValues[j] := arrValues[j + 1];
      arrValues[j + 1] := tempValue;

      // Swap corresponding names
      tempName := arrNames[j];
      arrNames[j] := arrNames[j + 1];
      arrNames[j + 1] := tempName;
    end;
```

### 4. Finding Maximum/Minimum Values

```pascal
// Find highest value and its position
highest := arrValues[1];
position := 1;

for i := 2 to arraySize do
begin
  if arrValues[i] > highest then
  begin
    highest := arrValues[i];
    position := i;
  end;
end;

ShowMessage('Highest: ' + arrNames[position] +
            ' with value ' + FloatToStr(highest));
```

---

## Exam Tips

{: .important }
**Time Management:**

- Read through the entire paper first (10 minutes)
- Allocate time based on marks: ~1 minute per mark
- Leave time for testing and debugging

{: .tip }
**Common Mistakes to Avoid:**

1. Forgetting to initialize variables
2. Off-by-one errors in loops
3. Not closing files after use
4. Forgetting to free objects
5. Incorrect SQL syntax (missing quotes, semicolons)

{: .note }
**Quick Checks Before Submitting:**

- All buttons have event handlers
- SQL queries end with semicolon
- Files are properly closed
- Objects are freed after use
- Output is formatted as requested

---

- Practice writing complete classes from scratch
- Create small programs combining GUI, database, and OOP
- Review the class activties and Virtual learner support day

Good luck with your exam!
