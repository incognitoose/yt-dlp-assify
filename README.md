## Installation
You should use yt-dlp from pip, not executable from releases page.  
Requires yt-dlp `2023.01.02` or above, and [YTSubConverter](https://github.com/arcusmaximus/YTSubConverter/releases/latest).

You can install this package with pip:
```sh
python3 -m pip install -U https://github.com/incognitoose/yt-dlp-assify/archive/master.zip yt-dlp
```
or with pipx:
```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install yt-dlp
pipx inject yt-dlp secretstorage
pipx inject yt-dlp https://github.com/incognitoose/yt-dlp-assify/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.


Ensure that [`YTSubConverter`](https://github.com/arcusmaximus/YTSubConverter/releases/latest) is in your PATH. You need `mono` if you are using Linux:
```sh
# After installing mono, ensure ~/.local/bin is in $PATH
mkdir -p ~/.local/YTSubConverter
cd ~/.local/YTSubConverter
curl -L https://github.com/arcusmaximus/YTSubConverter/releases/latest/download/YTSubConverter-Linux.tar.xz -o ~/.local/YTSubConverter/YTSubConverter.tar.xz
tar -vxf YTSubConverter.tar.xz
echo '#!/bin/bash' > ~/.local/bin/YTSubConverter
echo 'mono ~/.YTSubConverter/YTSubConverter.exe $@' >> ~/.local/bin/YTSubConverter
chmod +x ~/.local/bin/YTSubConverter
```

---

## Usage

To use it, simply run:

```sh
yt-dlp --embed-subs --postprocessor-args assify $YOUTUBE_URL
# Example:
yt-dlp -fba+bv --extractor-args youtube:skip=translated_subs --embed-subs --sub-lang=all,-live_chat --sub-format=srv3/ytt --use-postprocessor assify --embed-thumbnail --embed-metadata https://www.youtube.com/watch?v=8MImc3MxYZg
```

##### Note: output format must be .mkv without `--merge-format=mkv` because it won't fix error (at least on my environment)

---

## Contributing
Pull requests and issues are super welcome! Feel free to submit any bug reports.

---

## License

This project is licensed under The Unlicense, same as the [yt-dlp](https://github.com/yt-dlp/yt-dlp) does<!--, at least when commit -->. See the [LICENSE](LICENSE) file for details.

This repository contains a sample plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme). 

See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details.

## Development

See the [Plugin Development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) section of the yt-dlp wiki.
