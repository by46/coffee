from jinja2 import nodes
from jinja2.ext import Extension

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers import guess_lexer


class PygmentsExtension(Extension):
    tags = set(['code'])

    def __init__(self, environment):
        super(PygmentsExtension, self).__init__(environment)
        environment.extend(pygments=self,
                           pygments_support=True)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        lang_type = parser.parse_expression()

        args = []

        if lang_type is not None:
            args.append(lang_type)

        body = parser.parse_statements(['name:endcode'], drop_needle=True)

        return nodes.CallBlock(self.call_method('_pygmentize', args), [], [], body).set_lineno(lineno)

    def _pygmentize(self, lang_type, caller):
        formatter = HtmlFormatter(linenos='table')
        content = caller()
        if lang_type is None:
            lexer = guess_lexer(content)
        else:
            lexer = get_lexer_by_name(lang_type)
        return highlight(content, lexer, formatter)
