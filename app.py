# Copyright (c) 2017, 2018, 2021, 2022, 2023 Ryo ONODERA <ryo@tetera.org>
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

from flask import Flask, render_template, json, request
app = Flask(__name__)

import subprocess
import urllib.parse

def get_command_resp(command):
  return subprocess.Popen(command, stdout=subprocess.PIPE,
    shell=True).communicate()

def get_command_ret(command):
  return subprocess.Popen(command, stdout=None,
    shell=True).wait()

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/downloadVideo', methods=['POST'])
def downloadVideo():
  ytdlpath = '/usr/pkg/bin/yt-dlp'
  ffmpegPath = '/usr/pkg/bin/ffmpeg7'
  inputURI = request.form['inputURI']
  hostname = urllib.parse.urlparse(inputURI).netloc
  youtubeMaxFilenameLength = 234

  print(inputURI)
  if hostname == 'www.nicovideo.jp':
    print('nicovideo.jp case')
    nico_userID = request.form['userID']
    nico_password = request.form['password']
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs --get-filename --format best[ext=mp4] --username ' + nico_userID + ' --password ' + nico_password + ' ' + inputURI
    videoFilename = get_command_resp(command)[0].strip().decode('utf-8')
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs --format best[ext=mp4] --username ' + nico_userID + ' --password ' + nico_password + ' ' + inputURI

  elif hostname == 'www.youtube.com':
    print('youtube case')
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs --output "%(title).150B [%(id)s].%(ext)s" --get-filename --ffmpeg-location ' + ffmpegPath + ' ' + inputURI
    videoFilename = get_command_resp(command)[0].decode(encoding='utf-8', errors='ignore')
    print('videoFilename =', videoFilename)
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs --ffmpeg-location ' + ffmpegPath + ' ' + inputURI
  elif hostname == 'tver.jp':
    print('TVer case')
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs --output "%(title).150B [%(id)s].%(ext)s" --get-filename ' + inputURI
    videoFilename = get_command_resp(command)[0].decode(encoding='utf-8', errors='ignore')
    print('videoFilename = ', videoFilename)
    command = 'cd static && ' + ytdlpath + ' --js-runtimes quickjs -w --concurrent-fragments 3 ' + '--output "%(title).150B [%(id)s].%(ext)s" --ffmpeg-location ' + ffmpegPath + ' ' + inputURI
  else:
    return json.dumps({'html': '<span>Download failed with error code: ' + str(error) + '</span><br>'})

  print(command)
  error = get_command_ret(command)
  print("Download has finished.")
  print(error)
  if error == 0:
    return json.dumps({'html': '<span>Downloaded: <a href="static/' + urllib.parse.quote(videoFilename).rstrip('%0A') + '" download>'+ videoFilename + '</a></span><br>'})
  else:
    return json.dumps({'html': '<span>Please input a URI.<span><br>'})

if __name__ == "__main__":
  app.run(host='0.0.0.0')
