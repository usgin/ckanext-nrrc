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
        facets_dict['organization'] = _('Organizations')
        facets_dict['groups'] = _('Groups')
        facets_dict['tags'] = _('Tags')
        facets_dict['custom_text4'] = _('Statuses')
        facets_dict['custom_text5'] = _('Deadlines')
        return facets_dict

    def group_facets(self, facets_dict, organization_type, package_type):
        facets_dict = OrderedDict()
        facets_dict['tags'] = _('Tags')
        facets_dict['custom_text4'] = _('Statuses')
        facets_dict['custom_text5'] = _('Deadlines')
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict = OrderedDict()
        facets_dict['groups'] = _('Groups')
        facets_dict['tags'] = _('Tags')
        facets_dict['custom_text4'] = _('Statuses')
        facets_dict['custom_text5'] = _('Deadlines')
        return facets_dict

    def get_helpers(self):
        return {}

    def before_map(self, map):
        controller = 'ckanext.nrrc.client.controllers.view:ViewController'
        map.connect('notifications', 'organization/notifications', controller=controller, action='render_notifications')
        map.connect('documents', 'organization/documents', controller=controller, action='render_documents')
        map.connect('map_search', '/map_search', controller=controller, action='render_map_search')
        map.connect('library_search', '/library_search', controller=controller, action='render_library_search')
        map.connect('resources', '/resources', controller=controller, action='render_resources')
        map.connect('contribute', '/contribute', controller=controller, action='render_contribute')
        map.connect('harvest', '/harvest_nrrc', controller=controller, action='render_harvest')
        return map

    #def after_map(self, map):
     #   return

    def _modify_package_schema(self, schema):
        schema.update({
            'custom_text1': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text2': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text3': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text4': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text5': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text6': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text7': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text8': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text9': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text10': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text11': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'custom_text12': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(NRRCClient, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(NRRCClient, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(NRRCClient, self).show_package_schema()
        schema.update({
            'custom_text1': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text2': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text3': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text4': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text5': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text6': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text7': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text8': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text9': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text10': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text11': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'custom_text12': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        return True

    # Note: Make sure that this is the correct package_type
    def package_types(self):
        return []