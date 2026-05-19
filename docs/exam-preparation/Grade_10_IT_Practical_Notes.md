# Grade 10 Information Technology — Practical Programming Reference

*A topic-by-topic reference for Delphi programming concepts and syntax.*

These notes cover the fundamental Delphi concepts and syntax patterns a Grade 10 IT learner needs. They are written as a reference: each section explains a concept and then shows the syntax that goes with it. There are no exam-specific scenarios — only generic patterns that can be applied to any problem.

A **cheat sheet appendix** at the end of the document summarises every syntax pattern on a handful of pages.

---

# SECTION 1: THE DELPHI ENVIRONMENT

## 1.1 What a Delphi project consists of

A Delphi project is a collection of files that work together as one program. The main file types are:

* `.dpr` — the project file, the entry point of the program. You usually do not edit it directly.
* `.pas` — the unit file, which holds the actual code (procedures, functions, event handlers).
* `.dfm` — the form file, which stores the visual layout of a form (the position and properties of each component).
* `.exe` — the compiled program, produced when the project is built.

When opening a project to work on it, double-click the `.dpr` file. To edit code, work on the `.pas` file. To edit the form visually, work in the form designer (the `.dfm` is updated automatically).

## 1.2 The structure of a unit file

Every `.pas` unit file has the same outer skeleton:

```pascal
unit UnitName;

interface
   uses
      Classes, SysUtils, ...;     // libraries the unit needs

   // declarations visible to other units go here

implementation

   // the actual code of procedures and functions goes here

end.
```

When writing programs that use mathematical functions, the `Math` unit must be added to the `uses` clause, e.g. `uses Classes, SysUtils, Math;`.

## 1.3 Adding a comment with your name

Every event handler in an exam should start with a comment. Single-line comments use `//`. Block comments use `{` `}` or `(*` `*)`.

```pascal
// Name: Firstname Surname
// Date:
// Purpose:

{ This is a block comment
  that can span multiple lines }
```

---

# SECTION 2: VARIABLES AND DATA TYPES

## 2.1 What a variable is

A **variable** is a named container in memory that holds a value. Before a variable can be used, it must be **declared** with a name and a data type. The data type determines what kind of value the variable can hold.

## 2.2 The main primitive data types

| Type | Holds | Example value |
|---|---|---|
| `Integer` | Whole number (positive or negative) | `42`, `-17`, `0` |
| `Real` (or `Double`) | Number with a decimal part | `3.14`, `-0.5`, `1000.0` |
| `Boolean` | One of two values | `True` or `False` |
| `Char` | A single character | `'A'`, `'7'`, `'?'` |
| `String` | A sequence of characters (text) | `'Hello'`, `'Pretoria'` |

## 2.3 The Hungarian-notation naming convention

By convention, variable names begin with a one-letter prefix that shows the data type. This makes the code easier to read because the type is visible at every use.

| Prefix | Type | Example name |
|---|---|---|
| `i` | Integer | `iAge`, `iCount`, `iTotal` |
| `r` | Real | `rPrice`, `rAverage` |
| `b` | Boolean | `bFound`, `bValid` |
| `c` | Char | `cInitial`, `cGrade` |
| `s` | String | `sName`, `sAddress` |
| `arr` | Array (Grade 11+) | `arrNames` |

## 2.4 Declaring variables

Variables are declared after the keyword `var`, before the `begin` of the procedure. Several variables of the same type can be declared together using commas:

```pascal
var
   iAge      : Integer;
   rPrice    : Real;
   sName     : String;
   bValid    : Boolean;
   iX, iY, iZ : Integer;        // three integers in one line
```

## 2.5 Assignment — putting a value into a variable

The assignment operator is `:=` (colon-equals), **not** `=`:

```pascal
iAge   := 16;
rPrice := 99.95;
sName  := 'Sipho';
bValid := True;
```

`=` is used for comparison (testing equality), not assignment — getting this wrong is one of the most common errors.

## 2.6 Constants

