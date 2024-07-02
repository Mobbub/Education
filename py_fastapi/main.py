from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'ХУЙ'}

@app.get("/html")
async def html_test():
    return FileResponse('html/index.html')

@app.get('/get_post_test_html')
async def get_post_test_html():
    return FileResponse('html/post_test.html')

@app.post('/post_test_html')
async def post_test_html(data = Body()):
    num_1 = data['num_1']
    num_2 = data['num_2']
    print(num_1 + num_2)
    return {'message': f'{num_1 + num_2}'}

@app.post('/post_test')
async def post_test(data = Body()):
    num_1 = data['num_1']
    num_2 = data['num_2']
    result = num_1 + num_2
    return {'result_str': f'{num_1 + num_2}',
            'result_int': result}

# нерабочая хуйня
# @app.post('/post_test_1')
# async def post_test_1(num_1: int, num_2: int):
#     print(num_1 + num_2)
#     return {'result': f'{num_1 + num_2}'}