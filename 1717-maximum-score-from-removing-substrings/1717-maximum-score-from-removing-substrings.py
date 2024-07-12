class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        p=0
        st=[]
        if y>x:
            for i in s:
                if i=='a':
                    if st and st[-1]=='b':
                        p=p+y
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
            temp=st
            st=[]
            for i in temp:
                if i=='b':
                    if st and st[-1]=='a':
                        p=p+x
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        else:
            for i in s:
                if i=='b':
                    if st and st[-1]=='a':
                        p=p+x
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
            temp=st
            st=[]
            for i in temp:
                if i=='a':
                    if st and st[-1]=='b':
                        p=p+y
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        return p