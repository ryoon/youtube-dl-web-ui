# Copyright (c) 2017 Ryo ONODERA <ryo@tetera.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from flask import Flask, render_template, json, request, make_response
app = Flask(__name__)

from subprocess import Popen, PIPE
from urllib.parse import quote

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/downloadVideo', methods=['POST'])
def downloadVideo():
    inputURI = request.form['inputURI']

    if inputURI:
      command = '/home/ryoon/youtube-dl-web-ui/pkg/bin/' + 'youtube-dl ' + '--format best[ext=mp4] --get-filename ' + inputURI
      process = Popen(command.split(), stdout=PIPE)
      stdout, error = process.communicate()
      exit_code = process.wait()
      if exit_code == 0:
        filename = stdout.strip().decode('utf-8')
      else:
        return render_template('index_error.html')
      command = '/home/ryoon/youtube-dl-web-ui/pkg/bin/' + 'youtube-dl ' + '--format best[ext=mp4] ' + '-o - ' + inputURI
      process = Popen(command.split(), stdout=PIPE)
      stdout, error = process.communicate()
      exit_code = process.wait()
      if exit_code == 0:
        response = make_response(stdout)
        response.headers['Content-Disposition'] = 'attachment;' "filename*=UTF-8''{utf8_filename}".format(utf8_filename=quote(filename))
        response.mimetype = 'application/octet-stream'
        return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)
