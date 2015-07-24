from codebase import mysql
#from flaskext.mysql import MySQL
from flask import Flask,render_template, request, url_for, session, redirect, escape,flash,jsonify
#mysql=MySQL()

#app.config['MYSQL_DATABASE_USER']='root'
#app.config['MYSQL_DATABASE_PASSWORD']='student'
#app.config['MYSQL_DATABASE_DB'] ='Restaurant'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)


        
        
        
        
def insert_restaurant_entry(name,address,phone,rating,desciption):
    conn=mysql.connect()
    cursor=conn.cursor()
    try:
        cursor.execute("""insert into Restaurant_Entry(RE_name,RE_address,RE_phoneNumber,RE_rating,RE_description) values (%s,%s,%s,%s,%s)""",(name,address,phone,rating,desciption))
        conn.commit()
        return 1
    except Exception, e:
        print "insert failed"+"str(e)"
        return 0
    
    finally:
        cursor.close()
        conn.close()
        
    
def select_restaurant_entry():
    conn=mysql.connect()
    cursor=conn.cursor()
    try:
        
        
        return jsonify(cursor.execute("select * from Restaurant_Entry").fetchall()) 
    except Exception, e:
        print "select failed"+"str(e)"
               
    finally:
        conn.close()
        cursor.close()
        
        
        
def insert_menu_entry(mid,dish,price,desciption):
    conn=mysql.connect()
    cursor=conn.cursor()
    try:
        cursor.execute("""insert into Restaurant_Menu(RM_REid,RM_dish,RM_price,RM_description) values (%s,%s,%s,%s)""",(mid,dish,price,desciption))
        conn.commit()
        return 1
    except Exception, e:
        print "insert failed"+"str(e)"
        return 0
    
    finally:
        cursor.close()
        conn.close()
            
        
    
def select_menu_entry():
    conn=mysql.connect()
    cursor=conn.cursor()
    try:
        
        return jsonify(cursor.execute("select * from Restaurant_Menu").fetchall())
    except Exception, e:
        print "select failed"+"str(e)"
               
    finally:
        conn.close()
        cursor.close()        
