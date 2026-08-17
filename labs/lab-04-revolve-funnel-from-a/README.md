# Lab 4 — Revolve — Funnel from a 2D Profile

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — apply the revolve technique and choose a print orientation that avoids supports

## Goal

Model a funnel in Fusion 360 by sketching its half cross-section and revolving it about the vertical axis, then invert it in Cura and 3D print it.

## What you'll build

A working funnel revolved from a single 2D profile, printed wide-end down.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA)

## Steps

1. Sketch the funnel's half profile on the XZ plane: a wide cone tapering into a narrow spout, drawn as a closed outline 2 mm thick.

   ```
   Create Sketch ▸ Line — cone Ø 60 mm → spout Ø 8 mm, wall 2 mm
   ```

2. Revolve the profile 360° around the vertical (Z) axis to form the funnel body.

   ```
   Create ▸ Revolve — profile: half section, axis: Z, angle 360°
   ```

3. Check the wall is watertight and uniform using the Inspect ▸ Section Analysis tool.

   ```
   Inspect ▸ Section Analysis
   ```

4. Export the funnel as an STL file.

   ```
   File ▸ Export ▸ STL
   ```

5. Open it in Cura — it imports spout-up; rotate it so the wide mouth sits on the build plate.

   ```
   Cura ▸ Rotate — 180° about X (wide end down)
   ```

6. Slice and confirm the cone angle prints without supports, then print.

   ```
   Cura ▸ Slice ▸ Preview ▸ Save to Disk
   ```


## Test it

Sliced upside-down the funnel needs no supports; water poured into the printed funnel flows cleanly through the spout.
