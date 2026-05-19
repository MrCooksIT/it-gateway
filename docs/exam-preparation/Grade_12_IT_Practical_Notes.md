# Grade 12 Information Technology — Practical Programming Reference

*A topic-by-topic reference for Delphi programming concepts and syntax, building on the Grade 10 and 11 references.*

These notes assume the Grade 10 and 11 material is already known: variables and types, type conversions, components, the three loops, arrays (including parallel arrays), text files, modular programming with procedures and functions, sorting and filtering. Each section below begins with a brief **Recap** of any earlier material it depends on before introducing the new Grade 12 concepts.

A **cheat sheet appendix** at the end of the document summarises every new pattern.

---

# SECTION 1: OBJECT-ORIENTED PROGRAMMING

The Grade 11 reference introduced **modular programming**: breaking code into procedures and functions. **Object-oriented programming (OOP)** takes the idea further — group related data and the procedures that work on that data into a single named unit called a **class**, then make many independent **objects** from the class.

## 1.1 Key terminology

| Term | Meaning |
|---|---|
| **Class** | The blueprint or template — describes what data and behaviour every object of this kind will have. |
| **Object** | An actual instance of a class — created at run time, with its own values. |
| **Attribute** (also called *field*) | A variable that belongs to the class. Each object has its own copy. |
| **Method** | A procedure or function that belongs to the class. Methods can read and change the object's attributes. |
| **Constructor** | A special method (always called `Create`) that runs when an object is created, to initialise its attributes. |
| **Encapsulation** | Hiding the attributes inside the class and only allowing outside code to access them through methods. |

## 1.2 Naming conventions

* **Classes** start with `T`: `TPerson`, `TStudent`, `TVehicle`.
* **Attributes** start with `f` (for "field"): `fName`, `fAge`, `fPrice`.
* **Method names** describe an action: `getName`, `setAge`, `calculateTotal`, `processOrder`, `toString`.

## 1.3 The two-file structure

OOP programs are usually split into two files:

* The **class file** (e.g. `Person_U.pas`) — contains the class definition.
* The **main form unit** (e.g. `Question_U.pas`) — contains the form code that creates and uses objects.

The main form unit must add the class unit to its `uses` clause:

```pascal
uses
   Classes, SysUtils, …, Person_U;        // import the class
```

## 1.4 The skeleton of a class file

```pascal
unit Person_U;

interface

type
   TPerson = class
      private
         fName : String;
         fAge  : Integer;
      public
         constructor Create(sName : String; iAge : Integer);
         function getName : String;
         function getAge : Integer;
         procedure setAge(iNewAge : Integer);
         function toString : String;
   end;

implementation

constructor TPerson.Create(sName : String; iAge : Integer);
begin
   fName := sName;
   fAge  := iAge;
end;

function TPerson.getName : String;
begin
   Result := fName;
end;

function TPerson.getAge : Integer;
begin
   Result := fAge;
end;

procedure TPerson.setAge(iNewAge : Integer);
begin
   fAge := iNewAge;
end;

function TPerson.toString : String;
begin
   Result := fName + ' (' + IntToStr(fAge) + ')';
end;

end.
```

### The pieces explained

* **`interface`** — the public face of the file: what other units can see.
* **`type … = class`** — declares a new class.
* **`private`** — these attributes can only be accessed by methods of this class. Outside code cannot read or write them directly.
* **`public`** — these methods can be called by outside code.
* **`implementation`** — the actual code of the methods.
* Each method's full definition starts with the class name and a dot: `TPerson.Create`, `TPerson.getName`. This tells Delphi which class the method belongs to.

## 1.5 Categories of methods

OOP methods generally fall into a few standard categories.

### Constructor

Runs once when an object is created. Its job is to set up the initial values of the attributes — usually from parameters passed in.

```pascal
constructor TPerson.Create(sName : String; iAge : Integer);
begin
   fName := sName;
   fAge  := iAge;
end;
```

The keyword is `constructor`, not `function` or `procedure`. There is no return type. Inside, attributes are assigned from the parameters.

### Accessor methods (getters)

Read-only access to a private attribute. Conventionally named `getXxx`.

```pascal
function TPerson.getName : String;
begin
   Result := fName;
end;
```

