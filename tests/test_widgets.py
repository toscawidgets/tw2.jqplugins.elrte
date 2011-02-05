from webob import Request
from webob.multidict import NestedMultiDict
from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest
from nose.tools import raises
from cStringIO import StringIO
from tw2.core import EmptyField, IntValidator, ValidationError
from tw2.jquery import widgets as twjqwidgets
from cgi import FieldStorage
import formencode

import webob
if hasattr(webob, 'NestedMultiDict'):
    from webob import NestedMultiDict
else:
    from webob.multidict import NestedMultiDict

import tw2.jqplugins.elrte.widgets as w

class TestjQueryJS(WidgetTest):
    widget = twjqwidgets.jquery_js
    attrs = {}
    params = {}
    expected = """
<script type="text/javascript" src="/resources/tw2.jquery/static/jquery/1.4.2/jquery.js"></script>
"""
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
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elrte({"toolbar": "maxi"});
});
</script>
"""
