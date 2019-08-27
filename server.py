from flask import (Flask, render_template)
import connexion

#app instance
app = connexion.App(__name__, specification_dir='./')

#swagger.yml
app.add_api('swagger.yml')

#route for "/"
@app.route('/')
def home():
    """
    @ localhost:5000/

    :return: template 'home.html'
    """
    return render_template('home.html')

#for standalone mode, run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)