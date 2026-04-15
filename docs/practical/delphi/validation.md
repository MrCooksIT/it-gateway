# Input Validation

Every program that accepts user input must defend against bad data. A user might type letters where you expect a number, leave a field blank, or enter a value outside the acceptable range. Validation is the code that catches these mistakes before they crash your program or corrupt your data.

> [!NOTE] Grade 10+
> Basic input validation (range checks, presence checks) is introduced in Grade 10. Try/except is extended in Grade 11.

---

## Why Validate?

```pascal
// Without validation — crashes if user types "abc"
iScore := StrToInt(edtScore.Text);

// With validation — handles bad input gracefully
IF edtScore.Text = '' THEN
  ShowMessage('Please enter a score')
ELSE
  iScore := StrToInt(edtScore.Text);
```

`StrToInt` raises an exception (runtime error) if the string is not a valid integer. Validation prevents the program from reaching that code with invalid data.

---

## Types of Validation to Know

| Type | What it checks | Example |
|---|---|---|
| **Presence check** | Field is not empty | Name cannot be blank |
| **Type check** | Value is the correct type | Score must be a number |
| **Range check** | Value is within min–max | Score must be 0–100 |
| **Length check** | String length within limits | Password must be ≥ 8 characters |
| **Format check** | Matches a pattern | Email must contain @ |

---

## Presence Check (Not Empty)

```pascal
IF Trim(edtName.Text) = '' THEN
BEGIN
  ShowMessage('Name cannot be blank.');
  edtName.SetFocus;
  Exit;
END;
```

> [!TIP] Always Trim Before Checking
> `Trim` removes leading/trailing spaces. A user who types just spaces would otherwise pass a blank check.

---

## Range Check

```pascal
var
  iScore : Integer;
begin
  iScore := StrToInt(edtScore.Text);  // assumes input is numeric

  IF (iScore < 0) OR (iScore > 100) THEN
  BEGIN
    ShowMessage('Score must be between 0 and 100.');
    edtScore.SetFocus;
    Exit;
  END;

  // proceed with valid iScore
end;
```

---

## Type Check Using Try/Except

The safest way to handle potentially non-numeric input:

```pascal
var
  iScore : Integer;
  bValid : Boolean;
begin
  bValid := True;
  
  try
    iScore := StrToInt(edtScore.Text);
  except
    on E : EConvertError do
    BEGIN
      ShowMessage('Please enter a valid whole number.');
      edtScore.SetFocus;
      bValid := False;
    END;
  end;
  
  IF NOT bValid THEN Exit;
  
  // iScore is now guaranteed to be a valid integer
end;
```

### For Real Numbers

```pascal
var
  rPrice : Real;
begin
  try
    rPrice := StrToFloat(edtPrice.Text);
  except
    ShowMessage('Enter a valid price (e.g. 12.99)');
    edtPrice.SetFocus;
    Exit;
  end;
  
  // rPrice is valid
end;
```

---

## Combining Multiple Validations

Real exam questions often require several validations together:

```pascal
procedure TForm1.btnSubmitClick(Sender: TObject);
var
  sName  : String;
  iAge   : Integer;
  iScore : Integer;
begin
  // ── 1. Presence check ──────────────────────────────────────────
  IF Trim(edtName.Text) = '' THEN
  BEGIN
    ShowMessage('Name cannot be blank.');
    edtName.SetFocus;
    Exit;
  END;

  sName := Trim(edtName.Text);

  // ── 2. Type check for age ───────────────────────────────────────
  try
    iAge := StrToInt(edtAge.Text);
  except
    ShowMessage('Age must be a whole number.');
    edtAge.SetFocus;
    Exit;
  end;

  // ── 3. Range check for age ──────────────────────────────────────
  IF (iAge < 10) OR (iAge > 20) THEN
  BEGIN
    ShowMessage('Age must be between 10 and 20.');
    edtAge.SetFocus;
    Exit;
  END;

  // ── 4. Type + range check for score ─────────────────────────────
  try
    iScore := StrToInt(edtScore.Text);
  except
    ShowMessage('Score must be a whole number.');
    edtScore.SetFocus;
    Exit;
  end;

  IF (iScore < 0) OR (iScore > 100) THEN
  BEGIN
    ShowMessage('Score must be 0–100.');
    edtScore.SetFocus;
    Exit;
  END;

  // ── All validated — proceed ──────────────────────────────────────
  redOutput.Lines.Add(sName + ' | Age: ' + IntToStr(iAge) +
                      ' | Score: ' + IntToStr(iScore));
end;
```

