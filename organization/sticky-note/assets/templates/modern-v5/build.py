import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, 'sources', 'art.jpg')
FONT = os.path.join(HERE, 'fonts', 'Outfit.ttf')
NOTE = os.path.join(HERE, 'sources', 'note.jpg')
TEXT=(0x1F,0x33,0x26); GREEN=(0x45,0xA1,0x63); YEL=(0xFF,0xDE,0x32); BASE=(0xF7,0xF9,0xF8)
def font(sz,style):
    f=ImageFont.truetype(FONT,sz); f.set_variation_by_name(style); return f
art=Image.open(ART).convert('RGB')
def level(im,wp):  # levels: white point wp -> 255, background becomes pure white
    return im.point(lambda v: min(255,round(v*255/wp)))
import numpy as np
def whiten_bg(im,lo=222,hi=238):
    # push only near-white, low-saturation pixels to pure white; notes untouched
    a=np.asarray(im).astype(float); mn=a.min(2); mx=a.max(2)
    w=np.clip((mn-lo)/(hi-lo),0,1)*np.clip(1-(mx-mn-8)/12,0,1)
    return Image.fromarray(np.uint8(np.round(a+(255-a)*w[...,None])))
def tint_to(im,src_box,ref_rgb):
    a=np.asarray(im).astype(float); m=a[src_box[1]:src_box[3],src_box[0]:src_box[2]].reshape(-1,3).mean(0)
    sat=(a.max(2)-a.min(2)); w=np.clip((sat-15)/25,0,1)[...,None]   # only coloured note pixels
    return Image.fromarray(np.uint8(np.clip(a*(1-w)+a*(np.array(ref_rgb)/m)*w,0,255)))
ref=np.asarray(art)[460:600,1000:1150].reshape(-1,3).mean(0)  # header yellow note
art=whiten_bg(art)
A0=np.asarray(art)
def samp(x0,y0,x1,y1): return A0[y0:y1,x0:x1].reshape(-1,3).mean(0)
NOTE_IM=Image.open(NOTE).convert('RGB')
import colorsys
def boost(c,ds=2.6,dv=0.93):
    h,sa,v=colorsys.rgb_to_hsv(*[x/255 for x in c]); return tuple(255*x for x in colorsys.hsv_to_rgb(h,min(1,sa*ds),v*dv))
COLORS={'Fix it':(0x45,0xA1,0x63),
        "What we're working on":(0x8E,0xD6,0xAE),
        'Waiting on you':ref,
        'Parked for later':(0xA8,0xBF,0xA0),
        'To talk about':(0x9C,0xCF,0xD8),
        'Lessons learned':(0xD6,0xE8,0xA8),
        'To go over with [owner name]':(0xF7,0xB2,0x67)}
notes={k:whiten_bg(tint_to(NOTE_IM,(500,200,800,500),v)) for k,v in COLORS.items()}
WHITE=(255,255,255)
def place(crop,size,bg,feather=160):
    """paste art crop at right of a bg canvas with feathered left edge"""
    W,H=size; c=crop.resize((int(crop.width*H/crop.height),H),Image.LANCZOS)
    can=Image.new('RGB',size,bg)
    m=Image.new('L',c.size,255); d=ImageDraw.Draw(m)
    for x in range(min(feather,c.width)): d.line([(x,0),(x,H)],fill=int(255*x/feather))
    can.paste(c,(W-c.width,0),m); return can
# Header: three notes, crop 1:1 region around notes
hdr=place(art.crop((540,120,1280,700)),(1600,400),WHITE,feather=60)
d=ImageDraw.Draw(hdr)
d.text((96,110),'Sticky Note',font=font(96,'Bold'),fill=TEXT)
d.text((100,262),'Everything open, in one place',font=font(56,'Regular'),fill=GREEN)
d.rectangle((100,340,172,346),fill=YEL)
hdr.save(os.path.join(HERE, 'header.png'))
# Banners: single yellow note crop
# "To go over with [owner name]" is a sample name. Rename it for the human. See ../README.md.

names=['Fix it',"What we're working on",'Waiting on you','Parked for later','To talk about','Lessons learned','To go over with [owner name]']
BANNER_FILES={
    'Fix it':'banner-fix-it.png',
    "What we're working on":'banner-what-were-working-on.png',
    'Waiting on you':'banner-waiting-on-you.png',
    'Parked for later':'banner-parked-for-later.png',
    'To talk about':'banner-to-talk-about.png',
    'Lessons learned':'banner-lessons-learned.png',
    'To go over with [owner name]':'banner-to-go-over.png',
}
ban={}
for n in names:
    b=Image.new('RGB',(1600,160),WHITE)
    n_=notes[n].crop((370,80,930,630)).resize((128,126),Image.LANCZOS)
    b.paste(n_,(1600-96-128,17))
    ImageDraw.Draw(b).line((96,158,1504,158),fill=(0xE3,0xE8,0xE5),width=1)
    # tint the white around note toward base: blend crop region bg
    d=ImageDraw.Draw(b)
    d.rectangle((96,50,103,110),fill=GREEN)
    d.text((124,80),n,font=font(60,'SemiBold'),fill=TEXT,anchor='lm')
    b.save(os.path.join(HERE, BANNER_FILES[n])); ban[n]=b
# Mockup
body=font(32,'Regular')
s1=['Finish the spring email plan draft','Review the new landing page copy','Confirm next week\'s posting schedule']
s2=['Approve the logo colors for the welcome kit','Send the photos for the team page']
def lines(ls):
    im=Image.new('RGB',(1600,40+len(ls)*58+30),'white'); d=ImageDraw.Draw(im)
    for i,t in enumerate(ls):
        y=40+i*58; d.ellipse((124,y+12,136,y+24),fill=GREEN); d.text((160,y),t,font=body,fill=TEXT)
    return im
samples={'Fix it':s1,'To talk about':['Which brand kit to build first'],'To go over with [owner name]':['Sticky Note art test results'],"What we're working on":['Drafting the fall newsletter','Updating the service page photos'],
 'Waiting on you':s2,'Parked for later':['Refresh the about page story'],'Lessons learned':['Short captions get more replies','Batching posts on Mondays saves time']}
parts=[hdr,Image.new('RGB',(1600,40),'white')]
for n in names: parts+= [ban[n],lines(samples[n]),Image.new('RGB',(1600,30),'white')]
parts.append(Image.new('RGB',(1600,30),'white'))
M=Image.new('RGB',(1600,sum(p.height for p in parts)),'white'); y=0
for p in parts: M.paste(p,(0,y)); y+=p.height
ImageDraw.Draw(M).line((96,400,1504,400),fill=(0xDD,0xE5,0xE0),width=2)
M.save(os.path.join(HERE, 'mockup.png'))
