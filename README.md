# OVOS HiTZ STT

## Description

OpenVoiceOS STT plugin for **Basque** models trained by [HiTZ](https://huggingface.co/HiTZ)

> GPU is **strongly recommended**

Online demo [HiTZ/Aholab's Basque Speech-to-Text](https://huggingface.co/spaces/HiTZ/Demo_Basque_ASR)

## Install

`pip install ovos-stt-plugin-HiTZ`

## Configuration

```json
  "stt": {
    "module": "ovos-stt-plugin-HiTZ",
    "ovos-stt-plugin-HiTZ": {
        "model": "stt_eu_conformer_transducer_large"
    }
  }
```

currently two models are available, [conformer-CTC](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) and [conformer-transducer](https://huggingface.co/HiTZ/stt_eu_conformer_transducer_large)

## Credits

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337

<img src="img_1.png"  width="64"/>

[HiTZ/Aholab's Basque Speech-to-Text model Conformer](https://huggingface.co/HiTZ/stt_eu_conformer_ctc_large) - models trained on a composite dataset comprising of 548 hours of Basque speech. The model was fine-tuned from a pre-trained Spanish stt_es_conformer_ctc_large model. It is a non-autoregressive "large" variant of Conformer, with around 121 million parameters

> This project with reference 2022/TL22/00215335 has been partially funded by the Ministerio de Transformación Digital and by the Plan de Recuperación, Transformación y Resiliencia – Funded by the European Union – NextGenerationEU ILENIA and by the project IkerGaitu funded by the Basque Government. This model was trained at Hyperion, one of the high-performance computing (HPC) systems hosted by the DIPC Supercomputing Center.
