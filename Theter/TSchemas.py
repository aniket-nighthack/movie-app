from typing import Optional, List
from pydantic import BaseModel
import datetime
from sqlalchemy.orm import relationship


# create a schema for theter documents
class CreateTheterDocs(BaseModel):
    shop_act_license: str
    gst_license : str
    

class TheterDocs(CreateTheterDocs):
    id: int 
    tid: int  

    class Config:
        orm_mode = True

# for verification model           
class CreateVerification(BaseModel):
    shopact_verify: bool
    gst_verify: bool
    is_live: bool
    is_verifyed: bool
    tid : int

class Verification(CreateVerification):
    id : int

    class Config:
        orm_mode = True

# -------------- movies --------------
class CreateMovies(BaseModel):
    mov_name: str
    language: str
    mov_type: str

class Movie(CreateMovies):
    id: int
    create_at: datetime.datetime

    class Config:
        orm_mode = True


# -------------- shows --------------------
class CreateShows(BaseModel):
    tid: int
    screenid: int
    start_time: str 
    end_time: str
    mid: int
    available_seats: int 
    book_seats: int 
    show_type: bool 
    show_ticket: int 
    show_date: str 

class Show(CreateShows):
    id = int
    create_at = datetime.datetime

    class Config:
        orm_mode = True    

# -------------- screen seats schemas ----------------
class CreateSeat(BaseModel):
    screenid: int
    tid: int
    seat_name: str 
    seat_price: int 
    seat_status : bool

class Seats(CreateSeat):
    id : int

    class Config:
        orm_mode = True    


# -------------- screen schemas --------------------
class CreateScreen(BaseModel):
    screen_type: str  
    tid: int


class Screen(CreateScreen):
    id : int
    seats: List[Seats] 

    class Config:
        orm_mode = True




# for create and update
class CreateUpdateTheter(BaseModel):
    t_name : str
    t_address : str
    t_contact : str
    opening_time : str
    closing_time : str

class Theter(CreateUpdateTheter):
    id : int
    auth_token : str
    create_at: datetime.datetime
    docs: List[TheterDocs]
    verification: List[Verification]
    screens: List[Screen]

    class Config:
        orm_mode = True


 

