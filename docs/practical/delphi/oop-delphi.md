# OOP in Delphi — Writing Classes

This page is the practical guide to implementing classes in Delphi. If you need the theory (what OOP is, why we use it), see the [OOP Principles](/theory/programming/oop-principles) page. Here we focus on the exact Delphi syntax used in Paper 1.

> [!NOTE] Grade 11+
> OOP implementation in Delphi is introduced in Grade 11. Grade 12 extends with destructors, more complex class designs, and arrays of objects.

---

## Class Structure in Delphi

Every class in Delphi has two parts:

1. **Declaration** — in the `type` section of the unit (usually in the same section as `TForm1`)
2. **Implementation** — the actual code for each method

```pascal
// ─── DECLARATION (at the top of the unit, in type section) ─────────
type
  TClassName = class
  private
    // private fields (attributes) — hidden from outside
    iValue  : Integer;
    sName   : String;
  public
    // public methods — accessible from outside
    constructor Create(iV : Integer; sN : String);
    destructor  Destroy; override;
    function  GetValue : Integer;
    function  GetName  : String;
    procedure SetValue(iV : Integer);
  end;

// ─── IMPLEMENTATION (below all event handlers) ──────────────────────
constructor TClassName.Create(iV : Integer; sN : String);
begin
  iValue := iV;
  sName  := sN;
end;

destructor TClassName.Destroy;
begin
  inherited;   // always call inherited in destructor
end;

function TClassName.GetValue : Integer;
begin
  Result := iValue;
end;

function TClassName.GetName : String;
begin
  Result := sName;
end;

procedure TClassName.SetValue(iV : Integer);
begin
  IF iV >= 0 THEN
    iValue := iV;
end;
```

---

## Step-by-Step: Building a Class

### Step 1 — Identify the class

What real-world entity are you modelling? What data does it hold? What can it do?

**Example:** A `TProduct` class for a shop:
- **Attributes**: product name, price, quantity in stock
- **Methods**: get/set each attribute, calculate total value, apply discount

### Step 2 — Write the declaration

```pascal
type
  TProduct = class
  private
    sName     : String;
    rPrice    : Real;
    iQuantity : Integer;
  public
    constructor Create(sN : String; rP : Real; iQ : Integer);
    destructor  Destroy; override;

    // Accessors (getters)
    function GetName     : String;
    function GetPrice    : Real;
    function GetQuantity : Integer;

    // Mutators (setters)
    procedure SetPrice(rP : Real);
    procedure SetQuantity(iQ : Integer);

    // Other methods
    function TotalValue    : Real;
    procedure ApplyDiscount(rPercent : Real);
    function ToString       : String;
  end;
```

### Step 3 — Write the implementations

```pascal
constructor TProduct.Create(sN : String; rP : Real; iQ : Integer);
begin
  sName     := sN;
  rPrice    := rP;
  iQuantity := iQ;
end;

destructor TProduct.Destroy;
begin
  inherited;
end;

// ─── Accessors ──────────────────────────────────────────────────────
function TProduct.GetName : String;
begin
  Result := sName;
end;

function TProduct.GetPrice : Real;
begin
  Result := rPrice;
end;

function TProduct.GetQuantity : Integer;
begin
  Result := iQuantity;
end;

// ─── Mutators ───────────────────────────────────────────────────────
procedure TProduct.SetPrice(rP : Real);
begin
  IF rP >= 0 THEN
    rPrice := rP;
end;

procedure TProduct.SetQuantity(iQ : Integer);
begin
  IF iQ >= 0 THEN
    iQuantity := iQ;
end;

// ─── Other methods ──────────────────────────────────────────────────
function TProduct.TotalValue : Real;
begin
  Result := rPrice * iQuantity;
end;

procedure TProduct.ApplyDiscount(rPercent : Real);
begin
  IF (rPercent > 0) AND (rPercent <= 100) THEN
    rPrice := rPrice * (1 - rPercent / 100);
end;

function TProduct.ToString : String;
begin
  Result := sName + ' | R' + FloatToStrF(rPrice, ffFixed, 8, 2) +
            ' | Qty: ' + IntToStr(iQuantity);
end;
```

