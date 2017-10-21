# CliffExampleAddon

CliffExampleAddon is an addon for cliffdemo, demonstrating how a separate package can act as a plugin for cliffdemo

(cliffdemo is the demo app that comes with the cliff package)

# Install

You should probably do this in a virtualenv so you can remove the entire virtualenv later

Clone the cliff repo from github (https://github.com/openstack/cliff), then install cliffdemo

```
cd cliffdemo
pip install -e .
```

Then clone this addon

```
cd addon
pip install -e .
```

# Usage

```
$ cliffdemo simple
sending greeting
hi!
$ cliffdemo addon
addon sending greeting
addon hi!
```

# Check

```
$ pip uninstall cliffexampleaddon
... elided ...
$ cliffdemo addon
cliffdemo: 'addon' is not a cliffdemo command. See 'cliffdemo --help'.
Did you mean one of these?
  error
  unicode
$
```