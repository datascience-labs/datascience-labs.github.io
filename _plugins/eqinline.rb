# Author: Trevor Bedford
# License: MIT
require 'liquid'

module Jekyll
	class EqInline < Liquid::Tag
		include ::Liquid::StandardFilters

		def initialize(tag_name, text, tokens)
		  super
		  @text = text.strip
		end

		def render(context)

			require 'execjs'

			parsed = Liquid::Template.parse(@markup).render context
			
			katexsrc = open("./js/katex.min.js").read
			@katex = ExecJS.compile(katexsrc)
			return eqn_to_html(parsed)

		end

		def eqn_to_html(string)
			return @katex.call("katex.renderToString", string)
		end

	end
end

Liquid::Template.register_tag('eqinline', Jekyll::EqInline)