### Step 4 — Create and use objects

```pascal
procedure TForm1.btnCreateClick(Sender: TObject);
var
  oProduct : TProduct;
begin
  // Create an object using the constructor
  oProduct := TProduct.Create('Laptop', 12999.99, 15);

  // Use methods on the object
  redOutput.Lines.Clear;
  redOutput.Lines.Add(oProduct.ToString);
  redOutput.Lines.Add('Total value: R' + FloatToStrF(oProduct.TotalValue, ffFixed, 8, 2));

  // Apply a 10% discount
  oProduct.ApplyDiscount(10);
  redOutput.Lines.Add('After 10% discount: R' + FloatToStrF(oProduct.GetPrice, ffFixed, 8, 2));

  // Always free the object when done
  oProduct.Free;
end;
```

---

## Array of Objects

In Grade 12, you may need to store multiple objects in an array.

```pascal
const
  MAX = 5;
var
  aProducts : array[1..MAX] of TProduct;
  i         : Integer;

// Create objects
FOR i := 1 TO MAX DO
  aProducts[i] := TProduct.Create('Product ' + IntToStr(i), i * 10.0, i * 5);

// Use them
FOR i := 1 TO MAX DO
  redOutput.Lines.Add(aProducts[i].ToString);

// Free them all
FOR i := 1 TO MAX DO
  aProducts[i].Free;
```

---

## Common Patterns

### Display all attributes

```pascal
function TProduct.DisplayInfo : String;
begin
  Result := 'Name: '  + sName + sLineBreak +
            'Price: R' + FloatToStrF(rPrice, ffFixed, 8, 2) + sLineBreak +
            'Qty: '   + IntToStr(iQuantity);
end;
```

### Validation in mutator

```pascal
procedure TProduct.SetQuantity(iQ : Integer);
begin
  IF iQ >= 0 THEN
    iQuantity := iQ
  ELSE
    ShowMessage('Quantity cannot be negative.');
end;
```

### Boolean method (check condition)

```pascal
function TProduct.IsInStock : Boolean;
begin
  Result := iQuantity > 0;
end;

// Used as:
IF oProduct.IsInStock THEN
  lblStatus.Caption := 'Available'
ELSE
  lblStatus.Caption := 'Out of stock';
```

---

## Complete Worked Example — Student Class

This is the type of question that appears in Paper 1 OOP questions:

