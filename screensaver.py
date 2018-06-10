#!/usr/bin/python

import os
import sys
import gtk
from gtk import gdk


class ScreenSaverWindow(gtk.Window):
    def realize(self):
        if self.flags() & gtk.REALIZED:
            return

        ident = os.environ.get('XSCREENSAVER_WINDOW')

        if ident:
            self.window = gdk.window_foreign_new(
                int(ident, 16)
            )
            self.window.set_events(
                gdk.EXPOSURE_MASK | gdk.STRUCTURE_MASK
            )
            x, y, w, h, depth = self.window.get_geometry()
            self.size_allocate(
                gdk.Rectangle(x, y, w, h)
            )
            self.set_default_size(w, h)
            self.set_decorated(False)

            self.window.set_user_data(self)
            self.style.attach(self.window)
            self.set_flags(
                self.flags() | gtk.REALIZED
            )
            #self.window.connect("destroy", self.destroy)

        if not self.window:
            self.window = gdk.Window(
                None, 1024, 768,
                gdk.WINDOW_TOPLEVEL,
                (gdk.EXPOSURE_MASK | gdk.STRUCTURE_MASK),
                gdk.INPUT_OUTPUT
            )

        if self.window:
            #self.window.add_filter(lambda *args: self.filter_event(args))
            self.set_flags(self.flags() | gtk.REALIZED)


if __name__ == "__main__":
    window = ScreenSaverWindow()
    window.set_title('Floaters')
    window.connect('delete-event', gtk.main_quit)
    window.set_default_size(1024, 768)
    window.realize()

    window.modify_bg(gtk.STATE_NORMAL, gdk.color_parse("black"))

    label = gtk.Label()
    label.set_markup("<span foreground=\"white\"><big>Wer das liest is doooof!</big></span>")
    label.show()
    window.add(label)
    window.show()

    gtk.main()
