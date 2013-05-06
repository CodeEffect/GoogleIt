# coding=utf-8
import sublime
import sublime_plugin

import webbrowser
import urllib


class GoogleItCommand(sublime_plugin.TextCommand):
    def run(self, edit, include_language=False):
        """Google the selected text.

"""
        view = self.view
        # Get the highlighted string to search for
        selected = view.sel()[0]

        # If start and end cursor points are the same then nothing is selected
        if selected.a == selected.b:
            return sublime.status_message('''No text selected!''')

        # Get the text of the selection
        searchText = view.substr(sublime.Region(selected.a, selected.b))

        # If include_language is set then we add the syntax of the file to the query
        if include_language:
            syntax = view.settings().get("syntax").replace("Packages/", "")
            syntax = syntax[0:syntax.find("/")]
            searchText = "%s %s" % (syntax, searchText)

        # BOSH!
        webbrowser.open_new_tab("https://www.google.co.uk/search?q=%s" % urllib.quote_plus(searchText))
