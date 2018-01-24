from psd_tools import PSDImage
from random import randint

psd = PSDImage.load('psd_name.psd')
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
            thisId      = "crow_psd_"+str(crow_id)
            thisCSS     += "#"+thisId+"{position:absolute;width:"+str(k.bbox.width)+"px;height:"+str(k.bbox.height)+"px;margin-left:"+str(k.bbox.x2 - k.bbox.width)+"px;margin-top:"+str(k.bbox.y2 - k.bbox.height)+"px}\n"
            if 'layer_count' not in str(k):
                thisText    = k.text_data.text if k.text_data else ""
            else:
                thisText    = ""
            toHTML      += "<div id='"+thisId+"'>"+thisText+"</div>"
            getInsideGroup(k)


for i in psd.layers:
    crow_id     = crow_id+1
    thisId      = "crow_psd_"+str(crow_id)
    thisCSS     += "#"+thisId+"{position:absolute;width:"+str(i.bbox.width)+"px;height:"+str(i.bbox.height)+"px;margin-left:"+str(i.bbox.x2 - i.bbox.width)+"px;margin-top:"+str(i.bbox.y2 - i.bbox.height)+"px}\n"
    if 'layer_count' not in str(i):
        thisText    = i.text_data.text if i.text_data else ""
    else:
        thisText    = ""
    toHTML      += "<div id='"+thisId+"'>"+thisText+"</div>"
    getInsideGroup(i)

saveHTML        = """<!DOCTYPE html>
                    <html>
                        <head>
                            <style>html,body{margin:0px;padding:0px}\n.crow_bg{background:url(my_image.png) no-repeat;width:%spx;height:%spx}%s</style>
                        </head>
                        <body>
                            <div class="crow_bg">
                                %s
                            </div>
                        </body>
                    </html>"""

saveHTML        = saveHTML % (psd_to_img.size[0], psd_to_img.size[1], thisCSS, toHTML)

file = open("index.html","w+") 
file.write(saveHTML.encode('utf-8').strip())
file.close()