The function returns one value — usually the attribute itself, untouched. This is the only way outside code can read a private attribute.

### Mutator methods (setters)

Change a private attribute from outside. Conventionally named `setXxx`. They receive the new value as a parameter.

```pascal
procedure TPerson.setAge(iNewAge : Integer);
begin
   fAge := iNewAge;
end;
```

A setter could also include validation:

```pascal
procedure TPerson.setAge(iNewAge : Integer);
begin
   if (iNewAge >= 0) AND (iNewAge <= 120) then
      fAge := iNewAge;
   // otherwise ignore the change
end;
```

### Auxiliary methods

The methods that perform the actual business logic — calculations, transformations, decisions specific to the class. These are the methods that make the class useful.

```pascal
function TPerson.IsAdult : Boolean;
begin
   Result := (fAge >= 18);
end;
```

### The toString method

A method that returns a single string describing the whole object. Used by display code to avoid hard-coding the format in many places.

```pascal
function TPerson.toString : String;
begin
   Result := fName + ' (' + IntToStr(fAge) + ')';
end;
```

If the format ever changes, only `toString` needs updating — every place that displays an object benefits from the change automatically.

## 1.6 Using a class from the main form

### Declaring an object variable

```pascal
var
   objPerson : TPerson;
```

This declares the variable but does not yet create an object. Until `Create` is called, the variable is **nil** (empty).

### Instantiating an object — calling Create

```pascal
objPerson := TPerson.Create('Sipho', 17);
```

Important syntax: it is `TPerson.Create(...)` — the *class name* followed by a dot and `Create`. The constructor returns the new object, which is assigned to the variable.

### Calling methods on the object

Methods are called with dot notation — the object variable, a dot, then the method name:

```pascal
sName := objPerson.getName;
objPerson.setAge(18);
lblOut.Caption := objPerson.toString;
if objPerson.IsAdult then
   …
```

## 1.7 UML class diagrams

A **UML class diagram** is a visual blueprint of a class, often used in exam questions. It has three sections from top to bottom:

```
┌──────────────────────────────┐
│ TPerson                      │
├──────────────────────────────┤
│ - fName : String             │
│ - fAge  : Integer            │
├──────────────────────────────┤
│ + Create(sName: String;      │
│          iAge: Integer)      │
│ + getName : String           │
│ + setAge(iNewAge: Integer)   │
│ + toString : String          │
└──────────────────────────────┘
```

* **Top** — the class name.
* **Middle** — attributes, each with its type.
* **Bottom** — methods, each with parameters and (for functions) the return type.
* **Minus signs** `-` indicate **private** members.
* **Plus signs** `+` indicate **public** members.

To translate a UML diagram into a class file: take each attribute → put it under `private`, prefix with `f`. Take each method → put it under `public`, repeat in `implementation`.

## 1.8 Mapping a UI choice to an internal value

A frequent task is converting a user's choice (a RadioGroup index or a CheckBox state) into an internal representation, then calling a setter:

```pascal
case rgpCategory.ItemIndex of
   0 : objItem.setCategory('A');
   1 : objItem.setCategory('B');
   2 : objItem.setCategory('C');
end;
```

The mapping (`0 → 'A'`, etc.) is encoded in the `case` — the class itself does not need to know anything about the RadioGroup.

## 1.9 Working with multiple objects

A class can be instantiated many times — each call to `Create` returns a fresh object with its own attributes:

```pascal
objPerson1 := TPerson.Create('Sipho', 17);
objPerson2 := TPerson.Create('Anna', 19);
// objPerson1 and objPerson2 are independent — changes to one do not affect the other.
```

Often a program holds many objects in an **array of objects**:

```pascal
var
   arrPeople : array [1..100] of TPerson;

// Create each object
for i := 1 to iCount do
   arrPeople[i] := TPerson.Create(arrNames[i], arrAges[i]);

// Use them
for i := 1 to iCount do
   memOut.Lines.Add(arrPeople[i].toString);
```

---

# SECTION 2: DATABASES AND SQL

A **database** stores related data in **tables**. Each table has named columns (fields) and rows (records). A **Database Management System (DBMS)** like Microsoft Access or MySQL provides ways to add, read, update and remove the data.

