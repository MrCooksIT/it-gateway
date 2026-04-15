# ShowMessage & Dialogs

Delphi provides built-in dialog functions for displaying messages and getting user input without designing a custom form. These are used constantly in exam questions.

> [!NOTE] Grade 10+
> ShowMessage and InputBox are introduced in Grade 10 and used in nearly every practical question.

---

## ShowMessage

Displays a popup message box with an OK button. The program **pauses** until the user clicks OK.

```pascal
ShowMessage('Calculation complete!');
ShowMessage('Error: please enter a valid number.');
ShowMessage('The average is: ' + FloatToStrF(rAvg, ffFixed, 8, 2));
```

**Building the message:**
```pascal
// Concatenate strings and variables
ShowMessage('Name: ' + sName + ', Score: ' + IntToStr(iScore));

// Multi-line using sLineBreak
ShowMessage('Name: ' + sName + sLineBreak +
            'Grade: ' + IntToStr(iGrade) + sLineBreak +
            'Mark: ' + IntToStr(iMark));
```

> [!TIP] ShowMessage vs lblResult.Caption
> `ShowMessage` is intrusive (user must click OK) — use it for alerts, confirmations, and errors. For continuous display of data, use `lblResult.Caption` or `redOutput.Lines.Add` instead.

---

## InputBox

Displays a dialog with a text input field. Returns the user's typed text as a **String**.

```pascal
// Syntax:
sResult := InputBox('Title', 'Prompt', 'DefaultValue');

// Examples:
sName  := InputBox('Student Data', 'Enter student name:', '');
sScore := InputBox('Score Entry', 'Enter score (0-100):', '0');
iNum   := StrToInt(InputBox('Input', 'Enter a number:', ''));
```

**Always convert the result for numeric input:**
```pascal
var
  iAge : Integer;
begin
  iAge := StrToInt(InputBox('Age', 'Enter your age:', ''));
  // WARNING: crashes if user types non-numeric text
  // Use try/except or validate the string before converting
end;
```

---

## MessageDlg — Dialog with Multiple Buttons

`MessageDlg` shows a message with Yes/No/Cancel or other button combinations. Returns which button was clicked.

```pascal
var
  iChoice : Integer;
begin
  iChoice := MessageDlg('Are you sure you want to delete this record?',
                         mtConfirmation,
                         [mbYes, mbNo],
                         0);

  IF iChoice = mrYes THEN
    DeleteRecord
  ELSE
    ShowMessage('Deletion cancelled.');
end;
```

**Message types (`mtXxx`):**

| Constant | Icon |
|---|---|
| `mtInformation` | i (blue) |
| `mtWarning` | ! (yellow) |
| `mtError` | x (red) |
| `mtConfirmation` | ? (question mark) |

**Button sets (`mbXxx`):**

| Button | Constant |
|---|---|
| OK | `mbOk` |
| Cancel | `mbCancel` |
| Yes | `mbYes` |
| No | `mbNo` |
| Abort | `mbAbort` |
| Retry | `mbRetry` |

**Return values (`mrXxx`):**

```pascal
IF MessageDlg(...) = mrYes THEN ...
```

---

## InputQuery — InputBox with OK/Cancel

Unlike `InputBox` (always returns a string even if cancelled), `InputQuery` returns `True` if OK was clicked, `False` if cancelled:

```pascal
var
  sInput  : String;
  bOkClicked : Boolean;
begin
  sInput     := '';
  bOkClicked := InputQuery('Input', 'Enter your name:', sInput);

  IF bOkClicked THEN
    lblName.Caption := 'Hello, ' + sInput
  ELSE
    lblName.Caption := 'Cancelled.';
end;
```

---

## Common Dialog Patterns

### Confirm before action

```pascal
IF MessageDlg('Clear all data?', mtConfirmation, [mbYes, mbNo], 0) = mrYes THEN
BEGIN
  redOutput.Lines.Clear;
  edtName.Clear;
  edtScore.Clear;
END;
```

### Loop input with InputBox

```pascal
procedure TForm1.btnLoadClick(Sender: TObject);
const
  MAX = 5;
var
  aScores : array[1..MAX] of Integer;
  i       : Integer;
begin
  FOR i := 1 TO MAX DO
  BEGIN
    aScores[i] := StrToInt(
      InputBox('Score', 'Enter score ' + IntToStr(i) + ' of ' + IntToStr(MAX) + ':', ''));
  END;
  ShowMessage('All ' + IntToStr(MAX) + ' scores entered.');
end;
```

### Error message with focus

```pascal
IF edtName.Text = '' THEN
BEGIN
  ShowMessage('Name cannot be blank.');
  edtName.SetFocus;
  Exit;
END;
```

---

## Quick Reference

| Function | Returns | Modal? | Use for |
|---|---|---|---|
| `ShowMessage(msg)` | Nothing | Yes | Simple notification/error |
| `InputBox(t, p, d)` | String | Yes | Get one text input from user |
| `InputQuery(t, p, v)` | Boolean | Yes | Get input; detect if cancelled |
| `MessageDlg(m, t, b, 0)` | Integer | Yes | Multi-button confirmation |

---

> [!TIP] Exam Tip
> In Paper 1, `ShowMessage` and `InputBox` appear in almost every question. Make sure you know: (1) how to include a variable in a ShowMessage — concatenate with `IntToStr`/`FloatToStrF`; (2) that `InputBox` always returns a `String` — convert immediately with `StrToInt` or `StrToFloat`; (3) that both pause execution until the user responds.
