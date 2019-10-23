import requests
import base64
import json

class spotify(object):
    def __init__(self,params):
        self.baseURL = "https://api.spotify.com/v1"
        self.clientID = params["clientID"]
        self.clientSecret = params["clientSecret"]
        self.refreshToken = params["refreshToken"]
        self.getAccessToken()
        self.userId = self.getUserId()

    def killToken(self):
        self.token = "Bad_TOKEN"
        self.header = {"Authorization":"Bearer " + self.token}

    def getAccessToken(self):
        authURL = "https://accounts.spotify.com/api/token"
        bodyParams = bodyParams = {
            "grant_type":"refresh_token",
            "refresh_token":self.refreshToken
        }
        headerConcat = (self.clientID + ":" + self.clientSecret).encode('UTF-8')
        header = {
            "Authorization":"Basic " + base64.b64encode(headerConcat).decode('ascii')
        }

        result = self.runRequest(mthd="POST",reqUrl=authURL, dta=bodyParams, head=header)
        if result.status_code != 200:
            print("There was an error with authentication")
            print(result.json())
        else:
            self.accessToken = result.json()["access_token"]
            self.header = {"Authorization": "Bearer " + self.accessToken}

    def addSongToPlaylistByUrl(self,listID,trackURL):
        songId = trackURL[trackURL.find("/track/")+7:]
        return self.addSongToPlaylistById(listID,songId)
        # return "Added " + songId + " to list: " + listID

    def addSongToPlaylistById(self,listID,trackID):
        if not self.trackInPlaylist(listID,trackID):
            url = self.baseURL + "/users/{0}/playlists/{1}/tracks".format(self.userId,listID)
            bodyParams = {"uris":[self.getURI(trackID)]}
            return self.runRequest(mthd="POST", reqUrl=url, dta=json.dumps(bodyParams)).json()
        else:
            return "Track already in playlist"

    def trackInPlaylist(self,listID,trackID):
        playList = self.getPlaylistTracks(listID, fields="total,items(track.id)")
        tracks = playList["items"]
        while playList["total"] > len(tracks):
            playList = self.getPlaylistTracks(listID, fields="total,items(track.id)", offset=len(tracks))
            tracks += playList["items"]
        for track in tracks:
            if trackID == track["track"]["id"]:
                return True
        return False

    def getPlaylistTracks(self,listID,fields="", offset=0):
        queryString = "?fields={0}&offset={1}".format(fields, offset)
        url = self.baseURL + '/users/{0}/playlists/{1}/tracks{2}'.format(self.userId,listID, queryString)
        return self.runRequest(reqUrl=url).json()

    def getUserId(self):
        url = self.baseURL + "/me"
        return self.runRequest(reqUrl=url).json()["id"]

    def getURI(self,trackId):
        url = self.baseURL + "/tracks/{0}".format(trackId)
        return self.runRequest(reqUrl=url).json()["uri"]

    def getCurrentTrack(self):
        url = self.baseURL + "/me/player/currently-playing"
        result = self.runRequest(reqUrl=url).json()
        return result["item"]["id"]

    def runRequest(self, reqUrl, head=None, mthd="GET", dta=None):
        retryLogic = False
        if not head:
            head = self.header
            retryLogic = True
        response = requests.request(mthd, reqUrl, headers=head, data=dta)
        print(reqUrl)
        print(response.status_code)
        if response.status_code > 299:
            if retryLogic and response.status_code == 401:
                self.getAccessToken()
                return self.runRequest(reqUrl, mthd=mthd, dta=dta)
        return response