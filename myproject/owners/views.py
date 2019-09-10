from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Puppy
from myproject.owners.forms import AddOwner

owners_blueprint=Blueprint('owners',__name__,template_folder='templates/owners')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():
    form=AddOwner()
    if form.validate_on_submit():
        owner=form.name.data
        id=form.id.data
        pup=Puppy.query.get(id)
        pup.owner=owner
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template("add_owner.html",form=form)
