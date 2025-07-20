
# 🔊 Audio Replacement with Lip Sync

This project takes a short video of a person speaking and replaces the original audio with a new voice recording, modifying the lip movements to match the new speech using the Wav2Lip model.

---

## 🎯 Objective

Given:
- `input_video.mp4`: A 10–15 sec video of someone speaking Paragraph A.
- `new_audio.wav`: A separate audio recording of Paragraph B.

The system outputs:
- `output_video.mp4`: A realistic video where the original voice is replaced and lip movements are synced with `new_audio.wav`.

---

## 📁 Folder Structure

```
lip-sync-project/
├── Wav2Lip/                   # Contains inference.py, audio.py, and checkpoints
├── input_video.mp4            # Original input video (Paragraph A)
├── new_audio.wav              # New audio file (Paragraph B)
├── output_video.mp4           # Final generated output
├── wav2lipenv/                # Virtual environment
├── lip_sync_pipeline.py       # (Optional) Custom pipeline if you write your own
└── README.md
```

---

## 🧰 Dependencies

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python -m venv wav2lipenv

# Activate (Windows CMD)
wav2lipenv\Scripts\activate

# OR PowerShell
.\wav2lipenv\Scripts\Activate.ps1

# Install dependencies
pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
pip install opencv-python numpy scipy matplotlib moviepy tqdm pandas requests
pip install librosa==0.8.1
```

---

## 🏁 How to Run

Make sure the model checkpoint `wav2lip_gan.pth` is in `Wav2Lip/checkpoints/`.

Then run:

```bash
python Wav2Lip/inference.py \
  --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth \
  --face input_video.mp4 \
  --audio new_audio.wav \
  --outfile output_video.mp4
```

---

## 📌 Assumptions & Constraints

- Lip sync accuracy depends on clarity of the face and audio.
- You must speak Paragraph A and B with relatively similar expressions and head movements.
- `input_video.mp4` should contain a clear frontal view of your face.

---

## 📖 Paragraphs Used

**Paragraph A**  
> Today, I’m going to show you how machine learning can transform everyday tasks. Whether it’s identifying objects in images or generating text from scratch, the possibilities are truly endless. Let’s dive into some amazing examples together.

**Paragraph B**  
> The quick brown fox jumps over the lazy dog while a curious cat watches from the rooftop. Suddenly, a loud bark sends the animals running in every direction — pure chaos ensues.

---

## ✅ Output

- `output_video.mp4` will have your face from the original video,
- your new voice from `new_audio.wav`,
- and lip movements synced naturally.

---

## 🔗 Credits

- [Wav2Lip (Original GitHub)](https://github.com/Rudrabha/Wav2Lip)
- OpenCV, Librosa, PyTorch, MoviePy, FFmpeg

---

## 🛠 Troubleshooting

- ❌ `No module named 'cv2'` → Run: `pip install opencv-python`
- ❌ `librosa mel() error` → Use: `librosa==0.8.1`
- ❌ Environment issues → Delete and recreate `wav2lipenv`

---