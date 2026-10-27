# 🤖 Natty or Not: Avatar Criado por IA Generativa

## 📒 Descrição

Este projeto explora a capacidade das IAs Generativas de criar conteúdo
fotorrealista. A proposta: gerar um avatar "natty" — tão realista que é difícil
dizer que foi criado por uma máquina — e um vídeo curto em que esse avatar fala.

O resultado é um retrato corporativo hiper-realista e um vídeo de 33 segundos
com o avatar apresentando o próprio desafio, com movimento de câmera, narração
em voz sintetizada e tomada natural.

## 🤖 Tecnologias Utilizadas

- **OpenAI GPT-5 Image Mini** (via API OpenRouter) — geração do retrato
  hiper-realista do avatar
- **Microsoft Edge TTS** — síntese de voz em português brasileiro
  (voz `pt-BR-FranciscaNeural`)
- **ffmpeg** — montagem do vídeo com efeito Ken Burns (zoom lento) e
  sincronização de áudio
- **Python** — automação de todo o pipeline (script reproduzível)

## 🧐 Processo de Criação

1. **Imagem**: prompt de retrato profissional hiper-realista enviado ao modelo
   de imagem — mulher brasileira, 35 anos, sorrindo, blazer escuro, fundo de
   escritório moderno, iluminação natural.
2. **Voz**: roteiro curto escrito sobre o próprio desafio Natty or Not e
   sintetizado com Edge TTS (voz feminina pt-BR, rate -5%).
3. **Vídeo**: o retrato foi animado com efeito Ken Burns (zoom progressivo de
   1.0x a 1.12x) via ffmpeg, sobreposto à narração, exportado em 1080x1080,
   H.264 + AAC.

## 🚀 Resultados

<!-- Resultado do vídeo do avatar -->

| Artefato | Arquivo |
|----------|---------|
| Retrato do avatar (imagem) | [`assets/avatar.jpg`](assets/avatar.jpg) |
| Narração (áudio) | [`audio/narracao.mp3`](audio/narracao.mp3) |
| Vídeo do avatar falando | [`output/avatar_natty.mp4`](output/avatar_natty.mp4) |

### 🎬 Vídeo

<p align="center">
<video src="output/avatar_natty.mp4" controls width="480"></video>
</p>

### 🖼️ Retrato

<p align="center">
<img src="assets/avatar.jpg" width="400"/>
</p>

### 🔊 Áudio da narração

<div align="center">
<audio src="audio/narracao.mp3" controls></audio>
</div>

## 💭 Reflexão

Criar algo "natty" com IA ainda exige artesanato. A imagem sai quase pronta,
mas detalhes como posição da câmera, expressão e iluminação dependem de um bom
prompt — e o vídeo só fica natural com edição cuidadosa de movimento e ritmo.
O que impressiona é o quanto a fronteira entre o real e o gerado já está
tênue: o retrato convence à primeira vista, e a voz sintetizada passa
despercebida no fluxo da fala. O desafio de hoje não é mais "a IA consegue?",
mas "você consegue perceber?".

---

### 👩‍💻 Autora

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/104384378?v=4"
    />
    <p>&nbsp&nbsp&nbspEver Maria Tobias Ferreira<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/everferreira">GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/evermaria">LinkedIn</a>
    </p>
</p>
<br/><br/>

---

*Lab Natty or Not — Bootcamp CAIXA - IA Generativa (DIO) • 2026*

[🔗 Repositório original do lab](https://github.com/digitalinnovationone/lab-natty-or-not)
