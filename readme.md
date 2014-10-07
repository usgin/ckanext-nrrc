### NRRC Specific Config File Settings

    ckan.plugins = stats text_preview recline_preview pdf_preview resource_proxy datastore datapusher nrrc_client harvest ckan_harvester spatial_metadata spatial_query csw_harvester disqus

    ckan.site_title = NRRC
    ckan.site_logo = /base/images/nrrc-logo.png
    ckan.favicon = /images/icons/arizona.ico
    
    ckan.auth.create_unowned_dataset = false
    ckan.auth.create_dataset_if_not_in_organization = false
    
    disqus.name = nrrc
    ckanext.spatial.search_backend = solr
    
### Solr Schema in:

    /ckanext-nrrc/ckanext/nrrc/config/solr/schema.xml