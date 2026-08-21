# Lab 4 — Revolve — Funnel from a 2D Profile

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — apply the revolve technique and choose a print orientation that avoids supports

## Goal

Model a funnel by revolving a half-profile, then invert, slice and print it.

## What you'll build

A working funnel revolved from a single 2D profile, printed wide-end down.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA)

## Steps

1. Sketch a closed 2 mm funnel half-profile on the XZ plane: wide cone to narrow spout.

   ```
   Create Sketch > Line — cone Ø 60 mm -> spout Ø 8 mm, wall 2 mm
   ```

2. Revolve the profile 360° around the vertical (Z) axis to form the funnel body.

   ```
   Create > Revolve — profile: half section, axis: Z, angle 360 degrees
   ```

3. Use Inspect > Section Analysis to confirm a watertight, uniform wall.

   ```
   Inspect > Section Analysis
   ```

4. Export the funnel as an STL file.

   ```
   File > Export > STL
   ```

5. Open it in Cura — it imports spout-up; rotate it so the wide mouth sits on the build plate.

   ```
   Cura > Rotate — 180 degrees  about X (wide end down)
   ```

6. Slice and confirm the cone angle prints without supports, then print.

   ```
   Cura > Slice > Preview > Save to Disk
   ```


## Evidence to capture

- Fusion 360 screenshot of the closed half-profile and 360-degree revolve.
- Cura Preview screenshot showing wide-end-down, support-free orientation.
- Photo or water-flow note confirming a clear spout.


## Test it

Sliced upside-down the funnel needs no supports; water poured into the printed funnel flows cleanly through the spout.
