a,b,c = map(int,input('nhap vao 3 canh cua mot tam giac').split())
if(a>0 and b>0 and c>0 and a+b >c and a+c >b and b+c >a):{
    print('YES')
}
else:
    print('NO')