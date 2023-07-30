##################### Hook Master | PNE Team #####################
version="1.0.0"
if("imports"=="imports"):
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from customtkinter import *
    from tkinter import messagebox
    import webbrowser
    import winshell
    import win32com
    import shutil
    from tkinter.ttk import *

if("create page"):
    window = CTk()

    window.title("Hook Master")

    window.minsize(800,400)
    window.resizable(0,0)

if("saves"=="saves"):
    Allfields=[]
    allfiledscount=0
    newtext=""

if("functions"=="functions"):

    def webhook_send(webhooklink,webhookiconlink,webhookusername,webhooktitle,webhookdescription,webhookcolor,authorname,authorurl,authoricon,footer):
        webhook = DiscordWebhook(url=webhooklink, username=webhookusername,avatar_url=webhookiconlink)
        embed = DiscordEmbed(
            title=webhooktitle, description=webhookdescription, color=webhookcolor
        )
        embed.set_author(
            name=authorname,
            url=authorurl,
            icon_url=authoricon,
        )
        embed.set_footer(text=footer)
        embed.set_timestamp()
        # Set `inline=False` for the embed field to occupy the whole line
        for itemm in Allfields:
            embed.add_embed_field(name=itemm[0], value=itemm[1], inline=False)

        webhook.add_embed(embed)



        response = webhook.execute()

    def change_appearance_mode_event(new_appearance_mode: str):
            set_appearance_mode(new_appearance_mode)

    def authorsave():
        global webhook_author_name_entry_get,webhook_author_icon_entry_get,webhook_author_link_entry_get

        webhook_author_name_entry_get=webhook_author_name_entry.get()
        webhook_author_icon_entry_get=webhook_author_icon_entry.get()
        webhook_author_link_entry_get=webhook_author_link_entry.get()


        setauthortab.destroy()
        webhook_setauthor_but.configure(text="Set Author (Saved)")

    def setauthorr():
        global webhook_author_name_entry,webhook_author_icon_entry,webhook_author_link_entry,webhook_author_save_entry,setauthortab
        setauthortab=CTkToplevel()
        setauthortab.title("Hook Master | Set Author")
        setauthortab.minsize(600,400)


        usernamefrm=CTkLabel(setauthortab,text="").pack()
        CTkLabel(setauthortab,text="Name",).pack()
        webhook_author_name_entry=CTkEntry(setauthortab,width=200)
        webhook_author_name_entry.pack()
        
        
        CTkLabel(setauthortab,text="Icon URL",).pack()
        webhook_author_icon_entry=CTkEntry(setauthortab,width=200)
        webhook_author_icon_entry.pack()

        usernamefrm=CTkLabel(setauthortab,text="").pack()
        CTkLabel(setauthortab,text="URL",).pack()
        webhook_author_link_entry=CTkEntry(setauthortab,width=200)
        webhook_author_link_entry.pack()

        usernamefrm=CTkLabel(setauthortab,text="").pack()
        webhook_author_save_entry=CTkButton(setauthortab,text="Save",width=200,command=authorsave)
        webhook_author_save_entry.pack()

        setauthortab.grab_set()

    def sendweb():
        try:
            webhook_link_entry_get=webhook_link_entry.get()
            webhook_username_entry_get=webhook_username_entry.get()
            webhook_title_entry_get=webhook_title_entry.get()
            webhook_des_entry_get=webhook_des_entry.get()
            webhook_color_entry_get=webhook_color_entry.get()
            webhook_icon_link_entry_get=webhook_icon_link_entry.get()
            webhook_footer_entry_get=webhook_footer_entry.get()
            webhook_send(webhook_link_entry_get,webhook_icon_link_entry_get,webhook_username_entry_get,webhook_title_entry_get,webhook_des_entry_get,webhook_color_entry_get,webhook_author_name_entry_get,webhook_author_link_entry_get,webhook_author_icon_entry_get,webhook_footer_entry_get)
        except:
            messagebox.showerror("خطا","لطفا مشخصات وبهوک را وارد کنید")

    def setfooterrsave():
        webhook_setfield_but.configure(text="Set Footer (Saved)")
        setfieldstab.destroy()
        
    def setfieldd():
        global Allfields,newtext,allfiledscount,setfieldstab
        setfieldstab=CTkToplevel()
        setfieldstab.title("Hook Master | Set Footer")
        setfieldstab.minsize(600,400)
        
        


        def add_new_field():
            global newtext,allfiledscount
            
            if((field_title_entry.get().isspace() is False and field_title_entry.get() != "") and (field_des_entry.get().isspace() is False and field_des_entry.get() != "")):
                
                if(allfiledscount<6):
                    field_title_entry_get=field_title_entry.get()
                    field_des_entry_get=field_des_entry.get()
                    Allfields.append([field_title_entry_get,field_des_entry_get])
                    allfiledscount=allfiledscount+1
                    newtext+=f"{allfiledscount}_ Title: {field_title_entry_get} | Description: {field_des_entry_get}\n"
                    allfieldstitle.configure(text=newtext)

        

        allfieldstitle=CTkLabel(setfieldstab,text=newtext)
        allfieldstitle.pack()

        usernamefrm=CTkLabel(setfieldstab,text="").pack()
        CTkLabel(setfieldstab,text="Field Title",).pack()
        field_title_entry=CTkEntry(setfieldstab,width=200)
        field_title_entry.pack()
        
        
        CTkLabel(setfieldstab,text="Field Description",).pack()
        field_des_entry=CTkEntry(setfieldstab,width=200)
        field_des_entry.pack()

        usernamefrm=CTkLabel(setfieldstab,text="").pack()
        webhook_author_save_entry=CTkButton(setfieldstab,text="Add",width=200,command=add_new_field)
        webhook_author_save_entry.pack()

        usernamefrm=CTkLabel(setfieldstab,text="").pack()
        webhook_author_save_entry=CTkButton(setfieldstab,text="Save",width=200,command=setfooterrsave )
        webhook_author_save_entry.pack()

        setfieldstab.grab_set()

    def seting():
        settop = CTkToplevel()
        settop.geometry("500x300")
        settop.title("Settings")
        CTkLabel(settop, text="Theme").place(y=30, x=350)
        appearance_mode_optionemenu = CTkOptionMenu(settop, values=["Dark", "Light"],
                                                    command=change_appearance_mode_event).place(y=60, x=300)

        import sys
        import os

        executable_path = sys.executable

        startup_folder = os.path.join(
            os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        script_path = executable_path
        startup_script_path = os.path.join(startup_folder, "hook-master.py")

        def create_shortcut():
            desktop = winshell.desktop()
            path = os.path.join(desktop, 'hook-master.lnk')
            target = executable_path
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.save()

        def toggle_startup():

            if os.path.exists(startup_script_path):
                os.remove(startup_script_path)
                ontog.configure(text='OFF')
            else:
                shutil.copy2(script_path, startup_folder)
                ontog.configure(text='ON')

        onti = CTkLabel(settop, text='Start Up')
        onti.place(y=30, x=110)
        ontog = CTkButton(settop, text='OFF', command=toggle_startup)
        ontog.place(y=60, x=60)
        ontog.configure(text='OFF' if not os.path.exists(
            startup_script_path) else 'ON')

        createsht = CTkLabel(settop, text='Create Shortcut')
        createsht.place(y=130, x=85)
        createsh = CTkButton(settop, text='Create', command=create_shortcut)
        createsh.place(y=160, x=60)

        def webgo(): return webbrowser.open('https://pne-team.ir/hook-master/')
        gowebsite = CTkButton(settop, text="Website",
                            command=webgo).place(y=160, x=300)


        settop.grab_set()
 

    def about_us():
        settop = CTkToplevel()
        settop.geometry("500x300")
        settop.title("About us")
        CTkLabel(settop, text="About us").pack()

        CTkLabel(settop, text="We are programmers who try to develop applications for your easier use ").pack(pady=20)


        def webgo(): 
            return webbrowser.open('https://pne-team.ir/')
        
        def gitgo(): 
            return webbrowser.open('https://github.com/nima-globals')
        
        gowebsite = CTkButton(settop, text="Github",
                           command=gitgo)
        
        gowebsite.pack(pady=5)
        


       
        
        gowebsite = CTkButton(settop, text="Website",
                           command=webgo)
        
        gowebsite.pack(pady=10)

        CTkLabel(settop, text=f"© 2023 PNE Team | {version}\nPowered By Wild-Life-Studio",height=40).pack(pady=40)

        settop.grab_set()
 
if("body"=="body"):
    # اضافه کردن نوار بالا
    header_frame = CTkFrame(window)
    header_frame.pack(fill=X, pady=5)

    header_label = CTkLabel(header_frame, text="Hook Master", font=("Helvetica", 20))
    header_label.pack(side=TOP)

    settings_button = CTkButton(header_frame, text="Settings", command=seting)
    settings_button.pack(side=RIGHT)

    about_button = CTkButton(header_frame, text="About us", command=about_us)
    about_button.pack(side=LEFT)


    CTkLabel(window,text="Webhook Link",).pack()
    webhook_link_entry=CTkEntry(window,width=400)
    webhook_link_entry.pack()
    
    CTkLabel(window,text="Webhook Icon Link",).pack()
    webhook_icon_link_entry=CTkEntry(window,width=400)
    webhook_icon_link_entry.pack()
    

    CTkLabel(window,text="Username",).pack()
    webhook_username_entry=CTkEntry(window,width=200)
    webhook_username_entry.pack()
    

    CTkLabel(window,text="Title",).pack()
    webhook_title_entry=CTkEntry(window,width=200)
    webhook_title_entry.pack()
    

    CTkLabel(window,text="Description",).pack()
    webhook_des_entry=CTkEntry(window,width=200)
    webhook_des_entry.pack()


    CTkLabel(window,text="Color Code",).pack()
    webhook_color_entry=CTkEntry(window,width=200)
    webhook_color_entry.pack()


    CTkLabel(window,text="Footer",).pack()
    webhook_footer_entry=CTkEntry(window,width=200)
    webhook_footer_entry.pack()
    
    CTkLabel(window,text="").pack()

    webhook_setauthor_but=CTkButton(window,text="Set author",width=200,command=setauthorr)
    webhook_setauthor_but.pack()

    CTkLabel(window,text="").pack()

    webhook_setfield_but=CTkButton(window,text="Set Fields",width=200,command=setfieldd)
    webhook_setfield_but.pack()

    CTkLabel(window,text="").pack()

    webhook_send_but=CTkButton(window,text="Send",width=200,command=sendweb)
    webhook_send_but.pack()


    footer_frame = CTkFrame(window,)
    footer_frame.pack(fill=X, pady=5, side=BOTTOM)

    footer_label = CTkLabel(footer_frame, text=f"© 2023 PNE Team | {version}", font=("Helvetica", 12))
    footer_label.pack(side=BOTTOM)

window.mainloop()

##################### The END #####################