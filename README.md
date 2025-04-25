## Installation
You should use yt-dlp from pip, not executable from releases page.  
Requires yt-dlp `2023.01.02` or above, and [YTSubConverter](https://github.com/arcusmaximus/YTSubConverter/releases/latest).

Install this package with pipx:
```sh
# python3 -m pip install --user pipx
# python3 -m pipx ensurepath
# pipx install yt-dlp
pipx inject yt-dlp secretstorage
pipx inject yt-dlp https://github.com/incognitoose/yt-dlp-assify/archive/master.zip
```
Or with pip:
```sh
python3 -m pip install -U https://github.com/incognitoose/yt-dlp-assify/archive/master.zip yt-dlp
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for other installation methods.

Make sure [YTSubConverter](https://github.com/arcusmaximus/YTSubConverter/releases/latest) is in your PATH. Linux users will need `mono`:
```sh
# After installing mono, ensure ~/.local/bin is in $PATH
mkdir -p ~/.local/YTSubConverter
cd ~/.local/YTSubConverter
curl -L https://github.com/arcusmaximus/YTSubConverter/releases/latest/download/YTSubConverter-Linux.tar.xz -o ~/.local/YTSubConverter/YTSubConverter.tar.xz
tar -vxf YTSubConverter.tar.xz
echo '#!/bin/bash' > ~/.local/bin/YTSubConverter
echo 'mono ~/.local/YTSubConverter/YTSubConverter.exe "$@"' >> ~/.local/bin/YTSubConverter
chmod +x ~/.local/bin/YTSubConverter
```

## Usage
To use it, simply run:
```sh
yt-dlp --embed-subs --postprocessor-args assify $YOUTUBE_URL
# Example:
yt-dlp -fba+bv --extractor-args youtube:skip=translated_subs --embed-subs --sub-lang=all,-live_chat --sub-format=srv3/ytt --use-postprocessor assify --embed-thumbnail --embed-metadata https://www.youtube.com/watch?v=8MImc3MxYZg
```

**Note:** Output format must be .mkv. Don't use `--merge-format=mkv` as it won't fix errors (at least in my environment this makes more unexceptable).

## Contributing
Pull requests and issues are welcome! Feel free to submit any bug reports.

## License
This project is licensed under The Unlicense, same as [yt-dlp](https://github.com/yt-dlp/yt-dlp). See the [LICENSE](LICENSE) file for details.

This repository contains a plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme).
See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details.

## Development
See the [Plugin Development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) section of the yt-dlp wiki.
