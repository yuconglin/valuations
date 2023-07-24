# Instructions
Set up a virtual environment.
```
$ cd valuations
$ python3 -m venv ../valuations_venv
$ . ../valuations_venv/bin/activate
(valuations_venv) $ pip install -r requirements.txt
```

If you are first time user or just updated the ``requirements.in`` file, please run the following commands to update ``requirements.txt``.
```
(valuations_venv) $ python -m pip install pip-tools
(valuations_venv) $ pip-compile -o requirements.txt --generate-hashes --allow-unsafe --resolver=backtracking requirements.in
```


We can then use the following command to run a notebook
```
(valuations_venv) $ jupyter-lab your-notebook.ipynb
```
You can see it in your browser.