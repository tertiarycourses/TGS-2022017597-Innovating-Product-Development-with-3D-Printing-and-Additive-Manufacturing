#!/usr/bin/env python3
"""Generate the labs/ tree — ONE FOLDER PER LAB — from the same single source as
the deck, LP and LG. Each labs/lab-NN-slug/ folder gets a README.md (objective,
goal, steps, test) and any sample STL model files the lab uses. Also generates
token.stl (an original elliptical keychain token model) for Lab 1.
"""
import os, sys, re, shutil, math, struct

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT=DOMAIN1+DOMAIN2+DOMAIN3

def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE)
LABS=os.path.join(REPO,"labs")

# sample STL sources (shipped with the original course application)
SAMPLES=os.path.join(os.path.dirname(REPO),"course_application","sample_files")
LAB_FILES={
 7:["cube10.stl"], 8:["cube10.stl"], 9:["twist.stl"],
 11:["cube10.stl"], 12:["cube10.stl"], 13:["cube10.stl"], 14:["cube10.stl"],
 15:["open vase.stl"], 16:["open vase.stl"],
}

def lab_dir(a):
    words=re.findall(r"[A-Za-z0-9]+", a["title"])[:4]
    return f"lab-{a['num']:02d}-" + "-".join(w.lower() for w in words)

def learner_command(text):
    """Keep code/path blocks portable in the Markdown-to-PDF renderer."""
    return (text.replace("▸", ">").replace("→", "->").replace("×", "x")
                .replace("≈", "~").replace("±", "+/-").replace("°", " degrees ").strip())

def learner_text(text):
    """Use glyphs supported by the lab PDF's learner-facing body font."""
    return text.replace("▸", ">").replace("→", "->")

# ---------------- original model: elliptical keychain token (Lab 1 sample solution)
def write_token_stl(path, a=25.0, b=15.0, t=3.0, hole_r=2.0, hole_dx=-18.0, n=96, nh=48):
    """Extruded ellipse (a×b, thickness t) with a keyring hole — binary STL."""
    tris=[]
    def tri(p1,p2,p3): tris.append((p1,p2,p3))
    ell=[(a*math.cos(2*math.pi*i/n), b*math.sin(2*math.pi*i/n)) for i in range(n)]
    hol=[(hole_dx+hole_r*math.cos(2*math.pi*i/nh), hole_r*math.sin(2*math.pi*i/nh)) for i in range(nh)]
    # side walls (outer, then hole inner)
    for ring,rev in ((ell,False),(hol,True)):
        m=len(ring)
        for i in range(m):
            x1,y1=ring[i]; x2,y2=ring[(i+1)%m]
            if rev: (x1,y1),(x2,y2)=(x2,y2),(x1,y1)
            tri((x1,y1,0),(x2,y2,0),(x2,y2,t)); tri((x1,y1,0),(x2,y2,t),(x1,y1,t))
    # top & bottom: fan from ellipse to centroid ring minus hole — simple ear-free approach:
    # triangulate between ellipse and hole by angle pairing, plus cap the far side fan.
    for z,flip in ((t,False),(0.0,True)):
        for i in range(n):
            x1,y1=ell[i]; x2,y2=ell[(i+1)%n]
            j1=int(i*nh/n)%nh; j2=int((i+1)*nh/n)%nh
            hx1,hy1=hol[j1]; hx2,hy2=hol[j2]
            quads=[((x1,y1,z),(x2,y2,z),(hx2,hy2,z)),((x1,y1,z),(hx2,hy2,z),(hx1,hy1,z))]
            for p1,p2,p3 in quads:
                if flip: tri(p1,p3,p2)
                else: tri(p1,p2,p3)
    with open(path,"wb") as f:
        f.write(b"token.stl - Tertiary Infotech original sample".ljust(80,b" "))
        f.write(struct.pack("<I",len(tris)))
        for p1,p2,p3 in tris:
            ux,uy,uz=(p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])
            vx,vy,vz=(p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2])
            nx,ny,nz=(uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx)
            ln=math.sqrt(nx*nx+ny*ny+nz*nz) or 1.0
            f.write(struct.pack("<3f",nx/ln,ny/ln,nz/ln))
            for p in (p1,p2,p3): f.write(struct.pack("<3f",*p))
            f.write(struct.pack("<H",0))
    return len(tris)

# ---------------- build the tree
os.makedirs(LABS,exist_ok=True)
index=["# Labs — "+C.TITLE,"",
       f"**{C.COURSE_CODE}** · one folder per lab · full step-by-step in each README and in the Learner Guide.",""]
for t in C.TOPICS:
    index.append(f"\n## Topic {t['code']} — {t['title']}\n")
    for a in [x for x in ACT if x["topic"]==t["num"]]:
        d=lab_dir(a); path=os.path.join(LABS,d)
        os.makedirs(path,exist_ok=True)
        files=LAB_FILES.get(a["num"],[])
        copied=[]
        for fn in files:
            src=os.path.join(SAMPLES,fn)
            if os.path.exists(src):
                shutil.copy(src,os.path.join(path,fn)); copied.append((fn,"Core sample model used by the lab procedure."))
        for asset in a.get("assets",[]):
            src=os.path.join(REPO,asset["source"])
            dst=os.path.join(path,asset["name"])
            if os.path.exists(src):
                shutil.copy2(src,dst)
            elif not os.path.exists(dst):
                raise FileNotFoundError(f"Required lab asset missing: {src}")
            copied.append((asset["name"],asset["purpose"]))
        if a["num"]==1:
            ntri=write_token_stl(os.path.join(path,"token.stl"))
            copied.append(("token.stl",f"Original sample solution generated by the build pipeline ({ntri} triangles)."))
        md=[f"# Lab {a['num']} — {a['title']}","",
            f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ",
            f"**Topic {t['code']}:** {t['title']}  ",
            f"**TSC objective:** {a['objective']}","",
            "## Goal","",a["desc"],"",
            "## What you'll build","",f"{a['build']}","",
            f"**Tools:** {a['services']}","",
            "## Steps",""]
        for i,(instr,cmd) in enumerate(a["steps"],1):
            md.append(f"{i}. {learner_text(instr)}")
            if cmd: md+=["",f"   ```",f"   {learner_command(cmd)}","   ```",""]
        if a.get("evidence"):
            md+=["","## Evidence to capture","",*[f"- {learner_text(item)}" for item in a["evidence"]],""]
        md+=["","## Test it","",learner_text(a["test"]),""]
        if copied:
            md+=["## Files in this folder","",*[f"- `{fn}` — {purpose}" for fn,purpose in copied],""]
        with open(os.path.join(path,"README.md"),"w") as f: f.write("\n".join(md))
        extra=f"  ({', '.join(fn for fn,_ in copied)})" if copied else ""
        index.append(f"- [Lab {a['num']} — {a['title']}]({d}/README.md){extra}")
with open(os.path.join(LABS,"README.md"),"w") as f: f.write("\n".join(index)+"\n")
print(f"Labs written to {LABS} — {len(ACT)} lab folders")
