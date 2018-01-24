from psd_tools import PSDImage
from random import randint

psd = PSDImage.load('psd_name.psd')
psd_to_img = psd.as_PIL()
psd_to_img.save('my_image.png')

toHTML  = ""
thisCSS = "";
crow_id = 0

for i in psd.layers:
    crow_id     = crow_id+1
    thisId      = "#crow_psd_"+str(crow_id)
    thisCSS     += thisId+"{position:absolute;width:"+str(i.bbox.width)+"px;height:"+str(i.bbox.height)+"px}"
    #thisText    = i.text_data.text if 'text_data' in i else ""
    toHTML      += "<div id='"+thisId+"'></div>"


saveHTML      = """<!DOCTYPE html>
                    <html>
                        <head>
                            <style>%s</style>
                        </head>
                        <body>
                            %s
                        </body>
                    </html>"""

print saveHTML % (thisCSS, toHTML)