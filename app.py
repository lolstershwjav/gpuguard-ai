from statistics import mean

def forecast_demand(history: list[float], horizon: int = 3) -> list[float]:
    if not history or horizon < 1: raise ValueError('nonempty history and positive horizon required')
    if any(x < 0 for x in history): raise ValueError('demand cannot be negative')
    baseline=mean(history[-min(5,len(history)):])
    trend=(history[-1]-history[0])/max(1,len(history)-1)
    return [round(max(0,baseline+trend*(i+1)),2) for i in range(horizon)]

def validate_deployment(config: dict) -> dict:
    violations=[]
    if config.get('public_endpoint',False): violations.append('Public endpoint requires explicit approval')
    if config.get('privileged',False): violations.append('Privileged container is disallowed')
    if not config.get('image_digest','').startswith('sha256:'): violations.append('Pin container image by SHA256 digest')
    if config.get('gpu_count',0) <= 0: violations.append('Request at least one GPU')
    return {'approved':not violations,'violations':violations}

def recommend_capacity(forecast: list[float], gpu_capacity: float = 100) -> int:
    if gpu_capacity <= 0: raise ValueError('GPU capacity must be positive')
    return max(1,__import__('math').ceil(max(forecast,default=0)/gpu_capacity))
