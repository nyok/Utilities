# Collection of small utilities that I use

## Google Chrome Extension
[Translate in Google Translate (Japanese to English)](https://github.com/nyok/Utilities/tree/main/Google%20Chrome/Extensions/translateInGoogleTranslateJpToEn)
<br>
<img src="docs/screenshot_translateInGoogleTranslateJpToEn.png" alt="Screenshot" width="830">

## Console
[Yes or No](https://github.com/nyok/Utilities/tree/main/Console/YesOrNo) - Randomly displays "Yes" or "No"
<br>
<img src="docs/screenshot_yesOrNo.png" alt="Screenshot" width="360">

## Parsers
[checkAvailabilityLamoda](https://github.com/nyok/Utilities/tree/main/checkAvailabilityLamoda) - Checking the quantity of brand goods on Lamoda
<br>
<img src="docs/screenshot_checkAvailabilityLamoda.png" alt="Screenshot" width="360">

## Images
[createImageBookSet](https://github.com/nyok/Utilities/tree/main/Images/createImageBookSet) - Bash script to transform and merge an image together
<br>
<img src="docs/screenshot_createImageBookSet.jpg" alt="Screenshot" width="360">

## PingAndTelegramNotify
[PingAndTelegramNotify](https://github.com/nyok/Utilities/tree/main/PingAndTelegramNotify) - Script continuously monitors the availability of a specified IP address or domain and sends notification messages to a Telegram channel if the target becomes unavailable.

## Screenshsot
[ScreenshotWithChromedriverAndSelenium](https://github.com/nyok/Utilities/tree/main/ScreenshotWithChromedriverAndSelenium) - Create a screenshot of a webpage using Selenium WebDriver and ChromeDriver
<br>ChromeDriver matching your Google Chrome version from https://chromedriver.chromium.org/downloads

## CreateGalleryFromFolder
[CreateGalleryFromFolder](https://github.com/nyok/Utilities/tree/main/CreateGalleryFromFolder) - Create thumbnails and html file of gallery (including subfolders)

## TimematorBackupCleanup
Script that automatically deletes old .tmbackup files from Timemator, keeping only the last 3 backups. Runs daily at 13:00 via cron.
```
0 13 * * * ls -t "/Users/$(whoami)/Library/Application Support/com.catforce.timemator.macos/Backups/"*.tmbackup | tail -n +4 | xargs -I {} rm -- "{}"
```
