import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut(object):

    def __init__(self):
        # /tut/tut02
        from tut02 import tut02Handler
        self.tut02 = tut02Handler
        # /tut/tut03
        from tut03 import tut03Handler
        self.tut03 = tut03Handler
        # /tut/tut04
        from tut04 import tut04Handler
        self.tut04 = tut04Handler
        # /tut/tut05
        from tut05 import tut05Handler
        self.tut05 = tut05Handler
        # /tut/tut06
        from tut06 import tut06Handler
        self.tut06 = tut06Handler
        # /tut/tut07
        from tut07 import tut07Handler
        self.tut07 = tut07Handler
        # /tut/tut08
        from tut08 import tut08Handler
        self.tut08 = tut08Handler
        # /tut/tut09
        from tut09 import tut09Handler
        self.tut09 = tut09Handler
