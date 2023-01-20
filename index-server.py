from flask import Flask, send_file
from waitress import serve
import pathlib

app = Flask(__name__)

import bs4 as bs

@app.route('/<subj>')
def hello(subj):
    if "custom.css" in subj:
        return send_file("custom_css/custom.css")
    if "robots.txt" in subj:
        return ""
    
    with open(str(pathlib.Path(__file__).parent.absolute() / "filestore/{}/{}.html".format(subj[0:4], subj[4:8])), encoding="utf-8") as sitefile:
        txt = sitefile.read()
        
    soup = bs.BeautifulSoup(txt, "lxml")
    found = False
    for div in soup.select(".course"):
        if div.select(".courseanchor > a")[0]["name"] != subj[4:]:
            div.decompose()
        else:
            found = True
            
            
    
    #return send_file("filestore/{}.html".format(subj[0:4]))
    if found:
        
        for div in soup.find_all("div", {'id':'block'}): 
            div.decompose()
        for div in soup.find_all("div", {'id':'navigator'}): 
            div.decompose()
        new_div = soup.new_tag('link rel="stylesheet" href="custom.css" type="text/css"')
        soup.html.head.append(new_div)
        return str(soup)
    else:
        return "Not found"
    
@app.route('/<path:path>')   
def pathloader(path):
    if ".php" in path or ".map" in path:
        return ""
    elif path.endswith("js") or path.endswith("css"):
        
        return send_file(str(pathlib.Path(__file__).parent.absolute() / "res_css_js/{}".format(path.split("/")[-1])))
    elif path.endswith("gif") or path.endswith("png"):
        return send_file(str(pathlib.Path(__file__).parent.absolute() / "res_images/{}".format(path.split("/")[-1])))
    else:
        return ""
        
if __name__ == "__main__":
    # app.run(port=2280)
    serve(app, host='0.0.0.0', port=2280)