# Multimedia

A modern web page combines text, images, audio, video, and animations seamlessly. Behind every video that loads instantly and every photo that downloads in seconds is a compression algorithm carefully removing data that your eyes and ears won't miss.

> [!NOTE] Grade 11
> Multimedia and compression are Grade 11 topics. Focus on lossless vs lossy compression, file formats, and streaming.

---

## What is Multimedia?

**Multimedia** is the combination of multiple types of media content — text, images, audio, video, and animation — delivered through a computer or device.

| Media Type | File Formats | Typical Use |
|---|---|---|
| Text | .txt, .doc, .pdf | Documents, articles |
| Images | .jpg, .png, .gif, .svg, .webp | Photos, graphics, icons |
| Audio | .mp3, .wav, .flac, .aac | Music, podcasts, voice |
| Video | .mp4, .avi, .mkv, .webm | Films, tutorials, streaming |
| Animation | .gif, .webm, CSS animations | Web graphics, short loops |

---

## Compression

**Compression** reduces file size by encoding data more efficiently. Smaller files are faster to upload, download, and stream, and take up less storage.

### Lossless vs Lossy Compression

| Feature | **Lossless** | **Lossy** |
|---|---|---|
| How | Removes redundant data patterns; fully reversible | Permanently discards detail that humans barely notice |
| Quality | No quality loss — perfectly reconstructed | Reduced quality (often imperceptible at moderate compression) |
| File size reduction | Moderate | Much greater |
| Use case | Documents, medical images, archival | Photos, audio, video for web |
| Examples | PNG, GIF, ZIP, FLAC, BMP (raw) | JPEG, MP3, MP4, AAC, WebP |

> [!TIP] Choose the right type
> - Compress a logo or screenshot → use **PNG** (lossless — sharp edges preserved)
> - Compress a photograph for web → use **JPEG** (lossy — small file, minimal visible loss)
> - Never use JPEG for screenshots with text — the compression artefacts make text blurry

---

## Image Formats

| Format | Type | Best For | Notes |
|---|---|---|---|
| **JPEG / JPG** | Lossy | Photographs | Variable quality setting; no transparency |
| **PNG** | Lossless | Screenshots, logos, graphics | Supports transparency (alpha channel) |
| **GIF** | Lossless (limited) | Simple animations, icons | Only 256 colours; poor for photos |
| **SVG** | Vector | Icons, illustrations | Scalable to any size without quality loss |
| **WebP** | Both | Web images | Modern format; better compression than JPEG/PNG |
| **BMP** | Uncompressed | Raw image storage | Very large files |

### Image Quality and File Size
- **Resolution**: width × height in pixels (e.g. 1920 × 1080)
- **Colour depth**: bits per pixel — 24-bit = 16.7 million colours
- **File size (uncompressed)**: width × height × colour depth ÷ 8 bytes

```
Example: 1920 × 1080 × 24-bit = 1920 × 1080 × 3 bytes = ~6.2 MB uncompressed
After JPEG compression: ~300 KB–2 MB depending on quality setting
```

---

## Audio Formats and Compression

### How audio compression works:
- **Sampling**: audio wave measured thousands of times per second
- **Bit depth**: number of bits per sample (16-bit = 65,536 amplitude levels)
- **Sample rate**: number of samples per second (44,100 Hz = CD quality)

**Uncompressed audio size:** sample rate × bit depth × channels × duration  
`44,100 Hz × 16-bit × 2 channels = 1,411,200 bits/second ≈ 176 KB/s`

### Audio Formats

| Format | Type | Quality | Use |
|---|---|---|---|
| **WAV** | Uncompressed | Perfect | Recording, professional audio |
| **FLAC** | Lossless compressed | Perfect | Audiophile storage |
| **MP3** | Lossy | Very good at 128–320 kbps | Music streaming, downloads |
| **AAC** | Lossy | Better than MP3 at same size | Apple, streaming services |
| **OGG** | Lossy | Good | Open source streaming |

**MP3 compression removes:**
- Frequencies humans can barely hear
- Sounds masked by louder simultaneous sounds
- Result: file size ~90% smaller than WAV with similar perceived quality at 192+ kbps

---

## Video Formats and Compression

Video = sequence of image frames + audio track  
Uncompressed video is enormous — compression is essential.

