from typing import Optional

from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_nemo import NemoSTT
from ovos_utils import classproperty
from speech_recognition import AudioData


class HiTZSTT(STT):
    VALID_MODELS = [
        "stt_eu_conformer_ctc_large",
        "stt_eu_conformer_transducer_large"
    ]

    def __init__(self, config: dict = None):
        super().__init__(config)
        model = self.config.get("model", "stt_eu_conformer_transducer_large")
        if model in ["conformer_transducer", "conformer_ctc"]:
            model = f"stt_eu_{model}_large"
        if model not in self.VALID_MODELS:
            raise ValueError(f"invalid model, please choose one of {self.VALID_MODELS}")
        self.engine = NemoSTT(config={"model": model, "lang": "eu"})

    def execute(self, audio: AudioData, language: Optional[str] = None):
        return self.engine.execute(audio, language)

    @classproperty
    def available_languages(cls) -> set:
        return {"eu"}


if __name__ == "__main__":
    b = HiTZSTT()
    from speech_recognition import Recognizer, AudioFile

    eu = "/home/miro/PycharmProjects/ovos-stt-nemo-plugin/es.wav"
    ca = "/home/miro/PycharmProjects/ovos-stt-plugin-vosk/example.wav"
    with AudioFile(eu) as source:
        audio = Recognizer().record(source)

    a = b.execute(audio, language="eu")
    print(a)
    # asko eskertzen dut nirekin denbora ematea baina orain alde egin behar dut laster zurekin harrapatuko dudala agintzen dizut
