
# tw2-proper imports
import tw2.core as twc
import tw2.forms as twf
from tw2.core.resources import encoder
from tw2.jquery import base as jqbase, defaults as jqdefaults

# imports from this package
from tw2.jqplugins.ui import base as jquibase
from tw2.jqplugins.elrte import base as elrtebase
from tw2.jqplugins.elrte import defaults

modname = 'tw2.jqplugins.elrte'

#elRTE
elrte_images = jqbase.DirLink(modname=modname, filename=defaults._plugin_css_dirname_ % dict(name=defaults._elrte_name_, version=defaults._elrte_version_, subdir="images"))
elrte_css = jqbase.jQueryPluginCSSLink(resources=[elrte_images], name=defaults._elrte_name_,
    basename='%s.%s' % (defaults._elrte_basename_, defaults._elrte_debug_),
    version=defaults._elrte_version_,
    modname = modname
    )
elrte_js = jqbase.jQueryPluginJSLink(name=defaults._elrte_name_,
    basename='%s.%s' % (defaults._elrte_basename_, defaults._elrte_debug_),
    modname = modname,
    version=defaults._elrte_version_)

class elRTEWidget(jquibase.JQueryUIWidget):
    resources = jquibase.JQueryUIWidget.resources + [elrte_css, elrte_js]
    template = 'tw2.jqplugins.elrte.templates.widget'
