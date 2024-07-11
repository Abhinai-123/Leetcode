class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for i in s:
                if i!=")":
                    st.append(i)
                else:
                    temp=""
                    while(st[-1]!="("):
                        temp=temp+st.pop()
                    st.pop()
                    for j in temp:
                        st.append(j)
        if st:
            return "".join(st)