"""A video player class."""
import random
from .video_library import VideoLibrary

playing_video = []
paused_video = []
playlist = {"":[]}
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        list_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        print_list = []
        for i in range(len(list_videos)):
            temp=""
            temp += list_videos[i].title + " " + "(" + list_videos[i].video_id + ")" + " " + "["
            for j in range(len(list_videos[i].tags)):
                temp += list_videos[i].tags[j]
                if j != len(list_videos[i].tags)-1:
                    temp += " " 
            temp += "]"
            print_list.append(temp)
        print_list.sort(key = lambda x: x.split()[0])
        for i in range(len(print_list)):
            print(print_list[i],end="\n")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        list_videos = self._video_library.get_all_videos()
        flag = 0
        for i in range(len(list_videos)):
            if list_videos[i].video_id == video_id:
                flag = 1
                if(playing_video.count(video_id) == 0 and len(playing_video) == 0):
                    print("Playing video: " + list_videos[i].title)
                    playing_video.append(list_videos[i].video_id)
                else:
                    for x in range(len(list_videos)):
                        if list_videos[x].video_id == playing_video[0]:
                            name = list_videos[x].title
                            print("Stopping video: " + name)
                            playing_video.pop(0)
                            print("Playing video: " + list_videos[i].title)
                            playing_video.append(list_videos[i].video_id)
                            break
        if flag == 0:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if(len(playing_video) == 0):
            print("Cannot stop video: No video is currently playing")
        else:
            list_videos = self._video_library.get_all_videos()
            for x in range(len(list_videos)):
                if list_videos[x].video_id == playing_video[0]:
                    name = list_videos[x].title
                    print("Stopping video: " + name)
                    playing_video.pop(0)
                    break

    def play_random_video(self):
        """Plays a random video from the video library."""

        list_videos = self._video_library.get_all_videos()
        id_list = []
        for i in range(len(list_videos)):
            id_list.append(list_videos[i].video_id)
        if(len(id_list) == 0):
            print("No videos available")
        else:
            video_id_random = random.choice(id_list)
            for i in range(len(list_videos)):
                if list_videos[i].video_id == video_id_random:
                    if(playing_video.count(video_id_random) == 0 and len(playing_video) == 0):
                        print("Playing video: " + list_videos[i].title)
                        playing_video.append(list_videos[i].video_id)
                    else:
                        for x in range(len(list_videos)):
                            if list_videos[x].video_id == playing_video[0]:
                                name = list_videos[x].title
                                print("Stopping video: " + name)
                                playing_video.pop(0)
                                print("Playing video: " + list_videos[i].title)
                                playing_video.append(list_videos[i].video_id)
                                break

    def pause_video(self):
        """Pauses the current video."""
        if len(playing_video) == 0:
            print("Cannot pause video: No video is currently playing")
        else:
            list_videos = self._video_library.get_all_videos()
            if len(paused_video) == 1:
                for x in range(len(list_videos)):
                    if list_videos[x].video_id == paused_video[0]:
                        print("Video already paused: " + list_videos[x].title)
                        break
            else:
                paused_video.append(playing_video[0])
                for x in range(len(list_videos)):
                    if list_videos[x].video_id == playing_video[0]:
                        print("Pausing video: " + list_videos[x].title)

    def continue_video(self):
        """Resumes playing the current video."""
        if len(paused_video) == 0:
            print("Cannot continue video: Video is not paused")
        else:
            list_videos = self._video_library.get_all_videos()
            for x in range(len(list_videos)):
                if len(paused_video) > 0 and list_videos[x].video_id == paused_video[0]:
                    print("Continuing video: " + list_videos[x].title)
                    paused_video.pop(0)
                    break

    def show_playing(self):
        """Displays video currently playing."""
        if len(playing_video) == 0:
            print("No video is currently playing")
        else:
            list_videos = self._video_library.get_all_videos()
            for x in range(len(list_videos)):
                if list_videos[x].video_id == playing_video[0]:
                    print("Currently playing: " + list_videos[x].title + " (" + list_videos[x].video_id + ") [", end="")
                    for j in range(len(list_videos[x].tags)):
                        print(list_videos[x].tags[j], end="")
                        if j != len(list_videos[x].tags)-1:
                            print("", end=" ") 
                    print("]",end="")
                    if len(paused_video) > 0 and list_videos[x].video_id == paused_video[0]:
                        print(" - PAUSED")
                    else:
                        print("")
                    break

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if len(playlist) == 0:
            playlist[playlist_name] = []
            print("Successfully created new playlist: " + playlist_name)
        else:
            flag = 0
            for x in playlist.keys():
                if x.upper() == playlist_name.upper():
                    flag = 1
                    print("Cannot create playlist: A playlist with the same name already exists")
                    break
            if flag == 0:
                playlist[playlist_name] = []
                print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        flag1 = 0
        flag2 = 0
        for x in playlist.keys():
            if x.upper() == playlist_name.upper():
                for key,value in playlist.items():
                    if key == x:
                        for i in range(len(value)):
                            if value[i] == video_id:
                                flag2 = 1
                                break
                        if flag2 == 0:
                            playlist[x].append(video_id)
                            list_videos = self._video_library.get_all_videos()
                            for x in range(len(list_videos)):
                                if list_videos[x].video_id == video_id:
                                    name = list_videos[x].title
                                    break
                            print("Added video to my_playlist: "+ name)
                flag1 = 1
                break
        if flag1 == 0:
            print("Cannot add video to " + playlist_name +": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(playlist) == 1:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:",end = "")
            for i in sorted(playlist.keys()):
                print(i)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        flag1 = 0
        print("Showing playlist: " + playlist_name)
        for key,value in playlist.items():
            if key == playlist_name:
                flag1 = 1
                list_videos = self._video_library.get_all_videos()
                if len(value) == 0:
                    print("No videos here yet")
                else:
                    for i in range(len(value)):
                        for x in range(len(list_videos)):
                            if value[i] == list_videos[x].video_id:
                                print(list_videos[x].title + " (" + list_videos[x].video_id + ") [", end="")
                                for j in range(len(list_videos[x].tags)):
                                    print(list_videos[x].tags[j], end="")
                                    if j != len(list_videos[x].tags)-1:
                                        print("", end=" ") 
                                print("]",end="")
                                if len(paused_video) > 0 and list_videos[x].video_id == paused_video[0]:
                                    print(" - PAUSED")
                                else:
                                    print("")
                                break
        if flag1 == 0:
            print("Cannot show playlist " + playlist_name +": Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
