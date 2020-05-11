# Geowrap  

Geowrap is a wrap built using Python and Pandas able to enrich a list of places name with the corresponding ID from [geonames](https://www.geonames.org/) database.     

## Getting Started

### Prerequisites

- Python3
- [Pandas](https://pypi.org/project/pandas/)
- [Requests](https://pypi.org/project/request/)
- [Jsonlib](https://pypi.org/project/jsonlib/)
- [Geonames API access](http://www.geonames.org/login)

### Installing

#### Clone the git repo

```
git clone https://github.com/gtadigital/Script.git
```

#### Install the dependencies with pip

```
pip3 install pandas

pip3 install requests2

pip3 install jsonlib
```

## Workflow

- Create an Excel sheet file and write the place values in the column A 
- Run the script geowrap.py 
- Copy the output from the .txt file in the column B
- If needed split the output values in two columns ("Text to columns" command in Excel). E.g.
  
    |ColA                        |   ColB                           |
    |----------------------------|----------------------------------|
    |Zürich, Drusbergstrasse     |https://www.geonames.org/10382218 |
- Align results (1:1 correspondence between values)
  - Create a new empty column B 
  - In the column B write the formula: ``` =IF(ISNA(MATCH(A1;C:C;0));"";INDEX(C:C;MATCH(A1;C:C;0))) ``` and iterate the formula till the end of the list
  - Create a new empty column C
  - In the column C write the formula: ``` =IFERROR(INDEX($E:$E;MATCH($B1;$D:$D;0));"") ``` and iterate the formula till the end of the list

## Useful links:
- [GeoNames Web Services Documentation](https://www.geonames.org/export/web-services.html)
- [Pandas](https://pandas.pydata.org/)