#!/usr/bin/env python3
"""Generate the Learner Guide for 'Innovating Product Development with 3D Printing
and Additive Manufacturing' (TGS-2022017597) as BOTH a Markdown mirror
(LG-*.md at repo root) and a DOCX (courseware/LG-*.docx) from one source.

House format: cover page, Document Version Control Record, auto TOC, Arial 11pt
body, one section per lab (Objective · Goal · What you'll build · Step-by-step
· Test it), plus setup, revision and glossary. All content is driven by
course_data + the domain data files, keeping the LG 100% aligned with the
slide deck, Lesson Plan and labs.
"""
import os, sys, re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT=DOMAIN1+DOMAIN2+DOMAIN3
import prodoc
def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE); ASSETS=os.path.join(os.path.dirname(HERE),"assets")

def _slug(t):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in t).strip("-").replace("--","-")
def lab_dir(a):
    words=re.findall(r"[A-Za-z0-9]+", a["title"])[:4]
    return f"lab-{a['num']:02d}-" + "-".join(w.lower() for w in words)

# ---------------- block DSL (single content stream → MD + DOCX) ----------------
B=[]
def h1(t): B.append(("h1",t))
def h2(t): B.append(("h2",t))
def h3(t): B.append(("h3",t))
def p(t):  B.append(("p",t))
def bullets(xs): B.append(("bullets",xs))
def steps(xs): B.append(("steps",xs))
def code(t): B.append(("code",t))
def note(t): B.append(("note",t))
def rule(): B.append(("rule",))
def img(path,caption): B.append(("img",path,caption))
LEGACY=os.path.join(REPO,"courseware","assets","legacy")

# ---------------- content ----------------
h1("Introduction")
p(f"This Learner Guide accompanies the WSQ course {C.TITLE} ({C.COURSE_CODE}), conducted by {C.ORG}. "
  f"It provides step-by-step instructions for all 16 hands-on labs, organised by the three course topics, "
  f"and supports the TSC {C.TSC_TITLE} ({C.TSC_CODE}).")
p("Use this guide alongside the course slides and the per-lab folders in labs/ of the course repository. "
  "Each lab folder carries this guide's steps plus any sample model files (STL) the lab needs. "
  "The written and practical assessments are open book — bring this guide.")

h1("Course Learning Outcomes")
bullets(C.LEARNING_OUTCOMES)
h3("TSC coverage")
bullets(C.TSC_ABILITIES)
bullets(C.TSC_KNOWLEDGE)

h1("Before You Start — Environment Setup")
h3("What you need")
bullets([
 "A computer with Autodesk Fusion 360 installed — the free personal-use or education licence is sufficient (https://www.autodesk.com/products/fusion-360).",
 "Ultimaker Cura slicing software — free from https://ultimaker.com/software/ultimaker-cura (installed in Lab 7; install early if you want a head start).",
 "An FDM 3D printer with PLA filament (provided in class), plus digital calipers, pliers and sandpaper (120–400 grit) for the tolerance and post-processing labs.",
 "A smartphone with a 3D-scanning app for Lab 6 — Polycam or Kiri Engine (Android/iOS), or Scandy Pro / Heges on LiDAR iPhones/iPads.",
 "The sample models from the labs/ folders: cube10.stl, twist.stl, open vase.stl and token.stl.",
])
h3("Fusion 360 quick orientation")
bullets([
 "Sketch-driven CAD: draw 2D profiles on sketch planes, then turn them 3D with Extrude, Revolve, Sweep and Loft.",
 "The browser (left panel) lists bodies, sketches and construction planes; the timeline (bottom) records every operation for editing.",
 "Export any body for printing via File ▸ Export ▸ STL, or right-click the body ▸ Save As Mesh.",
])
h3("Conventions used in every lab")
bullets([
 "Menu paths are written as Tool ▸ Menu ▸ Command (e.g. Create ▸ Extrude).",
 "Values shown (dimensions, temperatures, percentages) are tested starting points — your printer may need small adjustments.",
 "Every lab ends with a 'Test it' check — do not move on until it passes.",
 "Safety: hot nozzles (200 °C+), moving axes and sharp tools — keep hands clear while printing and use pliers for support removal.",
])

# ---------------- per-topic, per-lab ----------------
for t in C.TOPICS:
    h1(f"Topic {t['code']} — {t['title']}")
    p(t["subtitle"])
    h3("Key concepts")
    bullets([f"{k} — {v}" for k,v in t["concepts"]])
    for a in [x for x in ACT if x["topic"]==t["num"]]:
        h2(f"Lab {a['num']} — {a['title']}")
        p(f"TSC objective: {a['objective']}.")
        p(f"Goal: {a['desc']}")
        h3("What you'll build")
        p(a["build"]+f"   (Tools: {a['services']}.)")
        for gi,im in enumerate(a.get("img") or []):
            ip=os.path.join(LEGACY,im)
            if os.path.exists(ip):
                img(ip, f"Lab {a['num']} reference — "+("target model / setting" if gi==0 else "as prepared in the tool"))
        h3("Step-by-step")
        steps(list(a["steps"]))
        h3("Test it")
        p(a["test"])
        note(f"This lab lives in labs/{lab_dir(a)}/ together with any sample files it needs.")
        rule()

