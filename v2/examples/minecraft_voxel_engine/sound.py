import pygame, threading, time

class Mixer:

    def __init__(self, pygame_session:pygame):
        """
        Mixer class for playing tracks and audio/sounds
        """
        self.pygame = pygame_session

        self.pygame.mixer.init()

        self.t = threading.Thread(target=self.check_finished)

        self.events = []
        self.sounds = []

    def play_track(self, name):
        self.audio = self.pygame.mixer.Sound(f'./sounds/tracks/{name}')
        self.audio.play()
        self.audio.set_volume(40)

    def play_sound(self, filename):
        try:
            aud = self.pygame.mixer.Sound(filename)
        except: 
            print(f"MIXER ERROR : Sound '{filename}' not found. Not playing the sound.")
            return
        aud.play()
        aud.set_volume(45)
        self.sounds.append(aud)

    def stop_all_audio(self):
        self.delete_events_by_name("track_finished")
        if self.pygame.mixer.get_busy():
            # stop all audio channels
            self.audio.stop()
            for x in self.sounds:
                x.stop()
        else: print("WARNING; NO AUDIO CHANNELS PLAYING/BUSY") # no audio channels playing
    
    def check_finished(self):
        time.sleep(2)
        while True:
            if self.pygame.mixer.get_busy(): pass
            else:
                print("Track has finished.")
                for i in self.events:
                    if i['n'] == "track_finished":
                        i['f'](self)

    def start_checking(self, event_name):
        if event_name == "track_finished":
            self.t.start()
        else: print("MIXER ERROR: Unknown event name : {}".format(event_name))

    def on_event(self, event):
        if event.__name__ == "track_finished":
            self.events.append({
                "n": event.__name__,
                "f": event
            })
        return None

    def delete_events_by_name(self, name):
        for i in self.events:
            if i['n'] == name:
                # stop them
                del i
        print("DELETED EVENTS BY NAME: %s" % (name))