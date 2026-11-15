import json
from app import *
rows = []
for name, history, public in [('Training',[90,105,120,135],False),('Inference',[40,70,110,170],True)]:
    forecast = forecast_demand(history)
    count = recommend_capacity(forecast)
    policy = validate_deployment(dict(gpu_count=count,image_digest='sha256:'+'a'*64,public_endpoint=public))
    rows.append(dict(workload=name,forecast=forecast,gpus=count,**policy))
print(json.dumps(rows))
