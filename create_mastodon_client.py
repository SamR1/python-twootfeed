from config import get_config
from mastodon import Mastodon
from getpass import getpass

if __name__ == '__main__':
    print("This script helps you create a new mastodon client and log in.")
    print("Before we start, make sure config.yml exists.")
    config = get_config()

    mast_cfg = config['mastodon']
    print("Configuration found.")
    print("Looks like you want to use this instance:", mast_cfg['url'])
    print("If that's wrong, now is a good time to cancel (^C) and fix it.")
    input("<enter> to continue")

    print("Registering a new app with {url} called {app_name} and saving credentials in {client_id_file}".format(**mast_cfg))

    Mastodon.create_app(mast_cfg['app_name'], api_base_url=mast_cfg['url'], to_file=mast_cfg['client_id_file'], scopes=['read'])
    mastodon = Mastodon(client_id=mast_cfg['client_id_file'], api_base_url=mast_cfg['url'])
    print("Registration successful.  Now to log in.")
    user_email = input("User email: ")
    password = getpass("Password (not shown and not saved):")

    # Log in - either every time, or use persisted        
    mastodon.log_in(user_email, password, to_file=mast_cfg['access_token_file'], scopes=['read'])

    print("Verifying credentials...")
    try:
        res = mastodon.account_verify_credentials()
        print("Credentials look good; client reports user's account name is: " + res['acct'])
        print("Configuration complete; app should appear at: " + mast_cfg['url'] + "/oauth/authorized_applications")
        print("You should not need to log in again unless this app is removed or credentials expire.")
    except Exception as ex:
        print("Something went wrong; mastodon client reported an error:")
        print(ex)
    
