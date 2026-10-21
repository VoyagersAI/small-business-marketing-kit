import re,sys,markdown,datetime
src,tpl,out=sys.argv[1:4]
md=open(src).read().splitlines()
title=md[0].lstrip('# ').strip(); upd=md[1].strip(); body='\n'.join(md[2:])
html=markdown.markdown(body,extensions=['extra','sane_lists'])
parts=re.split(r'(?=<h2>)',html); res=[]
for p in parts:
    if p.startswith('<h2>⭐'): p='<section class="top">'+p+'</section>'
    elif p.startswith('<h2>⏱'): p='<section class="ten">'+p+'</section>'
    res.append(p)
t=open(tpl).read().replace('{{TITLE}}',title).replace('{{UPDATED}}',upd).replace('{{MADE}}',datetime.datetime.now().strftime('%b %-d, %Y · %-I:%M %p')).replace('{{BODY}}',''.join(res))
open(out,'w').write(t)
