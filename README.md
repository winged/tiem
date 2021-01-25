# TIEM.

![](sshot.png)

## Web version

[Check it out](https://winged.ninja/clock.html)

## Commandline version

```bash
# fetch online
curl https://winged.ninja/clock-en.txt   # multiline
curl https://winged.ninja/clock-en-n.txt # inactive words hidden, one line

# run locally
python3 tiem.py  # normal version, english
python3 tiem.py ch # normal version, swiss german
python3 tiem.py nofill # don't show inactive filler words
python3 tiem.py nofill nocolor # only show time string, no coloring, no inactive words
```

## Contributions

Contributions are welcome (other languages, fixes, etc). Please make sure to
extend both HTML and python versions.

This was built as a quick hack, don't expect it to be perfect in every aspect

## License

Do whatever you want with it (WTFPL)
