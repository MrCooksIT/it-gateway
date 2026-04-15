# Object-Oriented Programming Principles

Procedural programming — writing one procedure after another — works for small programs. As programs grow, it becomes unmanageable. Object-Oriented Programming (OOP) organises code around **objects** that model real-world entities, making large programs easier to design, maintain, and extend.

> [!NOTE] Grade 11+
> OOP concepts are introduced theoretically in Grade 11 and implemented in Delphi (practical). Grade 12 extends with destructors, accessors/mutators, and more complex class design.

---

## The Core Idea

Instead of writing:
```
procedure CalculateStudentAverage
procedure PrintStudentReport
procedure UpdateStudentMark
```

OOP groups related data and behaviour into a **class**:
```
CLASS: Student
  Data:    name, marks, grade
  Methods: calculateAverage(), printReport(), updateMark()
```

An **object** is a specific instance of a class — a real student in memory.

---

## Key OOP Concepts

### Class

A **class** is a **blueprint** or template that defines:
- What **data** (attributes/fields) objects of this type will hold
- What **methods** (procedures/functions) objects of this type can perform

A class is not an object — it's the description of what an object will be.

```pascal
type
  TStudent = class
  private
    sName  : String;
    iMark  : Integer;
    iGrade : Integer;
  public
    constructor Create(sN : String; iG : Integer);
    function GetName  : String;
    function GetMark  : Integer;
    procedure SetMark(iM : Integer);
    function CalculateAverage : Real;
  end;
```

### Object

An **object** is a specific **instance** (occurrence) of a class — it has actual values.

```pascal
var
  oStudent1 : TStudent;
  oStudent2 : TStudent;
begin
  oStudent1 := TStudent.Create('Alice', 11);   // object 1
  oStudent2 := TStudent.Create('Bob', 12);     // object 2
  // Two separate objects from the same blueprint
end;
```

### Attribute (Field / Property)

An **attribute** is a variable that belongs to a class — it stores data about each object.

```
TStudent attributes:
  sName   → 'Alice'  (for oStudent1)
  iMark   → 87
  iGrade  → 11
```

### Method

A **method** is a procedure or function that belongs to a class — it defines what objects of that type can do.

```
TStudent methods:
  Create()           — initialises the object
  GetName()          — returns the student's name
  CalculateAverage() — computes average from stored marks
```

### Constructor

A **constructor** is a special method called when an object is created. It initialises the object's attributes to valid starting values.

```pascal
constructor TStudent.Create(sN : String; iG : Integer);
begin
  sName  := sN;
  iGrade := iG;
  iMark  := 0;  // default
end;
```

Called with: `oStudent := TStudent.Create('Alice', 11);`

### Destructor

A **destructor** is called when an object is destroyed — it cleans up resources (frees memory).

```pascal
destructor TStudent.Destroy; override;
begin
  // free any sub-objects if needed
  inherited;
end;
```

In Delphi, you call `oStudent.Free` to destroy an object (which internally calls the destructor).

---

## The Four Pillars of OOP

### 1. Encapsulation

**Encapsulation** means bundling data and the methods that operate on it inside a class, and **hiding** the internal details from the outside world.

- Attributes are declared `private` — cannot be accessed directly from outside the class
- Methods are declared `public` — provide controlled access to the data

```pascal
type
  TBankAccount = class
  private                        // hidden — no direct access
    rBalance : Real;
  public                         // accessible
    constructor Create(rInitial : Real);
    function GetBalance : Real;  // read-only access
    procedure Deposit(rAmount : Real);
    function Withdraw(rAmount : Real) : Boolean;
  end;
```

**Why encapsulation?**
- Protects data from accidental modification
- Code that uses the class doesn't need to know HOW it works internally
- Change the internal implementation without breaking other code

### 2. Inheritance

**Inheritance** allows a new class (child/derived class) to inherit attributes and methods from an existing class (parent/base class), and then add or modify its own.

```
TAnimal (parent)
  attributes: name, age
  methods: eat(), sleep(), breathe()
    ↓
TDog (child — inherits from TAnimal)
  adds: breed
  adds: bark(), fetch()
  all TAnimal methods also available
```

**Benefits:**
- Reuse existing code — no duplication
- Extend functionality without modifying the original class
- Represents "is-a" relationships: a Dog IS-A Animal

```pascal
type
  TAnimal = class
  private
    sName : String;
  public
    constructor Create(sN : String);
    procedure Eat;
    procedure Sleep;
  end;

  TDog = class(TAnimal)    // TDog inherits from TAnimal
  private
    sBreed : String;
  public
    constructor Create(sN, sB : String);
    procedure Bark;
    procedure Fetch;
  end;
```

### 3. Polymorphism

**Polymorphism** (Greek: "many forms") means the same method name can behave differently depending on which class is calling it.

```
TShape.Draw()       → draws a generic shape
TCircle.Draw()      → draws a circle (overrides parent)
TRectangle.Draw()   → draws a rectangle (overrides parent)
```

All three respond to `Draw()`, but each does it differently. The correct version runs based on the actual object type at runtime.

In Delphi, this is implemented with `virtual` and `override` keywords:

