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
        new_user.id = str(uuid.uuid4())
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
                      date=form.date.data, teamA=form.teamA.data,
                      teamB=form.teamB.data, ratio=form.ratio.data, maxParticipants=form.maxParticipants.data,
                      minParticipants=form.minParticipants.data, minVal=form.minVal.data, maxVal=form.maxVal.data,
                      sportType=form.sportType.data, active=True)
        new_bet.uuid = str(uuid.uuid4())
        db.session.add(new_bet)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f' There was an error creating a user: {err_msg}', category='danger')
        return redirect(url_for('home_page'))
    return render_template('buildContracts.html', form=form)


@app.route("/hardcoded", methods=['GET', 'POST'])
def hardCoded_page():
    # Dummy contract:
    dummy_numberOfParticipants = [1, 2, 3]
    dummy_date = ["10-10-2020", "2-2-2020", "3-3-2020"]
    dummy_sportType = ["football", "baseball", "basketball"]
    dummy_teamA = ["Tel-aviv", "Haifa", "Jerusalem"]
    dummy_teamB = ["Madrid", "FCB", "Juventus"]
    dummy_ratio = ["1:10", "2:7", "3:22"]
    dummy_maxParticipants = [4, 6, 4]
    dummy_minParticipants = [2, 2, 2]
    dummy_minVal = [100, 200, 300]
    dummy_maxVal = [1000, 2000, 300]

    for feed_data in zip(dummy_numberOfParticipants, dummy_date, dummy_sportType,
                         dummy_teamA, dummy_teamB, dummy_ratio, dummy_maxParticipants, dummy_minParticipants,
                         dummy_minVal, dummy_maxVal):
        feed = Bet(public=True, numberOfParticipants=feed_data[0],
                   date=feed_data[1], teamA=feed_data[3],
                   teamB=feed_data[4], ratio=feed_data[5], maxParticipants=feed_data[6],
                   minParticipants=feed_data[7], minVal=feed_data[8], maxVal=feed_data[9],
                   sportType=feed_data[2], active=True)
        feed.uuid = str(uuid.uuid4())

        db.session.add(feed)

    dummyUserName = ["Tamir", "Dor", "George"]
    dummyEmail = ["tamir@gmail.com", "dor@gmail.com", "george@gmail.com"]
    dummyPass = ["12345236", "12345643", "12345678"]
    dummyId = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]

    for feed_user in zip(dummyUserName, dummyEmail, dummyPass, dummyId):
        user = User(username=feed_user[0], email_address=feed_user[1],
                    password=feed_user[2], id=feed_user[3])

        db.session.add(user)

    db.session.commit()
    return redirect(url_for('home_page'))