A **constant** is a named value that cannot change while the program runs. Constants are declared after the keyword `const` before the `var` block, or at the top of the unit.

```pascal
const
   VAT_RATE  = 0.15;
   MAX_AGE   = 120;
   GREETING  = 'Welcome';
```

Constants are useful because:

* The name makes the code self-documenting (`PRICE * VAT_RATE` is clearer than `PRICE * 0.15`).
* If the value ever changes (e.g. VAT goes up to 16%), only one line needs to be updated.
* The compiler will not let you accidentally change the value.

---

# SECTION 3: CONVERTING BETWEEN DATA TYPES

Input from text boxes always arrives as **strings**, and most output back to the screen also needs to be a string. Numerical work happens in between. Conversion is therefore one of the most common operations in any program.

## 3.1 The conversion functions

| From | To | Function | Example |
|---|---|---|---|
| String | Integer | `StrToInt(s)` | `StrToInt('42')` → `42` |
| Integer | String | `IntToStr(i)` | `IntToStr(42)` → `'42'` |
| String | Real | `StrToFloat(s)` | `StrToFloat('3.14')` → `3.14` |
| Real | String (default) | `FloatToStr(r)` | `FloatToStr(3.14)` → `'3.14'` |
| Real | String (formatted) | `FloatToStrF(r, fmt, w, d)` | see below |

## 3.2 `FloatToStrF` — formatting a Real for display

`FloatToStrF(value, format, totalWidth, decimals)` controls how a real number appears on screen.

| Format constant | Effect | Example output for `1234.5` |
|---|---|---|
| `ffCurrency` | Adds R symbol and thousands separator | `R1 234,50` |
| `ffFixed` | Fixed-point, no symbol | `1234,50` |
| `ffGeneral` | Drops trailing zeros | `1234,5` |

A standard money display:

```pascal
sDisplay := FloatToStrF(rAmount, ffCurrency, 10, 2);
```

The `10` is the total width (a safe value to use for almost any number); the `2` is the number of decimal places.

## 3.3 Why conversion matters

Trying to do arithmetic on the raw text from an edit box always fails:

```pascal
// This DOES NOT WORK — sName.Text is a String:
iTotal := edtNumberOne.Text + edtNumberTwo.Text;     // joins as strings: '5' + '3' = '53'!

// This works — convert first:
iTotal := StrToInt(edtNumberOne.Text) + StrToInt(edtNumberTwo.Text);  // 5 + 3 = 8

// And to display back, convert the answer to a string:
lblTotal.Caption := IntToStr(iTotal);
```

---

# SECTION 4: WORKING WITH FORM COMPONENTS

A Delphi form is built up of visual components (controls). Every event handler typically reads input from one or more components, processes the data, and writes the result back to another component.

## 4.1 The common visual components

| Component | Naming prefix | Used for |
|---|---|---|
| Edit | `edt` | Single-line text input |
| Label | `lbl` | Display-only text |
| Panel | `pnl` | A coloured/labelled rectangle, also for display |
| Memo | `mem` | Multi-line text area |
| Rich Edit | `red` | Multi-line text with formatting |
| Button | `btn` | Clickable button |
| SpinEdit | `sed`, `spn` | Number input with up/down arrows |
| ComboBox | `cmb` | Drop-down list |
| ListBox | `lst`, `lsb` | Scrollable list of items |
| RadioGroup | `rgp` | Choose one of several options |
| Image | `img` | Picture display |
| CheckBox | `chk`, `cbx` | True/false tick |

## 4.2 Properties that hold the component's value

Different components store their value in different properties. The pattern is always: read the property to get the value, assign to the property to write a value.

