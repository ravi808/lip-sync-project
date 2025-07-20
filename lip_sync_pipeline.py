# lip_sync_pipeline.py

import subprocess
import os
# from Wav2Lip.inference import load_model

def main():
    video = "input_video.mp4"
    audio = "input_audio.wav"
    output = "output_video.mp4"
    model = "Wav2Lip/checkpoints/wav2lip_gan.pth"

    if not os.path.exists(model):
        raise FileNotFoundError("Wav2Lip model not found. Download wav2lip_gan.pth and place it in Wav2Lip/checkpoints")

    # Run inference
    subprocess.run([
        "python", "Wav2Lip/inference.py",
        "--checkpoint_path", model,
        "--face", video,
        "--audio", audio,
        "--outfile", output
    ], check=True)

if __name__ == "__main__":
    main()