A Delphi program connects to a database, sends queries, and displays or processes the results.

## 2.1 Database terminology

| Term | Meaning |
|---|---|
| **Table** | A collection of records, each with the same set of fields |
| **Record** (row) | One entity — e.g. one person, one product |
| **Field** (column) | One named attribute that every record has |
| **Primary key** | A field whose value uniquely identifies each record |
| **Foreign key** | A field that refers to the primary key of another table — creates a relationship |
| **Query** | A statement that asks the database to do something |
| **SQL** | Structured Query Language — the standard language for querying databases |

## 2.2 SQL — the four basic verbs

| Verb | Purpose |
|---|---|
| `SELECT` | Read data — return rows matching a query |
| `INSERT` | Add a new record |
| `UPDATE` | Change values in existing records |
| `DELETE` | Remove records |

For Paper 1 most of the SQL work focuses on `SELECT`, plus some `UPDATE`.

## 2.3 SELECT — the most important statement

The general form:

```sql
SELECT <fields>
FROM <tables>
WHERE <condition>
GROUP BY <field>
ORDER BY <field> [ASC | DESC];
```

Every part except `SELECT` and `FROM` is optional. The order of the clauses is fixed.

### Selecting fields

```sql
SELECT *               -- every field
SELECT FirstName       -- one field
SELECT FirstName, Surname, Age      -- several fields
```

### Filtering with WHERE

`WHERE` filters which records are included. Multiple conditions can be combined with `AND`, `OR`, `NOT`:

```sql
SELECT *
FROM tblStudents
WHERE Grade = 11;

SELECT *
FROM tblStudents
WHERE (Grade = 11) AND (Age >= 16);

SELECT *
FROM tblProducts
WHERE Price < 100 OR Price > 500;
```

Field comparison operators are the same as Pascal except equality is `=` (single equals):

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `<>` | Not equal |
| `<`, `>`, `<=`, `>=` | Comparisons |
| `LIKE` | Pattern match — `%` is any characters, `?` (or `_`) is one character |
| `IN (..., ..., ...)` | Value is one of a list |
| `BETWEEN x AND y` | Value is between x and y (inclusive) |
| `IS NULL`, `IS NOT NULL` | Field has no value / has a value |

### Ordering results with ORDER BY

```sql
SELECT *
FROM tblStudents
ORDER BY Surname;                       -- ascending by default

SELECT *
FROM tblStudents
ORDER BY Age DESC;                      -- descending

SELECT *
FROM tblStudents
ORDER BY Grade DESC, Surname ASC;       -- multiple keys
```

### Removing duplicates with DISTINCT

When you only want each unique value once:

```sql
SELECT DISTINCT Country
FROM tblStudents;
```

Without `DISTINCT`, "South Africa" would appear once for every student from South Africa.

### Counting and grouping with COUNT and GROUP BY

`COUNT(*)` returns the number of rows. Combined with `GROUP BY`, it counts how many rows fall into each group:

```sql
SELECT Grade, COUNT(*) AS NumberOfStudents
FROM tblStudents
GROUP BY Grade;
```

This produces one output row per unique Grade, with the count alongside. The `AS` keyword renames the calculated column.

Other aggregate functions: `SUM`, `AVG`, `MIN`, `MAX`. All work with `GROUP BY`:

```sql
SELECT Category, AVG(Price) AS AveragePrice
FROM tblProducts
GROUP BY Category;
```

### Joining tables — combining data from two tables

When data is split across two tables linked by a foreign key, both tables must be queried together. The older "WHERE-join" style (preferred by CAPS):

```sql
SELECT tblStudents.Name, tblClasses.ClassName
FROM   tblStudents, tblClasses
WHERE  tblStudents.ClassID = tblClasses.ClassID;
```

* List both tables in `FROM`.
* The `WHERE` clause includes the **join condition** — `tableA.fkField = tableB.pkField`. Without it the query returns every row of one table paired with every row of the other (often millions of nonsense rows).
* Additional `WHERE` conditions can be added with `AND`.

When a field name appears in more than one table (like `ClassID` above), prefix it with the table name (`tblStudents.ClassID`) to remove ambiguity.

