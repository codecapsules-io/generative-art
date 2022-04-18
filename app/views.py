from app import app
from flask import render_template, send_file, request
from app.make_squares import create
import io, base64
from PIL import Image
import os

db_directory = os.getenv('PERSISTENT_STORAGE_DIR')

@app.route("/", methods=["GET"])
def index():
    graphic_image = create()
    return render_template('home.html', image=graphic_image)

@app.route("/generate-another", methods=["GET"])
def generate_another():
    graphic_image = create()
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(graphic_image, "utf-8"))))
    img.save(os.path.join(db_directory, "imgnew.png"))
    response = f"""
    <img id="new-image" src="data:image/png;base64,{graphic_image}" />
    """
    return response

#Straight away download with no intermediary save() step
@app.route("/download", methods=["GET", "POST"])
def download():
    #if request.method == 'POST':
    #base64_str = request.form['image']
    #image = io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8")))
    return send_file(os.path.join(db_directory, "imgnew.png"), mimetype='image/png', as_attachment=True, download_name="graphic.png")

#First save the image using the Pillow package
@app.route("/download-with-save", methods=["GET", "POST"])
def download_with_save():
    if request.method == 'POST':
        base64_str = request.form['image']
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
        img.save('imgnew.png')
        return send_file("../imgnew.png", mimetype='image/png', as_attachment=True, download_name="graphic.png")
    