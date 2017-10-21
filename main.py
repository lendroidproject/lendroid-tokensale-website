from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def landing():
    """ Render the landing page continaing details about the Token Launch."""
    return render_template('index.html')

@app.route('/faq')
def faq():
    """ Render the 'Frequently Asked Questions' page that provides more details abou the protocol 
        and the Token Sale.
    """
    return render_template('faq.html')

@app.route('/lendroid-support-token')
def lendroid_support_token():
    """ Render the Lendroid Support Token page."""
    return render_template('lendroid-support-token.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