## 2.4 Building SQL dynamically from a Delphi value

When the SQL must depend on something the user chose (e.g. a category from a combo box), the SQL string is built by concatenation:

```pascal
sSQL := 'SELECT * '
      + 'FROM tblProducts '
      + 'WHERE Category LIKE "' + sUserChoice + '"';
```

Important traps:

* **Each line must end with a space inside the quote** (`'SELECT * '` not `'SELECT *'`), otherwise words run together — `'FROM tblProducts'` would become `'tblProductsWHERE'`.
* The inserted value usually needs to be surrounded by quotes inside the SQL — the pattern is `'…"' + sValue + '"…'`. Single quotes outside, double quotes inside (or escaped single quotes).
* The data type matters — numbers are inserted without quotes; strings need quotes around them.

## 2.5 UPDATE — changing existing records

```sql
UPDATE <table>
SET <field> = <newValue>
WHERE <condition>;
```

Examples:

```sql
UPDATE tblStudents
SET    Grade = 12
WHERE  StudentID = 105;

UPDATE tblProducts
SET    Price = Price * 1.10                  -- 10% increase
WHERE  Category = 'Books';
```

**Critical**: always include a `WHERE` clause — without it, every row in the table is updated. Forgetting `WHERE` on an `UPDATE` is the most dangerous SQL mistake.

## 2.6 INSERT and DELETE

```sql
INSERT INTO tblStudents (Name, Grade, Age)
VALUES ('Sipho', 11, 17);

DELETE FROM tblStudents
WHERE StudentID = 42;
```

Same warning as `UPDATE`: a `DELETE` without `WHERE` removes every row.

## 2.7 Manipulating a database with Delphi code (no SQL)

When SQL is not allowed, the same operations can be done in Delphi code using the **TADOTable** wrapper that represents a table.

### Navigation properties and methods

| Member | Purpose |
|---|---|
| `tbl.First` | Move to the first record |
| `tbl.Last` | Move to the last record |
| `tbl.Next` | Move to the next record |
| `tbl.Prior` | Move to the previous record |
| `tbl.EOF` | True once you have moved past the last record |
| `tbl.BOF` | True once you have moved before the first record |
| `tbl['FieldName']` | Read or write the field in the **current** record |
| `tbl.FieldByName('FieldName').AsString` (or `.AsInteger`, `.AsFloat`, …) | Alternative way to read with explicit type |

### The walk-every-record pattern

```pascal
tbl.First;
while not tbl.EOF do
   begin
      // … do something with the current record …
      // tbl['FieldName'] gives the current value
      tbl.Next;
   end;
```

### Editing one record

To change a value in the current record:

```pascal
tbl.Edit;                                 // put the table into edit mode
tbl['FieldName'] := <newValue>;
tbl.Post;                                  // save the change
```

The three steps must happen in this order: `Edit` first, then change, then `Post` to commit.

### Walking parent and child records (a "code-side join")

When two tables are related by a foreign key, the Delphi-code equivalent of an SQL join uses **nested loops**:

```pascal
tblParent.First;
while not tblParent.EOF do
   begin
      // … display or process this parent record …

      tblChild.First;                                  // RESET the inner cursor
      while not tblChild.EOF do
         begin
            if tblChild['ParentID'] = tblParent['ParentID'] then
               // … this child record belongs to this parent …
            tblChild.Next;
         end;

      tblParent.Next;
   end;
```

The critical step that is easy to forget is **`tblChild.First`** at the start of each outer iteration. Without it, the inner cursor starts wherever the previous iteration left off (probably at EOF), so the second parent's children are missed.

---

# SECTION 3: ADVANCED ARRAY AND FILE PROBLEM-SOLVING

## Recap (Grade 11)

Grade 11 covered parallel arrays, text files (the five-step pattern), delimited-line parsing with `Pos`/`Copy`/`Delete`, bubble sort with parallel-array swapping, and linear search. The principle of parallel arrays remains: *if you change the order of one, change the order of all*.

## 3.1 The "destructive" find-the-largest approach

When the task is to find the **top N** items in an array without fully sorting it, an alternative to a full sort is to repeat a "find the maximum" search N times and "mark" each maximum as already used so it does not win the next pass:

