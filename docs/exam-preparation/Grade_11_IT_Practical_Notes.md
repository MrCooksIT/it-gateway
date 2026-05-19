# Grade 11 Information Technology — Practical Programming Reference

*A topic-by-topic reference for Delphi programming concepts and syntax, building on the Grade 10 reference.*

These notes assume the Grade 10 reference is already known: variables, data types, type conversions, form components, simple IF/ELSE/CASE, the `for` loop, the InputBox, arithmetic and string functions. Each section below begins with a short **Recap** of the relevant Grade 10 material before introducing the new Grade 11 material.

A **cheat sheet appendix** at the end of the document summarises every new pattern.

---

# SECTION 1: LOOPS REVISITED — WHILE AND REPEAT

## Recap (Grade 10)

A **for loop** is used when the number of repetitions is known in advance. The syntax is:

```pascal
for iCount := 1 to 10 do
   <statement>;
```

## 1.1 The two new loop types

A `for` loop works when the count is known. Often the count is **not** known — the loop must keep going until something happens. There are two structures for this:

| Loop | When the condition is checked | Runs at least once? |
|---|---|---|
| `while…do` | **Before** each iteration | No — body can run zero times |
| `repeat…until` | **After** each iteration | Yes — body always runs at least once |

## 1.2 The while…do loop — pre-test

```pascal
while <condition> do
   <statement>;

while <condition> do
   begin
      <statement>;
      <statement>;
   end;
```

The condition is checked **before** the body runs. If the condition is false at the very start, the body never runs at all. The loop continues as long as the condition is **true**.

```pascal
iCount := 1;
while iCount <= 10 do
   begin
      memOutput.Lines.Add(IntToStr(iCount));
      iCount := iCount + 1;          // VITAL: change something so the loop can end
   end;
```

**The most common bug** is forgetting to change the variable that the condition tests. Without `iCount := iCount + 1` above, `iCount` stays at 1 forever and the loop never ends — the program freezes.

## 1.3 The repeat…until loop — post-test

```pascal
repeat
   <statement>;
   <statement>;
until <condition>;
```

The body runs **first**, then the condition is checked. The loop continues as long as the condition is **false**, and stops when it becomes **true**. The body always runs at least once.

Note that there is no `begin…end` — the `repeat…until` itself acts as the block. The condition logic is the opposite of `while`: `while` keeps going while *true*; `repeat` keeps going until *true*.

```pascal
repeat
   sInput := InputBox('Input', 'Enter a number (0 to quit):', '0');
   rValue := StrToFloat(sInput);
   // … process rValue …
until rValue = 0;
```

## 1.4 Choosing the right loop

| Situation | Loop |
|---|---|
| Count is known (1 to 10, every item in an array) | `for` |
| Continue while a condition holds, may run zero times | `while…do` |
| Keep prompting the user until they enter something specific | `repeat…until` |
| Read a text file until end-of-file | `while not EOF do` |

## 1.5 Common patterns

**Sentinel-controlled loop** — keep going until a special "end-of-data" value (the sentinel) is entered:

```pascal
rTotal := 0;
iCount := 0;
repeat
   sInput := InputBox('Price', 'Enter price (0 to finish):', '0');
   rPrice := StrToFloat(sInput);
   if rPrice > 0 then
      begin
         rTotal := rTotal + rPrice;
         Inc(iCount);
      end;
until rPrice = 0;
```

**Validation loop** — keep prompting until the user gives valid input:

```pascal
repeat
   sInput := InputBox('Age', 'Enter age (0–120):', '0');
   iAge := StrToInt(sInput);
until (iAge >= 0) AND (iAge <= 120);
```

---

# SECTION 2: ARRAYS

An **array** is a collection of values of the same type, stored under a single variable name and accessed by an index (a position number).

## 2.1 Declaring an array

```pascal
var
   arrNumbers : array [1..10] of Integer;
   arrNames   : array [1..50] of String;
   arrPrices  : array [1..100] of Real;
   arrFlags   : array [1..20] of Boolean;
```

The numbers in brackets are the **lowest index** and **highest index**. Indexes most commonly start at 1, but can start at any value (e.g. `[0..9]` is also valid).

Arrays can also be declared as a type alias for cleaner code:

