def palindrome(st):
    reverse_st=''
    counter=len(st)-1
    st=st.upper()
    
    while counter>=0:
        reverse_st=reverse_st+st[counter]
        counter-=1

    if reverse_st==st:
        return True
    else:
        return reverse_st


