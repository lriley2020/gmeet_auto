# gmeet_auto
Automatically joins your google meets so you don't have to!

## Instructions for installation and use

1. `git clone https://github.com/lriley2020/gmeet_auto.git`

2. (Optional) Create a virtual environment: `python3 -m venv gmeet_env` ... and activate it: `source gmeet_env/bin/activate`

3. `python3 -m pip install -r gmeet_auto/requirements.txt`

4. macOS: `brew install chromedriver`

   or

   linux: `sudo apt install chromium-chromedriver` or if your distro doesn't use apt, download from [official chromium page](https://chromedriver.chromium.org/downloads)

5. Edit the `hi.py` file and find the section beginning `### gmeet link + setup ###`. Add your config below.

6. Run the file with `python3 ~/gmeet_auto/hi.py` (you could schedule the execution of this script with `cron`)
