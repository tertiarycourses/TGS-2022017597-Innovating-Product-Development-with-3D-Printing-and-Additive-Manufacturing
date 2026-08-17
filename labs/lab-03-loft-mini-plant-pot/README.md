# Lab 3 — Loft — Mini Plant Pot with Custom Rails

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — apply the loft technique with guide rails to create a freeform printable vessel

## Goal

Model a mini plant pot in Fusion 360 by lofting between a square top and a circular base with custom guide rails, then slice and 3D print it.

## What you'll build

A mini plant pot lofted from circle to square, 3D printed without supports.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA)

## Steps

1. Sketch a 50 mm circle on the XY plane — this is the pot base.

   ```
   Create Sketch ▸ Circle — Ø 50 mm ▸ Finish Sketch
   ```

2. Create an offset plane 60 mm above the base and sketch a 60 mm square on it.

   ```
   Construct ▸ Offset Plane — 60 mm ▸ Sketch ▸ Rectangle 60 × 60 mm
   ```

3. Loft from the circle to the square; add guide rails between matching points to control the curve.

   ```
   Create ▸ Loft — profiles: circle + square, rails: optional splines
   ```

4. Shell the solid to a 2.5 mm wall, removing the top face, to hollow the pot.

   ```
   Modify ▸ Shell — face: top, thickness 2.5 mm
   ```

5. Export the pot as an STL file.

   ```
   File ▸ Export ▸ STL
   ```

6. Slice in Cura standing base-down; no supports are needed because the walls flare outward.

   ```
   Cura ▸ Open File ▸ pot.stl ▸ Slice
   ```

7. Print the pot and inspect the loft surface finish.

   ```
   Cura ▸ Save to Disk ▸ print
   ```


## Test it

The pot prints support-free with an even 2.5 mm wall; the loft transition from circle to square is smooth with no layer separation.
