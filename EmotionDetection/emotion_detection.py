import random

def emotion_detector(text_to_analyze):
    """
    Simulated emotion detection function
    """

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Simulación de emociones (para evitar problemas con API real)
    emotions = {
        "anger": round(random.uniform(0, 1), 2),
        "disgust": round(random.uniform(0, 1), 2),
        "fear": round(random.uniform(0, 1), 2),
        "joy": round(random.uniform(0, 1), 2),
        "sadness": round(random.uniform(0, 1), 2)
    }

    dominant = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant

    return emotions