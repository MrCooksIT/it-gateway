---
layout: page
title: Grade 11 Mid-Year Paper 1 Study Guide
parent: Paper 1 Preparation
grand_parent: Examination Preparation
nav_order: 2
---

# Grade 11 Mid-Year Paper 1 Study Guide
{: .text-blue-200 }

Master programming concepts for your Grade 11 practical exam
{: .fs-6 .fw-300 }

---

## Paper Structure Overview

| Section | Topic | Marks |
|---------|-------|-------|
| **Section A** | General Programming Skills | 30 |
| **Section B** | Text File Manipulation | 30 |
| **Section C** | Arrays | 30 |
| **Section D** | Problem Solving | 30 |
| **Total** | | **120** |

---

## Section A: General Programming Skills (30 marks)

### 1. Form Event Handling (OnShow)

Setting form properties when the application starts:

```pascal
// Example: Form OnShow event
procedure TfrmExample.FormShow(Sender: TObject);
begin
  // Position and size panels
  pnlExample.Top := 8;
  pnlExample.Left := 8;
  pnlExample.Width := 1320;
  pnlExample.Height := 200;
  
  // Set font properties
  pnlExample.Font.Size := 23;
  pnlExample.Font.Name := 'Consolas';
end;
```

{: .note }
The OnShow event runs once when the form first appears - perfect for initial setup!

### 2. Mathematical Calculations with Built-in Functions

Common mathematical operations and formulas:

```pascal
// Volume calculation: V = πr²h
var 
  radius, height, volume: real;
begin
  radius := StrToFloat(edtRadius.Text);
  height := spnHeight.Value;
  volume := Pi * Sqr(radius) * height;
  edtVolume.Text := FloatToStrF(volume, ffFixed, 15, 3);
end;

// Other useful math functions:
// Sqr(x)      - Square (x²)
// Sqrt(x)     - Square root
// Pi          - 3.14159...
// Random(n)   - Random integer from 0 to n-1
// Ceil(x)     - Round up to nearest integer
// Floor(x)    - Round down to nearest integer
```

### 3. List Box Operations

Searching through list box items:

```pascal
// Search for item in list box
var 
  i: integer;
  found: boolean;
  searchTerm: string;
begin
  searchTerm := edtSearch.Text;
  found := false;
  
  for i := 0 to lsbItems.Items.Count - 1 do
  begin
    if lsbItems.Items[i] = searchTerm then
    begin
      found := true;
      break;  // Exit loop early
    end;
  end;
  
  // Visual feedback with shape color
  if found then
    shpIndicator.Brush.Color := clGreen
  else
    shpIndicator.Brush.Color := clRed;
end;
```

### 4. Random Number Generation

Creating random numbers within specific ranges:

```pascal
// Generate 6 random numbers between 50-100 and calculate average
var 
  i: integer;
  total, average: real;
begin
  total := 0;
  
  for i := 1 to 6 do
  begin
    total := total + Random(51) + 50;  // Random(51) gives 0-50, add 50 for 50-100
  end;
  
  average := total / 6;
  pnlResult.Caption := IntToStr(Ceil(average));  // Round up
end;
```

{: .tip }
Remember: `Random(n)` generates 0 to n-1, so add base value for different ranges!

### 5. String Analysis

Analyzing characters in strings:

```pascal
// Count vowels in text
var 
  i, vowelCount: integer;
  text: string;
  ch: char;
begin
  text := redInput.Text;
  vowelCount := 0;
  
  for i := 1 to Length(text) do
  begin
    ch := LowerCase(text[i])[1];  // Convert to lowercase
    if (ch = 'a') or (ch = 'e') or (ch = 'i') or 
       (ch = 'o') or (ch = 'u') then
      Inc(vowelCount);  // Same as vowelCount := vowelCount + 1
  end;
  
  ShowMessage('Total vowels: ' + IntToStr(vowelCount));
end;
```

---

## Section B: Text File Manipulation (30 marks)

### 1. Appending Data to Text Files

Adding new records to existing files:

