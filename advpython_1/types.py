from typing import List, Tuple, Union

numbers= List[int]=[1,2,3,4,5]

person=Tuple[str, int]=("Anushka", 20)

#union type of variables that can store multiple data types
identifier: Union[int, str]="ID1234"
identifier=12345

n: int=5

name: str="Anushka"

def sum(a: int, b:int)-> int:
    return a+b