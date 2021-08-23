# 1. Build and run

Project is created using `pipenv virtualenv` manager and `python 3.8`. To install
dependencies run:

```
pipenv install
# or
pip install -r requirements.txt
```


To run the application:
```
pipenv run python main,py
# or
python main.py
```

to run unit tests:
```
pipenv run python pytest
# or
pytest .
```

# 2. Documentation

I focused and tested class `Name` as the main problem was the difference in
first names. The surnames looked pretty consistent and comparison between 
initials and names seemed crucial. I've also added class `Author` for utility
and comparison. 

The data preprocessing is 1) clearing data of unwanted signs 2) parsing to 
python array 3) parsing to `Author` - `Name` structure.

Then brute force algorithm uses methods on those classes and set operation to 
compare and create list of unique authors.


# 3. Failure points and bottlenecks

1. Brute force algorithm is not very efficient, could blow up if dataset big enough
2. The output not thoroughly tested (both unit tests and sanity tests)
3. Parsing not yet perfect (eg. 'von', 'de' treated as names)

# 4. Todo before deploy

1. Finish unit testing
2. Test the output and spend a bit of time on testing edge cases (more automatic tests)
3. Consider if algorithm is viable for potential future input size
4. Cache matches somewhere (S3?) for quicker access in the future
5. Build Dockerfile
6. Deploy and/or provision infrastructure
