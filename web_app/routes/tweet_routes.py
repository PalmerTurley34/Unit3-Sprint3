# from flask import Blueprint, jsonify, request, render_template, flash, redirect
# from web_app.models import db, Tweet, parse_records

# tweet_routes = Blueprint("tweet_routes", __name__)

# @tweet_routes.route("/tweets.json")
# def list_tweets():
#     tweet_records = Tweet.query.all()
#     tweets = parse_records(tweet_records)
#     return jsonify(tweets)

# # @tweet_routes.route("/tweets")
# # def list_tweets_for_humans():

# #     tweet_records = Tweet.query.all()
# #     print(tweet_records)
# #     tweets = parse_records(tweet_records)
# #     return render_template("tweets.html", message="Here's some books", books=books)

# @tweet_routes.route("/tweets/new")
# def new_tweet():
#     return render_template("new_tweet.html")

# @tweet_routes.route("/tweet/create", methods=["POST"])
# def create_tweet():
#     print("FORM DATA:", dict(request.form))

#     new_tweet = Tweet(tweet=request.form["Tweet"], user=request.form["user_name"])
#     db.session.add(new_tweet)
#     db.session.commit()

#     return jsonify({
#         "message": "TWEET CREATED OK (TODO)",
#         "tweet": dict(request.form)
#     })