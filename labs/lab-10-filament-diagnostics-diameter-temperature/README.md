# Lab 10 — Filament Diagnostics — Diameter, Temperature and Flow

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 02:** Process Related Issues for AM  
**TSC objective:** A2, A3 — analyse material-side causes of extrusion issues and verify filament quality

## Goal

Measure filament diameter with digital calipers, verify it against the slicer's material setting, and run a temperature check to place your filament in its working window.

## What you'll build

A verified filament diameter entry in Cura and a chosen printing temperature backed by test evidence.

**Tools:** Digital calipers, filament spool (PLA/ABS/PETG), Ultimaker Cura, FDM printer

## Steps

1. Cut off about 30 cm of filament from the spool end.

   ```
   Flush cutters — ~30 cm sample
   ```

2. Measure the diameter with digital calipers at five points along the sample, rotating the filament at each point.

   ```
   Calipers — 5 readings, 2 orientations each
   ```

3. Average the readings; a good 1.75 mm filament stays within ±0.05 mm.

   ```
   Expect 1.70–1.80 mm
   ```

4. Enter the measured diameter in Cura's material settings so flow is computed from reality, not the label.

   ```
   Print Settings ▸ Material ▸ Diameter — measured value
   ```

5. Check the material's temperature window: PLA 195–215 °C, PETG 240–260 °C, ABS 240–260 °C, Nylon 240–260 °C.

   ```
   Material box / temperature table
   ```

6. Set the printing temperature to the middle of the window and print a small test cube; drop 5 °C if strings appear, raise 5 °C if layers don't bond.

   ```
   Material ▸ Printing Temperature — tune in 5 °C steps
   ```

7. Watch the first layers: clicking from the extruder or ground filament means the temperature is too low or the nozzle is partially blocked.

   ```
   Listen: extruder clicks = under-extrusion warning
   ```


## Test it

Your five caliper readings average within ±0.05 mm of nominal, Cura carries the measured diameter, and the test cube prints with bonded layers and no stringing at the temperature you selected.
