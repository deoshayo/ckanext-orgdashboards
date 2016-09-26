ckan.module('orgdashboards_map', function ($, _) {
  "use strict";

  return {
    initialize: function () {
      
      ckan.orgdashboards.dashboardmap.init(this.options.id,
                                      this.options.countryname,
                                      this.options.mapurl,
                                      this.options.color,
                                      this.options.main_property);
    }
  }
});