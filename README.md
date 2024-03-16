## [Features](/#Features) | [Dependencies](/#Required-Dependencies) | [Install](/How-to-install) | [Usage](/#How-to-use) | [Models](/#Where-can-I-get-models-voices-and-avatars) | [Roadmap](/#Roadmap) | [Acknowledgment](/#Acknowledgment-to-developers)

# ![icon (1)](https://github.com/Dartvauder/NeuroChatWebUI/assets/140557322/e3c1d95a-828f-4a65-bea6-64c336dbe6fa) NeuroChatWebUI
English | [Русский](/README_RU.md)
## Description:

Simple and easy interface for chatting with LLM using text or voice input. TTS functions are available here for voice output with a choice of language and voice sample. The goal of the project - to create the easiest possible application for beginners in the topic of neural networks.

|![Image1](https://github.com/Dartvauder/NeuroChatWebUI/assets/140557322/98e185c1-6011-434c-af9f-885d1c5ded48) |
|:---:|

## Features:

* Easy install (Windows only)
* Flexible and optimized interface
* TTS and STT models
* Avatar choose (for LLM)
* Transformers (Llama.cpp in feature)
* And much more...

## Required Dependencies:

* [Python](https://www.python.org/downloads/) (3.10 minimum)
* [Git](https://git-scm.com/downloads)
* [CUDA](https://developer.nvidia.com/cuda-downloads) (12.1 only)
* [FFMPEG](https://ffmpeg.org/download.html)

## How to install:

### Windows

1) `Git clone` or [download](https://github.com/Dartvauder/NeuroChatWebUI/files/14624563/NeuroChatWebUI.zip) the repository.
2) Unzip the archive file to any location
3) Run the `install.bat` and wait for installation.
4) After installation, run `start.bat`.
5) Select the file version and wait for the application to launch.
6) Have fun!

To get update, run `update.bat`

### Linux

1) `Git clone` or [download](https://github.com/Dartvauder/NeuroChatWebUI/files/14624563/NeuroChatWebUI.zip) the repository.
2) Unzip the archive file to any location
3) In the terminal, run the `pip install -r requirements.txt` and wait for installation of all dependencies.
4) After installation, run `py appEN.py` or `py appRU.py`.
5) Wait for the application to launch.
6) Have fun!

To get update, run `git pull`

## How to use:

* First download the models by folders. Model paths: LLM = inputs/text/llm_models
#### Optional: Voice sample = inputs/audio/voices; Avatars = inputs/image/avatars
* To begin, select your model in the `LLM` drop-down list, enter (or say) your prompt and press `generate` button and receive your text response. If you want, you can choose an `avatar`
#### Optional: You can also `enable TTS` mode and select the `voice` and `language` you need to get an audio response
* You can also click the `clear` button to reset your selection.
#### To close the application, close the terminal

The voice needs to be pre-processed (22050 kHz, mono sound, WAV), avatar should preferably be PNG or JPG, the LLM model must be Transformers. When you turn on TTS, selecting a language and voice is required, otherwise there will be errors.

#### Chat history is saved in the outputs folder

## Where can I get models, voices and avatars?

* Language models can be taken from [HuggingFace](https://huggingface.co/models)
* You can take voices anywhere. Record yours or take a recording from the Internet. The main thing is that it is pre-processed!
* It’s the same with avatars as with voices. You can download them on the Internet, generate them using neural networks, or take a photo of yourself. The main thing is to comply with the required file format
* #### TTS and STT models are downloaded automatically

## Roadmap

* https://github.com/Dartvauder/NeuroChatWebUI/wiki/Roadmap

## Acknowledgment to developers

Thank you very much to these projects for allowing me to create my application:

* `Gradio` - https://github.com/gradio-app/gradio
* `Transformers` - https://github.com/huggingface/transformers
* `TTS` - https://github.com/coqui-ai/TTS
* `openai-Whisper` - https://github.com/openai/whisper
* `torch` - https://github.com/pytorch/pytorch
* `Soundfile` - https://github.com/bastibe/python-soundfile

## Donation

### If you really liked my project and want to donate, here is options to donate. Thank you very much in advance! 

* CryptoWallet(BEP-20) - 0x3d86bdb5f50b92d0d7Eb44F1a833acC5e91aAEcA

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/Dartvauder)

