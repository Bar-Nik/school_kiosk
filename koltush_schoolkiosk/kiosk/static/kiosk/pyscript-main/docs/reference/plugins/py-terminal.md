# &lt;py-terminal&gt;

This is one of the core plugins in PyScript, which is active by default. With it, you can print to `stdout` and `stderr` from your python code, and the output will be displayed on the page in `<py-terminal>`.

## Configuration

You can control how `<py-terminal>` behaves by setting the value of the `terminal` configuration in your `<py-config>`, together with the `docked` one.

For the **terminal** field, these are the values:

| value | description |
|-------|-------------|
| `false` | Don't add `<py-terminal>` to the page |
| `true` | Automatically add a `<py-terminal>` to the page |
| `"auto"` | This is the default. Automatically add a `<py-terminal auto>`, to the page. The terminal is initially hidden and automatically shown as soon as something writes to `stdout` and/or `stderr` |

For the **docked** field, these are the values:

| value | description |
|-------|-------------|
| `false` | Don't dock `<py-terminal>` to the page |
| `true` | Automatically dock a `<py-terminal>` to the page |
| `"docked"` | This is the default. Automatically add a `<py-terminal docked>`, to the page. The terminal, once visible, is automatically shown at the bottom of the page, covering the width of such page |

Please note that **docked** mode is currently used as default only when `terminal="auto"`, or *terminal* default, is used.

In all other cases it's up to the user decide if a terminal should be docked or not.


### Examples

```html
<py-config>
    terminal = true
    docked = false
</py-config>

<py-script>
    print("Hello, world!")
</py-script>
```

This example will create a new `<py-terminal>`, the value "Hello, world!" that was printed will show in it.

You can also add one (or more) `<py-terminal>` to the page manually.

```html
<py-script>
    print("Hello, world!")
</py-script>

<py-terminal></py-terminal>
```

```{note}
If you include a `<py-terminal>` in the page, you can skip `terminal` from your `<py-config>`.
```
