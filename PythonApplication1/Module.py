def Kontroll(ik:str):
    """Isikukoodi kontroll number
    On vaja isikukoodi sisestada
    :param str ik: Inimese isikukood
    :rtype: var Maramata tuup
    """
    ik_list=list(ik)
    s=0
    for i in range(0,10):
         s+=(i%9+1)*int(ik_list[i])
         print(f"{i%9+1}*{int(ik_list[i])}+", end="")
    print(s)
    s=s-(s//11)*11
    print(s)
    if s==int(ik_list[10]):
        vastus=s
    else:
        vastus="Kontroll number on vale"
    return vastus
def Haigla(ik3:int):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3:
    :rtype str Haigla ja koht:
    """
    if ik3>1 and ik3<=10:
       haigla="Kuresaare"
    elif ik3>10 and ik3<19:
       haigla="Tartu"
    elif ik3>20 and ik3<221:
       haigla="Ida-Tallinna keskhaigla"
    elif ik3>220 and ik3<271:
       haigla="Ida-Viru keskhaigla"
    elif ik3>270 and ik3<371:
       haigla="Maarjamoisa kliinikum"
    elif ik3>370 and ik3<421:
       haigla="Narva"
    elif ik3>420 and ik3<471:
       haigla="Parnu"
    elif ik3>470 and ik3<491:
       haigla="Pelgulinna sunnitusmaja"
    elif ik3>490 and ik3<521:
       haigla="Jarvamaa"
    elif ik3>520 and ik3<571:
       haigla="Rakvere"
    elif ik3>570 and ik3<601:
       haigla="Valga"
    elif ik3>600 and ik3<651:
       haigla="Viljandi"
    elif ik3>650 and ik3<701:
       haigla="Louna-Eesti(Voru)"
    return haigla
def Sugu(ik1:int)->str:
    if ik1%2:
        sugu="naine"
    else:
        sugu="mees"
    return sugu
    
