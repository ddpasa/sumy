# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import math

from pprint import pformat
from .._compat import to_unicode, to_string, unicode, Counter


class TfDocumentModel(object):
    """Term-Frequency document model (term = word)."""
    def __init__(self, text, tokenizer):
        words = tokenizer.to_words(to_unicode(text))
        self._terms = Counter(map(unicode.lower, words))

    @property
    def magnitude(self):
        """
        Lenght/norm/magnitude of vector representation of document.
        This is usually denoted by ||d||.
        """
        return math.sqrt(sum(t**2 for t in self._terms.values()))

    @property
    def terms(self):
        return self._terms.keys()

    def term_frequency(self, term):
        """Returns frequency of term in document."""
        return self._terms.get(term, 0)

    def __repr__(self):
        return "<TfDocumentModel %s>" % pformat(self._terms)