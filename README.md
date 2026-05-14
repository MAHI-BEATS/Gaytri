<h1 align="center">MecoMusic</h1>

<p align="center">
  <img src="https://files.catbox.moe/3m7pfb.jpg" alt="MecoMusic Logo" width="600" height="400">
</p>

<h3 align="center">Delivering Superior Music Experience to Telegram</h3>

<p align="center">
  <a href="https://t.me/MecoMusicSupport"><img src="https://img.shields.io/badge/Support-Group-blue?style=for-the-badge&logo=telegram"></a>
  <a href="https://t.me/MecoMusicUpdates"><img src="https://img.shields.io/badge/Updates-Channel-blue?style=for-the-badge&logo=telegram"></a>
  <a href="https://github.com/SkyBotsDeveloper/Meco-Music/blob/main/LICENSE"><img src="https://img.shields.io/github/license/SkyBotsDeveloper/Meco-Music?style=for-the-badge"></a>
</p>

---

## Table of Contents

- [Features](#features)
- [Deploy on Heroku](#deploy-on-heroku)
- [Quick Setup](#quick-setup)
- [Commands and Usage](#commands-and-usage)
- [Updates and Support](#updates-and-support)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- Multi-source streaming from YouTube, Telegram, and more.
- Queue support for uninterrupted playback.
- Playback controls including skip, pause, resume, repeat, and shuffle.
- High-quality audio output.
- Custom settings and admin tools.
- Cookie-free and API key based playback flow.

---

## Deploy on Heroku

Click the button below to deploy the bot on Heroku instantly:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/MAHI-BEATS/Gaytri)

---

## Quick Setup

1. Upgrade and update packages:
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```
2. Install required packages:
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```
3. Upgrade `pip`:
   ```bash
   sudo pip3 install -U pip
   ```
4. Install Node.js:
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
   ```
5. Clone the repository:
   ```bash
   git clone https://github.com/SkyBotsDeveloper/Meco-Music && cd Meco-Music
   ```
6. Install requirements:
   ```bash
   pip3 install -U -r requirements.txt
   ```
7. Edit environment variables:
   ```bash
   nano .env
   ```
8. Optional: run inside `tmux`:
   ```bash
   sudo apt install tmux -y && tmux
   ```
9. Start the bot:
   ```bash
   bash start
   ```

---

## Commands and Usage

The MecoMusic bot offers a range of commands to enhance your music listening experience on Telegram:

| Command | Description |
|---------|-------------|
| `/play <song name>` | Play the requested song. |
| `/pause` | Pause the currently playing song. |
| `/resume` | Resume the paused song. |
| `/skip` | Move to the next song in the queue. |
| `/stop` | Stop the bot and clear the queue. |
| `/queue` | Display the list of songs in the queue. |

For the full command list, use `/help` in your deployed bot.

---

## Updates and Support

Stay updated with the latest features and improvements to MecoMusic:

<p align="center">
  <a href="https://t.me/MecoMusicSupport">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://t.me/MecoMusicUpdates">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

## Contributing

We welcome contributions to the MecoMusic project. If you'd like to contribute:

1. Fork the repository.
2. Create a new branch with a meaningful name.
3. Make your changes and commit them with a descriptive message.
4. Open a pull request against the main branch.

For more details, reach out on Telegram.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Thanks to all contributors, supporters, and users of MecoMusic.
