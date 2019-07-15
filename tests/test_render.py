import unittest

import render


class TestRender(unittest.TestCase):

    def test_render_to_js_single_line(self):
        query = "db.getCollection('rating_class_detail').count({});"
        render.render_to_js(query)

    def test_render_to_js_multiple_lines(self):
        query = """
        var dealOrg = db.getCollection('organization').distinct('deal_org_id',{$and:[{$or:[{"deal_org_id":
        {$exists:true}},{"deal_sponsor_id":{$exists:true}}]},{"facets.Facet.Key":"Covered_Bonds"}]})
        var dealSpor = db.getCollection('organization').distinct('deal_sponsor_id',{$and:[{$or:[{"deal_org_id":{
        $exists:true}},{"deal_sponsor_id":{$exists:true}}]},{"facets.Facet.Key":"Covered_Bonds"}]})
        db.getCollection('sfg_debt').find({$and:[{$or:[{'orig_org_id':{$in:dealOrg}},
        {'orig_org_id':{$in:dealSpor}}]},{'sponsor':{$exists:true}},
        {$or:[{"ratg_txt":{$exists:false}},
        {'ratg_dirn':{$exists:false}},
        {'debt_senr':{$exists:false}},
        {'ratg_clss':{$exists:false}},
        {'inst_id':{$exists:false}},
        {'org_id':{$exists:false}},
        ]}
        ]}).count()
        """
        render.render_to_js(query)
