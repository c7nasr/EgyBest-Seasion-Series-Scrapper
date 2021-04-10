from os.path import join
import threading


class EBThreads():
    def single_episode_info_thread(self):
        threading.Thread(target=self.single_episode_info).start()

    def msgbox_thread(self, title):
        threading.Thread(target=self.info_box, args=(title,)).start()

    def series_signal_thread(self):
        threading.Thread(target=self.start_series_signal).start()
