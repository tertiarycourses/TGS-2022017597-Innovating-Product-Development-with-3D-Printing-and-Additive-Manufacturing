# Lab 6 — 3D Scan and Print a Real Object

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A4 — evaluate reverse engineering of a component through 3D scanning and subsequent AM

## Goal

Scan a real object with a mobile 3D-scanning app, export the mesh as an STL file, repair it if needed, then slice and 3D print the reproduction.

## What you'll build

A 3D-printed reproduction of a real object captured by photogrammetry on your phone.

**Tools:** Polycam / Kiri Engine / Scandy Pro (mobile), Fusion 360, Ultimaker Cura

## Steps

1. Install a 3D scanning app on your phone — Polycam or Kiri Engine (Android/iOS), or Scandy Pro / Heges (iOS LiDAR).

   ```
   App Store / Google Play ▸ Polycam or Kiri Engine
   ```

2. Pick a matte, textured object about the size of a mug and place it on a contrasting background with even lighting.

   ```
   Object: non-shiny, non-transparent, stable
   ```

3. Capture 30–60 photos in two orbits around the object — one at eye level, one from above — keeping it centred.

   ```
   App ▸ Photo mode ▸ capture 2 full orbits
   ```

4. Let the app reconstruct the mesh, then crop away the background and floor plane.

   ```
   App ▸ Process ▸ Crop / Remove floor
   ```

5. Export the model as an STL (or OBJ, then convert via Fusion 360's Mesh workspace).

   ```
   App ▸ Export ▸ STL
   ```

6. Repair holes or stray triangles: Fusion 360 ▸ Mesh ▸ Repair, or import directly into Cura if clean.

   ```
   Fusion 360 ▸ Mesh ▸ Repair ▸ Export STL
   ```

7. Scale the model in Cura to a 20-minute print size (~40 mm tall), slice with supports if needed, and print.

   ```
   Cura ▸ Scale 40 mm ▸ Slice ▸ print
   ```


## Test it

The exported STL loads into Cura as a watertight mesh, and the printed part is a recognisable scaled reproduction of the scanned object.
