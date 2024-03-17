import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import soundfile as sf
import os
import torch
from TTS.api import TTS
import whisper
from datetime import datetime
import warnings
import logging
warnings.filterwarnings("ignore")
logging.getLogger('transformers').setLevel(logging.ERROR)
logging.getLogger('TTS').setLevel(logging.ERROR)


def load_model(model_name):
    model_path = f"inputs/text/llm_models/{model_name}"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(model_path)
    return tokenizer, model.to(device)


def transcribe_audio(audio_file_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("medium", device=device)
    result = model.transcribe(audio_file_path)
    return result["text"]


def generate_text_and_speech(input_text, input_audio, llm_model_name, avatar_name, enable_tts, speaker_wav, language,
                             chat_dir=None):
    prompt = transcribe_audio(input_audio) if input_audio else input_text

    tokenizer, llm_model = None, None
    tts_model = None
    whisper_model = None

    try:
        tokenizer, llm_model = load_model(llm_model_name)
        if enable_tts:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            tts_model = TTS("xtts_v2").to(device)
        if input_audio:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            whisper_model = whisper.load_model("medium", device=device)

        inputs = tokenizer.encode(prompt, return_tensors="pt")
        device = llm_model.device
        inputs = inputs.to(device)
        outputs = llm_model.generate(inputs, max_length=512, pad_token_id=tokenizer.eos_token_id)
        generated_sequence = outputs[0][inputs.shape[-1]:]
        text = tokenizer.decode(generated_sequence, skip_special_tokens=True)

        avatar_path = f"inputs/image/avatars/{avatar_name}" if avatar_name else None
        audio_path = None

        if enable_tts:
            wav = tts_model.tts(text=text, speaker_wav=f"inputs/audio/voices/{speaker_wav}", language=language)
            if not chat_dir:
                now = datetime.now()
                chat_dir = os.path.join('outputs', f"chat_{now.strftime('%Y%m%d_%H%M%S')}")
                os.makedirs(chat_dir)
                os.makedirs(os.path.join(chat_dir, 'text'))
                os.makedirs(os.path.join(chat_dir, 'audio'))

            now = datetime.now()
            audio_filename = f"output_{now.strftime('%Y%m%d_%H%M%S')}.wav"
            audio_path = os.path.join(chat_dir, 'audio', audio_filename)
            sf.write(audio_path, wav, 22050)

        if not chat_dir:
            now = datetime.now()
            chat_dir = os.path.join('outputs', f"chat_{now.strftime('%Y%m%d_%H%M%S')}")
            os.makedirs(chat_dir)
            os.makedirs(os.path.join(chat_dir, 'text'))
            os.makedirs(os.path.join(chat_dir, 'audio'))

        chat_history_path = os.path.join(chat_dir, 'text', 'chat_history.txt')
        with open(chat_history_path, "a", encoding="utf-8") as f:
            f.write(f"Human: {prompt}\n")
            f.write(f"AI: {text}\n\n")

    finally:
        if tokenizer is not None:
            del tokenizer
        if llm_model is not None:
            del llm_model
        if tts_model is not None:
            del tts_model
        if whisper_model is not None:
            del whisper_model
        torch.cuda.empty_cache()

    return text, avatar_path, audio_path, chat_dir


llm_models_list = [model for model in os.listdir("inputs/text/llm_models") if not model.endswith(".txt")]
avatars_list = [None] + [avatar for avatar in os.listdir("inputs/image/avatars") if not avatar.endswith(".txt")]
speaker_wavs_list = [wav for wav in os.listdir("inputs/audio/voices") if not wav.endswith(".txt")]

iface = gr.Interface(
    fn=generate_text_and_speech,
    inputs=[
        gr.Textbox(label="Введите ваш запрос"),
        gr.Audio(type="filepath", label="Запишите ваш запрос"),
        gr.Dropdown(choices=llm_models_list, label="Выберите языковую модель"),
        gr.Dropdown(choices=avatars_list, label="Выберите аватар", value=None),
        gr.Checkbox(label="Включить TTS", value=False),
        gr.Dropdown(choices=speaker_wavs_list, label="Выберите голос", interactive=True),
        gr.Dropdown(choices=["en", "ru"], label="Выберите язык голоса", interactive=True),
        gr.State()
    ],
    outputs=[
        gr.Textbox(label="Текстовый ответ от LLM", type="text"),
        gr.Image(type="filepath", label="Аватар"),
        gr.Audio(label="Аудио ответ от LLM", type="filepath"),
        gr.State()
    ],
    title="НейроЧатWebUI (АЛЬФА)",
    description="Этот пользовательский интерфейс позволяет вам вводить любой текст или аудио и получать "
                "сгенерированный ответ. Вы можете выбрать модель, "
                "аватар, голос и язык из раскрывающихся списков. Попробуйте и посмотрите, что произойдет!",
    allow_flagging="never",
    css=".output-image { width: 100px; height: 100px; }"
)

iface.launch()
