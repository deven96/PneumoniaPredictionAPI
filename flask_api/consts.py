"""@desc 
		Constants

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2018-12-31 03:34:05
 		@modify date 2018-12-31 03:34:05

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """
import os
from types import SimpleNamespace

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(CURRENT_DIR, "static", "model")

TEMPLATE_DIR = os.path.join(CURRENT_DIR, "templates")

TARGET_SIZE = (224, 224)

LOADING_MESSAGE = ("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started")

#celery
CELERY_DICT = {
	"BROKER_URL": "redis://localhost:6379",
	"RESULT_BACKEND": "redis://localhost:6379",
}

CELERY = SimpleNamespace(**CELERY_DICT)

# model

MODEL_LOCATION = os.path.join(STATIC_DIR, "best.pneumonia.hdf5")
