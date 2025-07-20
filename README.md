
# Audio Replacement with Lip Sync

## 🎯 Objective

This project takes a short video of a person speaking (Paragraph A), replaces the original audio with a different audio (Paragraph B), and modifies the video to ensure the lip movements match the new speech — producing a natural-looking result.

### ✅ Input:
- `input_video.mp4` — Original 10–15s video of you speaking Paragraph A.
- `new_audio.wav` — Audio file of you speaking Paragraph B.

### ✅ Output:
- `output_video.mp4` — Modified video where:
  - Lip movements match `new_audio.wav`.
  - Head pose, lighting, identity remain consistent.

---

## ⚙️ Installation

### 1. Clone the Wav2Lip Repository
We clone the [original Wav2Lip repo](https://github.com/Rudrabha/Wav2Lip) because:
- It includes custom scripts like `inference.py` and `audio.py`.
- The open-source Python package `wav2lipy` has unresolved dependency issues (e.g. incompatible `torch==1.1.0`) and lacks the GAN-based improvements available in the full repo.

```bash
git clone https://github.com/Rudrabha/Wav2Lip.git
```

### 2. Download Pretrained Checkpoint

Place the checkpoint file `wav2lip_gan.pth` inside `Wav2Lip/checkpoints/`.

Download here: [Google Drive Link](https://drive.google.com/file/d/1lwNfovr1_ZzA1J1McM5DdMzGY3qNr6dR/view)

---

## 🐍 Python Environment Setup

### Windows Steps:

```bash
# Navigate to project root
cd path\to\lip-sync-project

# Create virtual environment
python -m venv wav2lipenv

# Activate the environment
wav2lipenv\Scripts\activate
```

### Install dependencies:

```bash
pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
pip install opencv-python numpy scipy matplotlib moviepy tqdm requests pandas
pip install librosa==0.8.1
```

---

## ▶️ Usage

Once everything is set up, run the following command:

```bash
python Wav2Lip/inference.py \
  --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth \
  --face input_video.mp4 \
  --audio new_audio.wav \
  --outfile output_video.mp4
```

You can also run it from Python using `subprocess`:

```python
import subprocess

subprocess.run([
    "python", "Wav2Lip/inference.py",
    "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth",
    "--face", "input_video.mp4",
    "--audio", "new_audio.wav",
    "--outfile", "output_video.mp4"
])
```

---

## 📄 Paragraphs Used

**Paragraph A** (Original video):
> Today, I’m going to show you how machine learning can transform everyday tasks. Whether it’s identifying objects in images or generating text from scratch, the possibilities are truly endless. Let’s dive into some amazing examples together.

**Paragraph B** (New audio):
> The quick brown fox jumps over the lazy dog while a curious cat watches from the rooftop. Suddenly, a loud bark sends the animals running in every direction — pure chaos ensues.

---

## 📌 Notes and Assumptions

- We use the original [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) repo because it includes all the custom modules (GAN enhancements, mel processing, etc.) needed for high-fidelity results.
- `wav2lipy` was avoided due to its dependency on outdated versions of PyTorch (`==1.1.0`) which conflict with modern Python.
- This project assumes the speaker identity, lighting, and pose stay reasonably stable between the original and modified video.

---

## 🧠 Acknowledgements

- [Wav2Lip: Accurate Lip-syncing for Speech to Lip Generation](https://github.com/Rudrabha/Wav2Lip)
