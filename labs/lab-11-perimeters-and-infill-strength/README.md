# Lab 11 — Perimeters and Infill — Strength vs Speed

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5, A6 — apply wall/infill optimisation and assess its measured impact on time and material

## Goal

Vary wall count and infill density on the same model in Cura, and record how each change moves print time, material use and expected strength.

## What you'll build

A comparison table of wall/infill settings against sliced print time and material grams.

**Tools:** Ultimaker Cura, cube10.stl, line-width-test.stl, cube20 hole-wall variants

## Steps

1. Open cube10.stl and slice with the defaults — 2 walls, 20% infill; record time and grams.

   ```
   Slice > record: baseline
   ```

2. Raise the wall line count to 4 and re-slice; record the change.

   ```
   Print Settings > Walls > Wall Line Count — 4
   ```

3. Reset walls to 2, then set infill density to 12% and re-slice; record.

   ```
   Infill > Density — 12%
   ```

4. Set infill density to 50% and re-slice; record.

   ```
   Infill > Density — 50%
   ```

5. In Preview, inspect how the infill lattice and wall thickness change at each setting.

   ```
   Preview > layer slider
   ```

6. Tabulate the four runs: time, grams, and where the strength actually comes from (walls more than infill).

   ```
   Table: setting -> time -> grams
   ```

7. Open line-width-test.stl and the two cube20 hole-wall variants; inspect Preview for missing thin features, then record the smallest feature and hole wall your profile resolves continuously.

   ```
   Open three diagnostic models > Preview > Color Scheme: Line Type
   ```


## Evidence to capture

- Wall/infill table with time, material and expected load-path notes.
- Cura Preview comparison of the line-width and matched hole-wall models.
- Measured hole diameter and wall thickness from any printed benchmark.


## Test it

Your evidence separates wall-count, infill and line-width effects; the matched hole models show how wall planning changes continuity and dimensional accuracy, and you can justify settings for functional versus decorative parts.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
- `line-width-test.stl` — Thin-wall benchmark for nozzle/line-width and single-wall behaviour.
- `cube20-hole-0-wall.stl` — Hole benchmark with the wall-control baseline geometry.
- `cube20-hole-1-wall.stl` — Matched hole benchmark for testing the effect of an additional wall.
