# Delphi Components

A Delphi program's visual interface is built from **components** — pre-built visual and non-visual elements you drag onto a form. Every component has **properties** (what it looks like/stores), **methods** (what it can do), and **events** (what triggers your code).

> [!NOTE] Grade 10+
> Delphi components and naming conventions are introduced in Grade 10. The component reference here covers all components used in Paper 1 exams.

---

## The Golden Rule: Naming Conventions

Every component must be renamed with the correct **Hungarian notation prefix**. Examiners deduct marks for wrong or missing prefixes.

| Component | Prefix | Example Name |
|---|---|---|
| TButton | `btn` | `btnCalculate`, `btnClear` |
| TLabel | `lbl` | `lblResult`, `lblTotal` |
| TEdit | `edt` | `edtName`, `edtScore` |
| TRichEdit | `red` | `redOutput`, `redNotes` |
| TMemo | `mmo` | `mmoText`, `mmoNotes` |
| TCheckBox | `chk` | `chkRemember`, `chkActive` |
| TRadioButton | `rdb` | `rdbMale`, `rdbFemale` |
| TComboBox | `cmb` | `cmbGrade`, `cmbSubject` |
| TListBox | `lst` | `lstItems`, `lstNames` |
| TGroupBox | `grp` | `grpOptions` |
| TPanel | `pnl` | `pnlTop` |
| TImage | `img` | `imgPhoto`, `imgLogo` |
| TTimer | `tmr` | `tmrClock`, `tmrRefresh` |
| TMainMenu | `mnu` | `mnuFile` |
| TOpenDialog | `dlg` | `dlgOpen` |
| TSaveDialog | `dlg` | `dlgSave` |
| TScrollBar | `scr` | `scrVolume` |
| TTrackBar | `trk` | `trkValue` |

---

## TButton

A clickable button that triggers an event.

**Key property:**

| Property | Type | Purpose |
|---|---|---|
| `Caption` | String | Text displayed on the button |
| `Enabled` | Boolean | Whether button can be clicked |
| `Visible` | Boolean | Whether button is shown |
| `Name` | String | Code identifier (`btnCalc`) |

**Key event:** `OnClick` — runs when button is clicked

```pascal
procedure TForm1.btnCalcClick(Sender: TObject);
begin
  // code here runs when button is clicked
end;

// In code:
btnCalc.Enabled := False;   // disable button
btnCalc.Visible := False;   // hide button
btnCalc.Caption := 'Done';  // change text
```

---

## TLabel

Displays read-only text on the form. Used for titles, results, and prompts.

| Property | Type | Purpose |
|---|---|---|
| `Caption` | String | Text displayed |
| `Font` | TFont | Font size, style, colour |
| `Color` | TColor | Background colour |
| `Visible` | Boolean | Whether label is shown |

```pascal
lblResult.Caption := 'Total: R' + FloatToStrF(rTotal, ffFixed, 8, 2);
lblStatus.Caption := 'Pass';
lblCount.Caption  := IntToStr(iCount) + ' items found';
```

---

## TEdit

A single-line text input box. All user typing is in `Text` property.

| Property | Type | Purpose |
|---|---|---|
| `Text` | String | Current content of the edit box |
| `ReadOnly` | Boolean | Prevent user from editing |
| `MaxLength` | Integer | Limit number of characters |
| `PasswordChar` | Char | Show `*` instead of typed chars |

```pascal
// Reading input
sName  := edtName.Text;
iScore := StrToInt(edtScore.Text);
rPrice := StrToFloat(edtPrice.Text);

// Setting content
edtName.Text := 'Alice';
edtScore.Text := '';       // clear

// Trim spaces
sName := Trim(edtName.Text);

// Set focus
edtName.SetFocus;

// Password field
edtPassword.PasswordChar := '*';
```

---

## TRichEdit

A multi-line text area. Used for displaying multiple lines of output.

| Property | Type | Purpose |
|---|---|---|
| `Lines` | TStrings | Collection of all lines of text |
| `Text` | String | All content as one string |
| `ReadOnly` | Boolean | Prevent user editing |

```pascal
// Add a line
redOutput.Lines.Add('Result: ' + IntToStr(iResult));

// Clear all content
redOutput.Lines.Clear;

// Access a specific line (0-based!)
sLine := redOutput.Lines[0];   // first line

// Count lines
iCount := redOutput.Lines.Count;

// Multiple lines at once
redOutput.Lines.Add('Name:    ' + sName);
redOutput.Lines.Add('Score:   ' + IntToStr(iScore));
redOutput.Lines.Add('Average: ' + FloatToStrF(rAvg, ffFixed, 8, 2));
```

