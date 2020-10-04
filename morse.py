import decrypt
import encrypt
import tkinter
import tkinter.font 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
class Encrypter:
    def __init__(self,d):
        d.title('Convert English to Morse code')
        d.configure(background="black")
        d.geometry('800x640')

        self.label1=tkinter.Label(d, text="Decode english to Morse code!", font=("Monotype Corsiva",30,'bold','underline'),fg='#ffffff',background='black')
        self.label2=tkinter.Label(d, text="Enter the english text which you want to encrypt in morse code:", font=("Monotype Corsiva",20,'bold'),fg='#ffffff',background='black')
        self.label3=tkinter.Label(d, text="Result:", font=("Monotype Corsiva",20,'bold'),fg='#ffffff',background='black')
        self.eng_text=tkinter.Text(d,highlightthickness=2,bg="black",fg="white",font=(30))
        self.eng_text.config(highlightbackground='Seagreen2',highlightcolor= "red",insertbackground="white")
        self.sumbit_button= tkinter.Button(d,text='Convert',background="Seagreen2",fg='#ffffff',command=lambda: EncryptIt(self,self.eng_text.get("1.0", "end"),self.morse_text))
        self.sound_button=tkinter.Button(d,text='Convert to sound',background="Seagreen2",fg='#ffffff',command=lambda: EmitSound(self,self.morse_text))
        self.bFont = tkinter.font.Font(weight="bold")
        self.morse_text=tkinter.Text(d,highlightthickness=2,bg="black",fg="white",font=(30))
        self.morse_text.config(highlightbackground='Seagreen2',highlightcolor= "red",insertbackground="white",state='disabled')

        
        self.label1.place(relx=0.03, rely=0.0)
        self.label2.place(relx=0.03, rely=0.15)
        self.eng_text.place(relx=0.03, rely=0.2,width=700,height=200)
        self.sumbit_button.place(relx=0.03, rely=0.52)
        self.label3.place(relx=0.03,rely=0.56)
        self.morse_text.place(relx=0.03, rely=0.61,width=700,height=200)
        self.sound_button.place(relx=0.03, rely=0.93)

        def EncryptIt(self,code,morse_text):
            morse_text.config(state="normal")
            morse_text.delete('1.0', 'end')
            code= code[:-1]
            print(code)
            result_List=encrypt.encrypt(code,MORSE_CODE_DICT)
            print(result_List)
            stri=""
            print(stri)
            for i in result_List:
                stri = stri+i+'/'+" "
            stri=stri[:-1]
            stri=stri[:-1]
            morse_text.insert('end',stri)
            morse_text.config(state="disabled")
        def EmitSound(self, morse_text):
            m_code=morse_text.get('1.0','end')
            m_code=m_code[:-1]
            if m_code=='':
                Error=tkinter.Tk()
                Error.title('Error')
                l1= tkinter.Label(Error,text='No Text found to convert')
                ok_button= tkinter.Button(Error,text='ok', command=Error.destroy)
                l1.pack(side='top')
                ok_button.pack(side='top')
            else:
                e_list=m_code.split("/ ")
            encrypt.MakeSound(e_list)
class Decrypter:
    def __init__(self,d):
        d.title('Convert Morse Code to English')
        d.configure(background="black")
        d.geometry('800x640')

        self.label1=tkinter.Label(d, text="Decode Morse code to english!", font=("Monotype Corsiva",30,'bold','underline'),fg='#ffffff',background='black')
        self.label2=tkinter.Label(d, text="Enter the encrypted code which you want to convert:", font=("Monotype Corsiva",20,'bold'),fg='#ffffff',background='black')
        self.label3=tkinter.Label(d, text="Result:", font=("Monotype Corsiva",20,'bold'),fg='#ffffff',background='black')
        self.morse_text=tkinter.Text(d,highlightthickness=2,bg="black",fg="white",font=(30))
        self.morse_text.config(highlightbackground='Seagreen2',highlightcolor= "red",insertbackground="white")
        self.sumbit_button= tkinter.Button(d,text='Convert',background="Seagreen2",fg='#ffffff',command=lambda: DecryptIt(self,self.morse_text.get("1.0", "end"),self.eng_text))
        self.bFont = tkinter.font.Font(weight="bold")
        self.eng_text=tkinter.Text(d,highlightthickness=2,bg="black",fg="white",font=(30))
        self.eng_text.config(highlightbackground='Seagreen2',highlightcolor= "red",insertbackground="white",state='disabled')

        
        self.label1.place(relx=0.03, rely=0.0)
        self.label2.place(relx=0.03, rely=0.15)
        self.morse_text.place(relx=0.03, rely=0.2,width=700,height=200)
        self.sumbit_button.place(relx=0.03, rely=0.52)
        self.label3.place(relx=0.03,rely=0.56)
        self.eng_text.place(relx=0.03, rely=0.61,width=700,height=200)

        def DecryptIt(self,code,eng_text):
            eng_text.config(state="normal")
            eng_text.delete('1.0', 'end')
            code= code[:-1]
            result_List=decrypt.decrypt(code,MORSE_CODE_DICT)
            stri=""
            for i in result_List:
                stri = stri+i
            eng_text.insert('end',stri)
            eng_text.config(state="disabled")


class  starting_window:
    def __init__(self,master):
        master.title('Text to Morse Code converter and vice-versa')
        master.configure(background="black")
        master.geometry('600x440')
        
        self.b1 = tkinter.Button(master,text="Convert English to Morse Code",background="Seagreen2",fg='#ffffff',command=self.EncryptIt)
        self.b2 = tkinter.Button(master,text="Convert Morse Code to English",background='Seagreen2',fg='#ffffff',command=self.DecryptIt)
        self.label1=tkinter.Label(master, text="Welcome to Morse Converter!!", font=("Monotype Corsiva",30,'bold','underline'),fg='#ffffff',background='black')
        self.bFont = tkinter.font.Font(weight="bold")
        self.b1['font']=self.bFont
        self.b2['font']=self.bFont
        
        self.b1.place(relx=0.5, rely=0.45, anchor='center')
        self.b2.place(relx=0.5, rely=0.55, anchor='center')
        self.label1.place(relx=0.5, rely=0.1,anchor='center')
    def DecryptIt(self):
        decrypy= tkinter.Tk()
        Decrypter(decrypy)
    def EncryptIt(self):
        encrypy= tkinter.Tk()
        Encrypter(encrypy)


if __name__ == "__main__":
    root= tkinter.Tk()
    
    sw=starting_window(root)
    root.mainloop()

    '''#m_to_t_window=tkinter.Tk()
    #t_to_m_window=tkinter.Tk()
    starting_window=tkinter.Tk()
    starting_window.title('Text to Morse Code converter and vice-versa')
    starting_window.geometry('800x640')
    starting_window.configure(background="black")
    b1 = tkinter.Button(starting_window,text="Convert English to Morse Code",background="Seagreen2",fg='#ffffff')
    b2=tkinter.Button(starting_window, text="Convert Morse Code to English",background='Seagreen2',fg='#ffffff')
    b1.config( height = 2)
    b2.config(height=2)
    bFont = tkinter.font.Font(weight="bold")
    b1['font']= bFont
    b2['font']=bFont
    label1=tkinter.Label(starting_window, text="Welcome to Morse Converter!!", font=("Monotype Corsiva",30,'bold','underline'),fg='#ffffff',background='black')
    label1.place(relx=0.0, rely=0.0)
    b1.place(relx=0.5, rely=0.4, anchor='center')
    b2.place(relx=0.5, rely=0.6, anchor='center')
    starting_window.mainloop()'''