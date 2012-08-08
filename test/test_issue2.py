# -*- coding: utf-8 -*-
"""
    test_issue2
    ~~~~~~~~~~~

    Test mixing of ``:cite:`` and ``[]_``.
"""

import nose.tools
from StringIO import StringIO

from util import *

srcdir = path(__file__).parent.joinpath('issue2').abspath()

def teardown_module():
    (srcdir / '_build').rmtree(True)

@with_app(srcdir=srcdir, warningiserror=True)
def test_mixing_citation_styles(app):
    app.builder.build_all()
    nose.tools.assert_equal(
        app.env.bibtex_cited, set([u"Test"]))
    nose.tools.assert_equal(
        app.env.bibtex_citation_label, {u"Test": "1"})