```pascal
for k := 1 to N do
   begin
      iMaxIndex := 1;
      for i := 2 to iCount do
         if arrValues[i] > arrValues[iMaxIndex] then
            iMaxIndex := i;
      // record / display arr[iMaxIndex]
      arrValues[iMaxIndex] := -1;                  // mark as already taken
   end;
```

The trick is to remember the **index** of the current maximum, not just the value, so other parallel arrays can be reached via the same index.

This approach is sometimes preferred when:

* You only need a few results from a much larger array.
* You do not want to permanently change the order of the arrays (although the "mark" does change one of them).
* You want simpler code that does not require swapping.

## 3.2 The "copy to a result array" approach

When the original data must stay intact, do not sort it in place — copy the matching items to a separate result array:

```pascal
iResultCount := 0;
for i := 1 to iCount do
   if <condition on arr[i]> then
      begin
         Inc(iResultCount);
         arrResult[iResultCount] := arr[i];
      end;

// arrResult now holds iResultCount items
```

## 3.3 Walking an array in reverse

When deleting from an array (or string) inside a loop, the loop must walk **backwards**, because deleting at position `i` shifts every later item one position towards the front — a forward loop would then skip the next item.

```pascal
for i := iCount downto 1 do
   if <delete condition> then
      begin
         // shift everything from i+1..iCount down by one
         for j := i to iCount - 1 do
            arr[j] := arr[j + 1];
         Dec(iCount);
      end;
```

## 3.4 Combining filter + count + accumulate in one pass

A single loop can perform several jobs at once — display each item, count items matching some condition, total something else:

```pascal
rTotal := 0;
iPremiumCount := 0;
for i := 1 to iCount do
   begin
      memOutput.Lines.Add(arrItems[i] + #9 + FloatToStrF(arrPrices[i], ffCurrency, 10, 2));
      rTotal := rTotal + arrPrices[i];
      if arrPrices[i] > 1000 then
         Inc(iPremiumCount);
   end;
rAverage := rTotal / iCount;
```

One pass through the data is more efficient than three separate loops and is good programming practice.

---

# SECTION 4: ADVANCED CONTROL FLOW — TRANSLATING COMPLEX LOGIC

## 4.1 Translating a flowchart into code (recap and expansion)

Grade 10 introduced the basic flowchart-to-code translation. At Grade 12, flowcharts can mix sequence, multiple decisions and loops in the same diagram. The same rules apply:

| Flowchart shape | Code |
|---|---|
| Rounded oval | `begin`/`end` of the routine |
| Parallelogram | Input from a component, or output to one |
| Rectangle | Assignment or calculation |
| Diamond | `IF…THEN…ELSE` |
| Diamond with a back-arrow | `WHILE` or `REPEAT` loop |

**Strategy for a complex flowchart**:

1. Identify the **outer structure** — is the whole diagram inside one IF, or one loop? Code that first.
2. Inside the structure, work top-to-bottom, translating one shape at a time.
3. Nest IFs and loops where the flowchart nests its arrows.

## 4.2 Nested decisions

When a decision depends on the outcome of another decision, the IFs nest:

```pascal
if <outer condition> then
   begin
      if <inner condition> then
         <stmt>
      else
         <stmt>;
   end
else
   <stmt>;
```

## 4.3 Useful built-in character tests

Pascal provides set tests for character classification:

| Test | Returns True for |
|---|---|
| `c IN ['0'..'9']` | A digit |
| `c IN ['A'..'Z']` | An upper-case letter |
| `c IN ['a'..'z']` | A lower-case letter |
| `c IN ['A'..'Z', 'a'..'z']` | Any letter |
| `c IN ['A', 'E', 'I', 'O', 'U']` | A vowel (upper case) |
| `c IN [' ', #9, #13]` | Whitespace |

These are much shorter than chains of comparisons and read clearly.

---

# SECTION 5: STRING-MANIPULATION TECHNIQUES

## Recap (Grade 11)

Grade 11 covered character-by-character loops to build a transformed string, character removal, and the palindrome / prime checks. Key tools: `Length`, `Copy`, `Pos`, `Delete`, `UpperCase`, `LowerCase`, `UpCase`.

