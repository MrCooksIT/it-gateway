# String Functions — Quick Reference

Complete reference for all Delphi string and conversion functions. No prose — scan and use.

---

## Core String Functions

| Function | Syntax | Returns | What it does |
|---|---|---|---|
| `Length` | `Length(s)` | Integer | Number of characters in s |
| `UpperCase` | `UpperCase(s)` | String | All characters uppercase |
| `LowerCase` | `LowerCase(s)` | String | All characters lowercase |
| `Trim` | `Trim(s)` | String | Remove leading and trailing spaces |
| `TrimLeft` | `TrimLeft(s)` | String | Remove leading spaces only |
| `TrimRight` | `TrimRight(s)` | String | Remove trailing spaces only |
| `Copy` | `Copy(s, start, count)` | String | Extract substring |
| `Pos` | `Pos(find, source)` | Integer | Position of substring (0 = not found) |
| `Delete` | `Delete(s, start, count)` | — modifies s | Remove characters from string |
| `Insert` | `Insert(ins, s, pos)` | — modifies s | Insert string at position |
| `StringOfChar` | `StringOfChar(c, n)` | String | Repeat character n times |
| `UpCase` | `UpCase(c)` | Char | Single char to uppercase |
| `Succ` | `Succ(c)` | Char | Next character in ASCII table |
| `Pred` | `Pred(c)` | Char | Previous character in ASCII table |
| `Concat` | `Concat(s1, s2, ...)` | String | Join strings (prefer `+` operator) |

---

## Conversion Functions

| Function | Syntax | Returns | Example |
|---|---|---|---|
| `IntToStr` | `IntToStr(i)` | String | `IntToStr(42)` → `'42'` |
| `StrToInt` | `StrToInt(s)` | Integer | `StrToInt('42')` → `42` |
| `StrToIntDef` | `StrToIntDef(s, default)` | Integer | Returns default if conversion fails |
| `FloatToStr` | `FloatToStr(r)` | String | `FloatToStr(3.14)` → `'3.14'` |
| `StrToFloat` | `StrToFloat(s)` | Real | `StrToFloat('3.14')` → `3.14` |
| `FloatToStrF` | `FloatToStrF(r, ffFixed, 8, n)` | String | n decimal places |
| `IntToHex` | `IntToHex(i, digits)` | String | `IntToHex(255, 2)` → `'FF'` |
| `HexToInt` | `StrToInt('$' + sHex)` | Integer | Convert hex string to integer |
| `Chr` | `Chr(i)` | Char | `Chr(65)` → `'A'` |
| `Ord` | `Ord(c)` | Integer | `Ord('A')` → `65` |
| `BoolToStr` | `BoolToStr(b, True)` | String | `BoolToStr(True, True)` → `'True'` |

---

## Examples by Use Case

### Extract first N characters
```pascal
sFirst3 := Copy(sWord, 1, 3);
```

### Extract last N characters
```pascal
sLast3 := Copy(sWord, Length(sWord) - 2, 3);
```

### Extract from position to end
```pascal
// Everything after the @ in an email
iAt := Pos('@', sEmail);
sDomain := Copy(sEmail, iAt + 1, Length(sEmail) - iAt);
```

### Split on a delimiter (e.g. space in a full name)
```pascal
iSpace   := Pos(' ', sFullName);
sFirst   := Copy(sFullName, 1, iSpace - 1);
sSurname := Copy(sFullName, iSpace + 1, Length(sFullName) - iSpace);
```

### Case-insensitive comparison
```pascal
IF UpperCase(sInput) = UpperCase(sTarget) THEN
```

### Check if string contains a substring
```pascal
IF Pos('error', LowerCase(sLog)) > 0 THEN
```

### Pos — Finding a substring (three cases to know)

```pascal
// Returns the position of the first character of the match.
// Returns 0 if the substring is NOT found. Pos is case-sensitive.

Pos('at', 'I am at school')   // → 6  (found at position 6)
Pos('IT', 'Python is cool')   // → 0  (not found)
Pos('oo', 'I am cool')        // → 8  (found at position 8)
```

Always check the result before using it:
```pascal
iPos := Pos('@', sEmail);
IF iPos > 0 THEN
  sDomain := Copy(sEmail, iPos + 1, Length(sEmail) - iPos)
ELSE
  ShowMessage('Not a valid email address');
```

### Succ and Pred — stepping through characters

```pascal
cNext := Succ('M');    // → 'N'  (next in ASCII)
cPrev := Pred('M');    // → 'L'  (previous in ASCII)

// Step through A-Z using Inc (same effect as Succ):
cLetter := 'A';
Inc(cLetter);          // cLetter → 'B'
```

### Count occurrences of a character
```pascal
iCount := 0;
FOR i := 1 TO Length(sText) DO
  IF sText[i] = cFind THEN Inc(iCount);
```

### Reverse a string
```pascal
sReversed := '';
FOR i := Length(sInput) DOWNTO 1 DO
  sReversed := sReversed + sInput[i];
```

### Check if character is a digit
```pascal
IF (c >= '0') AND (c <= '9') THEN
```

### Check if character is a letter
```pascal
IF ((c >= 'A') AND (c <= 'Z')) OR ((c >= 'a') AND (c <= 'z')) THEN
```

### Build a formatted output line
```pascal
sLine := Format('%-20s %5d %6.2f', [sName, iScore, rAvg]);
// or simpler:
sLine := sName + ': ' + IntToStr(iScore);
```

---

## ASCII Reference (Common Characters)

| Dec | Char | Dec | Char | Dec | Char |
|---|---|---|---|---|---|
| 48 | `0` | 65 | `A` | 97 | `a` |
| 49 | `1` | 66 | `B` | 98 | `b` |
| ... | ... | ... | ... | ... | ... |
| 57 | `9` | 90 | `Z` | 122 | `z` |
| 32 | ` ` (space) | 33 | `!` | 46 | `.` |

**Key facts:**
- `'A'` = 65, `'Z'` = 90  
- `'a'` = 97, `'z'` = 122  
- `'0'` = 48, `'9'` = 57  
- Difference between uppercase and lowercase = 32

### Using Ord and Chr for letter arithmetic
```pascal
// Next letter
cNext := Chr(Ord(cLetter) + 1);   // 'A' → 'B'

// Shift cipher (Caesar cipher by 1)
cShifted := Chr(Ord(cLetter) + 1);

// Convert uppercase to lowercase manually
cLower := Chr(Ord(cUpper) + 32);
```

---

## FloatToStrF Format Specifiers

| Specifier | Name | Effect |
|---|---|---|
| `ffFixed` | Fixed | Always shows decimal places: `3.14` |
| `ffGeneral` | General | Shortest representation |
| `ffExponent` | Scientific | `3.14E+00` |
| `ffCurrency` | Currency | Platform currency format |

**Syntax:**
```pascal
FloatToStrF(rValue, ffFixed, 8, 2)
//                  ^^^^^^  ^  ^
//                  format  total_digits  decimal_places
```

Safe defaults: `ffFixed, 8, 2` for 2 decimal places in most exam questions.

---

## Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `sText[0]` | Out of bounds — strings are 1-based | Use `sText[1]` for first char |
| `= 'hello'` instead of `UpperCase(...) = 'HELLO'` | Case-sensitive mismatch | Always normalise case before comparing |
| `Pos` returns 0 | Substring not found | Check `> 0` before using the result |
| `Delete(sText, 1, 3)` changes nothing | Delete modifies the variable directly | Pass the actual variable, not a literal |
| `StrToInt('3.14')` | Crash — not a valid integer | Use `StrToFloat` for decimals |
