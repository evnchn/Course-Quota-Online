from flask import Flask, send_file
from waitress import serve
import pathlib



from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    # default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

import bs4 as bs

@app.route('/custom.css')
def ignore():
    return send_file("custom_css/custom.css")
    
    
@app.route('/robots.txt')
def ignore2():
    return ""
    

@app.route('/favicon.ico')
def return_icon():
    return send_file(str(pathlib.Path(__file__).parent.absolute() / "res_images/{}".format("favicon.ico")))
   

@app.route('/<subj>')
@limiter.limit("10/10 second")
def hello(subj):
    if "custom.css" in subj:
        return "bad"
    if "robots.txt" in subj:
        return "bad"
    
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
        for div in soup.find_all("a"):
            div["href"] = "#"
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