import streamlit as st

def response(code, condition, mylist=[]):       
    if code=='Pass':
            return True, False

    state =  False, False
    try:
        exec(code)
    except Exception as e:
        st.markdown(f""" Your code has an erorr ({e}). Modify your code and submit again. Hint: if you can't get the right answer but nevertheless want to advance to the next question, you can enter `Pass` as your code and submit that.""")
    else:
        if eval(condition):
            state = True, True
        else:
            st.markdown(""" Wrong answer, modify your code and submit again. Hint: if you can't get the right answer but nevertheless want to advance to the next question, you can enter `Pass` as your code and submit that. """)
    return state


def app():
    
    num_qs = 5
    for i in range(1, num_qs+1):
        setattr(st.session_state, 'q'+str(i), getattr(st.session_state, 'q'+str(i), (False, False)))
    st.session_state.score = 0

    st.title("BP EXPO 2021 Python coding challenge")
    st.markdown(""" ## Welcome! 
    Want to test your Python coding skills? Let's get started! 
    """)

    st.sidebar.markdown("""# Your Scoreboard""")
    scoring = st.sidebar.empty()
    scoring.markdown(""" You haven't earned any points yet. \n 
    Try to answer at least the first question!""")

    st.markdown(""" ## Question 1 """)
    st.markdown(""" A list is one of the basic data structures in Python. It can be created using square brackets and data items separated with commas. Like this:""")
    st.code("mylist = [1, 2, 3]", language='python')
    st.markdown(""" The way we can add elements to a Python list is by using the append method. Let's say we wanted to add 4 to our list, we'd write:""")
    st.code("mylist.append(4)", language='python')
    st.markdown(""" In the cell below, write Python code to add element 33 to `mylist` and click the Sumbit button.""")

    mylist = [1,2,3]
    q1_code = st.text_area('', key='q1_text')
    if st.button('Submit', key='1'):
        st.session_state.q1 = response(q1_code, 'mylist==[1,2,3,33]', mylist)

    if st.session_state.q1[0]:
        if st.session_state.q1[1]:
            st.session_state.score = sum([getattr(st.session_state, 'q'+str(i))[1] for i in range(1, num_qs+1)])
            scoring.markdown(f"""Congrats! Your score is **{st.session_state.score} point**.\n
Can you also get the next question?""")

        st.markdown(""" ## Question 2 """)
        st.markdown(""" When you want to write multiple commands, you need to write them in separate lines. Let's say we wanted to add 4 as well as 5 to our list, we'd write:""")
        st.code("""mylist.append(4)
mylist.append(5)""", language='python')
        st.markdown(""" In the cell below, write Python code to add elements 66 and 99 to `mylist`. """)

        q2_code = st.text_area('', key='q2_text')
        if st.button('Submit', key='2'):
            st.session_state.q2 = response(q2_code, 'mylist==[1,2,3,66,99]', mylist)
    
                
    if st.session_state.q2[0]:
        if st.session_state.q2[1]:
            st.session_state.score = sum([getattr(st.session_state, 'q'+str(i))[1] for i in range(1, num_qs+1)])
            scoring.markdown(f"""Well done! Your score is **{st.session_state.score} points**.\n
Can you also get the next question?""")
        st.markdown(""" ## Question 3 """)
        st.markdown(""" Under construction...""")
        
        
if __name__ == '__main__':
    app()