---

## Validation with REPEAT...UNTIL (Loop Until Valid)

When using `InputBox` (console-style scenarios), keep asking until the input is valid:

```pascal
procedure TForm1.btnInputClick(Sender: TObject);
var
  sInput : String;
  iNum   : Integer;
  bValid : Boolean;
begin
  bValid := False;

  REPEAT
    sInput := InputBox('Input', 'Enter a number between 1 and 10:', '');

    try
      iNum := StrToInt(sInput);
      IF (iNum >= 1) AND (iNum <= 10) THEN
        bValid := True
      ELSE
        ShowMessage('Must be between 1 and 10.');
    except
      ShowMessage('Not a valid number. Try again.');
    end;

  UNTIL bValid;

  ShowMessage('Valid input: ' + IntToStr(iNum));
end;
```

---

## Format Check — Email Example

```pascal
function IsValidEmail(sEmail : String) : Boolean;
var
  iAt, iDot : Integer;
begin
  sEmail := Trim(sEmail);
  iAt    := Pos('@', sEmail);
  
  // Must have @ and at least one . after the @
  Result := (iAt > 1) AND (Pos('.', Copy(sEmail, iAt, Length(sEmail))) > 0);
end;

// Usage:
IF NOT IsValidEmail(edtEmail.Text) THEN
BEGIN
  ShowMessage('Please enter a valid email address.');
  edtEmail.SetFocus;
  Exit;
END;
```

---

## Length Check

```pascal
IF Length(Trim(edtPassword.Text)) < 8 THEN
BEGIN
  ShowMessage('Password must be at least 8 characters.');
  edtPassword.SetFocus;
  Exit;
END;
```

---

## StrToIntDef — Conversion with Default

An alternative to try/except for integer conversion — returns a default value if conversion fails:

```pascal
iScore := StrToIntDef(edtScore.Text, -1);  // returns -1 if not a valid integer

IF iScore = -1 THEN
BEGIN
  ShowMessage('Enter a valid integer.');
  Exit;
END;
```

Choose a default value that can't be a valid input (e.g. -1 for a score that must be ≥ 0).

---

## Common Validation Patterns

### Check before converting

```pascal
// Always validate type before converting, then validate range
try
  iValue := StrToInt(edtInput.Text);
except
  ShowMessage('Must be an integer.');
  Exit;
end;
IF (iValue < MIN) OR (iValue > MAX) THEN ...
```

### SetFocus after error

Always call `edtField.SetFocus` after showing an error — puts the cursor back in the problematic field:

```pascal
ShowMessage('Invalid input.');
edtScore.SetFocus;
Exit;
```

### Clear and re-enter

```pascal
edtScore.Clear;       // wipe the bad input
edtScore.SetFocus;    // cursor to the field
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Not trimming before presence check** — spaces pass an empty check
> 2. **Converting before validating type** — `StrToInt('abc')` crashes before you can check
> 3. **Not calling `Exit` after error** — code continues to execute with invalid data
> 4. **Forgetting `SetFocus`** — user has to click back to the problematic field manually
> 5. **Using `= 0` as a default for StrToIntDef** — if 0 is a valid input, use a different sentinel value

---

## Practice Exercises

**Exercise 1 — Grade input**

Validate input from `edtGrade` — must be an integer, value must be 10, 11, or 12. Show appropriate error messages for each failure case.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnValidateGradeClick(Sender: TObject);
var
  iGrade : Integer;
begin
  IF Trim(edtGrade.Text) = '' THEN
  BEGIN
    ShowMessage('Grade cannot be blank.');
    edtGrade.SetFocus;
    Exit;
  END;

  try
    iGrade := StrToInt(edtGrade.Text);
  except
    ShowMessage('Grade must be a whole number.');
    edtGrade.SetFocus;
    Exit;
  end;

  IF NOT (iGrade IN [10, 11, 12]) THEN
  BEGIN
    ShowMessage('Grade must be 10, 11, or 12.');
    edtGrade.SetFocus;
    Exit;
  END;

  lblResult.Caption := 'Valid grade: ' + IntToStr(iGrade);
end;
```
</details>

---

> [!TIP] Exam Tip
> Validation questions in Paper 1 test a specific pattern: (1) check for blank, (2) check for correct type, (3) check for valid range/format. Write them in that order — check presence first (prevents crashes), then type, then range. Use `Exit` after each `ShowMessage` to stop execution.
