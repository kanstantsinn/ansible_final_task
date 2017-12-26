from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
import re

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        ret = []
        regex = 'Firefox'
        i = 0
        for term in terms:
            lookupfile = self.find_file_in_search_path(variables, 'files', term)
            contents, show_data = self._loader._get_file_contents(lookupfile)
            tmp = contents.split('\n')
            for line in tmp:
              if re.search(regex, line):
                i = i + 1
        ret.append(i)
        return ret



