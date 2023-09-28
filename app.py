from flask import Flask, jsonify, url_for, redirect, request
from werkzeug.utils import secure_filename
from get_ext import get_ext
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config["MAX_CONTENT_LENGTH"] = 15 * (1024 * 1024)
app.config["UPLOAD_EXTENSIONS"] = get_ext()


@app.route("/<string:user_name>", methods=["POST"])
def upload_video(user_name):
    upload = request.files["file"]
    file_name = upload.filename
    file_name = secure_filename(file_name)
    if file_name == "":
        return jsonify({"error": "Bad Request", "message": "File has no name"}), 400
    file_ext = os.path.splitext(file_name)[1]
    if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
        return (
            jsonify(
                {"error": "Forbidden", "message": "This file type is not supported"}
            ),
            403,
        )

    if not os.path.exists(f"static/{user_name}"):
        os.mkdir(f"static/{user_name}")
    if os.path.exists(f"static/{user_name}/{file_name}"):
        return (
            jsonify(
                {"error": "bad request", "message": "this file name already exists"}
            ),
            400,
        )
    upload.save(os.path.join("static", user_name, file_name))
    return (
        jsonify(
            {
                "message": "success",
                "video_name": file_name,
                "video_url": url_for(
                    "get_video",
                    user_name=user_name,
                    video_name=file_name,
                    _external=True,
                ),
            }
        ),
        201,
    )


@app.route("/<string:user_name>")
def get_all_user_uploads(user_name):
    if not os.path.exists(os.path.join("static", user_name)):
        return jsonify({"message": "no uploads yet", "videos_urls": []}), 200
    videos = [
        {
            "video_name": f,
            "video_url": url_for(
                "get_video", user_name=user_name, video_name=f, _external=True
            ),
        }
        for f in os.listdir(os.path.join("static", user_name))
    ]
    return jsonify({"message": "success", "videos": videos}), 200


@app.route("/<string:user_name>/<string:video_name>")
def get_video(user_name, video_name):
    if not os.path.exists(os.path.join("static", user_name, video_name)):
        return (
            jsonify({"error": "Resource not found", "message": "Video does not exist"}),
            404,
        )

    return (
        redirect(
            url_for("static", filename=f"{user_name}/{video_name}", _external=True)
        ),
        302,
    )

@app.route("/")
def cron():
    return jsonify({
        "message":"success",
        "types":app.config["UPLOAD_EXTENSIONS"]

    }),200