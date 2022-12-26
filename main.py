from ytmusicapi import YTMusic
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

ytmusic = YTMusic('headers_auth.json')
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    res = ytmusic.get_home(5)
    return jsonify({"data": res})


@app.route('/song', methods=['GET'])
def get_song():
    song_id = request.args.get('id')
    if song_id is None:
        res = 'please provide song ID'
    else:
        res = ytmusic.get_song(song_id)
    return jsonify({"data": res})


@app.route('/album', methods=['GET'])
def get_album():
    album_id = request.args.get('id')
    if album_id is None:
        res = 'please provide album ID'
    else:
        res = ytmusic.get_album(album_id)
    return jsonify({"data": res})


@app.route('/artist', methods=['GET'])
def get_artist():
    artist_id = request.args.get('id')
    if artist_id is None:
        res = 'please provide Artist ID'
    else:
        res = ytmusic.get_artist(artist_id)
    return jsonify({"data": res})


@app.route('/playlist', methods=['GET'])
def get_playlist():
    playlist_id = request.args.get('id')
    if playlist_id is None:
        res = 'please provide playlist ID'
    else:
        res = ytmusic.get_playlist(playlist_id)
    return jsonify({"data": res})


if __name__ == '__main__':
    app.run(debug=True, port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
