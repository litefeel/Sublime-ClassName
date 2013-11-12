Sublime-ClassName
=============
sublime-ClassName is a tiny and simple plugin for [Sublime Text](http://www.sublimetext.com) .
It copy class full name to clipboard.

Usage
============
Install it using [Sublime Package Control](http://wbond.net/sublime_packages/package_control).


The default key bindings are 
- [ctrl+alt+c] : copy class full name of current file to clipboard.

You can also call ClassName commands when right-clicking files in the side bar.

Settings
==============

If you need you will be able to add the prefix and suffix of classname.  
please modify the path by selecting 
"Preferences->Package Settings->ClassName->Settings - User" in the menu.

The default setting is:

    {
        // set this string as prefix of class name
         "classname_prefix": "",
         // set this string as suffix of class name
         "classname_suffix": ""
    }

IMPORTANT
==============

1. How to find class full name.
An folder '`xxxx/src`' in sibe bar and an file '`xxxx/src/com/litefeel/MyClass.ext`', the file's class full name is '`com.litefeel.MyClass`'.
