import tkinter as tk
import emoji as ej
import sympy as sy
import numpy as np


def main():
    main_part_of_my_project()

def main_part_of_my_project():
    form=tk.Tk()
    form.title('User Login System')
    form.attributes('-fullscreen', False)
    form.geometry('1920x1080')
    name=tk.Label(text='Name:',fg='black',font='Times 15 bold')
    name.place(x=5,y=8)
    name_entry=tk.Entry()
    name_entry.place(x=75,y=13)
    last_name=tk.Label(text='Last Name:',fg='black',font='Times 15 bold')
    last_name.place(x=5,y=48)
    last_name_entry=tk.Entry()
    last_name_entry.place(x=115,y=55)
    student_id=tk.Label(text='Student ID:',fg='black',font='Times 15 bold')
    student_id.place(x=5,y=88)
    student_id_entry=tk.Entry()
    student_id_entry.place(x=115,y=95)
    rules_of_users=tk.Label(form,text='BEFORE LOGIN PLEASE READ THE FOLLOWING STATEMENTS!',fg='red',font='Times 18 bold')
    rules_of_users.place(x=3,y=125)

    first_rule=tk.Label(form,text='1) PLEASE ENTER YOUR NAME AND LAST NAME CORRECTLY AND WITH CAPITAL LETTERS,OTHERWISE YOU CAN SEE THE EXAM PAGE BUT YOUR EXAM WILL NOT BE SCORED!',font='Times 13 bold')
    first_rule.place(x=3,y=170)

    second_rule=tk.Label(form,text='2) YOUR NAME AND LAST NAME SHOULD NOT INCLUDE ANY CHARACTER EXCEPT FOR ALPHABET WORDS, OTHERWISE YOU CANNOT SEE THE EXAM PAGE',font='Times 13 bold')
    second_rule.place(x=3,y=200)

    third_rule=tk.Label(form,text='3) YOUR STUDENT ID SHOULD INCLUDE JUST NUMERICAL CHARACTERS, OTHERWISE YOU CANNOT SEE THE EXAM PAGE',font='Times 13 bold')
    third_rule.place(x=3,y=230) 

    good_luck=tk.Label(form,text='GOOD LUCK'+   ej.emojize(':thumbs_up:'),font='Times 15 bold')
    good_luck.place(x=630,y=700)

    def checking_informations():
        def go_to_exam_page_and_questions():
            form_succ_login.destroy()
            form_quest=tk.Tk()
            form_quest.title('QUESTIONS')
            form_quest.geometry('1920x1080')
            form_quest_label=tk.Label(form_quest,text='YOU HAVE 15 QUESTIONS(5 LIMIT,5 DERIVATIVE,5 LINEAR ALGEBRA)')
            form_quest_label2=tk.Label(form_quest,text='LIMIT QUESTIONS ARE SCORED AS 4 POINTS, OTHER QUESTIONS ARE SCORES AS 8 POINTS')
            form_quest_label.pack()
            form_quest_label2.pack()

    #------------------------------------------------------------LIMIT PART OF EXAM------------------------------------------------------------

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
            
            
            

    #----------------------------------------------------DERIVATIVE PART OF EXAM-----------------------------------------------------------------
            with open('derivatives_expr.txt','r') as derivs:
                derivs=derivs.read()
                derivs=derivs.split(',')
            
            
            with open('derivative_questions.txt','r') as derivatives:
                derivatives=derivatives.read()
                derivatives=derivatives.split(',')
            solution_of_der=[]
            for j in range(5):
                expr_2=derivatives[j]
                dx=sy.diff(expr_2,x)
                sol_der=dx.evalf(subs={x: j})
                sol_der=int(sol_der)
                solution_of_der.append(sol_der)
            derivative_question_title=tk.Label(form_quest,text="2)FIND THE DERIVATIVE(f'(x)) OF THE FOLLOWING EXPRESSIONS AT POINT (0,1,2,3,4 RESPECTIVELY)", font='Times 13 bold')
            derivative_question_title.place(x=5,y=210)
            
            
            derivatives_label1=tk.Label(form_quest,text='f(x)='+derivs[0]+'=',fg='black',font='Times 13')
            derivatives_label1.place(x=5,y=230)
            derivatives_1_entry=tk.Entry()
            derivatives_1_entry.place(x=64,y=235,height=17,width=40)


            derivatives_label2=tk.Label(form_quest,text='f(x)=x²'+'=',fg='black',font='Times 13')
            derivatives_label2.place(x=5,y=255)
            derivatives_2_entry=tk.Entry()
            derivatives_2_entry.place(x=70,y=260,height=17,width=40)
            
            
            derivatives_label3=tk.Label(form_quest,text='f(x)=x⁵-7x-5'+'=',fg='black',font='Times 13')
            derivatives_label3.place(x=5,y=280)
            derivatives_3_entry=tk.Entry()
            derivatives_3_entry.place(x=109,y=285,height=17,width=40)
            
            
            derivatives_label4=tk.Label(form_quest,text='f(x)='+derivs[3]+'=',fg='black',font='Times 13')
            derivatives_label4.place(x=5,y=305)
            derivatives_4_entry=tk.Entry()
            derivatives_4_entry.place(x=65,y=310,height=17,width=40)
            
            
            derivatives_label5=tk.Label(form_quest,text='f(x)=x³+5'+'=',fg='black',font='Times 13')
            derivatives_label5.place(x=5,y=330)
            derivatives_5_entry=tk.Entry()
            derivatives_5_entry.place(x=88,y=333,height=17,width=40) 
                

    #-------------------------------------------L.ALGEBRA PART OF EXAM---------------------------------------------------------------------------
            
            my_matrix=np.array([[1,0,5],[2,1,6],[3,4,0]])
            det_of_matrix=np.linalg.det(my_matrix)
            det_of_matrix=round(det_of_matrix)
            
            l_algebra_title=tk.Label(form_quest,text='3)YOU ARE GIVEN A 3x3 MATRIX A. FIND THE DETERMINANT AND INVERSE OF A(A⁻¹).',font='Times 13 bold')
            l_algebra_title.place(x=5,y=350)
            
            matrix_label=tk.Label(form_quest,text='[',font='Times 75 normal')
            matrix_label.place(x=41,y=375)
            
            matrix_label2=tk.Label(form_quest,text=']',font='Times 75 normal')
            matrix_label2.place(x=153,y=375)
            
            matrix_a=tk.Label(form_quest,text='A=',font='Times 20')
            matrix_a.place(x=3,y=415)
            
            matrix_first_row=tk.Label(form_quest,text='1    0    5',font='Times 15 normal')
            matrix_first_row.place(x=78,y=400)
            
            matrix_second_row=tk.Label(form_quest,text='2    1    6',font='Times 15 normal')
            matrix_second_row.place(x=78,y=430)
            
            matrix_third_row=tk.Label(form_quest,text='3    4    0',font='Times 15 normal')
            matrix_third_row.place(x=78,y=460)
            
            
            
            inv_symbol=tk.Label(form_quest,text='A⁻¹  =',font='Times 20 normal')
            inv_symbol.place(x=3,y=569)
            
            inv_parant=tk.Label(form_quest,text='[',font='Times 75 normal')
            inv_parant.place(x=75,y=525)
            
            inv_parant_2=tk.Label(form_quest,text=']',font='Times 75 normal')
            inv_parant_2.place(x=190,y=525)
            
            matrix_det_label=tk.Label(form_quest,text='det(A)=',font='Times 27 normal')
            matrix_det_label.place(x=500,y=477)
            
            det_entry=tk.Entry()
            det_entry.place(x=619,y=489,height=23,width=30)
            
            inv_1_1=tk.Entry()
            inv_1_1.place(x=100,y=557,height=17,width=23)
            
            inv_1_2=tk.Entry()
            inv_1_2.place(x=138,y=557,height=17,width=23)
            
            inv_1_3=tk.Entry()
            inv_1_3.place(x=176,y=557,height=17,width=23)
            
            inv_2_1=tk.Entry()
            inv_2_1.place(x=100,y=587,height=17,width=23)
            
            inv_2_2=tk.Entry()
            inv_2_2.place(x=138,y=587,height=17,width=23)
            
            inv_2_3=tk.Entry()
            inv_2_3.place(x=176,y=587,height=17,width=23)
            
            inv_3_1=tk.Entry()  
            inv_3_1.place(x=100,y=617,height=17,width=23)
            
            inv_3_2=tk.Entry()  
            inv_3_2.place(x=138,y=617,height=17,width=23)
            
            inv_3_3=tk.Entry()  
            inv_3_3.place(x=176,y=617,height=17,width=23)
            
    #--------------------------------------------------------------------------------------------------------------------------------------------


            
    #----------------------------------------------------BUTTON TO SEND ANSWERS------------------------------------------------------------------
            def send_answers():
                try:
                    actual_answers_matrix=[-24,20,-5,18,-15,4,5,-4,1]
                    users_answers_matrix=[]
                    users_answers_matrix.extend([inv_1_1.get(),inv_1_2.get(),inv_1_3.get(),inv_2_1.get(),inv_2_2.get(),inv_2_3.get(),inv_3_1.get(),inv_3_2.get(),inv_3_3.get()])
                    det_answer_of_user=det_entry.get()
                    for e in range(9):
                        users_answers_matrix[e]=int(users_answers_matrix[e])
                    #--------------------------------------------LIMIT CHECK-------------------------------------------------------------------------
                    score_of_limit=0
                    users_answers_limit=[]
                    users_answers_limit.extend([limit_1_entry.get(),limit_2_entry.get(),limit_3_entry.get(),limit_4_entry.get(),limit_5_entry.get()])
                    
                    for k in range(5):
                        if users_answers_limit[k]=='-':
                            score_of_limit+=0
                        else:
                            if int(users_answers_limit[k])==solutions_limit[k]:
                                score_of_limit+=4                
                            else:
                                continue
                        

                    #---------------------------------------------------------------------------------------------------------------------------------
                    
                    
                    #-------------------------------------------DERIVATICE CHECK----------------------------------------------------------------------
                    score_of_derivative=0
                    users_answers_derivative=[]
                    users_answers_derivative.extend([derivatives_1_entry.get(),derivatives_2_entry.get(),derivatives_3_entry.get(),derivatives_4_entry.get(),derivatives_5_entry.get()])
                    for t in range(5):
                        if users_answers_derivative[t]=='-':
                            score_of_derivative+=0
                        else:
                            if int(users_answers_derivative[t])==solution_of_der[t]:
                                score_of_derivative+=8
                            else:
                                continue
                    form_quest.destroy()
                    #------------------------------------------------------------------------------------------------------------------------------------
                        
                    
                    #------------------------------------------L.ALGEBRA CHECK---------------------------------------------------------------------------
                    inverse_part=0
                    det_part=0
                    
                    for b in range(9):
                        if users_answers_matrix[b]=='-':
                            inverse_part+=0
                        else:         
                            if users_answers_matrix[b]==actual_answers_matrix[b]:
                                inverse_part+=1
                            else:
                                continue

                    if det_answer_of_user=='-':
                        det_part+=0
                    else:       
                        if int(det_answer_of_user)==int(det_of_matrix):
                            det_part+=8
                        else:
                            pass
                    

                    
                    form_quest_2=tk.Tk()
                    form_quest_2.title('QUESTION 2')
                    form_quest_2.geometry('1920x1080')
                    
                    true_false_title=tk.Label(form_quest_2,text='4)DETERMINE THAT EACH OF THE FOLLOWING STATEMENTS ARE TRUE OR FALSE(WRITE T FOR TRUE, AND F FOR FALSE!).',font='Times 13 bold')
                    true_false_title.place(x=5,y=30)
                    
                    quest_1_tf=tk.Label(form_quest_2,text='a) A MXN MATRIX IS INVERTIBLE IF AND ONLY IF THE COLUMS OF MATRIX ARE LINEARLY INDEPENDENT')
                    quest_1_tf.place(x=3,y=88)
                    
                    answer_label1=tk.Label(form_quest_2,text='Answer:',font='Times 10 bold')
                    answer_label1.place(x=115,y=110)
                                    
                    quest_1_entry=tk.Entry(form_quest_2)
                    quest_1_entry.place(x=169,y=112,height=17,width=25)
                    
                    quest_2_tf=tk.Label(form_quest_2,text='b) A MATRIX IS INVERTIBLE IF AND ONLY IF IT IS A SQUARE MATRIX')
                    quest_2_tf.place(x=3,y=132)
                    
                    answer_label2=tk.Label(form_quest_2,text='Answer:',font='Times 10 bold')
                    answer_label2.place(x=115,y=152)
                    
                    quest_2_entry=tk.Entry(form_quest_2)
                    quest_2_entry.place(x=169,y=154,height=17,width=25)

                    quest_3_tf=tk.Label(form_quest_2,text='c) ROW OPERATIONS DO NOT CHANGE THE VALUE OF DETERMINANT')
                    quest_3_tf.place(x=3,y=176)
                    
                    answer_label3=tk.Label(form_quest_2,text='Answer:',font='Times 10 bold')
                    answer_label3.place(x=115,y=192)
                    
                    quest_3_entry=tk.Entry(form_quest_2)
                    quest_3_entry.place(x=169,y=194,height=17,width=25)
                    
                    bonus_question=tk.Label(form_quest_2,text='5) BONUS QUESTION(10P)',font='Times 13 bold')
                    bonus_question.place(x=3,y=225)
                    
                    question_of_b=tk.Label(form_quest_2,text="YOU ARE GIVEN A 3X3 MATRIX. FIND THE VALUE OF 'k' IF THE MATRIX IS NOT INVERTIBLE. ")
                    question_of_b.place(x=3,y=253)
                    
                    matrix_of_bonus_1=tk.Label(form_quest_2,text='[',font='Times 75 normal')
                    matrix_of_bonus_1.place(x=39,y=278)
                    

                    #--------------------------------------------BONUS QUESTION--------------------------------------------------------------
                    matrix_of_bonus_2=tk.Label(form_quest_2,text=']',font='Times 75 normal')       
                    matrix_of_bonus_2.place(x=151,y=278)
                    
                    matrix_b=tk.Label(form_quest_2,text='A=',font='Times 20')
                    matrix_b.place(x=3,y=318)
                    
                    matrix_b_first_row=tk.Label(form_quest_2,text='1    5    2',font='Times 15 normal')         
                    matrix_b_first_row.place(x=78,y=303)
                    
                    matrix_b_second_row=tk.Label(form_quest_2,text='4    k    3',font='Times 15 normal')         
                    matrix_b_second_row.place(x=78,y=333)
                    
                    matrix_b_third_row=tk.Label(form_quest_2,text='3    k    0',font='Times 15 normal')         
                    matrix_b_third_row.place(x=78,y=363)
                    
                    k_label=tk.Label(form_quest_2,text='k=',font='Times 30 bold')
                    k_label.place(x=220,y=326)
                    
                    k_entry=tk.Entry(form_quest_2)
                    k_entry.place(x=275,y=343,height=19,width=28)
                    
                    matrix_hint=tk.Label(form_quest_2,text='(HINT: A MXM MATRIX IS NOT INVERTIBLE IF AND ONLY IF ITS DETERMINANT IS 0.)')
                    matrix_hint.place(x=3,y=405)
                    #--------------------------------------------------------------------------------------------------------------------------    

                    
                    
                    
                    
                    def check_l_a():
                        bonus_part=0
                        tf_part=0
                        actual_answers_tf=['T','T','T']
                        users_ans_tf=[]
                        users_ans_tf.extend([quest_1_entry.get(),quest_2_entry.get(),quest_3_entry.get()])
                        actual_answer_bonus=45
                        users_ans_bonus=k_entry.get()
                        for f in range(3):
                            if users_ans_tf[f]=='-':
                                tf_part+=0
                            else:
                                if users_ans_tf[f]==actual_answers_tf[f]:
                                    tf_part+=8
                                else:
                                    continue
                        

                            
                        if users_ans_bonus=='-':
                            bonus_part+=0
                        else:                   
                            if int(actual_answer_bonus)==int(users_ans_bonus):
                                bonus_part+=10
                            else:
                                pass
                        

                        
                        form_quest_2.destroy()
                        form_score=tk.Tk()
                        form_score.title('SCORE PAGE!')
                        form_score.geometry('1920x1080')
                        
                        #-------------------------------TOTAL SCORE--------------------------------------------
                        total_score=score_of_derivative+score_of_limit+det_part+tf_part+inverse_part+bonus_part
                        #--------------------------------------------------------------------------------------
                        
                        form_score_label=tk.Label(form_score,text=f'DEAR {datas[0]} {datas[1]}',fg='black',font='Times 14 bold')
                        form_score_label.place(x=550,y=5)
                        
                        form_scores1=tk.Label(form_score,text=f'YOU GOT {score_of_limit} POINTS FROM LIMIT QUESTIONS',fg='black',font='Times 14 bold')
                        form_scores1.place(x=480,y=55)
                        
                        form_scores2=tk.Label(form_score,text=f'YOU GOT {score_of_derivative} POINTS FROM DERIVATIVE QUESTIONS',fg='black',font='Times 14 bold')
                        form_scores2.place(x=480,y=85)
                        
                        form_scores3=tk.Label(form_score,text=f'YOU GOT {det_part+tf_part+inverse_part} POINTS FROM LINEAR ALGEBRA QUESTIONS',fg='black',font='Times 14 bold')
                        form_scores3.place(x=480,y=115)
                        
                        form_scores4=tk.Label(form_score,text=f'YOU GOT {bonus_part} POINTS FROM BONUS QUESTION',fg='black',font='Times 14 bold')
                        form_scores4.place(x=480,y=145)
                        
                        form_scores_last=tk.Label(form_score,text=f'TOTALLY YOU GOT {total_score} POINTS ',fg='black',font='Times 14 bold')
                        form_scores_last.place(x=550,y=190)
                        
                        
                        
                        result=f'Name:{datas[0]}, Last Name: {datas[1]}, Student ID: {datas[2]}, SCORE: {total_score}'
                        with open('scores_of_students_exam.txt','w') as scores:
                            scores=scores.write(result)
                            
                    
                    
                    
                    
                    
                    finish_exam_button=tk.Button(form_quest_2,text='Finish',fg='black',command=check_l_a)
                    finish_exam_button.place(x=1473,y=750)
                    
                        
                                    
                    
                except:
                    form_quest.destroy()
                    form_empty_quest=tk.Tk()
                    form_empty_quest.title('ERROR!')
                    form_empty_quest.geometry('1920x1080')
                    form_empty_label=tk.Label(form_empty_quest,text='YOUR EXAM WAS CANCELLED BECAUSE YOU DID NOT OBEY THE RULES (YOU DID NOT ANSWER EACH OF THE QUESTIONS)',fg='red',font='Times 17 bold')
                    form_empty_label.place(relx=0.5,rely=0.5,anchor='center')
                    
                #----------------------------------------------------------------------------------------------------------------------------------
                

                
                
            button_send=tk.Button(text='Next Page',fg='black',command=send_answers)
            button_send.place(x=1473,y=750,anchor='center')
            
    #--------------------------------------------------------------------------------------------------------------------------------------------
    
        datas=[]
        datas.extend([name_entry.get(),last_name_entry.get(),student_id_entry.get()])
        if (datas[0].isupper()==False and datas[0].isalpha()==False) or (datas[1].isupper()==False) or (datas[2].isnumeric())==False:
            form.destroy()
            form2=tk.Tk()
            form2.title('ERROR!')
            form2.geometry('1920x1080')
            form2_label=tk.Label(form2,text='YOUR EXAM WAS CANCELLED BECAUSE YOU DID NOT OBEY THE RULES (YOU DID NOT ENTER YOUR INFORMATIONS ACCORDING TO THE RULES).',fg='red',font='Times 16 bold')
            form2_label.place(relx=0.5,rely=0.5,anchor='center')
        else:
            form.destroy()
            
            form_succ_login=tk.Tk()
            form_succ_login.geometry('1920x1080')
            form_succ_login.title('SUCCESSFUL LOGIN!')
            
            
            form_exam_rules=tk.Label(form_succ_login,text='BEFORE STARTING PLEASE READ THE RULES OF THE EXAM!',fg='red',font='Times 18 bold')
            form_exam_rules.place(x=3,y=5)
            
            form_exam_rules1=tk.Label(form_succ_login,text="1) YOU HAVE TO ANSWER EACH OF THE QUESTIONS (IF YOU DO NOT KNOW THE SOLUTION PLEASE WRITE '-' TO THE BLANK) OTHERWISE YOUR EXAM PAGE WILL BE CLOSED!",fg='black',font='Times 13 bold')
            form_exam_rules1.place(x=3,y=40)
            
            form_exam_rules2=tk.Label(form_succ_login,text='2) WHEN YOU SOLVE ALL OF THE QUESTIONS IN PAGE 1,YOU CAN SWITCH TO THE SECOND PAGE',fg='black',font='Times 13 bold')
            form_exam_rules2.place(x=3,y=70)
            
            form_exam_rules3=tk.Label(form_succ_login,text='3) YOU CANNOT TURN BACK TO THE FIRST PAGE AFTER SWITCHING TO THE SECOND PAGE',fg='black',font='Times 13 bold')
            form_exam_rules3.place(x=3,y=100)
            
            form_exam_rules4=tk.Label(form_succ_login,text='4) WHEN YOU FINISH THE EXAM, PLEASE CLICK THE FINISH BUTTON AND WAIT FOR THE SCORE PAGE',fg='black',font='Times 13 bold')
            form_exam_rules4.place(x=3,y=130)
            
            form_exam_info=tk.Label(form_succ_login,text='INFO: YOUR EXAM ARE SCORED AS 111 POINTS (1.QUESTION=20, 2.QUESTION=41, 3.QUESTION=40, BONUS QUESTION=10)',font='Times 13 bold')
            form_exam_info.place(x=3,y=160)        
            
            
            button_to_start=tk.Button(text='CLICK TO START THE EXAM!',fg='black',command=go_to_exam_page_and_questions)
            button_to_start.place(x=750,y=220, anchor='center')
            
            

    button_of_infos=tk.Button(text='SEND INFORMATIONS',fg='black',command=checking_informations)
    button_of_infos.place(x=300,y=55)


    form.mainloop()

if __name__=='__main__':
    main()