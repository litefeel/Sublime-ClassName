# ClassName

[![Build Status](https://travis-ci.org/litefeel/Sublime-ClassName.svg?branch=master)](https://travis-ci.org/litefeel/Sublime-ClassName)
[![Build status](https://ci.appveyor.com/api/projects/status/40vjxtplhvw82aw8/branch/master?svg=true)](https://ci.appveyor.com/project/litefeel/sublime-ClassName/branch/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/litefeel/Sublime-ClassName/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/litefeel/Sublime-ClassName/?branch=master)
[![codecov](https://codecov.io/gh/litefeel/Sublime-ClassName/branch/master/graph/badge.svg)](https://codecov.io/gh/litefeel/Sublime-ClassName)
<a href="https://packagecontrol.io/packages/ClassName"><img src="https://packagecontrol.herokuapp.com/downloads/ClassName.svg"></a>
<a href="https://www.paypal.me/litefeel/5usd" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" /></a>

ClassName is a tiny and simple plugin for [Sublime Text](http://www.sublimetext.com) .
It copy class full name and package path to clipboard.

### Installtion

1. Install it using [Sublime Package Control](https://packagecontrol.io/installation).
2. Run `Package Control: Install Package` command
3. find and install ClassName plugin.

### Usage

- Right click to copy class name and package path
- `Ctrl+Alt+C` to copy class name

### Key Bindings

Default Key Bindings:
~~~json5
[
    { "keys": ["ctrl+alt+c"], "command": "classname_copy" }
]
~~~

Change key bindings via menu:  
`Preferences > Package Settings > ClassName > Key Bindings`

### Settings

Default Settings:

~~~json5
{
    // set this string as prefix of class name
    "classname_prefix": "",
    // set this string as namespace separator
    "namespace_separator": ".",
    // set this string as suffix of class name
    "classname_suffix": ""
}
~~~

Change setting via menu:  
`Preferences > Package Settings > ClassName > Settings`

### Frequently Asked Questions

1. What is class full name?  
   If the path of a file in the sidebar is `src/com/litefeel/MyClass.lua`,  
   so the class full name is `com.litefeel.MyClass`.

2. What is package path?  
   If the path of a file in the sidebar is `src/com/litefeel/MyClass.lua`,  
   so the package path is `com.litefeel`.

### Related Links

homepage:<https://www.litefeel.com/sublime-classname/>  
github:<https://github.com/litefeel/Sublime-ClassName/>  
issues:<https://github.com/litefeel/Sublime-ClassName/issues>  
