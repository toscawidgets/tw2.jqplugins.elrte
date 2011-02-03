#!/bin/bash

devbase=development-deps
venv=$devbase/virtualenv-tw2.jquery
source $venv/bin/activate

pushd $devbase

pushd tw2.devtools
python setup.py install
popd

rm -rf tw2jquery
hg clone http://bitbucket.org/toscawidgets/tw2jquery
pushd tw2jquery
python setup.py install_lib install_egg_info
popd

popd

python setup.py install_lib install_egg_info && paster tw2.browser