h1("Revision — What to Master for the Assessment")
h3("Knowledge (Written Assessment, K1–K7)")
bullets([
 "K1 — AM characteristics: layer-by-layer construction from CAD, design freedom, rapid prototyping, no part-specific tooling; the 7 ISO/ASTM process families and DMLS/SLS/SLM.",
 "K2 — Process requirements: correct material choice (PLA/ABS/PETG/Nylon/resins), temperature windows, build environment (draughts, humidity, vibration), calibrated and maintained printers.",
 "K3 — Selection factors: material properties, design complexity, production volume and speed, post-processing needs, cost.",
 "K4 — Impact on operations: no tooling/molds, shorter development cycles, complex geometry, customisation without cost, less waste, distributed manufacturing.",
 "K5 — Performance review methods: dimensional accuracy and tolerance checks, surface-finish evaluation, material property tests, build speed/throughput, cost per part.",
 "K6 — Benefits vs trade-offs: rapid prototyping, design flexibility, low waste, customisation — against bulk-production cost, material limits, post-processing load, anisotropic strength.",
 "K7 — Sustainability: operator training, equipment calibration/maintenance, recycling and circular material use, sustainable-material R&D, stakeholder collaboration on standards.",
])
h3("Application (Practical Performance, A1–A6)")
bullets([
 "A1 — Material and design analysis: mechanical/thermal properties, stress points, load-bearing needs, AM-process compatibility, post-processing and surface treatments.",
 "A2 — Process issues: DMLS warping/powder inconsistency; SLS incomplete sintering/thermal distortion; SLM oxidation/residual stress; powder-bed spreading and recycling; inkjet nozzle clogs and layer misalignment.",
 "A3 — Processes and procedures: DMLS/SLM for metals, FDM/SLS for non-metals, separate post-processing per material, bonding techniques (e.g. electroless deposition) for hybrid parts, integrity testing.",
 "A4 — Reverse engineering: scan → refine mesh to CAD → repair wear digitally → select AM process → manufacture and post-process.",
 "A5 — Optimisation: layer height/orientation, walls/infill tuning, machine calibration, support optimisation, surface treatments (ironing, fuzzy skin), real-time monitoring and simulation.",
 "A6 — Impact assessment: baseline → change → measure → compare → decide, across production speed, material use/wastage, quality (accuracy, finish, properties), resource utilisation, cost and operator feedback.",
])
h3("Practice")
bullets([
 "Practice portal: https://exams.tertiaryinfotech.com",
 "Course portal (slides, guide, assessment submission): https://lms-tms.tertiaryinfotech.com",
 "Redo each lab's Test-it check from memory — the practical assessment mirrors the lab skills.",
])

h1("Glossary")
gl=[
 ("Additive Manufacturing (AM)","Building parts layer by layer directly from a CAD file — the industrial discipline around 3D printing."),
 ("STL","The mesh file format (triangles) exported from CAD and consumed by slicers."),
 ("G-code","The movement/temperature/extrusion command language slicers output and printers execute."),
 ("Slicer","Software (e.g. Cura) that converts a 3D model into layer-by-layer printer instructions."),
 ("FDM/FFF","Fused Deposition Modeling — melted filament extruded layer by layer; the desktop standard."),
 ("SLA / DLP / LCD","Vat photopolymerisation — light selectively cures liquid resin."),
 ("SLS","Selective Laser Sintering — a laser fuses polymer powder, no supports needed."),
 ("DMLS / SLM","Metal powder bed fusion — sintered (DMLS) vs fully melted (SLM)."),
 ("DED","Directed Energy Deposition — blown powder or wire melted in place; repair and large parts."),
 ("Infill","The internal lattice of a print — pattern and density trade strength for time/material."),
 ("Perimeter / wall","The solid outline of each layer; walls carry most of a part's strength."),
 ("Raft / brim / skirt","First-layer adhesion aids: platform under the part / border fused to its edge / non-touching priming loop."),
 ("Retraction","Pulling filament back during travel moves to stop oozing and stringing."),
 ("Heat creep","Heat spreading up the filament path causing jams before the melt zone."),
 ("Pillowing","Top-surface sagging/curling over sparse infill on thin roofs."),
 ("Ironing","A near-zero-flow hot pass that smooths top surfaces."),
 ("Fuzzy skin","Deliberate jitter on outer walls that hides layer lines behind texture."),
 ("Reverse engineering","Capturing an existing part (3D scanning) and rebuilding it as editable CAD for re-manufacture."),
 ("Photogrammetry","Reconstructing 3D geometry from many overlapping photographs."),
 ("Post-processing","Everything after the build: support removal, curing, heat treatment, machining, finishing."),
]
B.append(("dl",gl))

# ---------------- render Markdown ----------------
def _anchor(txt):
    return "".join(ch.lower() if ch.isalnum() else ("-" if ch in " -" else "") for ch in txt)