| Component | Property holding its main value | Notes |
|---|---|---|
| Edit | `.Text` | Always a String |
| Label | `.Caption` | Always a String |
| Panel | `.Caption` | Always a String |
| Memo | `.Lines` | A list of strings |
| Rich Edit | `.Lines` | A list of strings |
| SpinEdit | `.Value` | Already an Integer (no conversion needed) |
| ComboBox | `.ItemIndex` (Integer) or `.Text` (String) | `.ItemIndex` is `–1` if nothing is selected |
| ListBox | `.ItemIndex` (Integer) or `.Items[i]` (String) | Indexes start at `0` |
| RadioGroup | `.ItemIndex` (Integer) | `–1` if no option is selected |
| Image | `.Picture` | Loaded via `.LoadFromFile(filename)` |
| CheckBox | `.Checked` | Already a Boolean (True/False) |

## 4.3 Reading from a component

```pascal
sName  := edtName.Text;             // Edit → String
iAge   := sedAge.Value;             // SpinEdit → Integer (no conversion)
iAge   := StrToInt(edtAge.Text);    // Edit → Integer (convert)
rPrice := StrToFloat(edtPrice.Text);// Edit → Real (convert)
iIndex := rgpChoice.ItemIndex;      // RadioGroup → Integer
bAgree := chkAgree.Checked;         // CheckBox → Boolean
```

## 4.4 Writing to a component

```pascal
lblResult.Caption := 'Total: ' + IntToStr(iTotal);
pnlDisplay.Caption := FloatToStrF(rAmount, ffCurrency, 10, 2);
memOutput.Lines.Add('Line of text');
memOutput.Lines.Clear;                   // wipe the memo
imgPicture.Picture.LoadFromFile('photo.jpg');
```

## 4.5 Common cosmetic properties

These work the same way on most visual components:

| Property | What it controls | Example |
|---|---|---|
| `.Color` | Background colour | `pnl.Color := clYellow;` |
| `.Font.Color` | Text colour | `lbl.Font.Color := clRed;` |
| `.Font.Size` | Text size | `lbl.Font.Size := 18;` |
| `.Font.Name` | Font family | `lbl.Font.Name := 'Arial';` |
| `.Font.Style` | Bold/italic/underline (a *set*) | `lbl.Font.Style := [fsBold];` |
| `.Enabled` | Whether the user can interact | `btn.Enabled := False;` |
| `.Visible` | Whether the control is shown | `pnl.Visible := True;` |

`.Color` is the **background**; `.Font.Color` is the **text** colour — these are commonly confused.

`.Font.Style` is a *set* of style values. Assigning is done with square brackets:

```pascal
lbl.Font.Style := [fsBold];                 // bold only
lbl.Font.Style := [fsItalic];               // italic only
lbl.Font.Style := [fsBold, fsItalic];       // both
lbl.Font.Style := [];                       // plain — clear all styles
```

## 4.6 Useful built-in colour constants

`clRed`, `clBlue`, `clGreen`, `clYellow`, `clBlack`, `clWhite`, `clGray`, `clAqua`, `clMaroon`, `clNavy`, `clOlive`, `clTeal`, `clPurple`, `clMoneyGreen`, `clSkyBlue`, `clWebLightSalmon`. Any of these can be assigned to `.Color` or `.Font.Color`.

## 4.7 Building multi-line output

Two special characters are useful for output:

* `#13` — start a new line (carriage return).
* `#9` — tab character (used to align columns).

In a Memo or Rich Edit, each `Lines.Add` call produces a new line, so `#13` is not always needed there — but inside a single Caption or one combined string it forces a line break.

```pascal
lblMessage.Caption := 'Error in input.' + #13 + 'Please try again.';

memReport.Lines.Add('Name' + #9 + #9 + 'Age');
memReport.Lines.Add('----' + #9 + #9 + '---');
memReport.Lines.Add(sName + #9 + #9 + IntToStr(iAge));
```

Always clear an output area before writing fresh content:

```pascal
memReport.Lines.Clear;
redOutput.Clear;
```

---

# SECTION 5: GETTING INPUT WITH AN INPUTBOX

When a value is needed that does not have its own edit box on the form, an `InputBox` dialog can be used. It pops up, prompts for one value, and returns whatever the user typed as a **String**.

```pascal
sResult := InputBox('Window title', 'Prompt to the user', 'default text');
```

