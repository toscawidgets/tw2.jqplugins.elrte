tw2.jqplugins.elrte
=====================

:Author: Joseph Tate <jtate@dragonstrider.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/

tw2.jqplugins.elrte is a `toscawidgets2 (tw2)`_ wrapper for `elRTE`_.

Live Demo
---------
.. comment: Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.elrte>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.elrte>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.elrte>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.elrte/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`jQuery`_ is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

`elRTE`_ is a an open-source WYSIWYG HTML-editor written in JavaScript using jQuery UI. It features rich text editing, options for changing its appearance, style and many more. You can use it in any commercial or non-commercial projects.

Main goal of the editor - simplify work with text and formating (HTML) on sites, blogs, forums and other online services.

This module, tw2.jqplugins.elrte, provides `toscawidgets2 (tw2)`_ access to the
`elRTE`_ widget.

Sampling tw2.jqplugins.elrte in the WidgetBrowser
-------------------------------------------------

The best way to scope out ``tw2.jqplugins.elrte`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.elrte/tw2/jqplugins/elrte/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.elrte.git
    $ cd tw2.jqplugins.elrte
    $ mkvirtualenv tw2.jqplugins.elrte
    (tw2.jqplugins.elrte) $ pip install tw2.devtools
    (tw2.jqplugins.elrte) $ python setup.py develop
    (tw2.jqplugins.elrte) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
