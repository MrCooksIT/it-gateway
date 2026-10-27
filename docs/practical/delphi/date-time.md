---
title: Date and Time in Delphi (Grade 11)
description: TDateTime, Date, Now, FormatDateTime, date calculations and leap years in Delphi.
---

# Date and Time

::: info 📌 Key Points
- Delphi stores dates in the **TDateTime** type: a Real number where the **whole part is the day** and the **fraction is the time**.
- `Date` gives today's date, `Time` the current time, and `Now` both.
- `FormatDateTime` turns a date into any text format you need, for example `'dd/mm/yyyy'` or `'dddd, d mmmm yyyy'`.
- Because a date is a number, **subtracting two dates gives the number of days** between them.
:::

How many days has a dog been at the shelter? Is a learner 16 yet? Is 2028 a leap year? What date is 30 days from today? These questions come up in almost every real program, and Delphi answers each of them with one or two built-in functions.

---

## See it working

```pascal
procedure TfrmDates.btnInfoClick(Sender: TObject);
var
  dArrived: TDateTime;
  iDays: Integer;
begin
  dArrived := StrToDate('2025/03/14');
  iDays := Trunc(Date - dArrived);

  redOutput.Lines.Add('Today is ' + FormatDateTime('dddd, d mmmm yyyy', Date));
  redOutput.Lines.Add('Arrived on ' + FormatDateTime('dd/mm/yyyy', dArrived));
  redOutput.Lines.Add('Days at the shelter: ' + IntToStr(iDays));
  redOutput.Lines.Add('Check-up due: ' + DateToStr(dArrived + 365));
end;
```

```text
Today is Monday, 9 November 2026
Arrived on 14/03/2025
Days at the shelter: 605
Check-up due: 2026/03/14
```

---

## Understand it — a date is a number

```text
TDateTime value:    46335.354166...
                    └──┬──┘ └──┬───┘
            days since       fraction of a day
            30 Dec 1899      (0.354 × 24 h = 08:30)
```

This is why arithmetic works on dates:

| Expression | Result |
|---|---|
| `Date + 1` | tomorrow |
| `Date - 7` | a week ago |
| `dEnd - dStart` | number of days between the two dates (a Real, so use `Trunc`) |
| `Now - Date` | the time that has passed today |

---

## Getting dates

| Function | Returns | Unit |
|---|---|---|
| `Date` | today's date (time = 00:00) | SysUtils |
| `Time` | the current time | SysUtils |
| `Now` | today's date and the current time | SysUtils |
| `StrToDate('2026/12/25')` | a TDateTime from text | SysUtils |
| `EncodeDate(2026, 12, 25)` | a TDateTime from year, month and day | SysUtils |

::: warning ⚠️ Common Misconception
`StrToDate` uses the **regional date format of the computer**. `'2026/12/25'` works on a computer set to yyyy/mm/dd but may cause an error on one set to dd/mm/yyyy. `EncodeDate(2026, 12, 25)` works on every computer.
:::

---

## Displaying dates

| Code | Output (9 Nov 2026, 08:30) |
|---|---|
| `DateToStr(Date)` | 2026/11/09 (regional setting) |
| `TimeToStr(Now)` | 08:30:00 |
| `FormatDateTime('dd/mm/yyyy', Now)` | 09/11/2026 |
| `FormatDateTime('d mmmm yyyy', Now)` | 9 November 2026 |
| `FormatDateTime('dddd', Now)` | Monday |
| `FormatDateTime('dd mmm yy', Now)` | 09 Nov 26 |
| `FormatDateTime('hh:nn', Now)` | 08:30 |

::: danger 🚨 Watch Out For
1. Minutes are **`nn`**, not `mm`. `mm` means **month**, so `'hh:mm'` shows the month instead of the minutes.
2. `d` = 9, `dd` = 09, `ddd` = Mon, `dddd` = Monday. The same pattern applies to `m`/`mm`/`mmm`/`mmmm`.
:::

---

## Date calculations (DateUtils)

Add `DateUtils` to the `uses` clause for these functions:

| Function | Example | Result |
|---|---|---|
| `DaysBetween(d1, d2)` | `DaysBetween(Date, dBirth)` | whole days between two dates |
| `YearsBetween(d1, d2)` | `YearsBetween(Date, dBirth)` | age in full years |
| `IncDay(d, n)` / `IncMonth(d, n)` / `IncYear(d, n)` | `IncMonth(Date, 3)` | date n days/months/years later |
| `YearOf(d)`, `MonthOf(d)`, `DayOf(d)` | `MonthOf(Date)` | 11 |
| `DayOfTheWeek(d)` | `DayOfTheWeek(Date)` | 1 = Monday … 7 = Sunday |
| `IsLeapYear(iYear)` | `IsLeapYear(2028)` | True (SysUtils) |

::: info 📝 DayOfWeek vs DayOfTheWeek
`DayOfWeek` (SysUtils) counts **Sunday = 1**. `DayOfTheWeek` (DateUtils) counts **Monday = 1**. Check which one a question uses.
:::

### Worked example — is a learner old enough?

```pascal
dBirth := EncodeDate(spnYear.Value, spnMonth.Value, spnDay.Value);
iAge := YearsBetween(Date, dBirth);
if iAge >= 16 then
  lblResult.Caption := 'Old enough for a learner''s licence (' + IntToStr(iAge) + ')'
else
  lblResult.Caption := 'Too young – ' + IntToStr(16 - iAge) + ' year(s) to go';
```

### Leap years from first principles

You may be asked to code the leap-year rule yourself instead of calling `IsLeapYear`:

```pascal
function isLeap(iYear: Integer): Boolean;
begin
  Result := ((iYear mod 4 = 0) and (iYear mod 100 <> 0)) or (iYear mod 400 = 0);
end;
```

---

## 📋 Summary

| Concept | Key point |
|---|---|
| TDateTime | A Real: whole part = date, fraction = time |
| Today / now | `Date`, `Time`, `Now` |
| Display | `FormatDateTime('dd/mm/yyyy', d)`; minutes are `nn` |
| Days between | `Trunc(d2 - d1)` or `DaysBetween(d2, d1)` |
| Add time | `d + 30`, `IncMonth(d, 1)` |
| Leap year | `IsLeapYear(y)` or the mod 4 / 100 / 400 rule |

::: tip 🎯 Exam Tip
In a practical exam, the date on the computer is not the date in the example output. If a question uses `Date`, your number of days will differ from the paper's example, so check that your *method* is right rather than trying to match the number.
:::

## ✏️ Check Your Understanding

**Question 1:** What is displayed by `FormatDateTime('hh:mm', Now)` at 14:45 on 9 November, and why is it wrong?

**Question 2:** Write one statement that displays the date 90 days from today in the format 07 February 2027.

**Question 3:** Is 1900 a leap year? Use the rule to explain. (2)

::: details Check your answers
**Q1:** It displays `14:11`. `mm` means month (November = 11). Use `'hh:nn'`.

**Q2:** `lblDue.Caption := FormatDateTime('dd mmmm yyyy', Date + 90);`

**Q3:** No. 1900 is divisible by 4 and by 100 but **not** by 400, so it is not a leap year. ✓✓
:::

---

*Previous: [← Database Programming](./database-navigation) | Next: [Procedures & Functions →](./procedures-functions)*
