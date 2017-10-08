Material Design Icons Manager: a **Python** binary dedicated to Material Design Icons handling.

## Features
- Icons updates handling
- Icons requiring into Xcode projects
- [TODO] Icons colorizing


## Installation

### Manually

Clone this repo with the following command:

```
  $ git clone https://github.com/leloupnicolas/MaterialDesignIconsManager.git /path/where/you/want/it
```

Make the script usable everywhere:

```
  $ ln -s /usr/local/bin/mdim /path/where/you/want/it/mdim
```

That's all!

## How To

### Choose an icon

Find out the icon's group and name you want to use on [material.io/icons](https://material.io/icons/).

### Import the icon
The following example imports the `event` icon from the `action` to the `Assets.xcassets` assets catalog, in the current Xcode project.

```
  $ mdim require --group=action --icon-name=event
```

This example imports the `event` icon from the `action` to the `MyCustomCatalog.xcassets ` assets catalog, renaming the icon with the name `MyIcon`.

```
  $ mdim require --group=action --icon-name=event --assets-catalog-name=MyCustomCatalog.xcassets --rename-with=MyIcon
```

## Contributing

- If you **need help**, **have a feature request** or **found a bug**, open an issue.
- If you **want to contribute**, submit a pull request.


## Credits

Need is owned and maintained by Nicolas LELOUP [@leloupnicolas](https://twitter.com/leloupnicolas).


## License

This project is licensed under the MIT license.

Copyright (c) 2017 Nicolas LELOUP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.⏎    