ClassName
=============

[![Build Status](https://travis-ci.org/litefeel/Sublime-ClassName.svg?branch=master)](https://travis-ci.org/litefeel/Sublime-ClassName)
[![Build status](https://ci.appveyor.com/api/projects/status/40vjxtplhvw82aw8/branch/master?svg=true)](https://ci.appveyor.com/project/litefeel/sublime-ClassName/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/litefeel/Sublime-ClassName/badge.svg?branch=master)](https://coveralls.io/github/litefeel/Sublime-ClassName?branch=master)
[![codecov](https://codecov.io/gh/litefeel/Sublime-ClassName/branch/master/graph/badge.svg)](https://codecov.io/gh/litefeel/Sublime-ClassName)
<a href="https://packagecontrol.io/packages/ClassName"><img src="https://packagecontrol.herokuapp.com/downloads/ClassName.svg"></a>
<a href="https://www.paypal.me/litefeel/5usd" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" /></a>

ClassName is a tiny and simple plugin for [Sublime Text](http://www.sublimetext.com) .
It copy class full name and package path to clipboard.

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
        // set this string as namespace separator
        "namespace_separator": ".",
        // set this string as suffix of class name
        "classname_suffix": ""
    }

IMPORTANT
==============

1. How to find class full name.
An folder '`xxxx/src`' in sibe bar and an file '`xxxx/src/com/litefeel/MyClass.ext`', the file's class full name is '`com.litefeel.MyClass`'.
