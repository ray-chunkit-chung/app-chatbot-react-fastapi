rmdir /s /q static
xcopy ..\frontend\out static /e /i
pip install --upgrade -r requirements.txt
pip install --upgrade  -r dev-requirements.txt
python main.py