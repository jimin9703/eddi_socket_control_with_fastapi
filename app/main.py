import os.path
import sys

import colorama

import uvicorn
from fastapi import FastAPI

from deep_learning.controller.deep_learning_controller import deepLearningRouter
from system_initializer.init import SystemInitializer
from task_manager.manager import TaskManager
from include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()

app = FastAPI()

app.include_router(deepLearningRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
