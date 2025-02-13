from pydantic import BaseModel, EmailStr


class TestCaseData(BaseModel):
    test_case1: dict
    test_case2: dict
    test_case3: dict
    test_case5: dict


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    salary: int
    department: str


class UserData(BaseModel):
    User1: dict
    User2: dict


class ConfigData(BaseModel):
    initial_setup: dict
    options: dict


class BrowserOptions(BaseModel):
    window_size: str


class InitialSetup(BaseModel):
    base_url: str
    browser: str
    wait_time: int
    poll_frequency: int


class AlertData(BaseModel):
    Alert1: dict
    Alert2: dict
    Alert3: dict


class Alert(BaseModel):
    text: str
    comparable_text: str


class IFrames(BaseModel):
    ParentFrameText: str
    Child_IFrameText: str


class Engineer(BaseModel):
    age: int