import sublime
import sublime_plugin
import subprocess
import logging
import os

SETTINGS = 'google-java-format-sublime.sublime-settings'

logger = logging.getLogger('GoogleJavaFormat')


def get_user_settings():
    """Return user settings related to the plugin."""
    return sublime.load_settings(SETTINGS)

class GoogleJavaFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.is_enabled():
            if self.view.is_dirty():
                self.view.run_command('save')

            file_path = self.view.file_name()

            logger.info("Format", file_path)

            try:
                formatter = get_user_settings().get('formatter-path')
                if not formatter:
                    logger.error("Formatter not defined.")
                    return

                p = subprocess.Popen(
                    ['java', '-jar', formatter,
                     file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=None)
                stdout, stderr = p.communicate(timeout=get_user_settings().get('timeout', None))

                if p.returncode != 0:
                    # TODO: show warnings
                    return

                self.view.replace(edit,
                                  sublime.Region(0, self.view.size()),
                                  stdout.decode('utf-8'))
            except subprocess.TimeoutExpired as e:
                p.kill()
                logger.warn("Execution timeout")
            except Exception as e:
                logger.error("Failed to execute google-java-format.")
                raise

    def is_enabled(self):
        """
        Return whether the command is able to be run at this time.
        Command arguments are passed as keyword arguments. 
        """
        current_syntax = os.path.basename(self.view.settings().get('syntax'))
        syntax_list = get_user_settings().get('syntax_list', ["Java"])
        return os.path.splitext(current_syntax)[0] in syntax_list
