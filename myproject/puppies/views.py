from flask import Blueprint,render_template,redirect,url_for,flash
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm,DeleteForm

puppies_blueprint=Blueprint('puppies',__name__,template_folder='templates/puppies')


@puppies_blueprint.route('/add',methods=['GET','POST'])
def add():
    form=AddForm()
    if form.validate_on_submit():
        name=form.name.data
        owner=form.owner.data
        if owner=='':
            new_pup=Puppy(name,None)
        else:
            new_pup=Puppy(name,owner)
        db.session.add(new_pup)
        db.session.commit()
        flash(f"We added {new_pup.name} to our database!")
        #return redirect(url_for('puppies.list'))
    return render_template("add.html",form=form)


@puppies_blueprint.route('/list')
def list():
    puppies=Puppy.query.all()
    return render_template("list.html",puppies=puppies)



@puppies_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form=DeleteForm()
    if form.validate_on_submit():
        id=form.id.data
        pup=Puppy.query.get(id)
        if pup:
            db.session.delete(pup)
            db.session.commit()
            flash(f"We removed {pup.name} from our database!")
            #return redirect(url_for("puppies.list"))
        else:
            flash(f"Please enter a valid ID ")
    return render_template("delete.html",form=form)
