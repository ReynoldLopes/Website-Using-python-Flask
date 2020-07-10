from flask import Flask,render_template,url_for,flash,redirect
from form import Regristrationform,login

app=Flask(__name__)
app.config['SECRET_KEY']='73c498ad1854ef92ecea4d9163d2f928'
posts=[
    {
        "author":"Reynold Lopes",
        "date_posted":"20/01/2000",
        "title":"My Blog",
        "content":"This is the fist blog"
    },
    {
        "author":"Michael J.",
        "date_posted":"20/01/1991",
        "title":"My Blog123",
        "content":"This is blog"
    }


]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
@app.route("/about")
def about():
    return "This is about"
@app.route("/registration",methods=['GET','POST'])
def registration():
    form=Regristrationform()
    if form.validate_on_submit():
        flash(f"Account Successfully Created for {form.username.data}",'success')
        return redirect(url_for("home"))

    return render_template("register.html",form=form,title="Register")
@app.route("/Login",methods=['GET','POST'])
def Login():
    form = login()
    if form.validate_on_submit():
        flash(f" Successfully Loged In for {form.email.data}",'success')
        return redirect(url_for("home"))
    return render_template("login.html",form=form,title="LogIn")


if __name__=="__main__":
    app.run(debug=True)