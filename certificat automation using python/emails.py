import os
import json
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the path to the client secret file and scopes
SECRET_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Email content
SUBJECT = 'Votre Certificat de Participation à la Formation "{formation}"'
HTML_CONTENT = '''
<table class="pc-project-body" style="table-layout: fixed;min-width: 600px;background-color:#28282a;" bgcolor="#28282a" width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
    <tr>
        <td align="center" valign="top">
            <table class="pc-project-container" style="width: 600px; max-width: 600px;" width="600" align="center"border="0" cellpadding="0" cellspacing="0" role="presentation">
                <tr>
                    <td class="pc-w620-padding-0-0-0-0" style="padding: 20px 20px 20px 20px;" align="left" valign="top">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="width: 100%;">
                            <tr>
                                <td valign="top">
                                            <!-- BEGIN MODULE: Message -->
                                     <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                                        <tr>
                                            <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px;">
                                                <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                                                    <tr>
                                                        <td valign="top" class="pc-w620-padding-40-30-40-30" style="border-radius: 0px;background-color: transparent;" bgcolor="transparent">
                                                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                <tr>
                                                                    <td style="padding: 0px 3px 13px 0px;">
                                                                        <table class="pc-width-fill pc-w620-gridCollapsed-0" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                            <tr class="pc-grid-tr-first pc-grid-tr-last">
                                                                                <td class="pc-grid-td-first pc-w620-padding-30-0" align="center" valign="middle" style="width: 20%; padding-top: 0px; padding-right: 9.5px; padding-bottom: 0px; padding-left: 0px;">
                                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                        <tr>
                                                                                            <td align="center" valign="middle">
                                                                                                <table align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                                    <tr>
                                                                                                        <td align="center" valign="top">
                                                                                                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                                                                <tr>
                                                                                                                    <td align="center" valign="top">
                                                                                                                        <img src="https://i.ibb.co/0rb67jT/18-Artboard-1.png" class="" width="auto" height="auto" alt=""  style="display: block;border: 0;outline: 0;line-height: 100%;-ms-interpolation-mode: bicubic;width:128px;height: auto;max-width: 100%;" />
                                                                                                                    </td>
                                                                                                                </tr>
                                                                                                            </table>
                                                                                                        </td>
                                                                                                    </tr>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </table>
                                                                                </td>
                                                                                    <td class="pc-grid-td-last pc-w620-padding-30-0" align="center" valign="middle" style="width: 20%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 9.5px;">
                                                                                        <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                            <tr>
                                                                                                <td align="center" valign="middle">
                                                                                                    <table align="center" width="100%"  border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                                        <tr>
                                                                                                            <td align="center" valign="top">
                                                                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                                                                        <tr>
                                                                                                                            <td align="center" valign="top">
                                                                                                                                <img src="https://cloudfilesdm.com/postcards/image-1711979100880.png"class="" width="auto" height="80" alt="" style="display: block;border: 0;outline: 0;line-height: 100%;-ms-interpolation-mode: bicubic;width:387px;height: auto;max-width: 100%;" />
                                                                                                                            </td>
                                                                                                                        </tr>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </table>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0"cellspacing="0" role="presentation" style="width: 100%;">
                                                                        <tr>
                                                                            <td valign="top"style="padding: 0px 0px 3px 0px;">
                                                                                <table width="100%" border="0"cellpadding="0" cellspacing="0"role="presentation" style="margin: auto;">
                                                                                    <tr>
                                                                                        <td height="1" valign="top"style="line-height: 1px; font-size: 1px; border-bottom: 1px solid #7cff0066;">&nbsp;</td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                        <tr>
                                                                            <td valign="top" style="padding: 0px 0px 40px 0px;">
                                                                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin: auto;">
                                                                                    <tr>
                                                                                        <td height="1" valign="top"style="line-height: 1px; font-size: 1px; border-bottom: 1px solid #7cff0066;">&nbsp;</td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                        <tr>
                                                                            <td align="left" valign="top" style="padding: 0px 0px 40px 0px;">
                                                                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" align="left">
                                                                                    <tr>
                                                                                        <td valign="top" class="pc-font-alt pc-w620-fontSize-32px" align="left" style="padding: 0px 0px 0px 0px;mso-line-height: exactly;line-height: 120%;font-family: Space Grotesk, Arial, Helvetica, sans-serif;font-size: 23px;font-weight: bold;color: #ffffff;text-align: left;text-align-last: left;font-variant-ligatures: normal;">
                                                                                            <div>
                                                                                                <span class="custom-text" style="font-size: 30px;">Reconnaissance pour votre Présentation lors de la série </span> <span class="custom-text" style="color: rgb(255, 255, 0);"  >"l3ilm"</span>
                                                                                            </div>
                                                                                            </div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0"cellspacing="0" role="presentation">
                                                                        <tr>
                                                                            <td align="left" valign="top" style="padding: 0px 0px 20px 0px;">
                                                                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" align="left">
                                                                                    <tr>
                                                                                        <td valign="top" class="pc-font-alt" align="left" style="padding: 0px 0px 0px 0px;mso-line-height: exactly;line-height: 150%;letter-spacing: 0px;font-family: Space Grotesk, Arial, Helvetica, sans-serif;font-size: 18px;font-weight: normal;color: #ffffff;text-align: left;text-align-last: left;font-variant-ligatures: normal;">
                                                                                            <div><span>Chere</span><span style="color: #7cff00;"> {name},</span>
                                                                                            </div>
                                                                                            <div>
                                                                                                <span>&nbsp;</span>
                                                                                            </div>
                                                                                            <div>
                                                                                                <span>Le Computer Science Club et le marketing leaders club est heureux de vous décerner les certificats de participation pour a la formations suivantes de la série L3ilm :</span>
                                                                                                <br />
                                                                                                <br />
                                                                                                <span style="font-size: 20px;" class="custom-text">"{formation}"</span>
                                                                                            </div>
                                                                                            <div>
                                                                                                <span>
                                                                                                    <br />
                                                                                                    Votre participation active et votre engagement ont grandement contribué au succès de chacune de ces formations. 
                                                                                                    Nous vous félicitons pour votre dévouement et vos efforts constants tout au long du programme.
                                                                                                </span>
                                                                                            </div>
                                                                                            <div>   
                                                                                            </div>
                                                                                            <div>
                                                                                                <span>
                                                                                                    <br />
                                                                                                    Au cours de ces formations, vous avez acquis des compétences précieuses en :
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Planification Stratégique
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Analyse de Marché
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Développement de Stratégies Marketing
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Exécution de Campagnes Marketing
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Utilisation des Outils Marketing
                                                                                                    <br />&nbsp;&nbsp;&nbsp;&nbsp;- Gestion du Budget Marketing
                                                                                            </div>
                                                                                            <div>
                                                                                                <br>
                                                                                                <span>Nous sommes convaincus que ces compétences vous seront utiles dans vos études et votre future carrière.</span>
                                                                                            </div>
                                                                                            <div>
                                                                                                <br>
                                                                                                <span>
                                                                                                    Pour faciliter l'accès à votre certificat de participation à l'avenir, nous vous prions de bien vouloir noter et conserver précieusement le code suivant : 
                                                                                                    </span> 
                                                                                                    <span style="color: #7cff00;">{code}
                                                                                                    </span> 
                                                                                            </div>
                                                                                            <div>
                                                                                                <br>
                                                                                                <span>
                                                                                                    Le Computer Science Club et le marketing leaders vous remercie de votre participation et vous encourage à poursuivre votre passion pour l'apprentissage et le développement professionnel.
                                                                                                </span>
                                                                                            </div>
                                                                                            <div>
                                                                                                <span>
                                                                                                    <br />Cordialement,
                                                                                                    <br />Othmane Ferrah
                                                                                                    <br />Responsable Communication au sein du CSC
                                                                                                </span>
                                                                                                <span style="color: #7cff00;"><br />Computer Science Club </span><span>& </span><span style="color: rgb(154, 45, 255);">Marketing Leaders Club</span>
                                                                                                    <br />
                                                                                                    <br />
                                                                                                    <a style="display: inline-block; border-radius: 16px; background-color: #5cb300; 
                                                                                                    padding: 14px 18px 14px 18px; padding-left: 0; padding-right: 0; box-shadow: 0px 0px 10px 0px rgba(124,255,0,0.4); width: 100%; 
                                                                                                    font-family: Space Grotesk, Arial, Helvetica, sans-serif; font-weight: 500; font-size: 20px; line-height: 150%; letter-spacing: -0.2px; color: #ffffff; vertical-align: top; text-align: center; text-align-last: center; text-decoration: none; -webkit-text-size-adjust: none;" 
                                                                                                    href="{file_link}" target="_blank" >Certificat
                                                                                                    </a>
                                                                                                    <br />
                                                                                            </div>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0"cellspacing="0" role="presentation">
                                                                        <tr>
                                                                            <td>
                                                                                <table class="pc-width-fill pc-w620-gridCollapsed-0" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                                    <tr class="pc-grid-tr-first pc-grid-tr-last">
                                                                                        <td class="pc-grid-td-first pc-grid-td-last" align="left" valign="top"style="padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;">
                                                                                            <table width="100%" border="0"cellpadding="0" cellspacing="0" role="presentation"style="width: 100%;">
                                                                                                <tr>
                                                                                                    <td align="left" valign="top" style="padding: 0px 0px 10px 0px;">
                                                                                                        <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation"style="width: 100%;">
                                                                                                            <tr>
                                                                                                                <td align="left" valign="top"></td>
                                                                                                            </tr>
                                                                                                        </table>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                        <tr>
                                                                            <td valign="top" style="padding: 10px 0px 10px 0px;">
                                                                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin: auto;">
                                                                                    <tr>
                                                                                        <td height="1" valign="top" style="line-height: 1px; font-size: 1px; border-bottom: 1px solid #7cff00;">&nbsp;</td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                        <tr>
                                                                            <td style="padding: 0px 0px 0px 3px;">
                                                                                <table class="pc-width-fill pc-w620-gridCollapsed-0" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                                    <tr class="pc-grid-tr-first pc-grid-tr-last">
                                                                                        <td class="pc-grid-td-first pc-grid-td-last pc-w620-padding-30-0" align="center" valign="middle" style="width: 50%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;">
                                                                                            <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                                <tr>
                                                                                                    <td class="pc-w620-halign-center pc-w620-valign-top" align="center" valign="middle">
                                                                                                        <table class="pc-w620-halign-center" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 100%;">
                                                                                                            <tr>
                                                                                                                <td class="pc-w620-halign-center" align="center"valign="top">
                                                                                                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                                                                                                        <tr>
                                                                                                                            <td class="pc-w620-halign-center" align="center" valign="top">
                                                                                                                                <img src="https://cdn.xayman.net/csc/Form-rcrut.png" class="pc-w620-align-center" width="1460" height="207" alt="" style="display: block;border: 0;outline: 0;line-height: 100%;-ms-interpolation-mode: bicubic;width:1460px;height: auto;max-width: 100%;" />
                                                                                                                            </td>
                                                                                                                        </tr>
                                                                                                                    </table>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </table>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </table>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
'''
def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_emails():
    global recipients
    if not recipients:
        messagebox.showerror("Erreur", "Veuillez importer le fichier JSON d'abord.")
        return
    
    try:
        service = get_gmail_service()
    except Exception as e:
        messagebox.showerror("Erreur d'authentification", f"Échec de l'authentification : {e}")
        return

    progress_bar["maximum"] = len(recipients)
    progress_bar["value"] = 0
    
    for i, recipient in enumerate(recipients):
        try:
            name = recipient['name']
            email = recipient['email']
            file_link = recipient['file_link']
            code = recipient['code']
            formation = recipient['formation']

            msg = MIMEMultipart('alternative')
            msg['From'] = f"{SENDER_NAME} <{SMTP_USERNAME}>"
            msg['To'] = email
            msg['Subject'] = SUBJECT.format(formation=formation)

            personalized_html_content = HTML_CONTENT.format(name=name, file_link=file_link, code=code, formation=formation)
            msg.attach(MIMEText(personalized_html_content, 'html'))


            raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

            message = {
                'raw': raw
            }

            service.users().messages().send(userId="me", body=message).execute()

            progress_bar["value"] += 1
            progress_label.config(text=f"Envoyé {i + 1}/{len(recipients)} e-mails")
            root.update_idletasks()
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de l'envoi de l'e-mail à {email} : {e}")
    
    messagebox.showinfo("Succès", "Tous les e-mails ont été envoyés avec succès !")

def load_json_file():
    global recipients
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            recipients = json.load(file)
        messagebox.showinfo("Succès", f"{len(recipients)} destinataires chargés à partir du fichier JSON.")

# GUI Setup
root = tk.Tk()
root.title("Envoyeur d'E-mails")

recipients = []

SMTP_USERNAME = "0x0red.me@gmail.com"  
SENDER_NAME = "othmane ferrah"  

load_json_button = tk.Button(root, text="Importer le fichier JSON", command=load_json_file)
load_json_button.grid(row=0, column=0, padx=10, pady=10)

send_emails_button = tk.Button(root, text="Commencer à envoyer les e-mails", command=send_emails)
send_emails_button.grid(row=0, column=1, padx=10, pady=10)

progress_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

progress_label = tk.Label(root, text="Progression : 0%")
progress_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()