**Video = Images × Frame Rate**
At 30 fps, a 1920×1080 video generates: 30 × 6.2 MB = ~186 MB per second uncompressed.

### Video Codecs (compression algorithms)

| Codec | Container | Type | Notes |
|---|---|---|---|
| **H.264** | .mp4, .mkv | Lossy | Most widely supported |
| **H.265 (HEVC)** | .mp4, .mkv | Lossy | 50% smaller than H.264 at same quality |
| **AV1** | .webm | Lossy | Open source; efficient; used by YouTube/Netflix |
| **VP9** | .webm | Lossy | Google's codec; used in YouTube |

**Container vs Codec:**
- **Codec**: algorithm used to compress/decompress video
- **Container (.mp4, .mkv)**: file format that holds video + audio + metadata

### Frame Rate
- 24 fps — film
- 30 fps — standard TV
- 60 fps — gaming, sport
- Higher fps = smoother motion but larger file

---

## Streaming

**Streaming** delivers media continuously over the internet — playback begins before the file fully downloads.

### Types:
| Type | Description | Examples |
|---|---|---|
| **On-demand streaming** | Watch/listen anytime | Netflix, YouTube, Spotify |
| **Live streaming** | Real-time broadcast | Twitch, live sports, news |

### Adaptive Bitrate Streaming (ABR):
- Service continuously monitors your connection speed
- Automatically switches video quality (e.g. 4K → 1080p → 720p) if bandwidth drops
- Minimises buffering — keeps playback smooth

```
Good connection:  4K (15–25 Mbps)
Average connection:  1080p (5–8 Mbps)
Poor connection:  480p (1.5–3 Mbps)
```

### Buffering:
- Video is downloaded slightly ahead of playback
- If download speed drops below playback rate → buffer empties → buffering pause

---

## Digital Rights Management (DRM)

**DRM** is technology used to control how digital content is used, copied, and distributed.

- Prevents unauthorised copying and sharing
- Streaming services encrypt content — only licenced apps can decrypt
- Examples: Netflix, Spotify, Kindle
- Criticism: prevents legitimate personal use (e.g. moving content between devices)

---

## Multimedia on Websites

| Element | Consideration |
|---|---|
| Images | Compress before uploading; use WebP for best compression |
| Video | Embed from YouTube/Vimeo to avoid hosting bandwidth costs |
| Audio | Use compressed MP3/AAC; not WAV |
| Animation | Prefer CSS animations or SVG over heavy GIFs |
| Accessibility | Add alt text to images; captions to videos |
| Performance | Large uncompressed media slows page load → poor SEO |

---

## Key Terms

| Term | Definition |
|---|---|
| **Multimedia** | Combination of text, images, audio, video, animation |
| **Compression** | Reducing file size by encoding data more efficiently |
| **Lossless** | Compression that allows perfect reconstruction — no quality loss |
| **Lossy** | Compression that permanently discards data — smaller files |
| **Codec** | Algorithm for compressing/decompressing audio or video |
| **Container** | File format holding compressed video, audio, and metadata |
| **Streaming** | Delivering media in real-time over the internet |
| **Adaptive bitrate** | Streaming that adjusts quality based on available bandwidth |
| **Buffering** | Pre-loading media ahead of playback |
| **DRM** | Technology controlling how digital content is used/copied |
| **Sample rate** | Number of audio measurements per second (e.g. 44,100 Hz) |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between lossless and lossy compression? Give an example of each."** — Lossless: no quality loss, fully reversible (PNG, FLAC, ZIP); Lossy: permanently removes detail (JPEG, MP3, MP4)
>
> 2. **"Give a reason why JPEG is preferred over PNG for photographs on a website"** — JPEG produces much smaller file sizes using lossy compression; for photographs the quality loss is barely noticeable, resulting in faster page loads
>
> 3. **"What is streaming? How is it different from downloading?"** — Streaming delivers media continuously — playback starts immediately; downloading saves the complete file first before playback
>
> 4. **"What is adaptive bitrate streaming?"** — Automatically adjusts video quality based on the user's connection speed to minimise buffering and provide the best experience
>
> 5. **"Why is video compression necessary?"** — Uncompressed video is enormous (hundreds of MB per second); compression reduces file sizes making storage, transfer, and streaming practical