## 5.1 The standard transform-each-character template

```pascal
function Transform(sInput : String) : String;
var
   i    : Integer;
   sOut : String;
begin
   sOut := '';
   for i := 1 to Length(sInput) do
      sOut := sOut + <transformed version of sInput[i]>;
   Result := sOut;
end;
```

Variations:

* Skip characters that don't match a rule (filter).
* Replace some characters with others (substitution).
* Convert characters based on a condition (case change, encryption).

## 5.2 Counting occurrences

```pascal
function CountChar(sInput : String; cTarget : Char) : Integer;
var
   i, iCount : Integer;
begin
   iCount := 0;
   for i := 1 to Length(sInput) do
      if sInput[i] = cTarget then
         Inc(iCount);
   Result := iCount;
end;
```

## 5.3 Extracting words from a sentence

A sentence can be split into words by repeatedly finding the next space:

```pascal
while Pos(' ', sLine) > 0 do
   begin
      iPos := Pos(' ', sLine);
      sWord := Copy(sLine, 1, iPos - 1);
      // process sWord
      Delete(sLine, 1, iPos);
   end;
// what is left after the last space is the final word
sWord := sLine;
```

---

# SECTION 6: PUTTING IT TOGETHER — DESIGN STRATEGIES

## 6.1 Breaking a hard problem into small steps

When a problem feels large, the strategy is the same every time:

1. **Identify the inputs** — what does the user supply? Where does it come from (Edits, SpinEdits, Combo boxes, files)?
2. **Identify the outputs** — what must be shown? Where (Labels, Memos, files, dialogs)?
3. **Sketch the processing** — what calculations or decisions go in between?
4. **Decide which parts are independent** — can any of the processing be a separate function? OOP method?
5. **Write the routines one at a time**, testing each on its own before connecting them.

This is the **divide-and-conquer** approach. A large procedure is much easier to write if it is broken into half a dozen smaller named pieces.

## 6.2 Choosing between OOP and procedural style

OOP is the right choice when:

* The program deals with **multiple instances** of similar things (many students, many items, many vehicles).
* Each "thing" has its own data **and** behaviour that belongs to it (a student calculates their own average; a fashion item calculates its own discount).
* The same operations are used in many places — the class centralises them.

A procedural style (just procedures and functions, no classes) is fine when:

* There is essentially one "thing" being worked with at a time.
* The operations are simple and not specific to one entity.

## 6.3 Defensive programming

A robust program checks for failure cases:

* Files might not exist — use `FileExists` before `Reset`.
* User input might be wrong — use validation and `Exit` on bad input.
* Arrays might be empty — check `iCount > 0` before dividing by it (to avoid division-by-zero).
* Numbers might overflow — be aware that an Integer in Delphi has a maximum value (about 2 billion); use `Int64` for very large numbers.
* `TryStrToInt` and `TryStrToFloat` return False instead of crashing when the input is not a valid number:

```pascal
if not TryStrToInt(edtNumber.Text, iValue) then
   begin
      ShowMessage('Please enter a valid number');
      Exit;
   end;
```

## 6.4 Choosing the right data structure

| Need | Use |
|---|---|
| A fixed-size list of similar things | Array |
| Several related lists where index N in each is "item N" | Parallel arrays |
| Multiple things each with several attributes that belong together | Array of objects (OOP) |
| Permanent storage between runs | Text file |
| Structured, multi-table data with relationships | Database |

---

# CHEAT SHEET APPENDIX

## A. Class definition skeleton

```pascal
unit ClassName_U;

interface
   type
      TClassName = class
         private
            fAttr1 : Type;
            fAttr2 : Type;
         public
            constructor Create(p1 : Type; p2 : Type);
            function getAttr1 : Type;
            procedure setAttr2(pNew : Type);
            function someAction : Type;
            function toString : String;
      end;

implementation

constructor TClassName.Create(p1 : Type; p2 : Type);
begin
   fAttr1 := p1;
   fAttr2 := p2;
end;

function TClassName.getAttr1 : Type;
begin
   Result := fAttr1;
end;

procedure TClassName.setAttr2(pNew : Type);
begin
   fAttr2 := pNew;
end;

function TClassName.someAction : Type;
begin
   Result := <something using fAttr1, fAttr2>;
end;

function TClassName.toString : String;
begin
   Result := <a formatted string>;
end;

end.
```

