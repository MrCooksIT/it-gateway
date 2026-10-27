---
title: The Timer Component (Grade 10)
description: Use TTimer to run code repeatedly for countdowns, clocks and simple animations in Delphi.
---

# The Timer Component

::: info 📌 Key Points
- A **TTimer** runs its **OnTimer** event over and over, every **Interval** milliseconds (1000 ms = 1 second).
- Switch it on and off with **Enabled**.
- Timers are used for countdowns, clocks, moving images (animation) and quiz time limits.
- The timer is **invisible** when the program runs. It is a non-visual component (System tab).
:::

A quiz app gives you 30 seconds per question. A loading bar fills up slowly. A logo slides across the screen. None of these can be done with a normal loop, because a loop runs so fast that you would only see the end result. A **timer** lets the program do a small step, wait, and then do the next step.

---

## See it working — a 10-second countdown

Form: `tmrCountdown` (TTimer, Interval = 1000, Enabled = False), `btnStart`, `lblTime`, and a global variable `iSeconds`.

```pascal
var
  frmTimer: TfrmTimer;
  iSeconds: Integer;      // global – keeps its value between timer ticks

procedure TfrmTimer.btnStartClick(Sender: TObject);
begin
  iSeconds := 10;
  lblTime.Caption := IntToStr(iSeconds);
  tmrCountdown.Enabled := True;            // start ticking
end;

procedure TfrmTimer.tmrCountdownTimer(Sender: TObject);
begin
  Dec(iSeconds);                           // runs once every second
  lblTime.Caption := IntToStr(iSeconds);
  if iSeconds = 0 then
  begin
    tmrCountdown.Enabled := False;         // stop ticking
    ShowMessage('Time is up!');
  end;
end;
```

---

## Understand it

```text
btnStart clicked → Enabled := True
     │
     ▼
 ┌─ wait 1000 ms ─► OnTimer runs ─► iSeconds 9 ─┐
 │                                               │
 └──────────────── (repeat) ◄────────────────────┘
                     ... until iSeconds = 0 → Enabled := False
```

| Property / event | Purpose |
|---|---|
| `Interval` | Milliseconds between ticks (1000 = 1 s, 50 = 20 times per second) |
| `Enabled` | `True` = ticking, `False` = stopped |
| `OnTimer` | The event that runs every tick (double-click the timer to create it) |

::: warning ⚠️ Common Misconception
Learners often declare the counter as a **local** variable inside `OnTimer`. A local variable is created again on every tick, so it never counts down. A counter that must remember its value between ticks must be a **global** variable (or a form field).
:::

---

## Simple animation — moving an image

```pascal
procedure TfrmTimer.tmrMoveTimer(Sender: TObject);
begin
  imgBall.Left := imgBall.Left + 5;                 // move 5 pixels right
  if imgBall.Left + imgBall.Width >= ClientWidth then
    imgBall.Left := 0;                              // wrap back to the left
end;
```

Set `tmrMove.Interval := 30` for smooth movement. A smaller interval gives faster, smoother animation.

## A digital clock

```pascal
procedure TfrmTimer.tmrClockTimer(Sender: TObject);
begin
  lblClock.Caption := FormatDateTime('hh:nn:ss', Now);   // Interval = 1000
end;
```

::: tip 💡 Why This Matters
Every game you play runs on the same idea, called a *game loop*. Many times per second the game moves everything a little, checks for collisions and redraws the screen. A Delphi timer is the simplest version of that loop.
:::

---

## 📋 Summary

| Concept | Key point |
|---|---|
| TTimer | Non-visual component that fires OnTimer repeatedly |
| Interval | Time between ticks in milliseconds |
| Enabled | Start (`True`) / stop (`False`) the timer |
| Counters | Must be global so they keep their value between ticks |

::: tip 🎯 Exam Tip
Always include a **stop condition** in OnTimer (`Enabled := False`). A timer that never stops loses marks, and in a countdown it can produce negative numbers.
:::

---

*Previous: [← Debugging](./debugging) | Next: [Loops →](./loops)*
