from app import app
from flask import render_template, send_file, request
from app.make_squares import create
import io, base64
from PIL import Image
import os

tmp_file_path = "/tmp/imgnew.png"


@app.route("/", methods=["GET"])
def index():
    graphic_image = create(tmp_file_path)
    return render_template("home.html", image=graphic_image)


@app.route("/generate-another", methods=["GET"])
def generate_another():
    graphic_image = create(tmp_file_path)
    response = f"""
    <img id="new-image" src="data:image/png;base64,{graphic_image}" />
    """
    return response


@app.route("/download", methods=["GET", "POST"])
def download():
    return send_file(
        tmp_file_path,
        mimetype="image/png",
        as_attachment=True,
        download_name="graphic.png",
    )
