#!/usr/bin/env python
#
from mercurial.hgweb.hgweb_mod import hgweb
from mercurial.hgweb.hgwebdir_mod import hgwebdir

CONFIG = b'/var/hg/hgweb.config'
application = hgwebdir(CONFIG)