```pascal
type
   TIntArray = array [1..100] of Integer;
var
   arrScores : TIntArray;
```

## 2.2 Reading and writing individual elements

Use square brackets with the index:

```pascal
arrNumbers[1] := 42;                       // store 42 at position 1
arrNumbers[2] := arrNumbers[1] * 2;        // 84 at position 2
iValue := arrNumbers[1];                   // retrieve the value at position 1
```

## 2.3 Looping over an array

The standard way to walk through every element is with a `for` loop, using the counter as the index:

```pascal
for i := 1 to 10 do
   arrNumbers[i] := i * i;                 // populate with squares: 1, 4, 9, 16, ...

for i := 1 to 10 do
   memOutput.Lines.Add(IntToStr(arrNumbers[i]));     // display each element
```

## 2.4 The Low and High functions

Hard-coding `1 to 10` couples the loop to a specific size. The `Low` and `High` functions return the lowest and highest valid index of an array:

```pascal
for i := Low(arrNumbers) to High(arrNumbers) do
   …
```

If the array is later resized, the loops keep working without modification.

## 2.5 Parallel arrays

A **parallel array** structure uses two or more arrays where **the same index in each array refers to the same real-world item**. For example, position `[3]` of every array describes "the third item":

```pascal
var
   arrNames  : array [1..100] of String;     // names
   arrAges   : array [1..100] of Integer;    // ages
   arrEmails : array [1..100] of String;     // email addresses
```

Position `[7]` in every array refers to person 7's name, age and email.

### Critical rule of parallel arrays

**Whenever the order of one array changes, the same change must happen to every parallel array at the same indexes.** Sorting `arrAges` on its own breaks the link — person 7's age would end up next to a different person's name. Any swap must be performed on all three arrays at the same indexes.

## 2.6 Common array operations

**Searching for a value** — linear search:

```pascal
iFoundAt := -1;                                    // -1 means "not found"
for i := Low(arr) to High(arr) do
   if arr[i] = target then
      begin
         iFoundAt := i;
         Break;                                    // optional — stop searching
      end;
```

**Finding the maximum** — remember the index, not just the value:

```pascal
iMaxIndex := Low(arr);
for i := Low(arr) + 1 to High(arr) do
   if arr[i] > arr[iMaxIndex] then
      iMaxIndex := i;
// arr[iMaxIndex] is the largest value; iMaxIndex is its position
```

**Counting items that meet a condition**:

```pascal
iCount := 0;
for i := Low(arr) to High(arr) do
   if arr[i] > 100 then
      Inc(iCount);
```

**Summing and averaging**:

```pascal
rTotal := 0;
for i := Low(arr) to High(arr) do
   rTotal := rTotal + arr[i];
rAverage := rTotal / Length(arr);                  // or use High(arr) - Low(arr) + 1
```

---

# SECTION 3: SORTING — KEEPING ORDER

## 3.1 The bubble sort

A **bubble sort** repeatedly steps through the array, comparing each pair of adjacent items and swapping them if they are in the wrong order. After enough passes, the largest values "bubble" to the top.

Generic ascending sort:

```pascal
for i := 1 to iCount - 1 do
   for j := 1 to iCount - i do                  // inner loop shrinks each outer pass
      if arr[j] > arr[j + 1] then
         begin
            // swap arr[j] and arr[j+1]
            iTemp := arr[j];
            arr[j] := arr[j + 1];
            arr[j + 1] := iTemp;
         end;
```

For descending order, swap when `arr[j] < arr[j + 1]` instead.

The swap pattern (three lines, using a temporary variable) is what physically moves the values:

```pascal
iTemp    := arr[j];
arr[j]   := arr[j + 1];
arr[j + 1] := iTemp;
```

## 3.2 Sorting parallel arrays — swap them all

When the array being sorted has parallel partners (e.g. names alongside scores), every swap must happen on **all the parallel arrays at the same indexes**:

```pascal
if arrScores[j] < arrScores[j + 1] then
   begin
      // Swap scores
      iTemp := arrScores[j];
      arrScores[j] := arrScores[j + 1];
      arrScores[j + 1] := iTemp;
      // Swap names (parallel)
      sTemp := arrNames[j];
      arrNames[j] := arrNames[j + 1];
      arrNames[j + 1] := sTemp;
   end;
```

