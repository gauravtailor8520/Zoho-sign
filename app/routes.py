from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from app.zoho import ZohoSign

main = Blueprint('main', __name__)
zoho_client = ZohoSign()

@main.route('/')
def index():
    return render_template('contract.html')

@main.route('/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    if code:
        token_data = zoho_client.get_access_token(code)
        session['access_token'] = token_data.get('access_token')
        return redirect(url_for('main.index'))
    return 'Authorization failed', 400

@main.route('/sign', methods=['POST'])
def sign():
    if 'access_token' not in session:
        return redirect(zoho_client.get_auth_url())
    
    try:
        # Replace with your template ID
        template_id = "YOUR_TEMPLATE_ID"
        response = zoho_client.create_signing_request(
            session['access_token'],
            template_id
        )
        return redirect(response['sign_url'])
    except Exception as e:
        flash('Error creating signing request')
        return redirect(url_for('main.index'))

@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Handle signature completion webhook
    # Update your database or trigger necessary actions
    return '', 200
