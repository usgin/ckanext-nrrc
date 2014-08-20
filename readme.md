### NRRC Specific Config File Settings

    ckan.plugins = stats text_preview recline_preview pdf_preview resource_proxy datastore datapusher nrrc_client harvest ckan_harvester spatial_metadata spatial_query csw_harvester
    
    ckan.site_title = NRRC
    ckan.site_logo = /base/images/nrrc-logo.png
    ckan.favicon = /images/icons/arizona.ico
    ckan.featured_orgs = documents notifications
    
    ckan.auth.create_unowned_dataset = false
    ckan.auth.create_dataset_if_not_in_organization = false
    
    ckanext.spatial.search_backend = solr
    
### Solr Schema in:

    /ckanext-nrrc/ckanext/nrrc/config/solr/schema.xml