Forgetting any of the parallel swaps means names will no longer line up with scores after sorting.

## 3.3 Selection sort — an alternative

Selection sort repeatedly **finds the smallest remaining item** and puts it in the next position.

```pascal
for i := Low(arr) to High(arr) - 1 do
   begin
      iMinIndex := i;
      for j := i + 1 to High(arr) do
         if arr[j] < arr[iMinIndex] then
            iMinIndex := j;
      if iMinIndex <> i then
         begin
            iTemp := arr[i];
            arr[i] := arr[iMinIndex];
            arr[iMinIndex] := iTemp;
         end;
   end;
```

Selection sort is sometimes preferred over bubble sort because it does fewer swaps; the comparison count is similar.

---

# SECTION 4: TEXT FILES

A **text file** is a sequence of characters stored on disk, usually divided into lines. Reading and writing text files is the standard way to make data persist between program runs.

## 4.1 The five-step file pattern

Every text-file operation follows the same five steps:

1. **Declare** a file variable of type `TextFile`.
2. **Assign** the variable to a physical file with `AssignFile`.
3. **Open** the file with `Reset`, `Rewrite` or `Append`.
4. **Read or write** with `ReadLn` or `WriteLn` inside a loop.
5. **Close** the file with `CloseFile`.

## 4.2 The three open modes

| Mode | Purpose | If file does not exist | If file already exists |
|---|---|---|---|
| `Reset(f)` | Open for reading | Crashes (use `FileExists` first) | Reads from the start |
| `Rewrite(f)` | Create a new file for writing | Creates an empty file | **Wipes** all existing content |
| `Append(f)` | Add to the end of an existing file | Creates an empty file | Adds at the end, keeping existing content |

## 4.3 Checking if a file exists before opening

`Reset` on a missing file causes a runtime error and crashes the program. Always check first:

```pascal
if not FileExists('data.txt') then
   begin
      ShowMessage('File not found');
      Exit;
   end;
AssignFile(tFile, 'data.txt');
Reset(tFile);
```

## 4.4 Reading every line of a file

```pascal
var
   tFile : TextFile;
   sLine : String;
begin
   AssignFile(tFile, 'data.txt');
   Reset(tFile);
   while not EOF(tFile) do                     // EOF = end of file
      begin
         ReadLn(tFile, sLine);
         // … process sLine …
      end;
   CloseFile(tFile);
end;
```

`EOF(tFile)` returns True once the last line has been read. `while not EOF` is the standard way to walk every line.

## 4.5 Writing lines to a new file

```pascal
AssignFile(tFile, 'output.txt');
Rewrite(tFile);                                // create new (overwrites if exists)
WriteLn(tFile, 'First line');
WriteLn(tFile, 'Second line');
CloseFile(tFile);
```

`WriteLn(tFile, …)` writes a line followed by a newline. `Write(tFile, …)` writes without the newline.

## 4.6 Appending to an existing file

```pascal
AssignFile(tFile, 'log.txt');
Append(tFile);
WriteLn(tFile, 'New entry');
CloseFile(tFile);
```

## 4.7 Why CloseFile is essential

Forgetting `CloseFile` has serious consequences:

* The last writes may sit in a memory buffer and never reach the disk — **data loss**.
* The file remains "locked" — other programs (and other code) cannot open it.
* If the program crashes with the file still open, the file may become **corrupted**.

Always call `CloseFile` as the last step.

## 4.8 Parsing delimited lines

Data files often store multiple fields per line, separated by a special character (the **delimiter**). Common delimiters include `,` (CSV), `;`, `|`, `#` or a tab.

Example line with `#` delimiter:

```
Sipho#16#Pretoria
```

The standard pattern to split a delimited line uses `Pos`, `Copy` and `Delete` together:

| Function | Purpose |
|---|---|
| `Pos(sub, s)` | Returns the position of the first `sub` inside `s`, or 0 if not found |
| `Copy(s, start, count)` | Returns a piece of `s` starting at `start`, `count` characters long |
| `Delete(s, start, count)` | Removes `count` characters from `s` starting at `start` |

To split `'Name#Age#City'` into three pieces:

