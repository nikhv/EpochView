# EpochView

**EpochView** is a simple script that dynamically generates a live wallpaper displaying the elapsed time from a specific date. The generated wallpaper is periodically updated and set as the desktop background.

---

## Features
- Displays elapsed time in a visually appealing format.
- Dynamically updates the wallpaper image every second.
- Compatible with major Linux desktop environments such as GNOME, KDE, and others.

---

## Requirements
- Python 3.x
- `pygame` (for generating the wallpaper)
- `feh` (for setting the wallpaper on non-GNOME desktops)

Install required packages:

```bash
sudo apt install python3-pip feh
pip install pygame
```

---

## Usage
### 1. Clone the Repository
```bash
git clone https://github.com/nikhv/epochview.git
cd epochview
```

### 2. Run the Script
```bash
python3 epochview.py
```

The script will:
- Generate a wallpaper image dynamically showing the elapsed time.
- Set the generated image as the desktop wallpaper.

---

## Installation
### GNOME Desktop
For GNOME users, the script uses `gsettings` to set the wallpaper. Ensure `gsettings` is installed and available.

Example command for setting the wallpaper:

```bash
gsettings set org.gnome.desktop.background picture-uri "file:///tmp/live_wallpaper.png"
```

### Other Desktop Environments
For non-GNOME desktops, the script uses `feh` to set the wallpaper.

#### Install Feh:
```bash
sudo apt install feh
```

#### Set Wallpaper:
The script automatically sets the wallpaper using `feh`. If needed manually, you can run:

```bash
feh --bg-scale /tmp/live_wallpaper.png
```

---

## Script Details
1. **Generate Wallpaper:** The script creates an image displaying the elapsed time and saves it as `/tmp/live_wallpaper.png`.
2. **Set Wallpaper:** The script sets the generated image as the desktop background using `gsettings` (GNOME) or `feh` (others).

---

## Configuration
The script can be customized to:
- Change the starting epoch date.
- Modify text style, colors, or formatting.
- Adjust update intervals.

### Example Customization:
In `epochview.py`, update the following variables:
- **Starting Date:** Set the epoch time to count from.
- **Font and Colors:** Modify `font`, `background_color`, and `text_color` variables.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/epochview/issues) or create a pull request.

---

## Acknowledgments
- Inspired by the concept of dynamic live wallpapers.
- Built using `pygame` and `feh` for a seamless user experience.
- Concept development and troubleshooting support provided by ChatGPT.



