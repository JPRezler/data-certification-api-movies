import joblib
import pandas as pd

PATH_TO_LOCAL_MODEL = 'model.joblib'

def get_model(path_to_joblib):
    pipeline = joblib.load(path_to_joblib)
    return pipeline

def pred_api(original_title ,
        title          ,
        release_date   ,
        duration_min                ,
        description    ,
        budget                      ,
        original_language,
        status         ,
        number_of_awards_won        ,
        number_of_nominations       ,
        has_collection              ,
        all_genres     ,
        top_countries  ,
        number_of_top_productions   ,
        available_in_english        ):
    """
        the pipeline expects to be trained with a DataFrame containing
        the following data types in that order
        ```
        original_title              string
        title                       string
        release_date                string
        duration_min                float
        description                 string
        budget                      float
        original_language           string
        status                      string
        number_of_awards_won        int
        number_of_nominations       int
        has_collection              int
        all_genres                  string
        top_countries               string
        number_of_top_productions   float
        available_in_english        bool
        ```
    """
    df_pred = pd.DataFrame([{
    'original_title'            :original_title            ,
    'title'                     :title                     ,
    'release_date'              :release_date              ,
    'duration_min'             : float(duration_min)             ,
    'description'               :description               ,
    'budget'                   : float(budget)                   ,
    'original_language'         :original_language         ,
    'status'                    :status                    ,
    'number_of_awards_won'   :   int(number_of_awards_won)   ,
    'number_of_nominations'  :   int(number_of_nominations)  ,
    'has_collection'         :   int(has_collection)         ,
    'all_genres'                :all_genres                ,
    'top_countries'             :top_countries             ,
    'number_of_top_productions': float(number_of_top_productions),
    'available_in_english'    :  bool(available_in_english)    
    }])

    pipeline = joblib.load(PATH_TO_LOCAL_MODEL)
    y_pred = pipeline.predict(df_pred)
    return int(y_pred[0])