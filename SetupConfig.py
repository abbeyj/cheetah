#-------Main Package Settings-----------#
name = 'Cheetah'
from src.Version import Version as version
maintainer = "R. Tyler Ballance"
author = "Tavis Rudd"
author_email = "cheetahtemplate-discuss@lists.sf.net"
url = "http://www.cheetahtemplate.org/"
packages = ['Cheetah',
            'Cheetah.Macros',            
            'Cheetah.Templates',
            'Cheetah.Tests',
            'Cheetah.Tools',
            'Cheetah.Utils',
            'Cheetah.contrib',
            'Cheetah.contrib.markdown',
            ]
classifiers = [line.strip() for line in '''\
  #Development Status :: 4 - Beta
  Development Status :: 5 - Production/Stable
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: MIT License
  Operating System :: OS Independent
  Programming Language :: Python
  Topic :: Internet :: WWW/HTTP
  Topic :: Internet :: WWW/HTTP :: Dynamic Content
  Topic :: Internet :: WWW/HTTP :: Site Management
  Topic :: Software Development :: Code Generators
  Topic :: Software Development :: Libraries :: Python Modules
  Topic :: Software Development :: User Interfaces
  Topic :: Text Processing'''.splitlines() if not line.strip().startswith('#')]
del line

package_dir = {'Cheetah':'src'}

import os
import os.path
from distutils.core import Extension

## we only assume the presence of a c compiler on Posix systems, NT people will
#  have to enable this manually. 
if os.name == 'posix':
    ext_modules=[Extension("Cheetah._namemapper", [os.path.join("src" ,"_namemapper.c")]
                           )
                 ]
else:
    ext_modules=[]


## Data Files and Scripts
scripts = ['bin/cheetah-compile',
           'bin/cheetah',
           ]
data_files = ['recursive: src *.tmpl *.txt LICENSE README TODO CHANGES',
              ]

description = "Cheetah is a template engine and code generation tool."

long_description = '''Cheetah is an open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks. Web
development is its principle use, but Cheetah is very flexible and is also being
used to generate C++ game code, Java, sql, form emails and even Python code.

Documentation
================================================================================
For a high-level introduction to Cheetah please refer to the User\'s Guide
at http://www.cheetahtemplate.org/learn.html

Mailing list
================================================================================
cheetahtemplate-discuss@lists.sourceforge.net
Subscribe at http://lists.sourceforge.net/lists/listinfo/cheetahtemplate-discuss

Credits
================================================================================
http://www.cheetahtemplate.org/credits.html

Recent Changes
================================================================================
See http://www.cheetahtemplate.org/CHANGES.txt for full details

'''