def render_md():
    out=[f"# {C.TITLE} — Learner Guide",""]
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ','UEN ')})  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    out.append("## Contents"); out.append("")
    for kind,*rest in B:
        if kind=="h1": out.append(f"- [{rest[0]}](#{_anchor(rest[0])})")
        elif kind=="h2": out.append(f"  - [{rest[0]}](#{_anchor(rest[0])})")
    out.append("")
    for kind,*rest in B:
        if kind=="h1": out+=["",f"## {rest[0]}",""]
        elif kind=="h2": out+=["",f"### {rest[0]}",""]
        elif kind=="h3": out+=[f"**{rest[0]}**",""]
        elif kind=="p": out+=[rest[0],""]
        elif kind=="bullets": out+=[f"- {x}" for x in rest[0]]+[""]
        elif kind=="steps":
            for i,(instr,cmd) in enumerate(rest[0],1):
                out.append(f"{i}. {instr}")
                if cmd: out+=["",f"   ```",f"   {cmd}","   ```",""]
            out.append("")
        elif kind=="code": out+=["```",rest[0],"```",""]
        elif kind=="note": out+=[f"> **Note:** {rest[0]}",""]
        elif kind=="img":
            rel=os.path.relpath(rest[0],REPO).replace(" ","%20")
            out+=[f"![{rest[1]}]({rel})","",f"*{rest[1]}*",""]
        elif kind=="rule": out+=["---",""]
        elif kind=="dl":
            for term,defn in rest[0]: out.append(f"- **{term}** — {defn}")
            out.append("")
    return "\n".join(out)

MD_OUT=os.path.join(REPO,f"LG-{C.SHORT_TITLE}.md")
with open(MD_OUT,"w") as f: f.write(render_md())
print("Saved",MD_OUT)

# ---------------- render DOCX ----------------
BRAND=RGBColor(0x1F,0x6F,0xEB); GREY=RGBColor(0x55,0x5B,0x66)
INKCODE=RGBColor(0x0B,0x30,0x60)
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc,"LEARNER GUIDE",C.TITLE,C.VERSION.lstrip("v"),
                      org_logo=os.path.join(ASSETS,"tertiary-infotech-logo.png"),
                      course_logo=None, course_code=C.COURSE_CODE)
prodoc.add_version_control(doc,[
 ("7.0","1 June 2025","Legacy release accompanying the v7 trainer deck.",C.TRAINER),
 (C.VERSION.lstrip("v"),C.VERSION_DATE,
  "Full regeneration: 16 hands-on labs with detailed step-by-step guides (Fusion 360 design labs, "
  "Cura slicing/adhesion/support labs, optimisation and post-processing labs), enriched AM theory, "
  "revision section mapped to K1–K7 / A1–A5, and expanded glossary.",C.TRAINER),
])
prodoc.add_toc(doc)

def code_para(text):
    for line in text.split("\n"):
        para=doc.add_paragraph()
        r=para.add_run(line); r.font.name="Consolas"; r.font.size=Pt(9.5); r.font.color.rgb=INKCODE

for kind,*rest in B:
    if kind=="h1": doc.add_heading(rest[0],level=1)
    elif kind=="h2": doc.add_heading(rest[0],level=2)
    elif kind=="h3":
        para=doc.add_paragraph(); r=para.add_run(rest[0]); r.bold=True; r.font.size=Pt(11); r.font.color.rgb=BRAND
    elif kind=="p": doc.add_paragraph(rest[0])
    elif kind=="bullets":
        for x in rest[0]: doc.add_paragraph(x,style="List Bullet")
    elif kind=="steps":
        for i,(instr,cmd) in enumerate(rest[0],1):
            para=doc.add_paragraph(style="List Number"); para.add_run(instr)
            if cmd: code_para(cmd)
    elif kind=="code": code_para(rest[0])
    elif kind=="note":
        para=doc.add_paragraph(); r=para.add_run("Note: "); r.bold=True; r.font.color.rgb=BRAND
        para.add_run(rest[0]).font.size=Pt(10)
    elif kind=="img":
        from docx.shared import Inches as _In
        para=doc.add_paragraph(); para.alignment=WD_ALIGN_PARAGRAPH.CENTER
        try:
            para.add_run().add_picture(rest[0],width=_In(4.8))
            cap=doc.add_paragraph(); cap.alignment=WD_ALIGN_PARAGRAPH.CENTER
            cr=cap.add_run(rest[1]); cr.italic=True; cr.font.size=Pt(9); cr.font.color.rgb=GREY
        except Exception as e:
            print("  ! could not embed",rest[0],e)
    elif kind=="rule": doc.add_paragraph("")
    elif kind=="dl":
        for term,defn in rest[0]:
            para=doc.add_paragraph(style="List Bullet")
            r=para.add_run(term+" — "); r.bold=True; para.add_run(defn)

prodoc.add_page_numbers(doc)
prodoc.enable_update_fields(doc)
DOCX_OUT=os.path.join(REPO,"courseware",f"LG-{C.SHORT_TITLE}.docx")
doc.save(DOCX_OUT)
print("Saved",DOCX_OUT)
