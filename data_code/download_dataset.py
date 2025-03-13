from SoccerNet.Downloader import SoccerNetDownloader as SNdl
soccerNetDownloader = SNdl(LocalDirectory="data/dataset")
soccerNetDownloader.downloadDataTask(task="calibration-2023", split=["train","valid","test","challenge"])
