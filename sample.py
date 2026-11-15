from app import *
prediction=forecast_demand([90,105,120,135])
print(prediction, recommend_capacity(prediction))
print(validate_deployment({'gpu_count':2,'image_digest':'sha256:example','privileged':False}))
