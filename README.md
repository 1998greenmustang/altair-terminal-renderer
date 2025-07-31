# altair-terminal-renderer

`altair_term.py` adds a new renderer to your Altair instance (and automatically selects it)

This allows you to display `alt.chart`s in the Python REPL or IPython or PTPython or whatever.

It uses [vl_convert](https://github.com/vega/vl-convert) to convert your VegaLite chart to a PNG and then uses [Term-Image](https://github.com/AnonymouX47/term-image) to display it.

## Using

I would recommend importing this into your `$PYTHONSTARTUP` file, but all you have to do is import it at all.

```python
import import_lib
import_lib.import_module("altair_term")
```
