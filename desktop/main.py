import multiprocessing
import re
import webbrowser
from urllib import request

import colorama
from gooey import Gooey, GooeyParser, local_resource_path

from egybest.AdBypass import BypassAds
from utils.main import Tools
from utils.pc import PCInfo
from utils.printer import Printer


class main:
    @Gooey(program_name="EgyBest Downloader V6.1", default_size=(600, 600), language="english",
           program_description="Download Easily from EgyBest using this tool", image_dir=local_resource_path('images'),
           richtext_controls=True, )
    def __init__(self):
        colorama.init()
        parser = GooeyParser(description="Download Easily from EgyBest using this tool")
        parser.add_argument("url", help="Enter the url of the series or season you want to download",
                            widget="TextField")
        parser.add_argument("quality", help="Choose Quality of Download", widget="Dropdown",
                            choices=["1080p", "720p", "480p", "360p", "240p"], default="1080p")

        self.Parser = parser.parse_args()

        self.Tools = Tools()
        self.Printer = Printer()
        self.Pc = PCInfo()

        self.Season = ""
        self.Episodes = []
        self.Watches = []
        self.Domain = ""
        self.Slug = ""
        self.Cookie = ""
        self.isAdBypassed = False
        self.DirectLinks = []

        self.Quality = self.Parser.quality
        self.Url = self.Parser.url

        self.Run()

    def Run(self):
        self.Tools.SaveOrUpdatePCInfo(self.Pc.System_information())

        self.Printer.CationPrinter(
            "If there's any AdBlockers or Anti Viruses installed on your system you need to disable "
            "them first. They case false block to the App requests")
  
    

        ChromeInstalled = self.Tools.isChromeInstalled()
        if not ChromeInstalled:
            self.Printer.CationPrinter("Chrome is not installed on your system. Please install it first.")
            input()
            exit()
            return
        if "season" in self.Url:
            self.GetSeason()
        if "series" in self.Url:
            self.GetAllSeason()



        self.Printer.SuccessPrinter("Done! Thanks For using EgyBest downloader. Visit us @ https://eb.gitnasr.com.")
        webbrowser.open("https://eb.gitnasr.com")
        webbrowser.open("https://twitter.com/sgitnasr")

    # Phase 0

    def GetAllSeason(self):

        content = self.Tools.Requester(f"{self.Domain}{self.Url}")
        soup = self.Tools.Souper(content)
        series_name = soup.find(class_="movie_title")
        seasons = soup.find_all(class_="movies_small")[0]
        seasons = seasons.find_all(class_="movie")
        self.Printer.InfoPrinter(f"PHASE O: Detected #{len(seasons)} seasons")
        for tag in series_name:
            self.Season = tag.text
        self.Domain = self.Tools.Domainer(self.Url)
        for tag in seasons:
            self.Url = "https://{}{}".format(self.Domain, tag.get("href"))
            self.GetSeason()
            self.isAdBypassed = True

    # Phase I
    def GetSeason(self):
        soup = self.GetBasicInfo()
        episodes = soup.find_all(href=re.compile("/episode/"), class_="movie")
        for link in set(episodes):
            self.Episodes.append(link['href'])
        self.Printer.InfoPrinter(f'Phase I: Detected #{len(self.Episodes)} episodes.')

        self.GetWatchList()

    def GetBasicInfo(self):
        content = self.Tools.Requester(self.Url)
        soup = self.Tools.Souper(content)
        slug = self.Url.split("/season/")
        self.Slug = slug[1].replace("/", "")
        season_name_div = soup.find(class_="movie_title")
        for tag in season_name_div:
            self.Season = tag.text
        return soup

    # Phase 2
    def GetWatchList(self):
        self.Domain = self.Tools.Domainer(self.Url)
        for i, episode in enumerate(self.Episodes):
            content = self.Tools.Requester(f"https://{self.Domain}{episode}")
            soup = self.Tools.Souper(content)
            watch = soup.find(class_="auto-size")['src']
            self.Watches.append(f"https://{self.Domain}{watch}")
            self.Printer.InfoPrinter(f'Phase II: Episode: {i + 1}')
        self.BypassAds()

    # Phase A
    def BypassAds(self):

        self.Printer.PendingPrinter("Bypassing Ads")
        while not self.isAdBypassed:
            link_to_bypass = f"https://{self.Domain}{self.Episodes[0]}"

            Adbypass = BypassAds("/html/body", link_to_bypass)
            result = Adbypass.Run()
            if result.get("status"):
                self.Cookie = result.get("cookie")
                self.isAdBypassed = True
                self.Printer.SuccessPrinter("Ads Bypassed")

        self.GetStreamUrls()

    # Phase 3
    def GetStreamUrls(self):
        headers = {
            "cookie": self.Cookie
        }
        for i, Watches in enumerate(self.Watches):
            content = self.Tools.Requester(Watches, headers)
            soup = self.Tools.Souper(content)
            source = soup.find("source")['src']
            m3ue = self.Tools.Requester(f"https://{self.Domain}{source}").decode("utf-8")
            self.M3u8Parser(m3ue)
            self.Printer.InfoPrinter(f'Phase III: Episode: {i + 1}')
        self.SaveAndClose()

    def M3u8Parser(self, m3u):
        isAdded = False
        streamList = m3u.split("\n")
        streamList = self.Tools.Compact(streamList)
        streamList = self.Tools.FilterListByHttps(streamList)
        for i, line in enumerate(streamList):
            isAdded = self.QualityByFile(line)
        if not isAdded:
            isFoundByIndex = self.QualityByIndex(streamList)
            if not isFoundByIndex:
                direct = self.ConvertStreamToDownload(streamList[-1])
                self.DirectLinks.append(direct)

    def ConvertStreamToDownload(self, stream):
        url = stream.replace("/stream/", "/dl/")
        url = url.replace("/stream.m3u8", "")
        return url

    def QualityByFile(self, link):
        loopCount = 0
        while loopCount != 6:
            try:
                direct = self.ConvertStreamToDownload(link)
                filename = request.urlopen(request.Request(direct)).info().get_filename()
                if str(self.Quality) in filename.lower():
                    self.DirectLinks.append(direct)
                    return True
                return False
            except:
                loopCount += 1
        return False

    def QualityByIndex(self, streamList):
        for i, line in enumerate(streamList):
            if self.Quality == "240p":
                if i == 0:
                    direct = self.ConvertStreamToDownload(line)
                    self.DirectLinks.append(direct)
                    return True
            if self.Quality == "360p":
                if i == 1:
                    direct = self.ConvertStreamToDownload(line)
                    self.DirectLinks.append(direct)
                    return True
            if self.Quality == "480p":
                if i == 2:
                    direct = self.ConvertStreamToDownload(line)
                    self.DirectLinks.append(direct)
                    return True
            if self.Quality == "720p":
                if i == 3:
                    direct = self.ConvertStreamToDownload(line)
                    self.DirectLinks.append(direct)
                    return True
            if self.Quality == "1080p":
                if i == 4:
                    direct = self.ConvertStreamToDownload(line)
                    self.DirectLinks.append(direct)
                    return True
        return False

    def SaveAndClose(self):
        self.Printer.PendingPrinter("Saving")
        with open(self.Season + f'_{self.Tools.GenrateId(4)}.txt', 'w') as f:
            for item in set(self.DirectLinks):
                f.write("%s\n" % item)
        f.close()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = main()
