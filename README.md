# Web interface of youtube-dl command

## How to start
This uses youtube-dl, Flask and Python 3.6.

For pkgsrc users, please run as follows.

```
$ cd ~/youtube-dl-web-ui
$ git clone git@github.com:ryoon/youtube-dl-web-ui.git app
$ cd pkgsrc/bootstrap
$ ./bootstrap --workdir /tmp/bs --unprivileged --prefix ~/youtube-dl-web-ui/pkg
$ echo PYTHON_VERSION_DEFAULT=36 >> ~/youtube-dl-web-ui/pkg/etc/mk.conf
$ cd pkgsrc/www/py-flask
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd pkgsrc/net/youtube-dl
$ ~/youtube-dl-web-ui/pkg/bin/bmake install
$ cd ~/youtube-dl-web-ui/app
$ ~/youtube-dl-web-ui/pkg/bin/python3.6 app.py
```

And open http://localhost:5000/ with your browser on localhost.
