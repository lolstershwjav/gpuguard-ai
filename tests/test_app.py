from app import forecast_demand,validate_deployment,recommend_capacity

def test_policy_blocks_privileged():
    result=validate_deployment({'privileged':True,'image_digest':'sha256:abc','gpu_count':1})
    assert not result['approved']

def test_forecast_and_capacity():
    predicted=forecast_demand([100,110,120])
    assert len(predicted)==3 and recommend_capacity(predicted)>0
