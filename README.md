# google-java-format-sublime
A sublime plugin for formatting java code files with google-java-format

## Platforms supported:
Currently, it is only supported Linux(Ubuntu). Myabe it works on any platform by specfing corrrect path to the formatter by override `formatter-path`.

## Sublime version supported:
Currently, I tested on Sublime Text 4. However, it may run successfully for Sublime Text 3 as well.

## How to install the plugin

### Linux(Ubuntu) platform
1. Open Sublime.
2. Go to "Preferences -> Browse Packages".
3. This would open a Nautilus with the package path. For me, it opens up this path: "/home/ankit/.config/sublime-text-3/Packages/".
4. Clone the repo or download and extract the archive file at this location. After performing this step, I have google-java-format-sublime at the path "/home/ankit/.config/sublime-text-3/Packages/google-java-format-sublime".
5. Its done.

## How to run:

Default Ctrl+Shift+g for Linux, Control+Shift+g for OSX.

You can specify any version of google-java-format by override `formatter-path` in the configuration. (Default: v1.8)

## Reference:
https://github.com/google/google-java-format
