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
    def render_map_search(self):
        pass
        #render('mapsearch/map_search.html')

    def render_library_search(self):
        pass

    def render_notifications(self):
        return h.url_for(controller='organization', action='read', id="notifications")

    def render_documents(self):
        return h.url_for(controller='organization', action='read', id="documents")

    def render_resources(self):
        pass

    def render_contribute(self):
        pass

    def render_harvest(self):
        redirect('/harvest')