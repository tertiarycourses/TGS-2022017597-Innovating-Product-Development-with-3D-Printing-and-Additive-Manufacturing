# Lab 11 — Perimeters and Infill — Strength vs Speed

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5, A6 — apply wall/infill optimisation and assess its measured impact on time and material

## Goal

Vary wall count and infill density on the same model in Cura, and record how each change moves print time, material use and expected strength.

## What you'll build

A comparison table of wall/infill settings against sliced print time and material grams.

**Tools:** Ultimaker Cura, cube10.stl

## Steps

1. Open cube10.stl and slice with the defaults — 2 walls, 20% infill; record time and grams.

   ```
   Slice ▸ record: baseline
   ```

2. Raise the wall line count to 4 and re-slice; record the change.

   ```
   Print Settings ▸ Walls ▸ Wall Line Count — 4
   ```

3. Reset walls to 2, then set infill density to 12% and re-slice; record.

   ```
   Infill ▸ Density — 12%
   ```

4. Set infill density to 50% and re-slice; record.

   ```
   Infill ▸ Density — 50%
   ```

5. In Preview, inspect how the infill lattice and wall thickness change at each setting.

   ```
   Preview ▸ layer slider
   ```

6. Tabulate the four runs: time, grams, and where the strength actually comes from (walls more than infill).

   ```
   Table: setting → time → grams
   ```


## Test it

Your table shows infill density driving time/material roughly linearly while extra walls add strength more efficiently — and you can justify a setting choice for a functional vs decorative part.

## Files in this folder

- `cube10.stl`
