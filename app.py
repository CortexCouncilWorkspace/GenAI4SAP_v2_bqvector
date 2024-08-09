from vanna.google import BigQuery_VectorStore
from vanna.google import GoogleGeminiChat
from vanna.flask import VannaFlaskApp
from utilities import (PROJECT_ID, MODEL, LANGUAGE, LOGO_URL, APP_TITLE, APP_SUBTITLE, API_KEY)

class MyVanna(BigQuery_VectorStore, GoogleGeminiChat):
    def __init__(self, config=None):
        BigQuery_VectorStore.__init__(self, config=config)
        GoogleGeminiChat.__init__(self, config=config)

vn = MyVanna(config={'api_key': f'{API_KEY}', 'model': f'{MODEL}', 'language': f'{LANGUAGE}', 'bigquery_dataset_name': 'genai_audit_log'})

vn.connect_to_bigquery(project_id=PROJECT_ID)

app = VannaFlaskApp( 
    vn,
    debug=True, 
    allow_llm_to_see_data=False, 
    logo=LOGO_URL, 
    title=APP_TITLE, 
    subtitle=APP_SUBTITLE, 
    show_training_data=True, 
    suggested_questions=True, 
    sql=True, 
    table=True, 
    csv_download=True, 
    chart=True, 
    redraw_chart=True, 
    auto_fix_sql=True, 
    ask_results_correct=True, 
    followup_questions=True, 
    summarization=False
    )

app.run()