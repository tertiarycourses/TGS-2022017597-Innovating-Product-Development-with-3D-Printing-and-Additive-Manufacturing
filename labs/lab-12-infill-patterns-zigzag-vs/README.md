# Lab 12 — Infill Patterns — Zigzag vs Grid Strength Test

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — evaluate infill pattern and density as a quality-improvement technique

## Goal

Print cube10.stl with zigzag 20% and grid 30% infill, tune the top layers, then compare the two cubes' stiffness by hand.

## What you'll build

Two printed cubes with different infill patterns/densities and a hands-on strength comparison.

**Tools:** Ultimaker Cura, cube10.stl, Optimize1–4 model set, FDM printer

## Steps

1. Open cube10.stl and set infill pattern to Zigzag at 20% density.

   ```
   Infill > Pattern — Zigzag, Density — 20%
   ```

2. Set top layers to 4 so the roof closes cleanly over the infill.

   ```
   Top/Bottom > Top Layers — 4
   ```

3. Slice, save and print the first cube.

   ```
   Slice > Save to Disk > print
   ```

4. Change the pattern to Grid at 30% density and re-slice; note the time difference.

   ```
   Infill > Pattern — Grid, Density — 30%
   ```

5. Print the second cube.

   ```
   Save to Disk > print
   ```

6. Compare the cubes: squeeze the walls, press the top faces, and note pillowing or gaps over the infill.

   ```
   Hand test: wall flex + roof sag
   ```

7. Load optimize-1.stl through optimize-4.stl, orient each for minimum support, and record Cura's estimated time/material before choosing the most efficient printable variant.

   ```
   Open four models > Auto Orient/Rotate > Slice > record estimates
   ```


## Evidence to capture

- Optimisation scorecard for all four supplied variants: orientation, support volume, time and material.
- A justified selection of the best variant/settings for the stated business need.


## Test it

The grid 30% cube is stiffer and better supported, while your four-variant scorecard shows that geometry and orientation can outweigh infill choice; your final recommendation is backed by time, material and support evidence.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
- `optimize-1.stl` — Complex baseline part for printability and support-cost review.
- `optimize-2.stl` — Wide low-profile variant for build-orientation comparison.
- `optimize-3.stl` — Twisted variant for support and toolpath comparison.
- `optimize-4.stl` — Compact variant for rapid slicing and material-use comparison.
