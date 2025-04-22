import importlib

packages = [
    'cv2',         # opencv
    'numpy',
    'tensorflow',
    'imutils',
    'skimage',     # scikit-image
    'sklearn'      # scikit-learn
]

for pkg in packages:
    try:
        mod = importlib.import_module(pkg)
        print(f"{pkg}: {mod.__version__}")
    except Exception as e:
        print(f"{pkg}: not found or error - {e}")