For numerical input the result must be converted:

```pascal
sAnswer := InputBox('Age', 'Enter your age', '0');
iAge    := StrToInt(sAnswer);
```

To put an apostrophe inside a string, write it twice — `'Visitor''s name'` displays as `Visitor's name`.

---

# SECTION 6: ARITHMETIC AND OPERATORS

## 6.1 Arithmetic operators

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Real division | `5 / 2` | `2.5` |
| `div` | Integer division | `5 div 2` | `2` (the whole part) |
| `mod` | Remainder after integer division | `5 mod 2` | `1` |

`/` always returns a real number, even when both inputs are whole numbers. `div` and `mod` only work on integers.

## 6.2 Comparison operators (return a Boolean)

| Operator | Meaning |
|---|---|
| `=` | Equal to |
| `<>` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

Note: equality is `=` (single equals) in Pascal, not `==` as in some other languages.

## 6.3 Logical operators (combine Booleans)

| Operator | Effect |
|---|---|
| `AND` | True only when **both** sides are true |
| `OR` | True when **at least one** side is true |
| `NOT` | Inverts a Boolean (True becomes False, and vice versa) |

When combining comparisons with AND/OR, **wrap each comparison in parentheses** — without them, Pascal's operator precedence will misread the expression:

```pascal
// CORRECT:
if (iMark >= 0) AND (iMark <= 100) then ...

// WRONG (does not compile):
if iMark >= 0 AND iMark <= 100 then ...
```

## 6.4 Order of operations

The standard order is the same as in mathematics:

1. Parentheses `( )`
2. Unary operators (`NOT`, unary minus)
3. `*`, `/`, `div`, `mod`, `AND`
4. `+`, `-`, `OR`
5. Comparison operators

When in doubt, use parentheses — they make the intention clear and override default precedence.

---

# SECTION 7: BUILT-IN MATH FUNCTIONS

These functions are essential for most calculation tasks. Functions marked **(Math)** require the `Math` unit to be added to the `uses` clause.

| Function | Purpose | Example |
|---|---|---|
| `Abs(x)` | Absolute (positive) value | `Abs(-5)` → `5` |
| `Sqr(x)` | x squared (x²) | `Sqr(5)` → `25` |
| `Sqrt(x)` | square root of x | `Sqrt(25)` → `5` |
| `Round(x)` | round to nearest integer | `Round(13.5)` → `14` |
| `Trunc(x)` | chop off the decimal part | `Trunc(13.88)` → `13` |
| `Frac(x)` | the decimal part only | `Frac(13.88)` → `0.88` |
| `Int(x)` | the integer part as a Real | `Int(13.88)` → `13.0` |
| `Random(n)` | random Integer 0 up to but not including n | `Random(10)` → 0..9 |
| `RandomRange(a, b)` **(Math)** | random Integer from a up to but not including b | `RandomRange(1, 11)` → 1..10 |
| `Power(x, y)` **(Math)** | x to the power y | `Power(2, 3)` → `8` |
| `Floor(x)` **(Math)** | round down to nearest integer | `Floor(13.88)` → `13` |
| `Ceil(x)` **(Math)** | round up to nearest integer | `Ceil(13.05)` → `14` |
| `Pi` **(Math)** | the constant π ≈ 3.14159 | — |

## 7.1 Difference between Trunc, Floor, Round and Ceil

For positive numbers, `Trunc` and `Floor` give the same answer. They differ for negative numbers:

| Value | Trunc | Floor | Round | Ceil |
|---|---|---|---|---|
| 3.2 | 3 | 3 | 3 | 4 |
| 3.7 | 3 | 3 | 4 | 4 |
| –3.2 | –3 | –4 | –3 | –3 |
| –3.7 | –3 | –4 | –4 | –3 |

* `Trunc` always moves towards zero.
* `Floor` always moves towards negative infinity (down).
* `Round` goes to the nearest integer.
* `Ceil` always moves towards positive infinity (up).

## 7.2 Random numbers