```pascal
// Append data to file
var 
  txtFile: TextFile;
  name, registration: string;
  age: integer;
  carType: string;
begin
  // Get data from GUI
  name := edtName.Text;
  age := spnAge.Value;
  carType := cmbCarType.Text;
  registration := edtRegistration.Text;
  
  // Append to file
  AssignFile(txtFile, 'cars.txt');
  Append(txtFile);  // Open for adding (not overwriting!)
  WriteLn(txtFile, name + ',' + IntToStr(age) + ',' + 
          carType + ',' + registration);
  CloseFile(txtFile);
  
  ShowMessage('Data added to file successfully');
end;
```

### 2. Reading and Processing CSV Data

Parsing comma-separated values from text files:

```pascal
// Find fines for specific registration
var 
  txtFile: TextFile;
  line, regNum, selectedReg: string;
  fineAmount, totalFines: real;
  parts: array[1..3] of string;
  pos1, pos2: integer;
begin
  selectedReg := cmbRegistration.Text;
  totalFines := 0;
  redOutput.Clear;
  redOutput.Lines.Add('Fines for ' + selectedReg);
  
  AssignFile(txtFile, 'fines.txt');
  Reset(txtFile);  // Open for reading
  
  while not EOF(txtFile) do
  begin
    ReadLn(txtFile, line);
    
    // Parse CSV: Registration,Amount,Date
    pos1 := Pos(',', line);
    parts[1] := Copy(line, 1, pos1 - 1);  // Registration
    Delete(line, 1, pos1);
    
    pos2 := Pos(',', line);
    parts[2] := Copy(line, 1, pos2 - 1);  // Amount
    parts[3] := Copy(line, pos2 + 1, Length(line));  // Date
    
    // Check if registration matches
    if parts[1] = selectedReg then
    begin
      fineAmount := StrToFloat(parts[2]);
      totalFines := totalFines + fineAmount;
      redOutput.Lines.Add(parts[3] + ': R' + parts[2]);
    end;
  end;
  
  CloseFile(txtFile);
  redOutput.Lines.Add('------------------------');
  redOutput.Lines.Add('Total fines: R' + 
                      FloatToStrF(totalFines, ffFixed, 15, 2));
end;
```

{: .important }
**File Operations Sequence:**
1. `AssignFile` - Link variable to file
2. `Reset/Rewrite/Append` - Open file
3. `ReadLn/WriteLn` - Read/Write data
4. `CloseFile` - Always close when done!

---

## Section C: Arrays (30 marks)

### 1. Array Declaration and Initialization

Different ways to create arrays:

```pascal
// Global array with initial values
var 
  arrNums: array[1..3] of integer = (15, 19, 25);

// Empty array declaration
var 
  arrCars: array[1..10] of string;
  arrMarks: array[1..5] of integer;
```

### 2. Basic Array Operations

Working with array elements:

```pascal
// Display specific element
procedure TfrmExample.btnDisplayClick(Sender: TObject);
begin
  redOutput.Text := IntToStr(arrNums[2]);  // Display second element
end;

// Add item at specific index
procedure TfrmExample.btnAddClick(Sender: TObject);
var 
  carName: string;
  index: integer;
begin
  carName := edtCar.Text;
  index := spnIndex.Value;
  
  if (index >= 1) and (index <= 10) then  // Validate index
  begin
    arrCars[index] := carName;
    ShowMessage('Item added at position ' + IntToStr(index));
  end
  else
    ShowMessage('Invalid index!');
end;
```

### 3. Array Calculations

Common array algorithms:

```pascal
// Sum all elements
var 
  i, total: integer;
begin
  total := 0;
  for i := 1 to 5 do
    total := total + arrMarks[i];
  
  ShowMessage('Total: ' + IntToStr(total));
end;

// Find maximum value
var 
  i, bestMark: integer;
begin
  bestMark := arrMarks[1];  // Start with first
  
  for i := 2 to 5 do
  begin
    if arrMarks[i] > bestMark then
      bestMark := arrMarks[i];
  end;
  
  redOutput.Text := 'Best mark: ' + IntToStr(bestMark);
end;
```

