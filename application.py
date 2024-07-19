from flask import Flask,request,render_template;
import os


app= Flask(__name__)

APP_ROUTE=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def mainpage():
    return render_template("index2.html")

@app.route("/output", methods=['GET','POST'])
def output_page():
    image=request.files.get('file')
    filename=image.filename
    print("The gotten image file in the post request: ", filename);
    destination=os.path.join(APP_ROUTE,"static")
    if not os.path.isdir(destination):
        os.mkdir(destination)
    
    image.save("/".join([destination,"temp.jpg"]))
    print("The file path ot save the incoming image to: ",destination)
    return render_template("index.html", tasks=filename)

if(__name__=="__main__"):
    app.run(debug=True)