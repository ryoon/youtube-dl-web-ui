# Web interface of youtube-dl command

To download YouTube videos, youtube-dl command is reliable way.
There are many Firefox add-ons to download YouTube videos,
however almost all free add-ons does not work as expected.

## How to start
This uses youtube-dl, Flask and Python 3.7.

For pkgsrc users, please run as follows.

```
$ cd ~/youtube-dl-web-ui
$ git clone git@github.com:ryoon/youtube-dl-web-ui.git app
$ cd pkgsrc/bootstrap
$ ./bootstrap --workdir /tmp/bs --unprivileged --prefix ~/youtube-dl-web-ui/pkg
$ echo PYTHON_VERSION_DEFAULT=37 >> ~/youtube-dl-web-ui/pkg/etc/mk.conf
$ cd pkgsrc/www/py-flask
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd pkgsrc/net/youtube-dl
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd ~/youtube-dl-web-ui/app
$ LANG=ja_JP.UTF-8 ~/youtube-dl-web-ui/pkg/bin/python3.7 app.py
```

And open http://localhost:5000/ with your browser on localhost.

## Bugs
* Not secure for the internet use

## Plans
* Add a description about nicovideo.jp download

## Contact
Ryo ONODERA <ryo@tetera.org>
