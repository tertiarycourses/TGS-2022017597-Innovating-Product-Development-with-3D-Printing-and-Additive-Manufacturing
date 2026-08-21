# Lab 14 — Ironing — Glass-Smooth Top Surfaces

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — apply ironing to improve top-surface quality and assess its cost

## Goal

Enable Cura's ironing feature, which passes the hot nozzle over the top surface with a tiny extrusion, and compare the top finish with and without it.

## What you'll build

Two cube prints — ironed and standard — demonstrating the top-surface improvement.

**Tools:** Ultimaker Cura, cube10.stl, z-block.stl, FDM printer

## Steps

1. Open cube10.stl and slice with the standard 0.2 mm profile; print cube 1 as the control.

   ```
   Slice > print control cube
   ```

2. Enable ironing.

   ```
   Top/Bottom > Enable Ironing ✔
   ```

3. Inspect the ironing pass in Preview — a dense zigzag over the top face at ~10% flow.

   ```
   Preview > top layer > ironing pass
   ```

4. Slice and note the added time (ironing is slow but only on top faces).

   ```
   Slice > record extra minutes
   ```

5. Print cube 2 with ironing enabled.

   ```
   Save to Disk > print
   ```

6. Compare the two top faces under raking light: the ironed face should be near-flat with faint tool lines.

   ```
   Visual + touch comparison
   ```

7. Repeat the Preview comparison with z-block.stl to inspect how ironing travels around raised detail; print it only if time permits.

   ```
   Open z-block.stl > Enable Ironing > Preview top layers
   ```


## Evidence to capture

- Control-versus-ironed time/material record.
- Raking-light photos comparing the flat and detailed top surfaces.


## Test it

The ironed cube is visibly smoother than the control, z-block.stl shows ironing constrained to eligible top faces, and you can justify the added time for lids, logos and presentation surfaces.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
- `z-block.stl` — Detailed top-surface benchmark for evaluating ironing around raised geometry.