```pascal
iPos := Pos('#', sLine);
sField1 := Copy(sLine, 1, iPos - 1);           // everything before the first #
Delete(sLine, 1, iPos);                          // remove field 1 and its delimiter

iPos := Pos('#', sLine);
sField2 := Copy(sLine, 1, iPos - 1);           // everything before the next #
Delete(sLine, 1, iPos);                          // remove field 2 and its delimiter

sField3 := sLine;                                // what is left is the last field
```

The key idea: after each `Delete`, `sLine` shrinks. The next `Pos('#', sLine)` finds the **next** delimiter because the previous one is gone.

## 4.9 Loading file data into parallel arrays

The complete pattern — file existence check, reading each line, parsing fields, populating arrays:

```pascal
iCount := 0;

if not FileExists('people.txt') then
   begin
      ShowMessage('File not found');
      Exit;
   end;

AssignFile(tFile, 'people.txt');
Reset(tFile);
while not EOF(tFile) do
   begin
      ReadLn(tFile, sLine);
      Inc(iCount);

      iPos := Pos('#', sLine);
      arrNames[iCount] := Copy(sLine, 1, iPos - 1);
      Delete(sLine, 1, iPos);

      iPos := Pos('#', sLine);
      arrAges[iCount] := StrToInt(Copy(sLine, 1, iPos - 1));
      Delete(sLine, 1, iPos);

      arrCities[iCount] := sLine;
   end;
CloseFile(tFile);
```

`iCount` is the **logical size** of the arrays — how many items were actually loaded. Most subsequent loops should use `for i := 1 to iCount do …`, not `Low(arr) to High(arr)`, because the array slots beyond `iCount` will contain garbage.

---

# SECTION 5: FILTERING — FINDING ITEMS THAT MATCH A CONDITION

**Filtering** means walking through a collection (an array) and keeping only the items that meet some condition.

The pattern is always the same:

```pascal
for i := 1 to iCount do
   if <condition> then
      <do something with arr[i]>;
```

The "do something" might be:

* Display the matching item in a memo / rich edit.
* Write the matching item to a file.
* Count the matching items.
* Copy the matching item into a result array.
* Calculate a running total or average over the matching items.

A worked example — finding everyone older than 18 and displaying their name:

```pascal
redOutput.Clear;
redOutput.Lines.Add('Adults:');
for i := 1 to iCount do
   if arrAges[i] >= 18 then
      redOutput.Lines.Add(arrNames[i]);
```

Filtering does not require a separate result array unless the filtered items must be used again later. Often the items are processed (displayed, written, counted) directly inside the loop.

---

# SECTION 6: MODULAR PROGRAMMING

## Recap (Grade 10)

In Grade 10 all the code went inside the button's event handler. As programs grow, that approach makes them hard to read, test and maintain. The solution is **modular programming** — break the code up into small, named pieces called procedures and functions.

## 6.1 Procedure vs function

| Type | Performs a task | Returns a value? |
|---|---|---|
| `procedure` | Yes | No |
| `function` | Yes | Yes — exactly one value |

Use a **procedure** when you want to *do something* (display a message, clear a form, save to file). Use a **function** when you want to *get something back* (calculate an area, check if a number is prime, build a corrected string).

## 6.2 The shape of a procedure

```pascal
procedure ProcedureName(parameter1 : Type; parameter2 : Type);
var
   localVariables : Type;
begin
   <statements>;
end;
```

A worked example:

```pascal
procedure ClearAll;
begin
   edtName.Text := '';
   edtAge.Text  := '';
   memOutput.Lines.Clear;
end;
```

This procedure takes no parameters and just performs its task when called.

## 6.3 The shape of a function

```pascal
function FunctionName(parameter1 : Type; parameter2 : Type) : ReturnType;
var
   localVariables : Type;
begin
   <statements>;
   Result := <value to return>;
end;
```

The key differences from a procedure:

* The header ends with `: ReturnType;` — the function header declares what kind of value will come back (Integer, Real, String, Boolean, etc.).
* Inside the function, the special variable `Result` holds whatever the function will return. Assigning to `Result` is how you say "return this".

A worked example:

```pascal
function CalculateArea(rLength, rWidth : Real) : Real;
begin
   Result := rLength * rWidth;
end;
```

