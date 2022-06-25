"""determina si una lista es incremental o no"""
lista = [3,2,1]
def incre(List):
    reverse = 2
    next= 0
    List.reverse()
    for delet  in List:
        new = List[:]
        new.remove(delet)
        for i in new:
            if next < len(List)-1:
                if i < List[next-reverse]:
                    print(i ,"<", List[next-reverse],i < List[next-reverse])
                    next= next-reverse
                    if len(List)-1 == next:
                        print("lista incremental")
                        return True
                else:
                    next= 0
                    print("lista no incremental")

        if delet == List[len(List)-1]:
            print("loop fin")
            return False

       
    
print(
    incre(lista)
)