> [!WARNING] Lines is 0-Based
> `redOutput.Lines[0]` is the FIRST line, `Lines[1]` is the second, etc. This is different from Delphi arrays which are typically 1-based.

---

## TCheckBox

A tick box — the user checks or unchecks it. Provides a Boolean `Checked` property.

| Property | Type | Purpose |
|---|---|---|
| `Caption` | String | Label shown next to the checkbox |
| `Checked` | Boolean | True if checked, False if not |

```pascal
// Check if checked
IF chkNewsletter.Checked THEN
  ShowMessage('You will receive our newsletter.');

// Set checked state in code
chkRemember.Checked := True;

// Read in logic
IF chkDiscount.Checked THEN
  rPrice := rPrice * 0.9;   // 10% discount
```

---

## TRadioButton

Used in groups — only one in a group can be selected at a time.

| Property | Type | Purpose |
|---|---|---|
| `Caption` | String | Label next to the radio button |
| `Checked` | Boolean | True if this button is selected |

```pascal
IF rdbMale.Checked THEN
  sGender := 'M'
ELSE IF rdbFemale.Checked THEN
  sGender := 'F';
```

> [!TIP] Group Radio Buttons with TGroupBox
> Place radio buttons inside a TGroupBox to ensure only ONE within that group can be selected. Without a GroupBox, all radio buttons on the form compete.

---

## TComboBox

A dropdown list that also allows text input. User selects from a list.

| Property | Type | Purpose |
|---|---|---|
| `Items` | TStrings | List of dropdown options |
| `Text` | String | Currently selected/typed text |
| `ItemIndex` | Integer | Index of selected item (−1 if none) |
| `Style` | TComboBoxStyle | `csDropDown` (editable) vs `csDropDownList` (list only) |

```pascal
// Read selected item
sSubject := cmbSubject.Text;

// Get index (0-based)
iIndex := cmbGrade.ItemIndex;   // -1 if nothing selected

// Check if something selected
IF cmbSubject.ItemIndex = -1 THEN
  ShowMessage('Please select a subject.')
ELSE
  sSubject := cmbSubject.Text;

// Add items in code
cmbGrade.Items.Add('Grade 10');
cmbGrade.Items.Add('Grade 11');
cmbGrade.Items.Add('Grade 12');

// Set selected item
cmbGrade.ItemIndex := 0;   // select first item
```

---

## TListBox

Shows a scrollable list; user can select one or more items.

| Property | Type | Purpose |
|---|---|---|
| `Items` | TStrings | All items in the list |
| `ItemIndex` | Integer | Index of selected item |
| `MultiSelect` | Boolean | Allow selecting multiple items |

```pascal
// Add items
lstNames.Items.Add('Alice');
lstNames.Items.Add('Bob');

// Read selected item
IF lstNames.ItemIndex >= 0 THEN
  sSelected := lstNames.Items[lstNames.ItemIndex];

// Clear list
lstNames.Items.Clear;

// Count items
iCount := lstNames.Items.Count;
```

---

## TForm

The main window itself has properties you can set:

| Property | Purpose |
|---|---|
| `Caption` | Title bar text |
| `Color` | Background colour |
| `WindowState` | wsNormal, wsMaximized, wsMinimized |

```pascal
// Set in FormCreate or on button click
Form1.Caption := 'IT Gateway — Student App';
Form1.Color := clWhite;
```

**Key event:** `OnCreate` — runs when the form first loads

```pascal
procedure TForm1.FormCreate(Sender: TObject);
begin
  Randomize;              // seed random number generator
  edtName.SetFocus;       // focus first input
  lblStatus.Caption := ''; // clear any default caption
end;
```

---

## Reading Component Properties vs Variables

| Source | Access |
|---|---|
| Edit box text | `edtName.Text` (always String) |
| Label text | `lblResult.Caption` |
| Checkbox state | `chkBox.Checked` (Boolean) |
| Combobox selection | `cmbGrade.Text` or `cmbGrade.ItemIndex` |
| RichEdit lines | `redOutput.Lines.Add(...)` |

**Always convert types when reading from edit boxes:**
```pascal
iScore := StrToInt(edtScore.Text);    // String → Integer
rPrice := StrToFloat(edtPrice.Text);  // String → Real
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Wrong naming prefix** — `edtScore` not `Score` or `txtScore`
> 2. **Reading `.Text` on a Label** — Labels have `.Caption`, not `.Text`
> 3. **Not converting types** — `edtScore.Text` is always a String; use `StrToInt`
> 4. **`Lines` index is 0-based** — first line is `Lines[0]`, not `Lines[1]`
> 5. **Not checking `ItemIndex = -1`** — accessing `.Text` on unselected ComboBox still works, but returns empty string; check index first for validation