## 6.4 Parameters — passing information in

The values in the brackets after the function/procedure name are **parameters** — the inputs to the function. They behave like local variables; each call supplies a value.

```pascal
function Average(rA, rB, rC : Real) : Real;     // three parameters of the same type
begin
   Result := (rA + rB + rC) / 3;
end;
```

When two parameters share a type, they can be listed together with one type declaration: `rA, rB, rC : Real`. When the types differ, each gets its own type declaration, separated by semicolons:

```pascal
function Format(sName : String; iAge : Integer; rPrice : Real) : String;
begin
   Result := sName + ' (' + IntToStr(iAge) + '): R' + FloatToStr(rPrice);
end;
```

## 6.5 Calling functions and procedures

A **procedure** is called as a statement on its own:

```pascal
ClearAll;
DisplayHeader;
```

A **function** is called wherever a value of its return type would be valid — usually on the right of an `:=`, or inside another expression:

```pascal
rArea := CalculateArea(5.0, 3.0);                   // 15.0
lblOut.Caption := IntToStr(CalculateArea(5.0, 3.0));
if Average(rA, rB, rC) > 50 then
   …
```

## 6.6 Local vs global variables

The **scope** of a variable is the region of code where it is visible.

* A **local variable** is declared inside a procedure or function (in its own `var` block, between the header and `begin`). It exists only while that routine is running and is invisible outside it.
* A **global variable** is declared at the top of the unit (outside all the procedures). It is visible to every procedure and function in the unit.

Local variables are preferred because they cannot accidentally be changed by code elsewhere. Global variables should only be used when a value really must be shared across several procedures (e.g. an object that persists between button clicks).

## 6.7 Why modular programming matters

* **Readability** — small named routines are easier to follow than one giant block.
* **Testing** — each routine can be tested in isolation.
* **Reuse** — a function written once can be called from many places.
* **Maintenance** — if a calculation changes, the change happens in only one place.

---

# SECTION 7: COMMON PATTERNS FOR STRING-PROCESSING FUNCTIONS

A useful application of functions is **string manipulation**. The patterns below come up in many forms.

## 7.1 Building a new string from an old one

The general pattern: walk through the input one character at a time, decide what to do with each character, and build up a new string.

```pascal
function TransformString(sInput : String) : String;
var
   i    : Integer;
   sNew : String;
begin
   sNew := '';
   for i := 1 to Length(sInput) do
      sNew := sNew + <transformed version of sInput[i]>;
   Result := sNew;
end;
```

## 7.2 Replacing certain characters

The transformation is a `case` on each character:

```pascal
function ReplaceLetters(sInput : String) : String;
var
   i    : Integer;
   sNew : String;
begin
   sNew := '';
   for i := 1 to Length(sInput) do
      case sInput[i] of
         '0' : sNew := sNew + 'O';
         '1' : sNew := sNew + 'I';
         '3' : sNew := sNew + 'E';
      else
         sNew := sNew + sInput[i];      // unchanged
      end;
   Result := sNew;
end;
```

Don't forget the `else` branch — without it, characters not listed in the case would be silently dropped.

## 7.3 Removing certain characters

To remove a character, just **skip it** when building the new string:

```pascal
function RemoveChar(sInput : String; cBad : Char) : String;
var
   i    : Integer;
   sNew : String;
begin
   sNew := '';
   for i := 1 to Length(sInput) do
      if sInput[i] <> cBad then
         sNew := sNew + sInput[i];
   Result := sNew;
end;
```

An alternative is to walk the string **backwards** and `Delete` matching characters in place:

```pascal
for i := Length(sInput) downto 1 do
   if sInput[i] = cBad then
      Delete(sInput, i, 1);
```

Walking **backwards** (with `downto`) is important — if you walked forwards while deleting, positions of remaining characters would shift and some would be skipped.

## 7.4 Reversing a string

Build a new string by walking the original from end to start:

```pascal
function Reverse(sInput : String) : String;
var
   i    : Integer;
   sNew : String;
begin
   sNew := '';
   for i := Length(sInput) downto 1 do
      sNew := sNew + sInput[i];
   Result := sNew;
end;
```

