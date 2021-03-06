import logging
import json

from pylons import config
from ckan import logic

import ckan.plugins as p
import ckan.lib.helpers as h

from ckanext.orgdashboards.helpers import (_get_action, 
                                           orgdashboards_get_geojson_properties)

log = logging.getLogger(__name__)

@p.toolkit.side_effect_free
def orgdashboards_show_datasets(context, data_dict):
    dd = data_dict.copy()
    dd.update({'include_datasets': True})
    
    data = _get_action('organization_show', context.copy(), dd)
    return data.pop('packages', [])

@p.toolkit.side_effect_free
def orgdashboards_dataset_show_resources(context, data_dict):
    data = _get_action('package_show', context.copy(), data_dict)
    
    return data.pop('resources', [])
    
@p.toolkit.side_effect_free
def orgdashboards_resource_show_resource_views(context, data_dict):
    data = _get_action('resource_view_list', context.copy(), data_dict)
    data = filter(lambda i: i['view_type'] == data_dict['view_type'], data)
    
    return data

@p.toolkit.side_effect_free
def orgdashboards_resource_show_map_properties(context, data_dict):
    return orgdashboards_get_geojson_properties(data_dict.get('id'))

@p.toolkit.side_effect_free
def orgdashboards_get_map_main_property(context, data_dict):
    dd = data_dict.copy()
    dd.update({'include_datasets': True})
    
    data = _get_action('organization_show', context.copy(), dd)

    if 'orgdashboards_map_main_property' in data:
        return data['orgdashboards_map_main_property']
    else:
        return None