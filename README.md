# ID Card Photo Extractor

Extracts faces from ID card photos.

## Installation

### Clone the repository

```bash
git clone https://github.com/gcoulby/id-card-face-extractor.git

cd id-card-face-extractor
```

### Create a virtual environment (optional)

If you wish to create a virtual environment, run the following command:

```bash
python -m venv env
```

Activate the virtual environment:

```bash
# Linux/OsX
source env/bin/activate

# Windows
.\venv\Scripts\activate
```

### Install the pagkages

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --input_dir <input_dir> --output_dir <output_dir>
```

## Help

```bash
python main.py --help
```