## 7.5 Checking for a property — Boolean functions

A function that returns a Boolean answers a yes/no question. Common shape:

```pascal
function IsValid(sInput : String) : Boolean;
begin
   if <some condition on sInput> then
      Result := True
   else
      Result := False;
end;
```

Or more concisely, since the condition is already a Boolean:

```pascal
function IsValid(sInput : String) : Boolean;
begin
   Result := <some condition on sInput>;
end;
```

### Example — palindrome check

A palindrome reads the same forwards and backwards (`'radar'`, `'level'`, `'11311'`).

```pascal
function IsPalindrome(sInput : String) : Boolean;
var
   i        : Integer;
   sRev     : String;
begin
   sRev := '';
   for i := Length(sInput) downto 1 do
      sRev := sRev + sInput[i];
   Result := (sRev = sInput);
end;
```

### Example — prime number check

A prime number has exactly two factors: 1 and itself.

```pascal
function IsPrime(iNum : Integer) : Boolean;
var
   i, iFactors : Integer;
begin
   if iNum < 2 then
      begin
         Result := False;
         Exit;
      end;
   iFactors := 0;
   for i := 1 to iNum do
      if iNum MOD i = 0 then
         Inc(iFactors);
   Result := (iFactors = 2);
end;
```

`a MOD b` is the remainder when `a` is divided by `b`. A remainder of zero means `b` divides `a` exactly — `b` is a factor of `a`.

## 7.6 Composing functions

Functions can be combined to express more complex ideas. The result of one function becomes the input to another:

```pascal
sStep1   := RemoveChar(sInput, '#');         // strip out the hashes
sFinal   := ReplaceLetters(sStep1);          // then fix wrong letters
edtOut.Text := sFinal;
```

Or in one line — Delphi evaluates the inner function first:

```pascal
edtOut.Text := ReplaceLetters(RemoveChar(sInput, '#'));
```

Or with two Boolean functions in a single test:

```pascal
if IsPrime(iValue) AND IsPalindrome(IntToStr(iValue)) then
   …
```

---

# SECTION 8: USEFUL MATH AND ROUNDING FUNCTIONS (RECAP + EXPANSION)

## Recap (Grade 10)

The basic math functions covered in Grade 10 include `Abs`, `Sqr`, `Sqrt`, `Round`, `Trunc`, `Random` and `RandomRange`. The `Math` unit must be added to `uses` for `Power`, `Floor`, `Ceil`, `Pi` and `RandomRange`.

## 8.1 When to use Floor vs Ceil vs Trunc vs Round

| Function | Rounds toward… | Use when… |
|---|---|---|
| `Trunc` | Zero | The decimal part is unimportant and you just want the whole part |
| `Floor` | Negative infinity (down) | You must not exceed a limit — "only whole panels that fit" |
| `Ceil` | Positive infinity (up) | You must reach or exceed a target — "round up to the nearest km" |
| `Round` | Nearest integer | General-purpose rounding |

For **positive** numbers `Trunc` and `Floor` are identical. They differ on negative numbers — `Floor(-2.3) = -3` but `Trunc(-2.3) = -2`.

## 8.2 Round to a number of decimals (for calculation, not display)

`RoundTo(x, -n)` from the `Math` unit rounds a Real to `n` decimal places:

```pascal
rResult := RoundTo(3.14159, -2);        // 3.14
rResult := RoundTo(1234.5, -1);          // 1234.5 (no change — already at 1 dp)
```

For display, prefer `FloatToStrF(value, ffFixed, 10, n)` instead — it keeps the value as a Real and only changes how it looks.

---

# SECTION 9: APPLICATION-WIDE CONCERNS

## 9.1 The OnCreate event

The form's `OnCreate` event runs once when the program starts. It is the right place to:

* Call `Randomize` so random numbers are unpredictable.
* Initialise global variables.
* Disable buttons that should not be active yet.
* Pre-fill controls with default values.

```pascal
procedure TForm1.FormCreate(Sender : TObject);
begin
   Randomize;
   btnNext.Enabled := False;
end;
```

## 9.2 The OnClick event

Most buttons use the `OnClick` event — the code that runs when the user clicks the button. Double-click a button in the form designer to create the empty event handler automatically.

