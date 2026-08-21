# Lab 7 — Install Cura and Slice Your First Model

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 02:** Process Related Issues for AM  
**TSC objective:** A2 — set up the slicing toolchain used to analyse and fix AM process issues

## Goal

Install Ultimaker Cura, add your printer profile, and slice a calibration cube to understand how the slicer turns an STL into G-code printer instructions.

## What you'll build

A working Cura installation with your printer profile, and your first sliced G-code file.

**Tools:** Ultimaker Cura, cube10.stl, cube20.stl

## Steps

1. Download Ultimaker Cura for your operating system and run the installer.

   ```
   https://ultimaker.com/software/ultimaker-cura
   ```

2. Launch Cura and step through the first-run wizard; skip account sign-in if offered.

   ```
   Cura > Get Started
   ```

3. Add your printer — pick the exact model, or 'Custom FFF printer' with your bed size and nozzle diameter.

   ```
   Settings > Printer > Add Printer
   ```

4. Open the sample cube from the lab folder.

   ```
   File > Open File(s) > cube10.stl
   ```

5. Select the Standard Quality 0.2 mm profile and note the default wall, infill, speed and temperature values.

   ```
   Print Settings > Profile — Standard Quality 0.2 mm
   ```

6. Slice the model and read the estimated print time and material use.

   ```
   Slice > note time + grams
   ```

7. Open the Preview tab and drag the layer slider to watch the toolpath layer by layer — walls, infill, travels.

   ```
   Preview > layer slider
   ```

8. Save the G-code to disk (or SD card) — this file is the printer's complete instruction set.

   ```
   Save to Disk > cube10.gcode
   ```

9. Repeat the slice with cube20.stl, confirm Cura reads it as 20 × 20 × 20 mm, and compare the time/material estimate with cube10.stl.

   ```
   File > Open File(s) > cube20.stl > Scale > verify 20 mm on X/Y/Z
   ```


## Evidence to capture

- Screenshot of cube20.stl in Cura Preview with walls, infill and travel moves visible.
- Recorded print-time and material estimates for both the 10 mm and 20 mm cubes.


## Test it

Cura shows per-layer toolpaths for both cubes, cube20.stl measures 20 × 20 × 20 mm, and your comparison explains why doubling linear size increases print time and material by much more than two times.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
- `cube20.stl` — 20 mm calibration cube for scale, dimensional and time/material comparisons.
