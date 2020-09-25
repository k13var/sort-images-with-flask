from flask import Flask, render_template, request
from model.input_form import InputForm
from model.sort_images import sort_images
from model.load_image import show_cluster_images

app = Flask(__name__)

# # Home Page
# @app.route('/',methods = ['GET'])
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = sort_images(form.n_clusters.data, form.model.data)
    else:
        result = None
    return render_template('index.html',
                           form=form, result=result)

@app.route('/sorted', methods=['GET', 'POST'])
def see_sorted():
    full_filename = show_cluster_images(100)
    return render_template('sorted.html', user_image = full_filename)


@app.route('/manual', methods=['GET', 'POST'])
def manual_sorting():
    return render_template('manual.html')
    
if __name__ == "__main__":
    app.run(debug=True)