## 9.3 Setting form / window properties

| Property | Effect |
|---|---|
| `Form1.Caption` | The text in the title bar |
| `Form1.Color` | The form's background colour |
| `Form1.Width` / `Form1.Height` | Size in pixels |
| `Form1.Position := poScreenCenter` | Open in the centre of the screen |

---

# CHEAT SHEET APPENDIX

## A. The three loops

```pascal
// Count is known
for i := 1 to N do
   <stmt>;

// Pre-test — may run 0 times
while <condition> do
   begin
      <stmt>;
   end;

// Post-test — runs at least once
repeat
   <stmt>;
until <condition>;
```

## B. Array essentials

```pascal
// Declaration
var
   arr : array [1..100] of Integer;

// Access
arr[i] := <value>;
iValue := arr[i];

// Loop through every element
for i := Low(arr) to High(arr) do
   …

// Swap two elements
iTemp := arr[a];
arr[a] := arr[b];
arr[b] := iTemp;
```

## C. The five-step file pattern

```pascal
var
   tFile : TextFile;
   sLine : String;
begin
   if not FileExists('data.txt') then          // 0. Guard
      begin
         ShowMessage('File not found');
         Exit;
      end;
   AssignFile(tFile, 'data.txt');               // 1+2. Declare + Assign
   Reset(tFile);                                // 3. Open for reading
   while not EOF(tFile) do                      // 4. Read every line
      begin
         ReadLn(tFile, sLine);
         // process sLine
      end;
   CloseFile(tFile);                            // 5. Close
end;
```

## D. File open modes

| Mode | Purpose |
|---|---|
| `Reset(f)` | Open existing for reading |
| `Rewrite(f)` | Create new (wipes existing) for writing |
| `Append(f)` | Add to end of existing for writing |

## E. Delimited-line parsing

```pascal
iPos := Pos(<delim>, sLine);
sField := Copy(sLine, 1, iPos - 1);
Delete(sLine, 1, iPos);
// repeat for each delimiter; what remains is the last field
```

## F. Bubble sort (parallel arrays)

```pascal
for i := 1 to iCount - 1 do
   for j := 1 to iCount - i do
      if arrKey[j] > arrKey[j + 1] then         // > = ascending, < = descending
         begin
            // swap key
            iTemp := arrKey[j];
            arrKey[j] := arrKey[j + 1];
            arrKey[j + 1] := iTemp;
            // swap every parallel array at the same indexes
            sTemp := arrName[j];
            arrName[j] := arrName[j + 1];
            arrName[j + 1] := sTemp;
         end;
```

## G. Procedure and function syntax

```pascal
procedure ProcName(p1 : T1; p2 : T2);
var
   localVars : Type;
begin
   <stmts>;
end;

function FuncName(p1 : T1; p2 : T2) : ReturnType;
var
   localVars : Type;
begin
   <stmts>;
   Result := <value>;
end;
```

## H. String-processing template

```pascal
function Transform(sIn : String) : String;
var
   i    : Integer;
   sNew : String;
begin
   sNew := '';
   for i := 1 to Length(sIn) do
      sNew := sNew + <transform sIn[i]>;        // or skip it, or change it
   Result := sNew;
end;
```

## I. Common quick-reference operations

| Goal | Code |
|---|---|
| Walk backwards through a string | `for i := Length(s) downto 1 do …` |
| Is character a digit? | `if s[i] IN ['0'..'9'] then …` |
| Is character a letter? | `if s[i] IN ['A'..'Z', 'a'..'z'] then …` |
| String reverse | build a new string with `downto` |
| Round up | `Ceil(x)` (requires `Math` unit) |
| Round down | `Floor(x)` (requires `Math` unit) |
| Convert AU to km (or any unit-multiply) | `r := rValueInAU * 150000000;` |

## J. Mark-saving habits (in addition to Grade 10's)

* **Use `iCount`, not the array's maximum size**, in loops where the file did not fill the whole array.
* **Always close text files** with `CloseFile`.
* **Always check `FileExists`** before `Reset`.
* **Always swap every parallel array** when sorting.
* **Initialise `Result`** early in a function if there are multiple paths that might exit before assignment.

---

*End of Grade 11 Practical Programming Reference*
