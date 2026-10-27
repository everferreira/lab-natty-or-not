#!/usr/bin/env python3
"""Gera a narração do avatar do lab Natty or Not e monta o vídeo."""
import asyncio, os, subprocess, sys
import edge_tts

BASE = "/mnt/c/Users/conta/DIO/lab-natty-or-not"
os.makedirs(f"{BASE}/audio", exist_ok=True)
os.makedirs(f"{BASE}/output", exist_ok=True)

TEXTO = (
    "Será que você consegue dizer se eu sou real, ou se fui criada por uma "
    "inteligência artificial? Essa é a proposta do lab Natty or Not, da DIO: "
    "explorar o potencial das IAs generativas para criar conteúdos cada vez "
    "mais realistas. Retratos, vozes, vídeos. A fronteira entre o natural e o "
    "fake está ficando menor a cada dia. Mas uma coisa é certa: quem aprende a "
    "usar essas ferramentas com responsabilidade sai na frente. E você? "
    "Consegue adivinhar a minha resposta?"
)

async def main():
    com = edge_tts.Communicate(TEXTO, "pt-BR-FranciscaNeural", rate="-5%")
    await com.save(f"{BASE}/audio/narracao.mp3")
    print("NARRAÇÃO OK")

asyncio.run(main())

# monta o vídeo: avatar com zoom lento (Ken Burns) + narração
# descobre a duração do áudio
r = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
     "-of", "csv=p=0", f"{BASE}/audio/narracao.mp3"],
    capture_output=True, text=True)
dur = float(r.stdout.strip())
print("duração da narração:", dur, "s")

# zoompan em 1080x1080, fps 30, d = duração * 30 frames
frames = int(dur * 30)
cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", f"{BASE}/assets/avatar.jpg",
    "-i", f"{BASE}/audio/narracao.mp3",
    "-filter_complex",
    f"scale=2160:2160,zoompan=z='min(zoom+0.0008,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1080:fps=30,format=yuv420p",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20",
    "-c:a", "aac", "-b:a", "192k", "-shortest",
    f"{BASE}/output/avatar_natty.mp4",
]
subprocess.run(cmd, check=True)
print("VÍDEO OK")
