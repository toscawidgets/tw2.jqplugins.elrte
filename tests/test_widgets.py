from tw2.core.testbase import WidgetTest

import tw2.jqplugins.elrte.widgets as w

class TestelrteCSS(WidgetTest):
    widget = w.elrte_css
    attrs = {}
    params = {}
    expected = """
<link rel="stylesheet" type="text/css" href="/resources/tw2.jqplugins.elrte/static/jquery/plugins/elrte/1.2/css/elrte.full.css" media="all"/>
"""
class TestelrteJS(WidgetTest):
    widget = w.elrte_js
    attrs = {}
    params = {}
    expected = """
<script type="text/javascript" src="/resources/tw2.jqplugins.elrte/static/jquery/plugins/elrte/1.2/js/elrte.full.js"></script>
"""

class TestBase(WidgetTest):
    wrap = True
    widget = w.elRTEWidget
    attrs = {'id': 'widget'}
    params = {}
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elrte({});
});
</script>
"""

class TestAdvanced(TestBase):
    params = {
        'options': {
            'toolbar': 'maxi'
        }
    }
    wrap = True
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elrte({"toolbar": "maxi"});
});
</script>
"""
