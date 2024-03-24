import os
import openai
import pandas as pd
from dotenv import dotenv_values
from openai import OpenAI
from git import Repo
from pathlib import Path

pd.options.display.max_columns = None
# pd.options.display.max_rows = None

config = dotenv_values(f"{os.path.expanduser('~')}/.env")
os.environ['OPENAI_API_KEY'] = config["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)
PATH_TO_BLOG_REPO = Path(f'{os.path.dirname(__file__)}\\.get')
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)

def update_blog(commit_message='Updates blog'):
    #GitPython  --- Repo location
    repo = Repo(PATH_TO_BLOG_REPO)
    #git add
    repo.git.add(all=True)
    # git commit -m "update blog"
    repo.index.commit(commit_message)
    # git push origin
    origin = repo.remote(name='origin')
    origin.push()

random_test_string = 'lkdnsdbksdfksdkdsfk'
with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write(random_test_string)


