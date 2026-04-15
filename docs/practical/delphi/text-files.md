# Text Files

Text files allow your program to **save data permanently** and **read it back later**. Without file I/O, all data is lost when the program closes. In Paper 1, text file questions typically ask you to write to a file, read from a file, or both.

> [!NOTE] Grade 10+
> Text file I/O is introduced in Grade 10. The standard exam pattern is: open file → read/write with a loop → close file.

---

## The TextFile Type

Delphi uses a `TextFile` variable as a file handle — a connection to a file on disk.

```pascal
var
  f : TextFile;   // declares the file variable
```

The variable itself is not the file — it's a **handle** (reference) used to interact with it.

---

## The Five Essential Procedures

| Procedure | Purpose |
|---|---|
| `AssignFile(f, filename)` | Link the file variable to a file path |
| `Rewrite(f)` | Open for **writing** (creates file / overwrites existing) |
| `Reset(f)` | Open for **reading** (file must already exist) |
| `ReadLn(f, variable)` | Read one line from file into variable |
| `WriteLn(f, value)` | Write a value + newline to file |
| `CloseFile(f)` | Close the file (always do this) |
| `EOF(f)` | Returns True when end of file is reached |

> [!WARNING] Always Close the File
> If you don't call `CloseFile`, data may not be written to disk and the file remains locked. Put `CloseFile` in every code path.

---

## Writing to a Text File

```pascal
procedure TForm1.btnSaveClick(Sender: TObject);
var
  f      : TextFile;
  sName  : String;
  iScore : Integer;
begin
  sName  := edtName.Text;
  iScore := StrToInt(edtScore.Text);

  AssignFile(f, 'scores.txt');   // link to file
  Rewrite(f);                     // create/overwrite and open for writing

  WriteLn(f, sName);             // writes string + newline
  WriteLn(f, IntToStr(iScore));  // convert to string then write
  WriteLn(f, 'End of record');

  CloseFile(f);
  ShowMessage('Data saved successfully.');
end;
```

### Writing multiple records in a loop

```pascal
procedure TForm1.btnSaveAllClick(Sender: TObject);
const
  MAX = 5;
var
  f       : TextFile;
  aNames  : array[1..MAX] of String;
  aScores : array[1..MAX] of Integer;
  i       : Integer;
begin
  AssignFile(f, 'classdata.txt');
  Rewrite(f);

  FOR i := 1 TO MAX DO
  BEGIN
    WriteLn(f, aNames[i]);
    WriteLn(f, IntToStr(aScores[i]));
  END;

  CloseFile(f);
end;
```

---

## Reading from a Text File

```pascal
procedure TForm1.btnLoadClick(Sender: TObject);
var
  f     : TextFile;
  sLine : String;
begin
  AssignFile(f, 'scores.txt');
  Reset(f);                    // open for reading

  redOutput.Lines.Clear;

  WHILE NOT EOF(f) DO          // loop until end of file
  BEGIN
    ReadLn(f, sLine);          // read one line into sLine
    redOutput.Lines.Add(sLine);
  END;

  CloseFile(f);
end;
```

### Reading into variables (structured data)

```pascal
procedure TForm1.btnLoadDataClick(Sender: TObject);
var
  f      : TextFile;
  sName  : String;
  iScore : Integer;
  sTemp  : String;
begin
  AssignFile(f, 'classdata.txt');
  Reset(f);
  redOutput.Lines.Clear;

  WHILE NOT EOF(f) DO
  BEGIN
    ReadLn(f, sName);   // read name line
    ReadLn(f, sTemp);   // read score line (as string)
    iScore := StrToInt(sTemp);

    redOutput.Lines.Add(sName + ': ' + IntToStr(iScore));
  END;

  CloseFile(f);
end;
```

> [!NOTE] ReadLn Always Reads a String
> `ReadLn(f, sLine)` reads the text into `sLine`. If you need an integer, read into a String first then convert: `iScore := StrToInt(sLine)`.

---

## Appending to an Existing File

To add data without overwriting:

```pascal
AssignFile(f, 'log.txt');
Append(f);             // open for appending (adds to end of file)
WriteLn(f, 'New log entry: ' + TimeToStr(Time));
CloseFile(f);
```

> `Rewrite` — **creates** (overwrites if exists)  
> `Reset` — reads from start  
> `Append` — writes to end of existing file

---

## Check if File Exists Before Reading

Reading a file that doesn't exist causes a runtime error. Use `FileExists` to check first:

```pascal
IF FileExists('scores.txt') THEN
BEGIN
  AssignFile(f, 'scores.txt');
  Reset(f);
  // ... read ...
  CloseFile(f);
END
ELSE
  ShowMessage('File not found.');
```

---

## Common File Path Formats

