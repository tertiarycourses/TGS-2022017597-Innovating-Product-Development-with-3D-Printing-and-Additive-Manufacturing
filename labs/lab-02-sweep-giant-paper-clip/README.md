# Lab 2 — Sweep — Giant Paper Clip Bookmark

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — apply the sweep technique to produce a printable path-driven part

## Goal

Model a giant paper clip bookmark in Fusion 360 by sweeping a circular profile along a paper-clip path, then slice and 3D print it.

## What you'll build

A giant paper clip bookmark modelled with the sweep technique and 3D printed flat.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA)

## Steps

1. Start a sketch on the XY plane and draw the paper-clip path — three nested U-turns — using the Line and Arc tools.

   ```
   Create Sketch ▸ Line + Arc (3-point) — overall ~90 × 35 mm
   ```

2. Add fillets so every corner of the path is a smooth arc, then finish the sketch.

   ```
   Sketch ▸ Fillet — radius 5 mm ▸ Finish Sketch
   ```

3. Create a plane perpendicular to one end of the path and sketch a 2.5 mm circle on it.

   ```
   Construct ▸ Plane Along Path (t=0) ▸ Sketch ▸ Circle Ø 2.5 mm
   ```

4. Sweep the circle along the path to form the solid clip.

   ```
   Create ▸ Sweep — profile: circle, path: clip sketch
   ```

5. Export the body as an STL file.

   ```
   File ▸ Export ▸ STL
   ```

6. Open it in Cura and lay the clip flat on the build plate so no supports are needed.

   ```
   Cura ▸ Open File ▸ clip.stl ▸ Rotate — flat
   ```

7. Slice with a 0.2 mm profile and print.

   ```
   Cura ▸ Slice ▸ Save to Disk ▸ print
   ```


## Test it

The preview shows the whole clip printing in contact with the bed; the printed clip flexes slightly and grips a few pages like a real paper clip.
