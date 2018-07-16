import glob
import importlib
import os

from collections import namedtuple
from flask.helpers import safe_join
from flask import current_app as app, send_file, send_from_directory, abort
from Unit6.utils import (
    admins_only as admins_only_wrapper,
    override_template as utils_override_template,
    register_plugin_script as utils_register_plugin_script,
    register_plugin_stylesheet as utils_register_plugin_stylesheet,
    pages as db_pages
)


Menu = namedtuple('Menu', ['title', 'route'])
ADMIN_PLUGIN_MENU_BAR = []
USER_PAGE_MENU_BAR = []


def register_plugin_assets_directory(app, base_path, admins_only=False):
    """
    Registers a directory to serve assets

    :param app: A Unit6 application
    :param string base_path: The path to the directory
    :param boolean admins_only: Whether or not the assets served out of the directory should be accessible to the public
    :return:
    """
    base_path = base_path.strip('/')

    def assets_handler(path):
        return send_from_directory(base_path, path)

    if admins_only:
        asset_handler = admins_only_wrapper(assets_handler)

    rule = '/' + base_path + '/<path:path>'
    app.add_url_rule(rule=rule, endpoint=base_path, view_func=assets_handler)


def register_plugin_asset(app, asset_path, admins_only=False):
    """
    Registers an file path to be served by Unit6

    :param app: A Unit6 application
    :param string asset_path: The path to the asset file
    :param boolean admins_only: Whether or not this file should be accessible to the public
    :return:
    """
    asset_path = asset_path.strip('/')

    def asset_handler():
        return send_file(asset_path)

    if admins_only:
        asset_handler = admins_only_wrapper(asset_handler)
    rule = '/' + asset_path
    app.add_url_rule(rule=rule, endpoint=asset_path, view_func=asset_handler)


def override_template(*args, **kwargs):
    """
    Overrides a template with the provided html content.

    e.g. override_template('scoreboard.html', '<h1>scores</h1>')
    """
    utils_override_template(*args, **kwargs)


def register_plugin_script(*args, **kwargs):
    """
    Adds a given script to the base.html template which all pages inherit from
    """
    utils_register_plugin_script(*args, **kwargs)


def register_plugin_stylesheet(*args, **kwargs):
    """
    Adds a given stylesheet to the base.html template which all pages inherit from.
    """
    utils_register_plugin_stylesheet(*args, **kwargs)


def register_admin_plugin_menu_bar(title, route):
    """
    Registers links on the Admin Panel menubar/navbar

    :param name: A string that is shown on the navbar HTML
    :param route: A string that is the href used by the link
    :return:
    """
    am = Menu(title=title, route=route)
    ADMIN_PLUGIN_MENU_BAR.append(am)


def get_admin_plugin_menu_bar():
    """
    Access the list used to store the plugin menu bar

    :return: Returns a list of Menu namedtuples. They have name, and route attributes.
    """
    return ADMIN_PLUGIN_MENU_BAR


def register_user_page_menu_bar(title, route):
    """
    Registers links on the User side menubar/navbar

    :param name: A string that is shown on the navbar HTML
    :param route: A string that is the href used by the link
    :return:
    """
    p = Menu(title=title, route=route)
    USER_PAGE_MENU_BAR.append(p)


def get_user_page_menu_bar():
    """
    Access the list used to store the user page menu bar

    :return: Returns a list of Menu namedtuples. They have name, and route attributes.
    """
    return db_pages() + USER_PAGE_MENU_BAR


def bypass_csrf_protection(f):
    """
    Decorator that allows a route to bypass the need for a CSRF nonce on POST requests.

    This should be considered beta and may change in future versions.

    :param f: A function that needs to bypass CSRF protection
    :return: Returns a function with the _bypass_csrf attribute set which tells Unit6 to not require CSRF protection.
    """
    f._bypass_csrf = True
    return f


def init_plugins(app):
    """
    Searches for the load function in modules in the Unit6/plugins folder. This function is called with the current Unit6
    app as a parameter. This allows Unit6 plugins to modify Unit6's behavior.

    :param app: A Unit6 application
    :return:
    """
    modules = glob.glob(os.path.dirname(__file__) + "/*")
    blacklist = {'__pycache__'}
    for module in modules:
        module_name = os.path.basename(module)
        if os.path.isdir(module) and module_name not in blacklist:
            module = '.' + module_name
            module = importlib.import_module(module, package='Unit6.plugins')
            module.load(app)
            print(" * Loaded module, %s" % module)

    app.jinja_env.globals.update(get_admin_plugin_menu_bar=get_admin_plugin_menu_bar)
    app.jinja_env.globals.update(get_user_page_menu_bar=get_user_page_menu_bar)