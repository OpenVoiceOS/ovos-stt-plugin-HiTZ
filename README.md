> **This repository is archived. No further updates will be made.**
> This plugin has been superseded by [ovos-stt-plugin-nemo](https://github.com/OpenVoiceOS/ovos-stt-plugin-nemo). See the migration guide below.

# OVOS HiTZ STT

OpenVoiceOS STT plugin for **Basque** models trained by [HiTZ](https://huggingface.co/HiTZ).

> GPU is **strongly recommended**

Online demo: [HiTZ/Aholab's Basque Speech-to-Text](https://huggingface.co/spaces/HiTZ/Demo_Basque_ASR)

## Migration Guide

Install the parent plugin:

```bash
pip install ovos-stt-plugin-nemo
```

Update your `mycroft.conf`:

```json
"stt": {
    "module": "ovos-stt-plugin-nemo",
    "ovos-stt-plugin-nemo": {
        "model": "stt_eu_conformer_transducer_large",
        "lang": "eu"
    }
}
```

Two Basque models are available:

| Model | HuggingFace |
|-------|------------|
| `stt_eu_conformer_transducer_large` | [HiTZ/stt_eu_conformer_transducer_large](https://huggingface.co/HiTZ/stt_eu_conformer_transducer_large) |
| `stt_eu_conformer_ctc_large` | [HiTZ/stt_eu_conformer_ctc_large](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) |

## Credits

This plugin was developed by [TigreGotico](https://tigregotico.pt) for OpenVoiceOS under the [ILENIA](https://proyectoilenia.es) project.

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project [ILENIA](https://proyectoilenia.es) with reference 2022/TL22/00215337

<img src="img_1.png" width="64"/>

[HiTZ/Aholab's Basque Speech-to-Text model Conformer](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) — models trained on a composite dataset comprising 548 hours of Basque speech, fine-tuned from a pre-trained Spanish `stt_es_conformer_ctc_large` model. Non-autoregressive "large" Conformer variant, ~121 million parameters.

> This project with reference 2022/TL22/00215335 has been partially funded by the Ministerio de Transformación Digital and by the Plan de Recuperación, Transformación y Resiliencia – Funded by the European Union – NextGenerationEU ILENIA and by the project IkerGaitu funded by the Basque Government. This model was trained at Hyperion, one of the high-performance computing (HPC) systems hosted by the DIPC Supercomputing Center.