## B. Using an object

```pascal
var
   objX : TClassName;

// Create
objX := TClassName.Create(val1, val2);

// Read attribute (via accessor)
sValue := objX.getAttr1;

// Change attribute (via mutator)
objX.setAttr2(newValue);

// Call a method
rResult := objX.someAction;

// Display
lblOut.Caption := objX.toString;
```

## C. SQL templates

```sql
-- Select all
SELECT *
FROM <table>;

-- Select with filter and sort
SELECT <fields>
FROM <table>
WHERE <condition>
ORDER BY <field> [DESC];

-- Distinct values
SELECT DISTINCT <field>
FROM <table>;

-- Count per group
SELECT <field>, COUNT(*) AS <alias>
FROM <table>
WHERE <condition>
GROUP BY <field>;

-- Join two tables
SELECT a.<field>, b.<field>
FROM <tableA>, <tableB>
WHERE a.<fk> = b.<pk>
  AND <other conditions>;

-- Update
UPDATE <table>
SET <field> = <value>
WHERE <condition>;

-- Insert
INSERT INTO <table> (<fields>)
VALUES (<values>);

-- Delete
DELETE FROM <table>
WHERE <condition>;
```

## D. Dynamic SQL from Delphi

```pascal
sSQL := 'SELECT * '
      + 'FROM tblItems '
      + 'WHERE Category LIKE "' + sUserChoice + '"'
      + '  AND Price < ' + IntToStr(iMaxPrice);
```

Spaces at the ends of lines! Strings get quotes; numbers do not.

## E. Walking and editing records in code

```pascal
// Walk every record
tbl.First;
while not tbl.EOF do
   begin
      // tbl['FieldName'] is the current value
      tbl.Next;
   end;

// Edit a specific record
tbl.First;
while not tbl.EOF do
   begin
      if tbl['ID'] = targetID then
         begin
            tbl.Edit;
            tbl['FieldName'] := newValue;
            tbl.Post;
         end;
      tbl.Next;
   end;

// Nested walk for one-to-many
tblParent.First;
while not tblParent.EOF do
   begin
      tblChild.First;
      while not tblChild.EOF do
         begin
            if tblChild['ParentID'] = tblParent['ID'] then
               …
            tblChild.Next;
         end;
      tblParent.Next;
   end;
```

## F. Find top N in parallel arrays

```pascal
for k := 1 to N do
   begin
      iMaxIndex := 1;
      for i := 2 to iCount do
         if arrKey[i] > arrKey[iMaxIndex] then
            iMaxIndex := i;
      // record/display arrName[iMaxIndex] etc.
      arrKey[iMaxIndex] := -1;            // mark as used
   end;
```

## G. Useful Boolean character tests

| Test | Meaning |
|---|---|
| `c IN ['0'..'9']` | Digit |
| `c IN ['A'..'Z']` | Upper letter |
| `c IN ['a'..'z']` | Lower letter |
| `c IN ['A'..'Z', 'a'..'z']` | Any letter |
| `c IN ['A', 'E', 'I', 'O', 'U']` | Vowel |

## H. Safer string-to-number

```pascal
if TryStrToInt(s, i) then
   // succeeded, i now holds the value
else
   // input was not a valid integer
```

(Also `TryStrToFloat(s, r)` for Real.)

## I. Mark-saving habits (adds to Grade 10 and 11 lists)

* **Add the class unit to `uses`** in the main form unit.
* **Match constructor parameters to the question's order** exactly.
* **Use the question's attribute names** (e.g. `fItemName`, not `fName` if the question said `fItemName`).
* **End every SQL line with a space inside the quote** when building dynamic SQL.
* **Always include a WHERE clause** on `UPDATE` and `DELETE` unless you really mean to change every row.
* **Reset the inner cursor** (`tblChild.First`) at the start of every outer iteration in nested-loop joins.
* **Read the data type pages** carefully — using the correct primary-key field in joins is essential.

---

*End of Grade 12 Practical Programming Reference*
