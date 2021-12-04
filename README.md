# Meme Generator

Image creation tool to randomly generate memes based on input from four separate file types or user input.

Final output is .png file with text overlayed on image.


## Installation
```
git clone https://github.com/tcamack/meme_generator.git
```


## Usage

### Command Line
```
usage: meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

Meme Generator

optional arguments:
  -h, --help       show this help message and exit
  --body BODY      Quote to appear on the picture.
  --author AUTHOR  Author of the quote.
  --path PATH      File path for the background image.
```


### Web App

```
python app.py
```

Navigate to http://127.0.0.1:5000/ in a web browser.


## Output

All generated images are saved in the `~\static` directory that is created upon first launch.


## Requirements
* Flask
* pandas
* Pillow
* python-docx
* requests
