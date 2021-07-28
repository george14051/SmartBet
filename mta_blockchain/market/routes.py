from market import app, db
from market.models import User, Bet
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm, LoginForm, SearchForm, CreateStepOne
import uuid



@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email_address=form.email_address.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was an error creating a user: {err_msg}', category='danger')

    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email_address=form.email_address.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was an error creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route("/search_contract", methods=['GET', 'POST'])
def search_page():
    form = SearchForm()
    return render_template('search.html', form=form)

@app.route("/result/<id>", methods=['GET'])
def result_page(id):
    contracts = Bet.query.all()
    return render_template('result.html', contracts=contracts)

@app.route("/new_wallet")
def wallet_page():
    return render_template('newWallet.html')


@app.route("/make_bet", methods=['GET', 'POST'])
def contracts_page():
    form = CreateStepOne()
    if form.validate_on_submit():
        new_bet = Bet(public=form.public.data, numberOfParticipants=form.numberOfParticipants.data,
                      date=form.date.data, hour=form.hour.data, teamA=form.teamA.data,
                      teamB=form.teamB.data,  ratio=form.ratio.data, maxParticipants=form.maxParticipants.data,
                      minParticipants=form.minParticipants.data, minVal=form.minVal.data, maxVal=form.maxVal.data,
                      sportType=form.sportType.data, active=True, uuid=uuid.uuid4())
        db.session.add(new_bet)
        db.session.commit()
        print("done!")
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was an error creating a user: {err_msg}', category='danger')
        return redirect(url_for('home_page'))
    return render_template('buildContracts.html', form=form)
