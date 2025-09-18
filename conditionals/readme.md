Problem
Smart Traffic Fine System
You’re building part of a traffic management system for a city.

When a car passes a speed camera, the system must decide what fine to issue, based on:

Speed limit for the road.

Actual speed of the car.

Whether it’s raining (in bad weather, lower tolerance is allowed).

Whether the driver is a repeat offender (double fine if yes).

If speed exceeds a certain dangerous threshold, license gets suspended.


`note:`

& is bitwise AND, not logical AND
and is for boolean logic — it evaluates conditions as True/False.

& is for bitwise operations — it works on integers (and some booleans) by comparing their binary representation bit-by-bit.

Example:

```bash
True and True   # → True
True & True     # → 1   (because True is treated as 1)
```
So & doesn’t return a pure boolean — it returns an integer (or other type), which can cause unexpected results.