# Connecting Databases to Delphi

Writing SQL is only half the job. In the exam, you connect an Access or SQL database to a Delphi application and use code to query, display, and update data. This page covers everything you need: the components, the connection process, and the code patterns.

---

## The Component Chain

Data flows through a chain of components:

```
TADOConnection
      ↓
TADOQuery  (or TADOTable)
      ↓
TDataSource
      ↓
TDBGrid  (or TDBEdit, TDBLabel, etc.)
```

| Component | Prefix | Purpose |
|---|---|---|
| `TADOConnection` | `adoConn` | Holds connection string to the database file |
| `TADOQuery` | `adoQry` | Executes SQL and holds the result set |
| `TDataSource` | `dsSrc` | Bridge between ADO component and visual controls |
| `TDBGrid` | `dbgGrid` | Displays query results in a table |
| `TDBEdit` | `dbeField` | Displays/edits a single field value |
| `TDBNavigator` | `dbNav` | Buttons to navigate and edit records |

---

## Setting Up at Design Time

### Step 1 — TADOConnection

1. Drop `TADOConnection` on the form
2. Set `LoginPrompt` → `False`
3. Click `ConnectionString` → `Build...`
4. Select **Microsoft Jet 4.0 OLE DB Provider** (for `.mdb`) or **Microsoft ACE OLEDB 12.0** (for `.accdb`)
5. Browse to your `.accdb` file
6. Test connection → OK

**In code:**
```pascal
adoConn.ConnectionString :=
  'Provider=Microsoft.ACE.OLEDB.12.0;' +
  'Data Source=C:\Path\To\Database.accdb;' +
  'Persist Security Info=False';
adoConn.LoginPrompt := False;
adoConn.Open;
```

### Step 2 — TADOQuery

1. Drop `TADOQuery` on form
2. Set `Connection` → your `TADOConnection`
3. (Optional) Set `SQL.Text` at design time

### Step 3 — TDataSource

1. Drop `TDataSource` on form
2. Set `DataSet` → your `TADOQuery`

### Step 4 — TDBGrid

1. Drop `TDBGrid` on form
2. Set `DataSource` → your `TDataSource`

---

## Opening a Query (Displaying Data)

```pascal
procedure TForm1.FormCreate(Sender: TObject);
begin
  // Connect to the database
  adoConn.ConnectionString :=
    'Provider=Microsoft.ACE.OLEDB.12.0;' +
    'Data Source=' + ExtractFilePath(Application.ExeName) + 'Students.accdb;' +
    'Persist Security Info=False';
  adoConn.LoginPrompt := False;
  adoConn.Open;
  
  // Run initial query — show all students
  adoQryStudents.Connection := adoConn;
  adoQryStudents.SQL.Text := 'SELECT * FROM Students ORDER BY Surname';
  adoQryStudents.Open;
end;
```

---

## Dynamic SQL Queries

The most important skill: building SQL based on user input.

### Filter by a field:

```pascal
procedure TForm1.btnSearchClick(Sender: TObject);
var
  sGrade: String;
begin
  sGrade := edtGrade.Text;
  adoQryStudents.Close;
  adoQryStudents.SQL.Text :=
    'SELECT StudentID, FirstName, Surname, Grade ' +
    'FROM Students ' +
    'WHERE Grade = ' + sGrade + ' ' +
    'ORDER BY Surname';
  adoQryStudents.Open;
end;
```

### Search with LIKE:

```pascal
procedure TForm1.btnSearchSurnameClick(Sender: TObject);
var
  sSurname: String;
begin
  sSurname := edtSurname.Text;
  adoQryStudents.Close;
  adoQryStudents.SQL.Text :=
    'SELECT * FROM Students ' +
    'WHERE Surname LIKE ' + QuotedStr('%' + sSurname + '%') + ' ' +
    'ORDER BY Surname';
  adoQryStudents.Open;
end;
```

> [!TIP] Use QuotedStr() for string values in SQL
> `QuotedStr('hello')` returns `'hello'` (with single quotes added)  
> This prevents SQL injection and handles apostrophes in names.

---

## Reading Values from the Dataset

### Access a field value from the current record:

```pascal
// Access by field name (most readable)
sName := adoQryStudents.FieldByName('FirstName').AsString;
iGrade := adoQryStudents.FieldByName('Grade').AsInteger;
rMark := adoQryStudents.FieldByName('Mark').AsFloat;
```

### Loop through all records:

```pascal
procedure TForm1.btnListAllClick(Sender: TObject);
var
  sOutput: String;
begin
  adoQryStudents.First;
  sOutput := '';
  while not adoQryStudents.EOF do
  begin
    sOutput := sOutput +
      adoQryStudents.FieldByName('Surname').AsString + ', ' +
      adoQryStudents.FieldByName('FirstName').AsString +
      ' (Grade ' + adoQryStudents.FieldByName('Grade').AsString + ')' + #13#10;
    adoQryStudents.Next;
  end;
  redOutput.Text := sOutput;
end;
```

> [!WARNING] Always use First + while EOF loop
> - `.First` — moves to first record  
> - `.EOF` — True when past the last record  
> - `.Next` — advance to next record  
> - Forgetting `.Next` creates an infinite loop!

---

## Aggregate Queries (Single Values)

When your SQL returns one row/value:

```pascal
procedure TForm1.btnAverageClick(Sender: TObject);
var
  rAvg: Real;
begin
  adoQryTemp.Close;
  adoQryTemp.SQL.Text :=
    'SELECT AVG(Mark) AS AvgMark FROM Marks WHERE Grade = 12';
  adoQryTemp.Open;
  
  if not adoQryTemp.IsEmpty then
  begin
    rAvg := adoQryTemp.FieldByName('AvgMark').AsFloat;
    lblAvg.Caption := 'Class average: ' + FloatToStrF(rAvg, ffFixed, 8, 1) + '%';
  end;
end;
```

---

## JOIN Queries in Delphi

```pascal
procedure TForm1.btnJoinClick(Sender: TObject);
begin
  adoQryResults.Close;
  adoQryResults.SQL.Text :=
    'SELECT s.Surname, s.FirstName, sub.SubjectName, m.Mark ' +
    'FROM Students AS s ' +
    'INNER JOIN Marks AS m ON s.StudentID = m.StudentID ' +
    'INNER JOIN Subjects AS sub ON m.SubjectCode = sub.SubjectCode ' +
    'WHERE s.Grade = ' + edtGrade.Text + ' ' +
    'ORDER BY s.Surname, sub.SubjectName';
  adoQryResults.Open;
  // dbgGrid automatically shows results via TDataSource
end;
```

---

## Executing Non-SELECT Queries (INSERT, UPDATE, DELETE)

For DML statements that don't return a result set, use `ExecSQL` instead of `Open`.

```pascal
// INSERT
procedure TForm1.btnAddClick(Sender: TObject);
begin
  adoQryEdit.Close;
  adoQryEdit.SQL.Text :=
    'INSERT INTO Students (FirstName, Surname, Grade) ' +
    'VALUES (' +
    QuotedStr(edtFirstName.Text) + ', ' +
    QuotedStr(edtSurname.Text) + ', ' +
    edtGrade.Text + ')';
  adoQryEdit.ExecSQL;
  ShowMessage('Student added!');
  
  // Refresh display query
  adoQryStudents.Close;
  adoQryStudents.Open;
end;

// UPDATE
procedure TForm1.btnUpdateMarkClick(Sender: TObject);
begin
  adoQryEdit.Close;
  adoQryEdit.SQL.Text :=
    'UPDATE Marks ' +
    'SET Mark = ' + edtNewMark.Text + ' ' +
    'WHERE MarkID = ' + edtMarkID.Text;
  adoQryEdit.ExecSQL;
  ShowMessage('Mark updated!');
  adoQryStudents.Close;
  adoQryStudents.Open;    // refresh
end;

// DELETE
procedure TForm1.btnDeleteClick(Sender: TObject);
begin
  if MessageDlg('Delete this student?', mtConfirmation, [mbYes, mbNo], 0) = mrYes then
  begin
    adoQryEdit.Close;
    adoQryEdit.SQL.Text :=
      'DELETE FROM Students WHERE StudentID = ' +
      adoQryStudents.FieldByName('StudentID').AsString;
    adoQryEdit.ExecSQL;
    adoQryStudents.Close;
    adoQryStudents.Open;
  end;
end;
```

