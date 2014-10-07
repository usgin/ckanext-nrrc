import ckan.plugins as p
from ckan import model
import ckan.lib.base as base
import ckan.lib.helpers as h
from ckan.lib.base import BaseController, abort, response, render, redirect
from pylons.i18n import _

class ViewController(BaseController):
    """
    Controller object for rendering custom NRRC views and templates.
    @param BaseController: Vanillan CKAN object for extending controllers.
    """

    def render_harvest(self):
        redirect('/harvest')