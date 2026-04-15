# String Handling

Strings are sequences of characters. Almost every Paper 1 question involves string manipulation in some form — reading a name, checking a code, extracting part of a word, or converting between types. Knowing the string functions cold is non-negotiable.

> [!NOTE] Grade 10+
> String manipulation is introduced in Grade 10 and appears in every Paper 1 paper. Memorise the function names, their parameters, and what they return.

---

## What is a String?

A `String` in Delphi is a sequence of characters. Strings are **1-indexed** — the first character is at position `1`, not `0`.

```pascal
var
  sName : String;
begin
  sName := 'Ayden';
  // sName[1] = 'A'
  // sName[2] = 'y'
  // sName[5] = 'n'
end;
```

---

## Type Conversions — Most Used in Exams

These appear in nearly every question because user input arrives as text and must be converted.

| Function | Converts | Example | Result |
|---|---|---|---|
| `IntToStr(i)` | Integer → String | `IntToStr(42)` | `'42'` |
| `StrToInt(s)` | String → Integer | `StrToInt('42')` | `42` |
| `FloatToStr(r)` | Real → String | `FloatToStr(3.14)` | `'3.14'` |
| `StrToFloat(s)` | String → Real | `StrToFloat('3.14')` | `3.14` |
| `FloatToStrF(r, ffFixed, 8, 2)` | Real → String (formatted) | `FloatToStrF(3.14159, ffFixed, 8, 2)` | `'3.14'` |
| `IntToHex(i, digits)` | Integer → Hex String | `IntToHex(255, 2)` | `'FF'` |
| `Chr(i)` | Integer → Char | `Chr(65)` | `'A'` |
| `Ord(c)` | Char → Integer | `Ord('A')` | `65` |

> [!WARNING] StrToInt Crashes on Non-Numbers
> `StrToInt('hello')` throws a runtime exception. In exams the input is usually assumed valid, but in a real application you'd wrap it in `try...except`. See the Validation page.

---

## FloatToStrF — Formatting Decimal Places

This is the standard way to display a Real with a fixed number of decimal places:

```pascal
// Syntax: FloatToStrF(value, format, precision, digits)
// ffFixed = fixed decimal point format
// precision = total significant digits (use 8 as safe default)
// digits = decimal places to show

lblResult.Caption := FloatToStrF(rAverage, ffFixed, 8, 2);
// Shows average to 2 decimal places, e.g. "87.43"
```

---

## Length — How Many Characters?

```pascal
iLen := Length(sText);
```

| Example | Result |
|---|---|
| `Length('Hello')` | `5` |
| `Length('IT Gateway')` | `10` |
| `Length('')` | `0` |

**Use case — check minimum length:**
```pascal
IF Length(edtPassword.Text) < 8 THEN
  ShowMessage('Password must be at least 8 characters.');
```

---

## UpperCase and LowerCase — Change Case

```pascal
sResult := UpperCase(sText);    // all CAPS
sResult := LowerCase(sText);    // all lowercase
```

| Example | Result |
|---|---|
| `UpperCase('Hello World')` | `'HELLO WORLD'` |
| `LowerCase('IT GATEWAY')` | `'it gateway'` |

**Use case — case-insensitive comparison:**
```pascal
IF UpperCase(edtAnswer.Text) = 'YES' THEN
  // matches 'yes', 'Yes', 'YES', 'yEs' etc.
```

---

## Trim — Remove Leading/Trailing Spaces

```pascal
sResult := Trim(sText);
```

| Example | Result |
|---|---|
| `Trim('  Hello  ')` | `'Hello'` |
| `Trim('No spaces')` | `'No spaces'` |

Always trim before comparing user input — users often accidentally add spaces.

---

## Copy — Extract Part of a String (Substring)

```pascal
sResult := Copy(sSource, iStart, iCount);
```

- `iStart` — position to start copying (1-based)
- `iCount` — number of characters to copy

| Example | Result | Reason |
|---|---|---|
| `Copy('Gateway', 1, 4)` | `'Gate'` | 4 chars from position 1 |
| `Copy('Gateway', 5, 3)` | `'way'` | 3 chars from position 5 |
| `Copy('Hello', 2, 3)` | `'ell'` | 3 chars from position 2 |

**Use case — extract first 3 characters:**
```pascal
sCode := Copy(sInput, 1, 3);
```

---

## Pos — Find Position of Substring

```pascal
iResult := Pos(sNeedle, sHaystack);
```

Returns the **starting position** of `sNeedle` inside `sHaystack`. Returns **0** if not found.

| Example | Result |
|---|---|
| `Pos('lo', 'Hello World')` | `4` |
| `Pos('World', 'Hello World')` | `7` |
| `Pos('xyz', 'Hello World')` | `0` |

