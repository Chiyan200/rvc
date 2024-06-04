import os
import subprocess
import sys
import shutil
import gradio as gr
from assets.i18n.i18n import I18nAuto
from core import (
    run_preprocess_script,
    run_extract_script,
    run_train_script,
    run_index_script,
    run_prerequisites_script,
)
from rvc.configs.config import max_vram_gpu, get_gpu_info
from rvc.lib.utils import format_title
from tabs.settings.restart import restart_applio

i18n = I18nAuto()
now_dir = os.getcwd()
sys.path.append(now_dir)

pretraineds_v1 = [
    (
        "pretrained_v1/",
        [
            "D32k.pth",
            "D40k.pth",
            "D48k.pth",
            "G32k.pth",
            "G40k.pth",
            "G48k.pth",
            "f0D32k.pth",
            "f0D40k.pth",
            "f0D48k.pth",
            "f0G32k.pth",
            "f0G40k.pth",
            "f0G48k.pth",
        ],
    ),
]

folder_mapping = {
    "pretrained_v1/": "rvc/pretraineds/pretrained_v1/",
}

pretraineds_custom_path = os.path.join(
    now_dir, "rvc", "pretraineds", "pretraineds_custom"
)

pretraineds_custom_path_relative = os.path.relpath(pretraineds_custom_path, now_dir)

if not os.path.exists(pretraineds_custom_path_relative):
    os.makedirs(pretraineds_custom_path_relative)


def get_pretrained_list(suffix):
    return [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(pretraineds_custom_path_relative)
        for filename in filenames
        if filename.endswith(".pth") and suffix in filename
    ]


pretraineds_list_d = get_pretrained_list("D")
pretraineds_list_g = get_pretrained_list("G")
continueTrainingTrue = False


voiceActorArr = [
    "arjun",
    "keerthySuresh",
    "mysskin",
    "siddharth",
    "sjSuriya",
    "andrea",
    "berlin",
    "denver",
    "ladyPloice",
    "nairobi",
    "pelurmo",
    "policeOffice",
    "tokyo",
]


def runFull(actor):
    initialData = {
        "modelName": actor,
        "dataPath": rf"F:\softwareSrc\Applio-3.1.1\rvc\Voicemodels\download\{actor}",
        "sampleRate": 48000,
        "version": "v2",
        "f0method": "harvest",
        "hopLength": 128,
        "batch_size": 60,
        "saveEachEpoch": 600,
        "totalEpoch": 600,
        "pitchGuidance": True,
        "pretrained": True,
        "saveOnlyLatest": True,
        "saveEveryWeights": True,
        "gpu": 0,
        "overTraingDetect": False,
        "overTraining_thersold": 50,
        "pretrained": True,
        "custom_pretrained": False,
    }
    preprocessor = run_preprocess_script(
        initialData["modelName"], initialData["dataPath"], initialData["sampleRate"]
    )  # model_name, dataset_path, sampling_rate

    mName = initialData["modelName"]
    if preprocessor == f"Model {mName} preprocessed successfully.":

        featureExtract = run_extract_script(
            initialData["modelName"],
            initialData["version"],
            initialData["f0method"],
            initialData["hopLength"],
            initialData["sampleRate"],
        )  # model_name, rvc_version, f0method, hop_length, sampling_rate

    if (
        featureExtract == f"Model {mName} extracted successfully."
    ) or continueTrainingTrue == True:
        index = run_index_script(initialData["modelName"], initialData["version"])
        if index == f"Index file for {mName} generated successfully.":

            run_train_script(
                initialData["modelName"],
                initialData["version"],
                str(initialData["saveEachEpoch"]),
                initialData["saveOnlyLatest"],
                initialData["saveEveryWeights"],
                str(initialData["totalEpoch"]),
                str(initialData["sampleRate"]),
                str(initialData["batch_size"]),
                str(initialData["gpu"]),
                initialData["pitchGuidance"],
                initialData["overTraingDetect"],
                str(initialData["overTraining_thersold"]),
                initialData["pretrained"],
                initialData["custom_pretrained"],
                [],
                [],
            )
            # model_name,
            # rvc_version,
            # save_every_epoch,
            # save_only_latest,
            # save_every_weights,
            # total_epoch,
            # sampling_rate,
            # batch_size,
            # gpu,
            # pitch_guidance,
            # overtraining_detector,
            # overtraining_threshold,
            # pretrained,
            # custom_pretrained,
            # g_pretrained_path=None,
            # d_pretrained_path=None,


def runTrain(actor):
    initialData = {
        "modelName": actor,
        "dataPath": rf"F:\softwareSrc\Applio-3.1.1\rvc\Voicemodels\download\{actor}",
        "sampleRate": 48000,
        "version": "v2",
        "f0method": "harvest",
        "hopLength": 128,
        "batch_size": 60,
        "saveEachEpoch": 600,
        "totalEpoch": 600,
        "pitchGuidance": True,
        "pretrained": True,
        "saveOnlyLatest": True,
        "saveEveryWeights": True,
        "gpu": 0,
        "overTraingDetect": False,
        "overTraining_thersold": 50,
        "pretrained": True,
        "custom_pretrained": False,
    }
    run_train_script(
        initialData["modelName"],
        initialData["version"],
        str(initialData["saveEachEpoch"]),
        initialData["saveOnlyLatest"],
        initialData["saveEveryWeights"],
        str(initialData["totalEpoch"]),
        str(initialData["sampleRate"]),
        str(initialData["batch_size"]),
        str(initialData["gpu"]),
        initialData["pitchGuidance"],
        initialData["overTraingDetect"],
        str(initialData["overTraining_thersold"]),
        initialData["pretrained"],
        initialData["custom_pretrained"],
        [],
        [],
    )


for actor in voiceActorArr:
    runFull(actor)


# model_name, rvc_version
