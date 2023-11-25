import pygame, threading

class Mixer:

    def __init__(self, pygame_session:pygame):
        """
        Mixer class for playing tracks and audio/sounds
        """
        self.pygame = pygame_session

        self.pygame.mixer.init()

        self.t = threading.Thread(target=self.check_finished)

        self.events = []

    def play_track(self, name):
        self.audio = self.pygame.mixer.Sound(f'./sounds/tracks/{name}')
        self.audio.play()
        self.audio.set_volume(40)
    
    def check_finished(self):
        while True:
            if self.pygame.mixer.get_busy(): pass
            else:
                print("Track has finished.")
                for i in self.events:
                    if i['n'] == "track_finished":
                        i['f'](self)


    def on_event(self, event):
        if event.__name__ == "track_finished":
            self.events.append({
                "n": event.__name__,
                "f": event
            })
            self.t.start()
        return None