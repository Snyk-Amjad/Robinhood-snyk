from app.forms import WatchlistForm
from app.models import User, db, Watchlist, Asset
from flask_login import login_required
from flask import Blueprint, request

watchlist_routes = Blueprint('watchlists', __name__)



# get a users watchlists (read)
@watchlist_routes.route('/<int:id>')
@login_required
def user_watchlists(id):
    user = User.query.get(id)
    return {watchlist.id:watchlist.to_dict() for watchlist in Watchlist.query.filter(Watchlist.user_id==user.id).all()}


# add a watchlists (create)
@watchlist_routes.route('/add', methods=["POST"])
@login_required
def add_watchlists():
    user = User.query.get(watchlist.user_id)
    form = WatchlistForm()

    if(form.validate_on_submit):
        watchlist = Watchlist(
            name = form.data["name"],
            user_id = form.data["user_id"]
        )
        db.session.add(watchlist)
        db.session.commit()
        return user.to_dict()
    else:
        return None


# edit watchlists (update)
@watchlist_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
def edit_watchlists(id):
    user = User.query.get(watchlist.user_id)
    watchlist = Watchlist.query.get(id)
    form = WatchlistForm()

    if(form.validate_on_submit):
        watchlist.name = form.data["name"]
        watchlist.user_id = form.data["user_id"]
        db.session.commit()
        return user.to_dict()
    else:
        return None


# delete watchlist (destroy)
@watchlist_routes.route('/<int:id>/delete', methods=["DELETE"])
@login_required
def delete_watchlists(id):
    user = User.query.get(watchlist.user_id)
    watchlist = Watchlist.query.get(id)
    db.session.delete(watchlist)
    db.session.commit

    return user.to_dict()

#add assest watchlist
@watchlist_routes.route('/<int:id>/add', methods=["POST"])
@login_required
def add_to_watchlist(id):
    symbol = request.json['symbol']
    watchlist = Watchlist.query.get(id)
    assest = assest.query.filter_by(symbol=symbol).first()
    db.session.add(stock)
    db.session.commit()
    watchlist.watched_assets.append(stock)
    db.session.commit()
    user = User.query.get(watchlist.user_id)
    return user.to_dict()


#delete assest from a specfic watchlist