---

## Complete Worked Example

A form with: a DBGrid showing students, a grade filter, and a search by surname.

```pascal
unit StudentUnit;

interface

uses
  ADODB, DB, Grids, DBGrids, StdCtrls, Forms, ...;

type
  TfrmStudents = class(TForm)
    adoConn: TADOConnection;
    adoQryStudents: TADOQuery;
    adoQryEdit: TADOQuery;
    dsSrc: TDataSource;
    dbgStudents: TDBGrid;
    edtSurnameSearch: TEdit;
    cmbGrade: TComboBox;
    btnSearch: TButton;
    btnClear: TButton;
    lblCount: TLabel;
    procedure FormCreate(Sender: TObject);
    procedure btnSearchClick(Sender: TObject);
    procedure btnClearClick(Sender: TObject);
    procedure adoQryStudentsAfterOpen(DataSet: TDataSet);
  end;

implementation

procedure TfrmStudents.FormCreate(Sender: TObject);
begin
  adoConn.ConnectionString :=
    'Provider=Microsoft.ACE.OLEDB.12.0;Data Source=' +
    ExtractFilePath(Application.ExeName) + 'School.accdb;Persist Security Info=False';
  adoConn.LoginPrompt := False;
  adoConn.Open;

  adoQryStudents.Connection := adoConn;
  adoQryEdit.Connection := adoConn;
  dsSrc.DataSet := adoQryStudents;
  dbgStudents.DataSource := dsSrc;

  btnClearClick(nil);   // load all students on startup
end;

procedure TfrmStudents.btnSearchClick(Sender: TObject);
var
  sSQL, sWhere: String;
begin
  sSQL := 'SELECT StudentID, FirstName, Surname, Grade FROM Students';
  sWhere := '';

  if edtSurnameSearch.Text <> '' then
    sWhere := 'Surname LIKE ' + QuotedStr('%' + edtSurnameSearch.Text + '%');

  if cmbGrade.ItemIndex > 0 then  // 0 = 'All grades'
  begin
    if sWhere <> '' then sWhere := sWhere + ' AND ';
    sWhere := sWhere + 'Grade = ' + cmbGrade.Text;
  end;

  if sWhere <> '' then
    sSQL := sSQL + ' WHERE ' + sWhere;

  sSQL := sSQL + ' ORDER BY Surname, FirstName';

  adoQryStudents.Close;
  adoQryStudents.SQL.Text := sSQL;
  adoQryStudents.Open;
end;

procedure TfrmStudents.btnClearClick(Sender: TObject);
begin
  edtSurnameSearch.Clear;
  cmbGrade.ItemIndex := 0;
  adoQryStudents.Close;
  adoQryStudents.SQL.Text := 'SELECT * FROM Students ORDER BY Surname, FirstName';
  adoQryStudents.Open;
end;

procedure TfrmStudents.adoQryStudentsAfterOpen(DataSet: TDataSet);
begin
  lblCount.Caption := 'Records: ' + IntToStr(adoQryStudents.RecordCount);
end;
```

---

## Common Patterns and Tips

| Pattern | Code |
|---|---|
| Check if query returned results | `if not adoQry.IsEmpty then ...` |
| Count records returned | `adoQry.RecordCount` |
| Get current field value | `adoQry.FieldByName('Field').AsString` |
| Move to first record | `adoQry.First` |
| Loop all records | `while not adoQry.EOF do begin ... adoQry.Next; end` |
| Build relative path | `ExtractFilePath(Application.ExeName) + 'DB.accdb'` |
| String in SQL | `QuotedStr(sValue)` |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Call `Open` on INSERT/UPDATE/DELETE | Use `ExecSQL` for non-SELECT queries |
| Call `ExecSQL` on SELECT | Use `Open` for SELECT queries |
| Forget `.Close` before changing `SQL.Text` | Always `.Close` before modifying SQL |
| String value not quoted in SQL | Use `QuotedStr()` for string values |
| Hardcoded file path | Use `ExtractFilePath(Application.ExeName)` |
| Infinite loop — forgot `.Next` | Always call `adoQry.Next` inside EOF loop |
| Case sensitive field names | Match field names exactly as in the database |
