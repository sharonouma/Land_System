import pymysql
from user_crud.tables import LandOwners, TitleDeeds
from flask import Blueprint,flash, render_template, request, redirect, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from .models import TblUser, TitleDeed
from . import db
from json import dumps
from datetime import date
from sqlalchemy import delete
from flask_login import login_required, current_user
import pdfkit

main = Blueprint('main', __name__)

@main.route('/new_user')
@login_required
def add_user_view():

    return render_template('add.html')

@main.route('/login')
def login():

    return render_template('login.html')

@main.route('/')
def landing():

    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    print(len(TblUser.query.all()))
    return render_template('dashboard.html', titles=len(TitleDeed.query.all()), owners=len(TblUser.query.all()))

@main.route('/add', methods=['POST'])
@login_required
def add_user():
   
    try:
        
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _mobile = request.form['inputMobile']
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO tbl_user(user_name, user_email, user_password, phone_number) VALUES( %s, %s, %s, %s)"
            print(sql)
            new_user = TblUser(user_email=_email, user_name=_name, user_password=generate_password_hash(_password, method='sha256') ,phone_number=_mobile)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!')
            return redirect('/users')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        print("Saved.")


@main.route('/add-title-deed', methods=['POST'])
@login_required
def create_title_deed():
    
    try:
        
        location = request.form['location']
        area = request.form['area']
        plot_number = request.form['plot_number']
        id = request.form['id']
        # validate the received values
        if location and area and plot_number and serial_no and documentation_number and nature_of_title and issue_date and request.method == 'POST':
            # save edits
           
            new_title_deed = TitleDeed(location = location, area = area, plot_number = plot_number, serial_no=serial_no, documentation_number=documentation_number, nature_of_title=nature_of_title,issue_date=issue_date, owner_id=id)
            db.session.add(new_title_deed)
            db.session.commit()
            flash('Title deed added successfully!')
            return redirect('/add_title/' + id)
        else:
            return 'Error while adding title deed'
    except Exception as e:
        print(e)
    finally:
        print("Saved.")


@main.route('/users')
@login_required
def users():
    try:
        
        users = TblUser.query.all()
        for i in users:
            print(i.user_id)
        table = LandOwners(users)
        table.border = True
        table.classes = ["table", "table-striped"]
        return render_template('users.html', name=current_user.user_name, table=table)  
    except Exception as e:
        print(e)
    finally:
        print("Done.")
    
@main.route('/title-deeds')
@login_required
def title_deeds():
 
    try:
        
        users = db.session.query(TblUser, TitleDeed).join(TitleDeed, TitleDeed.owner_id == TblUser.user_id).all()
        print(users)
        return render_template('title_deeds.html',  data=users)  
    except Exception as e:
        print(e)
    finally:
        print("Done.")

@main.route('/edit/<int:id>')
@login_required
def edit_view(id):

    try:
        user = TblUser.query.get(id)
        
        if user:
            return render_template('edit.html', row=user)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        print("Done.")


@main.route('/add_title/<int:id>')
@login_required
def add_title_deed_view(id):
    try:
        row = TitleDeed.query.get(id)
        print(row.owner_id)
        return render_template('add_title_deed.html', id=id)
    except Exception as e:
        print(e)
    

@main.route('/update', methods=['POST'])
@login_required
def update_user():

    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _mobile = request.form['inputMobile']
        _id = request.form['id']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'POST':
        # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # save edits
            user = db.session.query(TblUser).get(_id)
            user.user_email = _email
            user.phone_number = _mobile
            user.user_password = _password
            user.user_name = _name
            db.session.commit()
            
            flash('User updated successfully!')
            return redirect('/users')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        print("done.")


@main.route('/delete/<int:id>')
@login_required
def delete_user(id):
    
    try:
        user = db.session.query(TblUser).get(id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!')
        return redirect('/users')
    except Exception as e:
        print(e)
    finally:
        print("done.")

@main.route('/test-search')
@login_required
def test_search():
    users = db.session.query(TblUser, TitleDeed).join(TitleDeed, TitleDeed.owner_id == TblUser.user_id).all() 
    
    count = 0
    for row in users :
        print(users[count][1].location)
        print("(")
        count=count+1
        for item in row:
            print(str(count) + "   ", item)
            
        print(")") 
    return ""

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    
@main.route('/print-title/<int:id>')  
def pdf_template(id):
    users = db.session.query(TblUser, TitleDeed).join(TitleDeed, TitleDeed.owner_id == TblUser.user_id, ).filter(TitleDeed.id==id) 
    print(users[0])
    for row in users:
        print (row[0].user_name)
    rendered = render_template('title-pdf.html', title=users[0])
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(rendered, configuration=config)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    
    return response
