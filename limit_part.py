import tkinter as tk
import sympy as sy


def main():
    main_part_of_my_project()

def main_part_of_my_project():
            with open('limit_expr.txt','r') as expr_lim:
                expr_lim=expr_lim.read()
                expr_lim=expr_lim.split(',')
            
            with open('limit_questions.txt','r') as limits:
                limits=limits.read()
                limits=limits.split(',')
            
            x=sy.symbols('x')
            solutions_limit=[]
            for i in range(5):
                expr_1=limits[i]
                solve_it=sy.limit(expr_1,x,i)
                solutions_lim=solve_it.evalf()
                solutions_lim=int(solutions_lim)
                solutions_limit.append(solutions_lim)
                
                
                
            limit_question_title=tk.Label(form_quest,text='1)FIND THE LIMIT OF THE FOLLOWING EXPRESSIONS AT POINT (0,1,2,3,4 RESPECTIVELY)',font='Times 13 bold')
            limit_question_title.place(x=5,y=40)
            limits_label1=tk.Label(form_quest,text='f(x)='+expr_lim[0]+'=',fg='black',font=('Times 13'))
            limit_1_entry=tk.Entry()#Entry
            limit_1_entry.place(x=93,y=74,height=17,width=40)
            limits_label1.place(x=5,y=70)
            
            limits_label2=tk.Label(form_quest,text='f(x)=x²+3x+9'+'=',fg='black',font=('Times 13'))
            limit_2_entry=tk.Entry()#Entry
            limit_2_entry.place(x=121,y=104,height=17,width=40)
            
            limits_label2.place(x=5,y=100)
            limits_label3=tk.Label(form_quest,text='f(x)=x⁵'+'=',fg='black',font=('Times 13'))
            limit_3_entry=tk.Entry()#Entry
            limit_3_entry.place(x=70,y=134,height=17,width=40)
            limits_label3.place(x=5,y=130)
            
            
            limits_label4=tk.Label(form_quest,text='f(x)='+expr_lim[3]+'=',fg='black',font=('Times 13'))
            limits_label4.place(x=5,y=160)
            limit_4_entry=tk.Entry()#Entry
            limit_4_entry.place(x=92,y=164,height=17,width=40)
            
            limits_label5=tk.Label(form_quest,text='f(x)='+expr_lim[4]+'=',fg='black',font=('Times 13'))
            limits_label5.place(x=5,y=190)
            limit_5_entry=tk.Entry()#Entry
            limit_5_entry.place(x=81,y=194,height=17,width=40)
            
            
            
