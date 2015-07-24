from codebase import app
from flask import Flask,render_template, request, url_for, redirect,flash
from codebase import models

   

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/RestaurantEntry')
def RestaurantEntry():
    return render_template('Restaurant_Entry.html')


@app.route('/SuccessRestaurantEntry')
def Success_SuccessRestaurantEntry():
    return render_template('SuccessRestaurantEntry.html')            



@app.route('/RestaurantMenu')
def RestaurantMenu():
    return render_template('Restaurant_Menu.html')

@app.route('/add_entry',methods=['GET','POST'])
def add_entry():
    error=None
    if request.method=='POST':
        _name=request.form['Rname']
        _address=request.form['Raddress']
        _phone=request.form['Rphone']
        _rating=request.form['Rrating']
        _description=request.form['Rdescription']
   
        i= models.insert_restaurant_entry(_name,_address,_phone,_rating,_description) 
        if i==1:
            flash("Entry done..")
            
            return redirect("/")
        else:
            flash('looks like that entry already exists')
            return redirect("/RestaurantEntry")   
    else:
        page_not_found(error)
        
        
        
@app.route('/add_menu',methods=['GET','POST'])    
def add_menu():
    error=None
    if request.method=='POST':
        _id1=request.form['RMid']
        _mdish=request.form['Mdish']
        _mprice=request.form['Mprice']
        _mdescription=request.form['Mdescription']
   
        i= models.insert_menu_entry(_id1,_mdish,_mprice,_mdescription)
        if i==1:
            flash("Entry done..")
            return redirect("/")                    
        else: 
            flash('looks like that entry already exists')
            return redirect("/RestaurantMenu")   
    else:
        page_not_found(error)
                    

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