---

## Section D: Problem Solving (30 marks)

### 1. File Backup with Headers

Creating backup files with additional information:

```pascal
// Copy file with header information
var 
  inputFile, outputFile: TextFile;
  line: string;
  lineCount: integer;
begin
  lineCount := 0;
  
  // Open files
  AssignFile(inputFile, edtInputFile.Text);
  AssignFile(outputFile, edtOutputFile.Text);
  Reset(inputFile);      // Open for reading
  Rewrite(outputFile);   // Create new file
  
  // Write header information
  WriteLn(outputFile, '=================================');
  WriteLn(outputFile, 'BACKUP FILE: ' + edtInputFile.Text);
  WriteLn(outputFile, 'Date/Time: ' + DateTimeToStr(Now));
  WriteLn(outputFile, '=================================');
  
  // Copy all lines
  while not EOF(inputFile) do
  begin
    ReadLn(inputFile, line);
    WriteLn(outputFile, line);
    Inc(lineCount);
  end;
  
  // Add footer
  WriteLn(outputFile, '=================================');
  WriteLn(outputFile, 'Total lines: ' + IntToStr(lineCount));
  
  CloseFile(inputFile);
  CloseFile(outputFile);
  
  redOutput.Text := 'Backup completed. Processed ' + 
                    IntToStr(lineCount) + ' rows.';
end;
```

### 2. Array Element Insertion

Inserting elements with shifting:

```pascal
// Insert element at position 5
var 
  arrCars: array[1..15] of string;
  arrCoolFactor: array[1..15] of integer;
  i: integer;
begin
  // Shift elements from position 5 onwards to the right
  for i := 14 downto 5 do  // Work backwards!
  begin
    arrCars[i + 1] := arrCars[i];
    arrCoolFactor[i + 1] := arrCoolFactor[i];
  end;
  
  // Insert new elements at position 5
  arrCars[5] := 'Toyota Supra MK5';
  arrCoolFactor[5] := 81;
  
  // Display updated arrays
  redOutput.Clear;
  for i := 1 to 15 do
  begin
    if arrCars[i] <> '' then  // Only show non-empty
      redOutput.Lines.Add(IntToStr(i) + ': ' + arrCars[i] + 
                         ' (Cool Factor: ' + 
                         IntToStr(arrCoolFactor[i]) + ')');
  end;
end;
```

---

## Key Programming Patterns

### String Parsing Functions

```pascal
// Essential string functions
Pos(',', text)         // Find position of comma
Copy(text, 1, 5)       // Extract 5 characters from position 1
Delete(text, 1, 5)     // Remove first 5 characters
Length(text)           // Get string length
LowerCase(text)        // Convert to lowercase
UpperCase(text)        // Convert to uppercase
```

### File Operation Patterns

```pascal
// Reading pattern
AssignFile(f, 'file.txt');
Reset(f);
while not EOF(f) do
begin
  ReadLn(f, line);
  // Process line
end;
CloseFile(f);

// Writing pattern
AssignFile(f, 'file.txt');
Rewrite(f);  // or Append(f)
WriteLn(f, data);
CloseFile(f);
```

### Array Patterns

```pascal
// Linear search
found := false;
for i := 1 to size do
  if arr[i] = searchValue then
  begin
    found := true;
    break;
  end;

// Find min/max
max := arr[1];
for i := 2 to size do
  if arr[i] > max then
    max := arr[i];
```

---

## Exam Tips

{: .important }
**Time Management:**
- Section A & B: ~20 minutes each
- Section C & D: ~25 minutes each
- Reserve 10 minutes for checking

{: .tip }
**Common Mistakes to Avoid:**
1. Forgetting to close files
2. Array index out of bounds
3. Not initializing totals to 0
4. Using `Rewrite` instead of `Append`
5. Incorrect string parsing positions

{: .note }
**Quick Checks:**
- All files closed with `CloseFile`
- Arrays start at index 1 (not 0)
- Variables initialized before use
- Loops use correct start/end values

Good luck with your exam!