```pascal
// ─── TYPE DECLARATION ───────────────────────────────────────────────
type
  TStudent = class
  private
    sName  : String;
    iMark  : Integer;
    iGrade : Integer;
  public
    constructor Create(sN : String; iG, iM : Integer);
    destructor  Destroy; override;

    function GetName   : String;
    function GetMark   : Integer;
    function GetGrade  : Integer;
    procedure SetMark(iM : Integer);

    function LetterGrade : Char;
    function HasPassed   : Boolean;
    function Describe    : String;
  end;

// ─── IMPLEMENTATIONS ────────────────────────────────────────────────
constructor TStudent.Create(sN : String; iG, iM : Integer);
begin
  sName  := sN;
  iGrade := iG;
  iMark  := iM;
end;

destructor TStudent.Destroy;
begin
  inherited;
end;

function TStudent.GetName  : String;  begin Result := sName;  end;
function TStudent.GetMark  : Integer; begin Result := iMark;  end;
function TStudent.GetGrade : Integer; begin Result := iGrade; end;

procedure TStudent.SetMark(iM : Integer);
begin
  IF (iM >= 0) AND (iM <= 100) THEN
    iMark := iM;
end;

function TStudent.LetterGrade : Char;
begin
  IF iMark >= 80 THEN      Result := 'A'
  ELSE IF iMark >= 70 THEN Result := 'B'
  ELSE IF iMark >= 60 THEN Result := 'C'
  ELSE IF iMark >= 50 THEN Result := 'D'
  ELSE                     Result := 'F';
end;

function TStudent.HasPassed : Boolean;
begin
  Result := iMark >= 50;
end;

function TStudent.Describe : String;
begin
  Result := sName + ' (Gr ' + IntToStr(iGrade) + '): ' +
            IntToStr(iMark) + '% — ' + LetterGrade;
end;

// ─── EVENT HANDLER ──────────────────────────────────────────────────
procedure TForm1.btnStudentClick(Sender: TObject);
var
  oS : TStudent;
begin
  oS := TStudent.Create('Finn', 11, 87);

  redOutput.Lines.Clear;
  redOutput.Lines.Add(oS.Describe);

  IF oS.HasPassed THEN
    redOutput.Lines.Add('Status: PASSED')
  ELSE
    redOutput.Lines.Add('Status: FAILED');

  // Update mark
  oS.SetMark(92);
  redOutput.Lines.Add('Updated mark: ' + IntToStr(oS.GetMark));

  oS.Free;
end;
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Not calling `inherited` in destructor** — always `inherited` in `Destroy`
> 2. **Forgetting `oObject.Free`** — memory leak; always free objects you create
> 3. **Accessing private field directly** — `oStudent.sName` from outside the class is a compiler error; use `oStudent.GetName`
> 4. **Missing `override` in destructor** — `destructor Destroy; override;` — the `override` is required
> 5. **Creating object without assigning** — `var oS : TStudent;` then using `oS.GetName` without `oS := TStudent.Create(...)` first — access violation
> 6. **Forgetting to declare in `private` section of TForm1** — the class declaration goes in the `type` section, not inside TForm1

---

## Practice Exercises

**Exercise 1 — Vehicle class**

Design and implement a `TVehicle` class with:
- Private attributes: registration number (String), speed (Integer), fuel level (Real)
- Constructor: takes registration and initial fuel
- Methods: GetReg, GetSpeed, GetFuel, Accelerate(iAmount), Brake(iAmount), Refuel(rAmount)
- Accelerate should not allow speed above 200; Brake should not allow speed below 0

<details>
<summary>Show solution structure</summary>

```pascal
type
  TVehicle = class
  private
    sReg   : String;
    iSpeed : Integer;
    rFuel  : Real;
  public
    constructor Create(sR : String; rF : Real);
    destructor  Destroy; override;
    function  GetReg   : String;
    function  GetSpeed : Integer;
    function  GetFuel  : Real;
    procedure Accelerate(iAmount : Integer);
    procedure Brake(iAmount : Integer);
    procedure Refuel(rAmount : Real);
  end;

constructor TVehicle.Create(sR : String; rF : Real);
begin
  sReg   := sR;
  iSpeed := 0;
  rFuel  := rF;
end;

destructor TVehicle.Destroy;
begin inherited; end;

function TVehicle.GetReg   : String;  begin Result := sReg;   end;
function TVehicle.GetSpeed : Integer; begin Result := iSpeed; end;
function TVehicle.GetFuel  : Real;    begin Result := rFuel;  end;

procedure TVehicle.Accelerate(iAmount : Integer);
begin
  iSpeed := iSpeed + iAmount;
  IF iSpeed > 200 THEN iSpeed := 200;
end;

procedure TVehicle.Brake(iAmount : Integer);
begin
  iSpeed := iSpeed - iAmount;
  IF iSpeed < 0 THEN iSpeed := 0;
end;

procedure TVehicle.Refuel(rAmount : Real);
begin
  IF rAmount > 0 THEN
    rFuel := rFuel + rAmount;
end;
```
</details>

---

> [!TIP] Exam Tip
> In Paper 1 OOP questions, you are usually given a partial class and asked to add methods, OR asked to write a complete class from a description. The marks go to: correct `constructor` with all parameters, correct accessor/mutator methods, correct return types, and validation logic in mutators. Always declare `override` on the destructor and always call `inherited` inside it.
