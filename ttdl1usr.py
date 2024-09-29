import os
import yt_dlp
from urllib.parse import urlparse
import pyfiglet
from colorama import Fore, init
import time

# Initialize Colorama
init(autoreset=True)

def print_colored_logo():
    # Generate ASCII art for the logo with a modern font
    logo = pyfiglet.figlet_format("SRIEVi", font="slant")
    
    # Center the logo in the terminal
    terminal_width = os.get_terminal_size().columns
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Colors for the gradient effect (cyber-like appearance)
    colors = [Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]

    # Apply a glowing effect to each character in the logo
    print("\n")  # Add spacing before the logo
    for i, char in enumerate(centered_logo):
        if char.strip():  # Apply color only to non-space characters
            print(colors[i % len(colors)] + char, end='', flush=True)
            time.sleep(0.03)  # Slight delay to create a glowing effect
        else:
            print(char, end='', flush=True)
    print("\n")  # New line after the logo

def get_profile_name(profile_url):
    parsed_url = urlparse(profile_url)
    path_parts = parsed_url.path.strip('/').split('/')
    return path_parts[-1]

def truncate_title(title, max_length=100):
    return title[:max_length]

def download_tiktok_profile(profile_url):
    profile_name = get_profile_name(profile_url)
    
    if not os.path.exists(profile_name):
        os.makedirs(profile_name)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(profile_name, '%(title).100s.%(ext)s'),  # Shorten the file name
        'noplaylist': True,
        'download_archive': os.path.join(profile_name, 'downloaded.txt'),
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([profile_url])

if __name__ == "__main__":
    print_colored_logo()

    # Updated GitHub and social links
    terminal_width = os.get_terminal_size().columns
    developer_info = f"{Fore.LIGHTGREEN_EX}Support us @eirsvi"
    centered_developer = developer_info.center(terminal_width)
    print(centered_developer)

    social_links = f"{Fore.LIGHTRED_EX}GitHub | X | YouTube \n"
    centered_social_links = social_links.center(terminal_width)
    print(centered_social_links)

    # Example URL without centering
    example_url = f"{Fore.LIGHTYELLOW_EX}EXAMPLE URL: ( https://tiktok.com/@eirsvi ) \n"
    print(example_url)

    # Prompt user for the TikTok profile URL
    profile_url = input(f"{Fore.LIGHTCYAN_EX}Enter the TikTok profile URL: {Fore.LIGHTCYAN_EX}")
    download_tiktok_profile(profile_url)
