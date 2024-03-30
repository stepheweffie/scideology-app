from nicegui import ui
import subprocess
from dotenv import load_dotenv
import os
load_dotenv()
DO_REFERRAL = os.getenv('DO_REFERRAL')
AUTH_URL = os.getenv('AUTH_URL')
auth_url = AUTH_URL
square_auth_url = os.getenv('SQUARE_AUTH_URL')


def create_droplet():
    subprocess.run(['python', 'snapshot_to_droplet.py'])


def do_auth():
    ui.open(auth_url, new_tab=True)


def do_account():
    ui.open(f'{DO_REFERRAL}', new_tab=True)


def open_payment():
    ui.open('https://square.link/u/sCQZfaJ5', new_tab=True)


def square_seller():
    ui.open('https://join.squareup.com/mQ7Vxuh', new_tab=True)


def authorize_square():
    ui.open(square_auth_url, new_tab=True)


@ui.page('/')
async def main():
    with ui.row():
        with ui.column():
            ui.label('Welcome to the Scideology App Service').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Open Digital Ocean Account for $200 Credit', on_click=do_account)
            ui.label('Setup A Square Seller Account').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Open Square Tab', on_click=square_seller)
            ui.label('Authenticate Digital Ocean Account').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Authenticate Digital Ocean Account', on_click=do_auth)
            ui.label('Payment').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Pay Now', on_click=open_payment)
            ui.label('Launch Your Setup Droplet').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Launch', on_click=create_droplet)
            ui.label('Authorize Your App To Take Square Payments').style(replace='font-size: 3.5vw; color: lightgrey;')
            ui.button('Authorize Square App', on_click=authorize_square)


@ui.page('/auth/payments')
async def payment():
    with ui.row():
        with ui.column():
            ui.label('Payment').style(replace='font-size: 3.5vw; color: lightgrey;')

ui.run()
