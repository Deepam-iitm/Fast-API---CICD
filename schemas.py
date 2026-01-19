from pydantic import BaseModel, Field
from typing import Annotated

class SimpleInterestRequest(BaseModel):
    principal: Annotated[float, Field(gt=1000, description="What is your principle amount?")]
    rate: Annotated[float, Field(gt=0, description="Annual interest rate (%)")]
    time: Annotated[float, Field(gt=0, lt=6, description="Time in years")]

