from psd_tools import PSDImage
from random import randint

psd = PSDImage.load('brandshop_site_localizador_v2_mobile.psd')
psd_to_img = psd.as_PIL()
psd_to_img.save('my_image.png')

toHTML  = ""
thisCSS = ""
crow_id = 0

def getInsideGroup(if_group):
    global toHTML
    global thisCSS
    global crow_id
    if 'layer_count' in str(if_group):
        for k in if_group.layers:
            crow_id     = crow_id+1
            thisId      = "#crow_psd_"+str(crow_id)
            thisCSS     += thisId+"{position:absolute;width:"+str(k.bbox.width)+"px;height:"+str(k.bbox.height)+"px}"
            if 'layer_count' not in str(k):
                thisText    = k.text_data.text if k.text_data else ""
            else:
                thisText    = ""
            toHTML      += "<div id='"+thisId+"'>"+thisText+"</div>"
            getInsideGroup(k)


for i in psd.layers:
    crow_id     = crow_id+1
    thisId      = "#crow_psd_"+str(crow_id)
    thisCSS     += thisId+"{position:absolute;width:"+str(i.bbox.width)+"px;height:"+str(i.bbox.height)+"px}"
    if 'layer_count' not in str(i):
        thisText    = i.text_data.text if i.text_data else ""
    else:
        thisText    = ""
    toHTML      += "<div id='"+thisId+"'>"+thisText+"</div>"
    getInsideGroup(i)

saveHTML        = """<!DOCTYPE html>
                    <html>
                        <head>
                            <style>%s</style>
                        </head>
                        <body>
                            %s
                        </body>
                    </html>"""

saveHTML        = saveHTML % (thisCSS, toHTML)

print saveHTML
