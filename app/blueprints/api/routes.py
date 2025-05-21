from flask import Blueprint, render_template, request, jsonify

from app.app import db
from app.blueprints.api.models import Transaction, User

api = Blueprint('api', __name__, template_folder='templates',
                    static_folder='static', static_url_path='/static')


@api.route('/', methods=['GET'])
def index():
    return render_template('api/index.html')


@api.route('/get-transaction-all', methods=['GET'])
def get_transaction_all():
    transactions = Transaction.query.all()
    transac_list = []

    for t in transactions:
        transac_list.append(t.serialize)

    return jsonify(transac_list)


@api.route('/get-user-all', methods=['GET'])
def get_user_all():
    users = User.query.all()
    user_list = []

    for u in users:
        user_list.append(u.serialize)

    return jsonify(user_list)


@api.route('/get-user-transaction-all/<int:uid>', methods=['GET'])
def get_user_transaction_all(uid):
    transactions = Transaction.query.filter(Transaction.id_user == uid)
    transac_list = []

    for t in transactions:
        transac_list.append(t.serialize)

    return jsonify(transac_list)


@api.route('/get-transaction/<int:tid>', methods=['GET'])
def get_transaction(tid):
    transac = db.session.get(Transaction, tid)

    if transac is None:
        return render_template('404.html'), 404
    
    return jsonify(transac.serialize)


@api.route('/get-user/<int:uid>', methods=['GET'])
def get_user(uid):
    user = db.session.get(User, uid)

    if user is None:
        return render_template('404.html'), 404
    
    return jsonify(user.serialize)


@api.route('/get-user/<string:email>', methods=['GET'])
def get_user_email(email):
    user = User.query.filter(User.email == email).first()

    if user is None:
        return render_template('404.html'), 404
    
    return jsonify(user.serialize)


@api.route('/post-transaction', methods=['POST'])
def post_transaction():
    data = request.get_json()
    transac = Transaction(value=float(data['value']), date=data['date'], desc=data['desc'], id_category=0, id_user=data['id_user'])

    db.session.add(transac)
    db.session.commit()

    return jsonify({"message": "Success"})

@api.route('/post-user', methods=['POST'])
def post_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], password=data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Success"})
