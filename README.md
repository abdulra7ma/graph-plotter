# Graph plotter

## Table of contents
- [Graph plotter](#graph-plotter)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Setup](#setup)
  - [More Customisation](#more-customisation)


## General info
This python script provides is an Online blog that aims to encourage the young generation to read more.

## Setup
1. install the task requirements
```
pip install -r requirements.txt
```
2. run the task
```
python manage.py
```

## More Customisation
1. add new function 
```
class CalculusFuncs:
    ...
    # add your new function
    def your_func_name(self, *args, **kwargs):
        write your code
```
2. plot the new function
```
...
calc_func = CalculusFunction()
plotter = Plotter()

plotter.draw_graph(coord_y=calc_func.your_func_name(plotter.inputs), label="my new function label")
...
```
