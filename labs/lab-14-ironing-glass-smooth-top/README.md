# Lab 14 — Ironing — Glass-Smooth Top Surfaces

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — apply ironing to improve top-surface quality and assess its cost

## Goal

Enable Cura's ironing feature, which passes the hot nozzle over the top surface with a tiny extrusion, and compare the top finish with and without it.

## What you'll build

Two cube prints — ironed and standard — demonstrating the top-surface improvement.

**Tools:** Ultimaker Cura, cube10.stl, FDM printer

## Steps

1. Open cube10.stl and slice with the standard 0.2 mm profile; print cube 1 as the control.

   ```
   Slice ▸ print control cube
   ```

2. Enable ironing.

   ```
   Top/Bottom ▸ Enable Ironing ✔
   ```

3. Inspect the ironing pass in Preview — a dense zigzag over the top face at ~10% flow.

   ```
   Preview ▸ top layer ▸ ironing pass
   ```

4. Slice and note the added time (ironing is slow but only on top faces).

   ```
   Slice ▸ record extra minutes
   ```

5. Print cube 2 with ironing enabled.

   ```
   Save to Disk ▸ print
   ```

6. Compare the two top faces under raking light: the ironed face should be near-flat with faint tool lines.

   ```
   Visual + touch comparison
   ```


## Test it

The ironed cube's top face is visibly smoother and flatter than the control's, and you can state when the extra time is worth it (visible top faces, lids, logos).

## Files in this folder

- `cube10.stl`
