import pygame
import pygtk
pygtk.require('2.0')
import gtk

class Player:
    def play(self,widget):
        pygame.mixer.music.load('C:\Users\inusa01\Desktop\Media\Neil_Young_-_Cortez_the_Killer.mp3')
        pygame.mixer.music.play(-1,0.0)
        self.STATE="PLAYING"
        
    def pause(self,widet):
        if self.STATE=="PLAYING":
            pygame.mixer.music.pause()
            self.STATE="PAUSED"
            #self.pauseButton.set_label("Unpause")
        elif self.STATE=="PAUSED":
            pygame.mixer.music.unpause()
            self.STATE="PLAYING"
        
    def stop(self,widget):
        if self.STATE=="PLAYING" or self.STATE=="PAUSED":
            pygame.mixer.music.stop()
            #self.stopButton.set_label("stopped")
            self.STATE="STOPPED"
        
        
    def __init__(self):
        self.STATE="NULL"
        pygame.mixer.init()
        window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Player using pygame")
        window.set_size_request(400,300)
        window.connect("destroy",lambda w : gtk.main_quit())
        
        vbox=gtk.VBox(False,5)
        window.add(vbox)
        
        vbox.set_border_width(120)
        hbox=gtk.HBox(False,5)
        
        self.playButton=gtk.Button("Play")
        self.playButton.connect("clicked",self.play)
        
        self.pauseButton=gtk.Button("Pause")
        self.pauseButton.connect("clicked",self.pause)
        
        self.stopButton=gtk.Button("Stop")
        self.stopButton.connect("clicked",self.stop)
        
        
        
        hbox.pack_start(self.playButton)
        hbox.pack_start(self.pauseButton)
        hbox.pack_start(self.stopButton)
        
        
        
        vbox.pack_start(hbox)
        
        
        self.playButton.show()
        self.pauseButton.show()
        self.stopButton.show()
        vbox.show()
        hbox.show()
        window.show()
        
        
def main():
    gtk.main()
    
Player()
main()