```pascal
// Same folder as the program (.exe)
AssignFile(f, 'data.txt');
AssignFile(f, 'output\results.txt');   // subfolder

// Absolute path (exam questions usually use relative paths)
AssignFile(f, 'C:\Data\scores.txt');

// Using a variable for the filename
AssignFile(f, edtFilename.Text);
```

> [!TIP] Exam Questions Usually Give the Filename
> In Paper 1, the filename is almost always given in the question (e.g. "save to a file called `Results.txt`"). You just need to know the correct procedure to use.

---

## Complete Worked Example — Save and Load

```pascal
// ─── SAVE ──────────────────────────────────────────────────────────
procedure TForm1.btnSaveClick(Sender: TObject);
const
  MAX = 3;
var
  f       : TextFile;
  aNames  : array[1..MAX] of String;
  aMarks  : array[1..MAX] of Integer;
  i       : Integer;
begin
  // Assume arrays already populated
  aNames[1] := 'Alice';  aMarks[1] := 87;
  aNames[2] := 'Bob';    aMarks[2] := 72;
  aNames[3] := 'Carol';  aMarks[3] := 91;

  AssignFile(f, 'marks.txt');
  Rewrite(f);

  FOR i := 1 TO MAX DO
  BEGIN
    WriteLn(f, aNames[i]);
    WriteLn(f, IntToStr(aMarks[i]));
  END;

  CloseFile(f);
  ShowMessage('Saved ' + IntToStr(MAX) + ' records.');
end;

// ─── LOAD ──────────────────────────────────────────────────────────
procedure TForm1.btnLoadClick(Sender: TObject);
var
  f      : TextFile;
  sName  : String;
  sTemp  : String;
  iMark  : Integer;
begin
  IF NOT FileExists('marks.txt') THEN
  BEGIN
    ShowMessage('marks.txt not found.');
    Exit;
  END;

  AssignFile(f, 'marks.txt');
  Reset(f);
  redOutput.Lines.Clear;

  WHILE NOT EOF(f) DO
  BEGIN
    ReadLn(f, sName);
    ReadLn(f, sTemp);
    iMark := StrToInt(sTemp);

    redOutput.Lines.Add(sName + ' — ' + IntToStr(iMark) + '%');
  END;

  CloseFile(f);
end;
```

**Contents of `marks.txt` after saving:**
```
Alice
87
Bob
72
Carol
91
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Forgetting `CloseFile`** — data may not flush to disk; file stays locked
> 2. **Using `Reset` when the file doesn't exist** — runtime error; check `FileExists` first
> 3. **Using `Rewrite` instead of `Reset`** for reading — `Rewrite` empties the file!
> 4. **Not converting types** — `ReadLn` always reads text; convert with `StrToInt`/`StrToFloat` as needed
> 5. **Hardcoding absolute paths** — `'C:\Users\me\scores.txt'` won't work on a different computer; use relative paths in exams
> 6. **Missing `EOF` check** — reading past the end of file causes a runtime error

---

## Quick Reference

```pascal
// Write
AssignFile(f, 'file.txt');  Rewrite(f);
WriteLn(f, sValue);
CloseFile(f);

// Read
AssignFile(f, 'file.txt');  Reset(f);
WHILE NOT EOF(f) DO BEGIN ReadLn(f, sLine); END;
CloseFile(f);

// Append
AssignFile(f, 'file.txt');  Append(f);
WriteLn(f, sNewData);
CloseFile(f);
```

---

## Practice Exercises

**Exercise 1 — Write then read**

Write a program that:
a) On button click "Save": writes the numbers 1 to 10 (one per line) to `numbers.txt`
b) On button click "Load": reads the file and displays the sum of all numbers in `lblSum`

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnSaveClick(Sender: TObject);
var
  f : TextFile;
  i : Integer;
begin
  AssignFile(f, 'numbers.txt');
  Rewrite(f);
  FOR i := 1 TO 10 DO
    WriteLn(f, IntToStr(i));
  CloseFile(f);
  ShowMessage('Saved.');
end;

procedure TForm1.btnLoadClick(Sender: TObject);
var
  f    : TextFile;
  sNum : String;
  iSum : Integer;
begin
  IF NOT FileExists('numbers.txt') THEN
  BEGIN
    ShowMessage('File not found.');
    Exit;
  END;

  AssignFile(f, 'numbers.txt');
  Reset(f);
  iSum := 0;

  WHILE NOT EOF(f) DO
  BEGIN
    ReadLn(f, sNum);
    iSum := iSum + StrToInt(sNum);
  END;

  CloseFile(f);
  lblSum.Caption := 'Sum = ' + IntToStr(iSum);
end;
```
</details>

---

> [!TIP] Exam Tip
> Text file questions in Paper 1 almost always follow the same pattern: open → loop with ReadLn → process → close. The three things to get right: (1) use `Reset` for reading and `Rewrite` for writing, (2) use `WHILE NOT EOF(f) DO` for the loop, (3) always `CloseFile`. Get those three right and you get the structure marks even if your processing logic has a small error.
