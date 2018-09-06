#!/usr/bin/python
#  -*- coding: utf-8 -*-

from psd_tools import PSDImage
import os
import sys

if not os.path.isdir("assets"): os.mkdir("assets")
if not os.path.isdir("assets/img"): os.mkdir("assets/img")

if len(sys.argv)>1:
	print "PSD: "+sys.argv[1]
	psd = PSDImage.load(sys.argv[1])
	psd_to_img = psd.as_PIL()
	psd_to_img.save('assets/img/bg.png')

	thisHTML    = ""
	thisCSS     = ""
	allLayers   = []

	def getOnlyLayers(thisPSD):
	    global allLayers
	    for i in thisPSD.layers:
	        if "layers" in dir(i):
	            getOnlyLayers(i)
	        else:
	            if i.visible: allLayers.append(i)

	getOnlyLayers(psd)

	for i in allLayers:
	    layerCSS        = ""
	    thisText        = ""

	    # Create all images
	    if not i.text_data:
	        layer_image = i.as_PIL()
	        layer_image.save('assets/img/layer_'+str(i.layer_id)+'.png')
	        layerCSS    += """background-image:url(assets/img/layer_%s.png);background-repeat:no-repeat;""" % str(i.layer_id)
	    else:
	        thisText    = i.text_data.text
	        layerCSS    += ""

	    # Create 
	    thisCSS         += """.crow_%s{%sposition:absolute;z-index:%s;width:%spx;height:%spx;margin-left:%spx;margin-top:%spx}\n""" % (str(i.layer_id), str(layerCSS), str(i.layer_id), str(i.bbox.width), str(i.bbox.height), str(i.bbox.x2 - i.bbox.width), str(i.bbox.y2 - i.bbox.height))
	    thisHTML        += """<div class='crow_%s'>%s</div>""" % (str(i.layer_id), thisText)

	file = open("index.html","w+") 
	file.write((("""<!DOCTYPE html>
	                <html>
	                    <head>
	                        <style>html,body{margin:0px;padding:0px}\n.crow_bg{background-image:url(assets/img/bg.png);overflow:hidden;position:relative;margin:0px auto;width:%spx;height:%spx}%s</style>
	                    </head>
	                    <body>
	                        <div class="crow_bg">
	                            %s
	                        </div>
	                    </body>
	                </html>""") % (psd_to_img.size[0], psd_to_img.size[1], thisCSS, thisHTML)).encode('utf-8').strip())
	file.close()
else:
	print "Ex: python "+sys.argv[0]+" /path/layout.psd"
