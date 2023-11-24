# Web interface of youtube-dl command

To download YouTube videos, yt-dlp command is reliable way.
There are many Firefox add-ons to download YouTube videos,
however almost all free add-ons does not work as expected.

youtube-dl is not updated recently as of 2021-11-09
and it downloads videos very slowly (throttled).
yt-dlp has no problem for download rate.

## How to start
This uses yt-dlp, Flask 3.0.0 and Python 3.11.

For pkgsrc users, please run as follows.
(Be sure to install pkgsrc/net/yt-dlp 2021.10.22nb1 or later for TVer.)

```
$ cd ~/youtube-dl-web-ui
$ git clone git@github.com:ryoon/youtube-dl-web-ui.git app
$ cd pkgsrc/bootstrap
$ ./bootstrap --workdir /tmp/bs --unprivileged --prefix ~/youtube-dl-web-ui/pkg
$ echo PYTHON_VERSION_DEFAULT=39 >> ~/youtube-dl-web-ui/pkg/etc/mk.conf
$ cd pkgsrc/www/py-flask
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd pkgsrc/net/yt-dlp
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd ~/youtube-dl-web-ui/app
$ LANG=ja_JP.UTF-8 ~/youtube-dl-web-ui/pkg/bin/python3.9 app.py
```

For TVer.jp downloads, you should install FFmpeg.
For pkgsrc users, please install multimedia/ffmpeg6 as follows.
And your PATH environment variable must contain ~/youtube-dl-web-ui/pkg/bin.

```
$ cd pkgsrc/multimedia/ffmpeg6
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
```

And open http://localhost:5000/ with your browser on localhost.

## Screenshot
![browser](https://raw.githubusercontent.com/ryoon/youtube-dl-web-ui/master/screenshot.png)

## Bugs
* Not secure for the internet use

## Plans
* Add a description about nicovideo.jp download

## Contact
Ryo ONODERA <ryo@tetera.org>
