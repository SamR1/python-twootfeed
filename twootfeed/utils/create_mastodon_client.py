import sys

import click
from mastodon import Mastodon
from twootfeed.utils.config import default_directory, get_config


@click.command()
def cli():
    click.secho(
        '\nThis script helps you create a new mastodon client and ' 'log in.',
        bold=True,
    )

    config = get_config()
    mast_cfg = config['mastodon']
    click.echo('\nConfiguration found.')

    click.echo(f"Looks like you want to use this instance: {mast_cfg['url']}")
    click.echo('If that\'s wrong, now is a good time to cancel and fix it.')
    click.confirm(
        click.style('Do you want to continue?', bold=True), abort=True
    )

    click.echo(
        '\nRegistering a new app with "{url}" called "{app_name}" and '
        'saving credentials in "{client_id_file}"'.format(**mast_cfg)
    )

    click.confirm(
        click.style('Do you want to continue?', bold=True), abort=True
    )

    try:
        Mastodon.create_app(
            mast_cfg['app_name'],
            api_base_url=mast_cfg['url'],
            to_file=default_directory + mast_cfg['client_id_file'],
            scopes=['read'],
        )
        mastodon = Mastodon(
            client_id=default_directory + mast_cfg['client_id_file'],
            api_base_url=mast_cfg['url'],
        )
    except Exception as ex:
        click.secho('Something went wrong!', bold=True, fg='red')
        click.secho(f'Mastodon registration reported an error: {ex}')
        sys.exit(1)

    click.secho('\nRegistration successful.', fg='green')
    click.echo('Now to log in.')
    user_email = click.prompt('User email', type=str)
    password = click.prompt(
        'Password (not shown and not saved)', hide_input=True
    )

    # Log in - either every time, or use persisted
    mastodon.log_in(
        user_email,
        password,
        to_file=default_directory + mast_cfg['access_token_file'],
        scopes=['read'],
    )

    click.echo('\nVerifying credentials...')
    try:
        mastodon.account_verify_credentials()
        click.secho("Credentials look good", fg='green')
        click.echo("Client reports user\'s account name is: {res['acct']}")
        click.echo(
            f"Configuration complete, app should appear at: "
            f"{mast_cfg['url']}/oauth/authorized_applications"
        )
        click.echo(
            'You should not need to log in again unless this app is '
            'removed or credentials expire.'
        )
    except Exception as ex:
        click.secho('Something went wrong!', bold=True, fg='red')
        click.secho(f'Mastodon client reported an error: {ex}')


if __name__ == '__main__':
    cli()
