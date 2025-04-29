import os
from huggingface_hub import InferenceClient


def build_prompt(message: str) -> str:
    return (
        "Berikut adalah sebuah pesan berisi informasi seseorang. "
        "Tugas Anda adalah mencari dan mengidentifikasi nama lengkap, usia, dan pekerjaan orang tersebut. "
        "Tulis jawaban Anda hanya dalam satu baris, dipisahkan dengan koma tanpa tambahan kata lain.\n\n"
        "Format jawaban: nama,usia,pekerjaan\n\n"
        f"Pesan:\n{message}"
    )

def extract_information(message: str) -> str:
    client = InferenceClient(provider="novita", api_key=os.getenv("API_KEY"))
    prompt = build_prompt(message)

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )

    return response.choices[0].message.content
