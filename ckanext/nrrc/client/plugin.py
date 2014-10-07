import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.model as model
from ckan.common import OrderedDict, _

class NRRCClient(p.SingletonPlugin, tk.DefaultDatasetForm):


    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IDatasetForm)
    p.implements(p.IFacets, inherit=True)

    """
    p.implements(p.IActions)
    p.implements(p.IAuthFunctions)
    p.implements(p.IPackageController)
    p.implements(p.IDatasetForm)
    """

    def update_config(self, config):
        """
        Extends 'update_config' function in IConfigurer object.  Registers the
        templates and static files directories with CKAN.

        @config: Pylons global config object
        """
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')

    def dataset_facets(self, facets_dict, package_type):
        facets_dict = OrderedDict()
        #facets_dict['organization'] = _('Organizations')
        #facets_dict['groups'] = _('Groups')
        facets_dict['tags'] = _('Tags')
        return facets_dict

    def get_helpers(self):
        return {}

    def before_map(self, map):
        controller = 'ckanext.nrrc.client.controllers.view:ViewController'
        map.connect('harvest', '/harvest_nrrc', controller=controller, action='render_harvest')
        return map

    def is_fallback(self):
        return True

    # Note: Make sure that this is the correct package_type
    def package_types(self):
        return []