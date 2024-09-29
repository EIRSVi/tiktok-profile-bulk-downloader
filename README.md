

<p align="center">
  <a href="#">
    <img src="https://skillicons.dev/icons?i=git,kali,windows,powershell" />
  </a>
</p>

<h1 align="center">TikTok Profile Downloader</h1>

<h2 align="center">Summary</h2>

<p>
The TikTok Profile Downloader is a tool designed to download videos from an entire TikTok profile quickly and efficiently. It organizes all videos into a dedicated folder named after the profile, ensuring that files are saved with a truncated version of the original title.
</p>

<h2 align="center">Features</h2>

<ul>
  <li>Download all videos from a specified TikTok profile.</li>
  <li>Stores videos in a folder named after the profile.</li>
  <li>Files are saved with shortened titles to avoid long filenames.</li>
  <li>Automatically skips already downloaded videos.</li>
  <li>Simple, terminal-based interface.</li>
</ul>

<h2 align="center">Prerequisites</h2>

<p>Ensure the following dependencies are installed on your system:</p>

<ul>
  <li><a href="https://www.python.org/downloads/">Python 3.x</a></li>
  <li><a href="https://github.com/yt-dlp/yt-dlp">yt-dlp</a> for handling TikTok downloads.</li>
  <li><a href="https://pypi.org/project/colorama/">Colorama</a> for terminal colors.</li>
  <li><a href="https://pypi.org/project/pyfiglet/">pyfiglet</a> for ASCII art.</li>
</ul>

<p>To install the necessary Python libraries, run:</p>

```bash
pip install yt-dlp colorama pyfiglet
```

<h2 align="center">Installation</h2>

<p>1. Clone this repository:</p>

```bash
git clone https://github.com/eirsvi/tiktok-profile-downloader.git
cd tiktok-profile-downloader
```

<p>2. Run the script:</p>

```bash
python ttdl1usr.py
```

<h2 align="center">Example</h2>

<p>
To download all videos from a TikTok profile, you can enter a URL such as:
</p>

<p>
 EXAMPLE URL: https://tiktok.com/@eirsvi
</p>

<p>
All videos will be downloaded and stored in a folder named after the profile (e.g., `eirsvi`), with each file having a truncated version of the video's title as the file name.
</p>

<h2 align="center">Troubleshooting</h2>

<p>
If you encounter any issues while downloading, check the following:
</p>

<ul>
  <li>Ensure yt-dlp is installed correctly.</li>
  <li>Verify that the TikTok profile URL is correct.</li>
  <li>Ensure proper permissions for creating directories and downloading files.</li>
  <li>If videos are missing, check the `downloaded.txt` file for already downloaded entries.</li>
</ul>

<h2 align="center">License</h2>

<p>
This project is open-source and available under the MIT License.
</p>

<h2 align="center">Credits</h2>

<p>
Support us: <a href="https://github.com/eirsvi/">@eirsvi</a>
</p>

<p>
Feel free to reach out if you have any questions or feedback!
</p>

---

Let me know if you need any changes or additions!