```pascal
type
  TShape = class
  public
    procedure Draw; virtual;   // can be overridden
  end;

  TCircle = class(TShape)
  public
    procedure Draw; override;  // replaces parent's Draw
  end;
```

### 4. Abstraction

**Abstraction** means hiding complexity and showing only what's necessary. A class exposes a simple interface; the user doesn't need to know the implementation details.

- `oStudent.CalculateAverage` — you call it and get a result; you don't see the calculation
- `oAccount.Withdraw(500)` — you call it; you don't see the balance checking logic inside

---

## Accessors and Mutators (Getters and Setters)

Since attributes are private, you access them through special methods:

- **Accessor (getter)**: Returns the value of a private attribute
- **Mutator (setter)**: Sets/changes the value of a private attribute (with validation)

```pascal
// Accessor — just returns the value
function TStudent.GetName : String;
begin
  Result := sName;
end;

// Accessor
function TStudent.GetMark : Integer;
begin
  Result := iMark;
end;

// Mutator — can validate before setting
procedure TStudent.SetMark(iM : Integer);
begin
  IF (iM >= 0) AND (iM <= 100) THEN
    iMark := iM
  ELSE
    ShowMessage('Invalid mark — must be 0 to 100');
end;
```

---

## Complete Delphi Class Example

```pascal
// ─── Declaration ───────────────────────────────────────────────────
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

    function GetLetterGrade : String;
    function HasPassed      : Boolean;
  end;

// ─── Implementation ────────────────────────────────────────────────
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

function TStudent.GetName : String;
begin Result := sName; end;

function TStudent.GetMark : Integer;
begin Result := iMark; end;

function TStudent.GetGrade : Integer;
begin Result := iGrade; end;

procedure TStudent.SetMark(iM : Integer);
begin
  IF (iM >= 0) AND (iM <= 100) THEN
    iMark := iM;
end;

function TStudent.HasPassed : Boolean;
begin
  Result := iMark >= 50;
end;

function TStudent.GetLetterGrade : String;
begin
  IF iMark >= 80 THEN      Result := 'A'
  ELSE IF iMark >= 70 THEN Result := 'B'
  ELSE IF iMark >= 60 THEN Result := 'C'
  ELSE IF iMark >= 50 THEN Result := 'D'
  ELSE                     Result := 'F';
end;

// ─── Using the class ───────────────────────────────────────────────
procedure TForm1.btnCreateClick(Sender: TObject);
var
  oStudent : TStudent;
begin
  oStudent := TStudent.Create('Alice', 11, 87);

  redOutput.Lines.Clear;
  redOutput.Lines.Add('Name:   ' + oStudent.GetName);
  redOutput.Lines.Add('Grade:  ' + IntToStr(oStudent.GetGrade));
  redOutput.Lines.Add('Mark:   ' + IntToStr(oStudent.GetMark));
  redOutput.Lines.Add('Letter: ' + oStudent.GetLetterGrade);
  IF oStudent.HasPassed THEN
    redOutput.Lines.Add('Status: Passed')
  ELSE
    redOutput.Lines.Add('Status: Failed');

  oStudent.Free;   // destroy the object
end;
```

---

## OOP vs Procedural — Summary

| Aspect | Procedural | OOP |
|---|---|---|
| **Organisation** | Functions and procedures | Classes and objects |
| **Data** | Separate from functions | Bundled with methods inside class |
| **Reuse** | Copy/paste procedures | Inheritance |
| **Complexity management** | Difficult for large programs | Encapsulation hides complexity |
| **Modelling real world** | Awkward | Natural (Student, Account, Car) |

---

## Key Terms

| Term | Definition |
|---|---|
| **Class** | Blueprint defining attributes and methods of an object type |
| **Object** | A specific instance of a class |
| **Attribute** | Variable belonging to a class (data the object holds) |
| **Method** | Procedure or function belonging to a class |
| **Constructor** | Special method that initialises an object when created |
| **Destructor** | Special method that cleans up an object when destroyed |
| **Encapsulation** | Hiding internal data; exposing only a public interface |
| **Inheritance** | Child class inherits attributes and methods from parent |
| **Polymorphism** | Same method name behaves differently in different classes |
| **Abstraction** | Hiding complexity; showing only necessary interface |
| **Accessor** | Method that returns the value of a private attribute (getter) |
| **Mutator** | Method that changes the value of a private attribute (setter) |
| **Private** | Attribute/method accessible only within the class |
| **Public** | Attribute/method accessible from outside the class |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Define encapsulation and explain its advantage"** — bundling data + methods in a class; advantage: protects data, hides implementation
>
> 2. **"What is the difference between a class and an object?"** — class = blueprint/template; object = specific instance created from the class
>
> 3. **"Explain inheritance with an example"** — child class inherits from parent; e.g. `TDog` inherits from `TAnimal` — gets all animal attributes/methods + adds its own
>
> 4. **"What is a constructor? What does it do?"** — special method called when object is created; initialises attributes to starting values
>
> 5. **"Why should attributes be declared as private?"** — encapsulation; prevents direct external access; controlled via accessors/mutators with validation
