from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prey import Prey
import uuid
from constants import BASE_RESUME_PATH

app = FastAPI()

# Define the allowed origins
origins = [
    "chrome-extension://cflffgdapomeanpinekfbogljaimjcmg",
    "http://localhost",
    "http://localhost:8000"
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class JobDescription(BaseModel):
    context: str


class ResumeData(BaseModel):
    new_tag: str
    new_skills: str
    instance_id: str


# In-memory storage for Prey instances
prey_instances = {}


@app.post("/process")
async def process(job_desc: JobDescription):
    instance_id = str(uuid.uuid4())
    prey_instance = Prey(
        doc_path=BASE_RESUME_PATH, context=job_desc.context)
    new_tag, new_skills = prey_instance.get_tag_and_skills()
    prey_instances[instance_id] = prey_instance
    return {"new_tag": new_tag, "new_skills": new_skills, "instance_id": instance_id}


@app.post("/modify_resume")
async def modify_resume(resume_data: ResumeData):
    instance_id = resume_data.instance_id
    prey_instance = prey_instances.get(instance_id)
    if not prey_instance:
        raise HTTPException(status_code=404, detail="Prey instance not found")
    try:
        prey_instance.modify_resume(
            new_tag=resume_data.new_tag, new_skills=resume_data.new_skills)
        return {"message": "Resume modified successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
