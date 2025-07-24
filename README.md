# 🎭 Live Webcam Face Filter

A simple Python script that applies live face filters to your webcam using OpenCV and NumPy. The idea simply comes to my mind when I was doing a TikTok livestream on mobile while showing my desktop monitor without Live Studio on desktop.

## 📸 Features

- Live webcam face detection
- Filter overlays for fun and experimentation
- Plug-and-play: Just run a Python script

## 🧰 Requirements
### 1. Software:
This project requires Python **3.8+** and the following Python packages:

- `opencv-python`
- `numpy`

The filters are stored in the sample `gifts/` folder (already included). You **can add or remove .png files from this folder** to run the project.

### 2. Hardware:
Don't forget your webcam!

## 📦 Installation

You can install the dependencies using **pip** or **uv** (if you prefer a faster, modern alternative).

### Using pip

```bash
pip install opencv-python numpy
````

### Using uv (if installed)

```bash
uv pip install opencv-python numpy
```

> Don't have `uv`? Check it out here: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## 🚀 Running the Script

Once dependencies are installed, check which filters you want to display by commenting/uncommenting inside `faizalingo_livestream.py`. Then, simply run it:

```bash
python faizalingo_livestream.py
```

This will launch your webcam with live face filtering enabled.

---

## 📂 Project Structure

```
📁 TikTok-Live-Webcam-Face-Filter/
├── faizalingo_livestream.py     # Main script to run
└── gifts/                       # Folder containing filter overlays
```

You can add or modify the filters inside the `gifts/` folder if you want to customize the effects.

## 🛠️ Troubleshooting

* Ensure your webcam is not being used by another application.
* If the window opens blank or freezes, try restarting your Python kernel or system.
* For best performance, use a well-lit environment.

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest new features/filters.

## 📄 License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for more information.

## 🙌 Acknowledgements

* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [House of Hikmah](https://houseofhikmah.org/)