**Use case — check if @ is in an email:**
```pascal
IF Pos('@', sEmail) = 0 THEN
  ShowMessage('Invalid email — missing @');
```

---

## Delete — Remove Characters from a String

`Delete` modifies the string in place (it's a procedure, not a function):

```pascal
Delete(sText, iStart, iCount);
```

| Example | Result |
|---|---|
| `Delete(s, 1, 3)` when s = `'Hello'` | s becomes `'lo'` |
| `Delete(s, 4, 2)` when s = `'Gateway'` | s becomes `'Gatay'` |

> [!NOTE] Delete Modifies In Place
> Unlike Copy, Delete changes the original variable. You don't assign the result — it modifies `sText` directly.

---

## Insert — Insert a String Into Another

```pascal
Insert(sInsert, sTarget, iPosition);
```

Inserts `sInsert` into `sTarget` at position `iPosition`. Modifies `sTarget` in place.

| Example | Before | After |
|---|---|---|
| `Insert('World', s, 7)` | `s = 'Hello '` | `s = 'Hello World'` |

---

## StringOfChar — Repeat a Character

```pascal
sResult := StringOfChar(cChar, iCount);
```

| Example | Result |
|---|---|
| `StringOfChar('*', 5)` | `'*****'` |
| `StringOfChar('-', 20)` | `'--------------------'` |

---

## UpCase — Single Character to Uppercase

```pascal
cResult := UpCase(cChar);
```

Works on a single `Char`, not a full string (use `UpperCase` for full strings).

```pascal
cFirst := UpCase(edtName.Text[1]);  // capitalise first letter typed
```

---

## Accessing Individual Characters

```pascal
sWord := 'Delphi';
cFirst := sWord[1];   // 'D'
cLast  := sWord[Length(sWord)];  // 'i'
```

**Use case — count vowels in a word:**
```pascal
procedure TForm1.btnVowelsClick(Sender: TObject);
var
  sWord  : String;
  i, iCount : Integer;
  cLetter   : Char;
begin
  sWord  := LowerCase(edtWord.Text);
  iCount := 0;

  FOR i := 1 TO Length(sWord) DO
  BEGIN
    cLetter := sWord[i];
    IF (cLetter = 'a') OR (cLetter = 'e') OR (cLetter = 'i') OR
       (cLetter = 'o') OR (cLetter = 'u') THEN
      Inc(iCount);
  END;

  lblResult.Caption := 'Vowels: ' + IntToStr(iCount);
end;
```

---

## Combining String Functions

Exam questions often combine several functions in one problem.

**Example — reverse a string:**
```pascal
procedure TForm1.btnReverseClick(Sender: TObject);
var
  sInput, sReversed : String;
  i                 : Integer;
begin
  sInput    := edtInput.Text;
  sReversed := '';

  FOR i := Length(sInput) DOWNTO 1 DO
    sReversed := sReversed + sInput[i];

  lblResult.Caption := sReversed;
end;
```

**Example — count how many times a character appears:**
```pascal
procedure TForm1.btnCountCharClick(Sender: TObject);
var
  sText  : String;
  cFind  : Char;
  i, n   : Integer;
begin
  sText := LowerCase(edtText.Text);
  cFind := LowerCase(edtChar.Text)[1];
  n     := 0;

  FOR i := 1 TO Length(sText) DO
    IF sText[i] = cFind THEN
      Inc(n);

  lblResult.Caption := 'Found ' + IntToStr(n) + ' times';
end;
```

**Example — check if a string is a palindrome:**
```pascal
procedure TForm1.btnPalindromeClick(Sender: TObject);
var
  s          : String;
  i          : Integer;
  bPalindrome : Boolean;
begin
  s           := LowerCase(Trim(edtWord.Text));
  bPalindrome := True;

  FOR i := 1 TO Length(s) DIV 2 DO
  BEGIN
    IF s[i] <> s[Length(s) - i + 1] THEN
    BEGIN
      bPalindrome := False;
    END;
  END;

  IF bPalindrome THEN
    lblResult.Caption := '"' + s + '" IS a palindrome'
  ELSE
    lblResult.Caption := '"' + s + '" is NOT a palindrome';
end;
```

---

## String Comparison

Strings are compared character by character using standard relational operators:

```pascal
IF sName = 'Ayden' THEN   // exact match
IF sName < 'M'    THEN   // alphabetically before M
IF sName > 'M'    THEN   // alphabetically from M onward
```

> [!WARNING] String Comparison is Case-Sensitive
> `'hello' = 'Hello'` is **FALSE**. Always convert both sides to the same case before comparing:
> ```pascal
> IF UpperCase(sInput) = UpperCase(sCorrect) THEN
> ```

---

## Quick Reference Table

| Function | Syntax | Returns | Example |
|---|---|---|---|
| `Length` | `Length(s)` | Integer | `Length('Hi') = 2` |
| `UpperCase` | `UpperCase(s)` | String | `UpperCase('hi') = 'HI'` |
| `LowerCase` | `LowerCase(s)` | String | `LowerCase('HI') = 'hi'` |
| `Trim` | `Trim(s)` | String | `Trim('  hi  ') = 'hi'` |
| `Copy` | `Copy(s, start, count)` | String | `Copy('Hello', 2, 3) = 'ell'` |
| `Pos` | `Pos(find, source)` | Integer | `Pos('lo', 'Hello') = 4` |
| `Delete` | `Delete(s, start, count)` | — (modifies s) | Removes chars in place |
| `Insert` | `Insert(ins, s, pos)` | — (modifies s) | Inserts in place |
| `IntToStr` | `IntToStr(i)` | String | `IntToStr(10) = '10'` |
| `StrToInt` | `StrToInt(s)` | Integer | `StrToInt('10') = 10` |
| `FloatToStr` | `FloatToStr(r)` | String | `FloatToStr(3.14) = '3.14'` |
| `StrToFloat` | `StrToFloat(s)` | Real | `StrToFloat('3.14') = 3.14` |
| `FloatToStrF` | `FloatToStrF(r, ffFixed, 8, n)` | String | Fixed n decimal places |
| `Chr` | `Chr(i)` | Char | `Chr(65) = 'A'` |
| `Ord` | `Ord(c)` | Integer | `Ord('A') = 65` |
| `UpCase` | `UpCase(c)` | Char | `UpCase('a') = 'A'` |
| `StringOfChar` | `StringOfChar(c, n)` | String | `StringOfChar('*', 3) = '***'` |

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Using 0-based index** — Delphi strings are 1-indexed; `sText[0]` is out of bounds
> 2. **Case-sensitive comparison** — always `UpperCase()` both sides before comparing
> 3. **Pos returns 0 if not found** — check `Pos(...) > 0` before using the result
> 4. **Copy past end of string** — `Copy('Hi', 1, 100)` is safe (returns all chars), but be careful with `Delete`
> 5. **StrToInt with spaces** — use `Trim(edtInput.Text)` before `StrToInt` if user might type spaces

---

## Practice Exercises

**Exercise 1 — Username formatter**

Read a first name and surname from two edit boxes. Display a username in the format: first letter of first name + full surname, all lowercase. (e.g. "Ayden" + "Coetzee" → "acoetzee")

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnUsernameClick(Sender: TObject);
var
  sFirst, sSurname, sUsername : String;
begin
  sFirst   := Trim(edtFirst.Text);
  sSurname := Trim(edtSurname.Text);

  sUsername := LowerCase(Copy(sFirst, 1, 1) + sSurname);

  lblUsername.Caption := 'Username: ' + sUsername;
end;
```
</details>

---

**Exercise 2 — Count digits in a string**

Read a string from `edtInput`. Count how many characters are digits (0–9) and display the count.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnCountDigitsClick(Sender: TObject);
var
  sText  : String;
  i, n   : Integer;
  c      : Char;
begin
  sText := edtInput.Text;
  n     := 0;

  FOR i := 1 TO Length(sText) DO
  BEGIN
    c := sText[i];
    IF (c >= '0') AND (c <= '9') THEN
      Inc(n);
  END;

  lblResult.Caption := 'Digits found: ' + IntToStr(n);
end;
```
</details>

---

**Exercise 3 — Extract domain from email**

Given an email address in `edtEmail`, extract and display the domain (everything after the @).
e.g. `"learner@school.co.za"` → `"school.co.za"`

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnDomainClick(Sender: TObject);
var
  sEmail  : String;
  iAt     : Integer;
  sDomain : String;
begin
  sEmail := Trim(edtEmail.Text);
  iAt    := Pos('@', sEmail);

  IF iAt = 0 THEN
    lblResult.Caption := 'Invalid email — no @ found'
  ELSE
  BEGIN
    sDomain := Copy(sEmail, iAt + 1, Length(sEmail) - iAt);
    lblResult.Caption := 'Domain: ' + sDomain;
  END;
end;
```
</details>

---

> [!TIP] Exam Tip
> The two most-tested string operations are `Copy` (extract substring) and `Pos` (find character position). A common combined question: "Find the position of the space in a full name, then use Copy to extract the first name and surname separately." Practice this pattern — it appears in some form almost every year.
