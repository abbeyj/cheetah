#!/usr/bin/env python
# $Id: FormatterDirective.py,v 1.3 2001/08/14 19:29:50 tavis_rudd Exp $
"""FormatterDirective Processor class Cheetah's codeGenerator

Meta-Data
================================================================================
Author: Tavis Rudd <tavis@calrudd.com>
License: This software is released for unlimited distribution under the
         terms of the Python license.
Version: $Revision: 1.3 $
Start Date: 2001/08/01
Last Revision Date: $Date: 2001/08/14 19:29:50 $
"""
__author__ = "Tavis Rudd <tavis@calrudd.com>"
__version__ = "$Revision: 1.3 $"[11:-2]

##################################################
## DEPENDENCIES ##

from types import StringType

# intra-package imports ...
import TagProcessor
import Formatters

##################################################
## CONSTANTS & GLOBALS ##

True = (1==1)
False = (0==1)

##################################################
## CLASSES ##

class Error(Exception):
    pass

class FormatterDirective(TagProcessor.TagProcessor):
    """A class for processing display logic tags in Cheetah Templates."""
    
    _token = 'formatterDirective'
    _tagType = TagProcessor.EXEC_TAG_TYPE

    def __init__(self, templateObj):
        TagProcessor.TagProcessor.__init__(self,templateObj)
        self._delimRegexs = self.simpleDirectiveReList(r'formatter[\f\t ]+(.+?)')
                    
    def translateTag(self, tag):
        """generate python code from setDirective tags, and register the vars with
        placeholderTagProcessor as local vars."""
        templateObj = self.templateObj()
        state = self.state()
        self.validateTag(tag)
        indent = self.setting('indentationStep')
        tagChunks = tag.split()

        theFormatters = self.templateObj()._theFormatters
        
        valueString = self.translateRawPlaceholderString(tag)
        val = self.evalPlaceholderString(valueString)

        if not val:
            formatter = str
            state['currFormatter'] = currFormatter = 'None'
            state['interactiveFormatter'] = False
        elif type(val) == StringType:
            if not theFormatters.has_key(val):
                klass = getattr(Formatters, val)
                formatter = klass( self.templateObj() ).format
            else:
                formatter = theFormatters[val]
            state['currFormatter'] = currFormatter = val
            state['interactiveFormatter'] = True
        else:
            formatter = val.format
            state['currFormatter'] = currFormatter = str(id(formatter))
            state['interactiveFormatter'] = True

        theFormatters[currFormatter] = formatter
        
        return indent*(state['indentLevel']) + \
               'format = self._theFormatters["' + currFormatter + '"]' + "\n" + \
               indent * state['indentLevel']
        