`Random(n)` returns a random Integer between 0 and n–1. So `Random(12)` returns a value in the range `0..11`.

For a number in an arbitrary range, the formulas are:

* `Random(N) + StartValue` — produces values from `StartValue` to `StartValue + N - 1`.
* `RandomRange(low, high)` — produces values from `low` up to but **not including** `high`.

For 1 to 6 (a dice): `Random(6) + 1` or `RandomRange(1, 7)`.
For 100 to 999: `Random(900) + 100` or `RandomRange(100, 1000)`.

**`Randomize`** must be called once when the program starts (usually in the form's `OnCreate` event). Without it, the program produces the same "random" sequence every time it is run.

---

# SECTION 8: STRING OPERATIONS

Strings are sequences of characters. Several common operations come up in every program.

## 8.1 Common string functions

| Function | Purpose | Example |
|---|---|---|
| `Length(s)` | Number of characters in `s` | `Length('Hello')` → `5` |
| `UpperCase(s)` | Converts whole string to upper case | `UpperCase('abc')` → `'ABC'` |
| `LowerCase(s)` | Converts whole string to lower case | `LowerCase('ABC')` → `'abc'` |
| `UpCase(c)` | Converts **one character** to upper case | `UpCase('a')` → `'A'` |
| `Copy(s, start, count)` | Extracts a piece of `s` | `Copy('Hello', 2, 3)` → `'ell'` |
| `Pos(sub, s)` | Returns position (1-based) of `sub` in `s`, or 0 if not found | `Pos('lo', 'Hello')` → `4` |
| `Delete(s, start, count)` | Removes `count` characters from `s` starting at `start` | modifies `s` in place |
| `Insert(sub, s, pos)` | Inserts `sub` into `s` at position `pos` | modifies `s` in place |

## 8.2 Accessing individual characters

A string is indexed from `1`. `s[1]` is the first character, `s[2]` the second, and so on. The data type of `s[i]` is `Char`.

```pascal
sName := 'Pretoria';
cFirst := sName[1];           // 'P'
cLast  := sName[Length(sName)];   // 'a'
```

## 8.3 Concatenation — joining strings

The `+` operator joins strings end to end. Numbers must be converted first using `IntToStr` or `FloatToStr`:

```pascal
sFullName := sFirstName + ' ' + sSurname;
sMessage  := 'You are ' + IntToStr(iAge) + ' years old.';
sPrice    := 'Total: ' + FloatToStrF(rAmount, ffCurrency, 10, 2);
```

## 8.4 Capitalising only the first letter

A common pattern — the first letter capital, the rest unchanged:

```pascal
sResult := UpCase(sName[1]) + Copy(sName, 2, Length(sName) - 1);
```

---

# SECTION 9: SELECTION — MAKING DECISIONS

## 9.1 IF…THEN

The simplest decision:

```pascal
if <condition> then
   <statement>;
```

If the body has more than one statement, wrap them in `begin…end`:

```pascal
if iMark >= 50 then
   begin
      lblResult.Caption := 'Pass';
      lblResult.Font.Color := clGreen;
   end;
```

## 9.2 IF…THEN…ELSE

Two-way decision:

```pascal
if <condition> then
   <statement when true>
else
   <statement when false>;
```

**Critical rule: there is no semicolon before `else`**. The statement before `else` ends without a semicolon — Pascal treats `if…else` as one combined statement.

```pascal
if iMark >= 50 then
   lblResult.Caption := 'Pass'         // no semicolon here
else
   lblResult.Caption := 'Fail';        // semicolon at the end
```

When the branches contain `begin…end`, the `end` before `else` likewise has **no semicolon**:

```pascal
if iMark >= 50 then
   begin
      lblResult.Caption := 'Pass';
      lblResult.Font.Color := clGreen;
   end                                  // no semicolon here
else
   begin
      lblResult.Caption := 'Fail';
      lblResult.Font.Color := clRed;
   end;
```

## 9.3 Chained IF…ELSE IF…ELSE

For three or more bands:

```pascal
if iMark >= 80 then
   sGrade := 'A'
else if iMark >= 70 then
   sGrade := 'B'
else if iMark >= 60 then
   sGrade := 'C'
else if iMark >= 50 then
   sGrade := 'D'
else
   sGrade := 'Fail';
```

Once a condition matches, the rest are skipped. So `iMark >= 70` in the second branch already implies `iMark < 80` — you don't need to write `if (iMark >= 70) AND (iMark < 80)`.

## 9.4 CASE — multi-way selection on one value

When checking many possible values of the same variable, `CASE` is cleaner than chained IFs:

```pascal
case <integer or char variable> of
   <value1> : <statement>;
   <value2> : <statement>;
   <value3> : begin
                <statement>;
                <statement>;
              end;
else
   <fallback statement>;
end;
```

A worked example:

```pascal
case iDayNumber of
   1 : sDay := 'Monday';
   2 : sDay := 'Tuesday';
   3 : sDay := 'Wednesday';
   4 : sDay := 'Thursday';
   5 : sDay := 'Friday';
   6, 7 : sDay := 'Weekend';        // multiple values per branch
else
   sDay := 'Invalid day';
end;
```

`CASE` only works on **whole-number-like** types: Integer, Char, Boolean, enumerated. It does **not** work with Strings or Reals.

## 9.5 The IN operator with a set

Pascal has a built-in `IN` operator that tests whether a value belongs to a set:

```pascal
if cLetter IN ['A', 'E', 'I', 'O', 'U'] then ...    // is it a vowel?

if cChar IN ['0'..'9'] then ...                      // is it a digit?

if iMark IN [50..100] then ...                       // is it a pass?
```

This is often the shortest way to test "is this one of several values".

---

# SECTION 10: VALIDATION

Validation is checking that the user's input is acceptable before the program tries to use it. The standard pattern: test → if bad, show a message and stop; if good, continue.

## 10.1 Common validation types

| Type | What it checks | Example |
|---|---|---|
| **Presence** | Field is not empty | `if edtName.Text = '' then ...` |
| **Length** | Correct number of characters | `if Length(sID) <> 13 then ...` |
| **Range** | Number falls within limits | `if (iMark < 0) OR (iMark > 100) then ...` |
| **Type** | Value can be converted to the expected type | use `TryStrToInt` |
| **Format** | Value follows a required pattern | check positions of characters |

## 10.2 Stopping further processing — Exit

The standard pattern is to display an error and then `Exit`, which immediately leaves the current procedure:

```pascal
if edtAge.Text = '' then
   begin
      ShowMessage('Please enter your age.');
      Exit;                            // stops this event handler immediately
   end;

iAge := StrToInt(edtAge.Text);          // only runs if input is valid
```

## 10.3 Range checks — three equivalent forms

```pascal
// Form 1: explicit AND
if (iMark >= 0) AND (iMark <= 100) then ...

// Form 2: inverted with NOT (useful when the question is phrased as 'out of range')
if NOT ((iMark >= 0) AND (iMark <= 100)) then ...

// Form 3: the IN-operator with a set
if iMark IN [0..100] then ...
```

All three give the same result. Choose whichever reads most clearly for the situation.

## 10.4 Pop-up dialogs

`ShowMessage(text)` displays a simple pop-up with an OK button.

`MessageDlg(text, mtType, [buttons], 0)` displays a more elaborate pop-up.

`Application.Terminate` shuts the program down entirely (more drastic than `Exit`, which only leaves one procedure).

---

# SECTION 11: REPETITION — LOOPS

Loops repeat a block of code multiple times. Grade 10 mostly uses the `for` loop; the other two kinds are covered in Grade 11.

## 11.1 The for loop — when the count is known

```pascal
for <counter> := <start> to <end> do
   <statement>;

for <counter> := <start> to <end> do
   begin
      <statement>;
      <statement>;
   end;
```

A simple example — display the numbers 1 to 10:

```pascal
for iCount := 1 to 10 do
   memOutput.Lines.Add(IntToStr(iCount));
```

To count backwards, replace `to` with `downto`:

```pascal
for iCount := 10 downto 1 do
   memOutput.Lines.Add(IntToStr(iCount));
```

## 11.2 Common loop patterns

**Accumulator** — keep a running total:

```pascal
rTotal := 0;
for i := 1 to 5 do
   rTotal := rTotal + StrToFloat(InputBox('Price', 'Enter price:', '0'));
lblTotal.Caption := FloatToStrF(rTotal, ffCurrency, 10, 2);
```

**Counter** — count items that meet a condition:

```pascal
iEvenCount := 0;
for i := 1 to 20 do
   if i MOD 2 = 0 then
      Inc(iEvenCount);                    // Inc(x) is shorthand for x := x + 1
```

---

# SECTION 12: TRANSLATING A FLOW DIAGRAM INTO CODE

A flow diagram is a visual way of describing an algorithm. Each shape becomes a different kind of Delphi statement:

| Flow diagram shape | What it represents | Delphi equivalent |
|---|---|---|
| Oval (rounded ends) | Start / End | `begin` / `end;` of the procedure |
| Parallelogram | Input or Output | reading from a component, or `Lines.Add` / `Caption :=` |
| Rectangle | A processing step (calculation, assignment) | `:=` assignment statement |
| Diamond | A decision | `if…then…else` |
| Arrow | Order of execution | Order of statements in code |

Reading order: follow the arrows from START down to END. Every shape becomes a statement; the order of the shapes becomes the order of the code.

**Decisions** become `if…then…else`. The "Yes" arrow goes into the THEN branch; the "No" arrow goes into the ELSE branch.

**Loops** appear as a diamond with one arrow that goes back up to an earlier point — these become `for`, `while` or `repeat` loops depending on the situation.

---

# SECTION 13: IMAGES AND OTHER COMMON COMPONENT TASKS

## 13.1 Loading a picture from a file

```pascal
imgPhoto.Picture.LoadFromFile('filename.jpg');
```

If only a filename is given (no path), Delphi looks for the file in the **same folder as the running program** (`.exe`). For files in another folder, give the full path.

## 13.2 Building a filename from variables

A common pattern: pick a number, build a matching filename, then load it.

```pascal
iIndex := Random(10);                                     // 0..9
sFile  := 'picture' + IntToStr(iIndex) + '.jpg';          // 'picture3.jpg'
imgPhoto.Picture.LoadFromFile(sFile);
```

## 13.3 Synchronising components

Setting one component's value to match another:

```pascal
cmbChoice.ItemIndex := iSelected;             // highlight the matching combobox item
lblChosen.Caption := cmbChoice.Items[iSelected];   // show the chosen text
```

## 13.4 Enabling and disabling buttons

Useful when a button should only become active after another step has run:

```pascal
btnNext.Enabled := False;       // disabled (greyed out) — clicks do nothing

// later, after the user has done what is required:
btnNext.Enabled := True;
```

---

# CHEAT SHEET APPENDIX

## A. Skeleton of an event handler

```pascal
procedure TForm1.btnExampleClick(Sender : TObject);
var
   iVar : Integer;
   sVar : String;
begin
   // 1. Read input from components
   sVar := edtInput.Text;
   iVar := StrToInt(sVar);

   // 2. Process (calculations, decisions, loops)

   // 3. Write output back to components
   lblOutput.Caption := IntToStr(iVar);
end;
```

## B. Conversion functions

| Direction | Function |
|---|---|
| String → Integer | `StrToInt(s)` |
| Integer → String | `IntToStr(i)` |
| String → Real | `StrToFloat(s)` |
| Real → String | `FloatToStr(r)` |
| Real → formatted String | `FloatToStrF(r, ffCurrency, 10, 2)` |

## C. Reading from components

| Component | Code |
|---|---|
| Edit (String) | `s := edtName.Text;` |
| Edit (Integer) | `i := StrToInt(edtAge.Text);` |
| Edit (Real) | `r := StrToFloat(edtPrice.Text);` |
| SpinEdit | `i := sedQty.Value;` |
| ComboBox index | `i := cmbChoice.ItemIndex;` |
| ComboBox text | `s := cmbChoice.Text;` |
| RadioGroup index | `i := rgpChoice.ItemIndex;` |
| CheckBox | `b := chkAgree.Checked;` |

## D. Writing to components

| Target | Code |
|---|---|
| Label / Panel | `lblOut.Caption := s;` |
| Edit | `edtOut.Text := s;` |
| Memo (add line) | `memOut.Lines.Add(s);` |
| Memo (clear) | `memOut.Lines.Clear;` |
| Background colour | `pnl.Color := clYellow;` |
| Text colour | `lbl.Font.Color := clRed;` |
| Bold | `lbl.Font.Style := [fsBold];` |
| Show image | `img.Picture.LoadFromFile('a.jpg');` |

## E. Pop-ups

| Code | Result |
|---|---|
| `ShowMessage('text');` | Simple OK pop-up |
| `s := InputBox('Title', 'Prompt', 'default');` | Ask user for input |
| `Application.Terminate;` | Close the program |
| `Exit;` | Leave this procedure only |

## F. Math functions (uses Math)

| Function | Result for example |
|---|---|
| `Sqr(5)` | `25` |
| `Sqrt(25)` | `5` |
| `Power(2, 3)` | `8` |
| `Abs(-5)` | `5` |
| `Round(3.6)` | `4` |
| `Trunc(3.9)` | `3` |
| `Floor(3.9)` | `3` |
| `Ceil(3.1)` | `4` |
| `Random(10)` | 0..9 |
| `RandomRange(1, 11)` | 1..10 |
| `Pi` | 3.14159… |

## G. String functions

| Function | Example | Result |
|---|---|---|
| `Length(s)` | `Length('Hello')` | `5` |
| `UpperCase(s)` | `UpperCase('abc')` | `'ABC'` |
| `LowerCase(s)` | `LowerCase('ABC')` | `'abc'` |
| `UpCase(c)` | `UpCase('a')` | `'A'` |
| `Copy(s, start, count)` | `Copy('Hello', 2, 3)` | `'ell'` |
| `Pos(sub, s)` | `Pos('lo', 'Hello')` | `4` |
| `s[i]` (one char) | `'Hello'[1]` | `'H'` |

## H. Decision structures

```pascal
// Simple IF
if <cond> then <stmt>;

// IF / ELSE (no semicolon before else)
if <cond> then <stmt1> else <stmt2>;

// Multi-statement branches
if <cond> then
   begin
      <stmt>;
   end
else
   begin
      <stmt>;
   end;

// CASE
case <integer or char> of
   1 : <stmt>;
   2 : <stmt>;
   3, 4 : <stmt>;
else
   <stmt>;
end;

// IN-operator
if cCh IN ['0'..'9'] then ...
```

## I. The for loop

```pascal
for iCount := 1 to 10 do
   <stmt>;

for iCount := 10 downto 1 do
   <stmt>;

for iCount := 1 to 10 do
   begin
      <stmt>;
      <stmt>;
   end;
```

## J. Common formatting characters

| Code | Meaning |
|---|---|
| `#13` | New line (carriage return) |
| `#9` | Tab |
| `''` (two apostrophes) | One apostrophe inside a string |

## K. Quick mark-saving habits

* Add your name and surname as a comment in every `.pas` file.
* Use the variable and component names exactly as given.
* Add `Math` to the `uses` clause when using `Power`, `Floor`, `Ceil`, `Pi`, `RandomRange`.
* Clear an output area before adding new content (`memo.Lines.Clear`).
* Format real numbers with `FloatToStrF` — never let raw scientific notation reach the screen.
* Use the constants given by the question, never hard-code their values.
* Match output formats (colons, spaces, brackets) exactly.

---

*End of Grade 10 Practical Programming Reference*
