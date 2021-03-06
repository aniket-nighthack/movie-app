from Theter.TCrud import *
from Theter.TModels import *
from Theter.TSchemas import *
from fastapi import APIRouter, Depends, HTTPException,  File, UploadFile
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from Connection.database import *
from Common.APIResponses import Responses
from fastapi_utils import *
import shutil
from User.crud import *
from Common import oauth, token
from Theter.cruds.screens import *
from Theter.cruds.show import *

router = APIRouter(prefix='/theter',
    tags=["Shows"])


@router.get("/show/all-shows/")
def allShows(session:Session = Depends(get_db),current_user: User = Depends(oauth.check_if_admin)):
    return getAllShows(session)

@router.get("/theter-show/{tid}")
def theter_show(tid:int,session:Session = Depends(get_db),current_user: User = Depends(oauth.check_if_admin)):
    return getTheterShows(session, tid)

@router.get("/current-show")
def currentTheterShows(session:Session = Depends(get_db), current_user: User = Depends(oauth.check_if_merchant)):
    return currentTShows(session, current_user.id)
    
@router.post("/show/create-show/")
def createshow(show:CreateShows, session:Session = Depends(get_db),current_user: User = Depends(oauth.check_if_merchant)):
    return addShow(session, show)

@router.put("/update-show")
def updateShow(show_id:int,show:CreateShows,session:Session = Depends(get_db), current_user:User = Depends(oauth.check_if_merchant)):
    return updateShowInfo(session, show, show_id)

@router.delete("/delete-show")
def showDelete(show_id:int, session:Session = Depends(get_db), current_user:User = Depends(oauth.check_if_merchant)):
    return deleteShow(session, show_id)


