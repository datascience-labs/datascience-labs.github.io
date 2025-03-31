# dash_app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import requests
import json
import time

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Machine Learning with Celery and FastAPI'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-data-upload'),
    dcc.Dropdown(id='x-columns', multi=True, placeholder='Select X columns'),
    dcc.Dropdown(id='y-column', placeholder='Select Y column'),
    dcc.Dropdown(
        id='algorithm',
        options=[
            {'label': 'kNN', 'value': 'kNN'},
            {'label': 'SVM', 'value': 'SVM'}
        ],
        placeholder='Select Algorithm'
    ),
    html.Button('Run Task', id='run-task', n_clicks=0),
    html.Div(id='task-status'),
    html.Div(id='task-result')
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
            return html.Div(['Unsupported file format'])
    except Exception as e:
        return html.Div(['There was an error processing this file.'])
    return df

@app.callback(
    Output('output-data-upload', 'children'),
    Output('x-columns', 'options'),
    Output('y-column', 'options'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is None:
        return html.Div(['No file uploaded']), [], []
    df = parse_contents(contents, filename)
    columns = [{'label': col, 'value': col} for col in df.columns]
    return html.Div([
        html.H5(filename),
        dcc.Markdown(f'### Data Preview\n{df.head().to_markdown()}')
    ]), columns, columns

@app.callback(
    Output('task-status', 'children'),
    Output('task-result', 'children'),
    Input('run-task', 'n_clicks'),
    State('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('x-columns', 'value'),
    State('y-column', 'value'),
    State('algorithm', 'value')
)
def run_task(n_clicks, contents, filename, x_columns, y_column, algorithm):
    if n_clicks == 0 or contents is None or x_columns is None or y_column is None or algorithm is None:
        return '', ''
    df = parse_contents(contents, filename)
    data = df.to_dict(orient='list')
    payload = {
        'data': data,
        'x_columns': x_columns,
        'y_column': y_column,
        'algorithm': algorithm
    }
    response = requests.post('http://fastapi:8000/tasks', json=payload)
    if response.status_code == 200:
        task_id = response.json().get('task_id')
        while True:
            response = requests.get(f'http://fastapi:8000/tasks/{task_id}')
            result = response.json()
            if result['status'] == 'PENDING':
                status = 'Task is pending...'
            elif result['status'] == 'STARTED':
                status = 'Task is started...'
            elif result['status'] == 'SUCCESS':
                status = 'Task is complete. Result:'
                return status, json.dumps(result['result'], indent=2)
            elif result['status'] == 'FAILURE':
                status = 'Task failed with error:'
                return status, result['result']
            else:
                status = f'Task state: {result["status"]}'
            time.sleep(1)
    else:
        return 'Error: ' + response.text, ''

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
