import imaplib
import email
from email.header import decode_header
import re
import csv

imap = imaplib.IMAP4_SSL("kusccoagm.co.ke")

usernames = [
    "AO11208281@kusccoagm.co.ke",
    "AO11200210@kusccoagm.co.ke",
    "AK11216074@kusccoagm.co.ke",
    "AM11211778@kusccoagm.co.ke",
    "AM11200006@kusccoagm.co.ke",
    "AM11215207@kusccoagm.co.ke",
    "AO11208380@kusccoagm.co.ke",
    "AM17215767@kusccoagm.co.ke",
    "AB18215520@kusccoagm.co.ke",
    "AM11200153@kusccoagm.co.ke",
    "AG11211940@kusccoagm.co.ke",
    "AK11200232@kusccoagm.co.ke",
    "AM11200380@kusccoagm.co.ke",
    "AM11206314@kusccoagm.co.ke",
    "AN11215376@kusccoagm.co.ke",
    "AS11207238@kusccoagm.co.ke",
    "AM11215442@kusccoagm.co.ke",
    "AH11215869@kusccoagm.co.ke",
    "AM11207169@kusccoagm.co.ke",
    "AN11216436@kusccoagm.co.ke",
    "AR11206076@kusccoagm.co.ke",
    "AW11216123@kusccoagm.co.ke",
    "AY11215215@kusccoagm.co.ke",
    "BM11211874@kusccoagm.co.ke",
    "BI11200268@kusccoagm.co.ke",
    "BJ11215821@kusccoagm.co.ke",
    "BK11207257@kusccoagm.co.ke",
    "BM11204578@kusccoagm.co.ke",
    "BM11216475@kusccoagm.co.ke",
    "BO11200009@kusccoagm.co.ke",
    "BO11206415@kusccoagm.co.ke",
    "BA11215811@kusccoagm.co.ke",
    "BC11207648@kusccoagm.co.ke",
    "BN11204569@kusccoagm.co.ke",
    "BK11200185@kusccoagm.co.ke",
    "BK11215865@kusccoagm.co.ke",
    "BM11208105@kusccoagm.co.ke",
    "BO11205791@kusccoagm.co.ke",
    "BM11200005@kusccoagm.co.ke",
    "BK10215963@kusccoagm.co.ke",
    "BK11216119@kusccoagm.co.ke",
    "BY11216070@kusccoagm.co.ke",
    "CM11215472@kusccoagm.co.ke",
    "CN11201208@kusccoagm.co.ke",
    "CL11206502@kusccoagm.co.ke",
    "CL16213264@kusccoagm.co.ke",
    "CS11207409@kusccoagm.co.ke",
    "CW11215974@kusccoagm.co.ke",
    "CN11215646@kusccoagm.co.ke",
    "CN11207587@kusccoagm.co.ke",
    "CM11200169@kusccoagm.co.ke",
    "CO11200170@kusccoagm.co.ke",
    "CK11211492@kusccoagm.co.ke",
    "CN11207174@kusccoagm.co.ke",
    "CA11100883@kusccoagm.co.ke",
    "CN10216054@kusccoagm.co.ke",
    "CN11216254@kusccoagm.co.ke",
    "CM11200470@kusccoagm.co.ke",
    "CO11201738@kusccoagm.co.ke",
    "CA11205573@kusccoagm.co.ke",
    "CK11216350@kusccoagm.co.ke",
    "CM11204599@kusccoagm.co.ke",
    "DO11212096@kusccoagm.co.ke",
    "DO11215736@kusccoagm.co.ke",
    "DO11208180@kusccoagm.co.ke",
    "DW11202943@kusccoagm.co.ke",
    "DM11200002@kusccoagm.co.ke",
    "DM11203124@kusccoagm.co.ke",
    "DM11211130@kusccoagm.co.ke",
    "DM18215507@kusccoagm.co.ke",
    "DO11204747@kusccoagm.co.ke",
    "DM11200404@kusccoagm.co.ke",
    "DG10212639@kusccoagm.co.ke",
    "DO11216259@kusccoagm.co.ke",
    "DB18205296@kusccoagm.co.ke",
    "DL11215206@kusccoagm.co.ke",
    "DM11205304@kusccoagm.co.ke",
    "DO11208528@kusccoagm.co.ke",
    "DS11212658@kusccoagm.co.ke",
    "DK1028498@kusccoagm.co.ke",
    "DL11216431@kusccoagm.co.ke",
    "EO11202909@kusccoagm.co.ke",
    "EO11215631@kusccoagm.co.ke",
    "EO11214937@kusccoagm.co.ke",
    "EO11216250@kusccoagm.co.ke",
    "EO11203137@kusccoagm.co.ke",
    "EM18215793@kusccoagm.co.ke",
    "EC11204522@kusccoagm.co.ke",
    "EK11207798@kusccoagm.co.ke",
    "EM11207826@kusccoagm.co.ke",
    "EA11215952@kusccoagm.co.ke",
    "EM18216479@kusccoagm.co.ke",
    "EB11205787@kusccoagm.co.ke",
    "EM11200471@kusccoagm.co.ke",
    "EO11212889@kusccoagm.co.ke",
    "EM11215598@kusccoagm.co.ke",
    "ES18216471@kusccoagm.co.ke",
    "EK11206862@kusccoagm.co.ke",
    "EN11200635@kusccoagm.co.ke",
    "EN11207543@kusccoagm.co.ke",
    "EV11200084@kusccoagm.co.ke",
    "EO11215917@kusccoagm.co.ke",
    "EM11205355@kusccoagm.co.ke",
    "FN11205251@kusccoagm.co.ke",
    "FM11216134@kusccoagm.co.ke",
    "FK18215508@kusccoagm.co.ke",
    "FW11315213@kusccoagm.co.ke",
    "FM16204214@kusccoagm.co.ke",
    "FO11216496@kusccoagm.co.ke",
    "FO11216392@kusccoagm.co.ke",
    "FN11204581@kusccoagm.co.ke",
    "FN11214439@kusccoagm.co.ke",
    "GW11202125@kusccoagm.co.ke",
    "GN11216344@kusccoagm.co.ke",
    "GO11200034@kusccoagm.co.ke",
    "GA11206715@kusccoagm.co.ke",
    "GM11208117@kusccoagm.co.ke",
    "GM11213307@kusccoagm.co.ke",
    "GO11200001@kusccoagm.co.ke",
    "GO11200091@kusccoagm.co.ke",
    "GO10215951@kusccoagm.co.ke",
    "GB16216525@kusccoagm.co.ke",
    "GM11213722@kusccoagm.co.ke",
    "GO11208432@kusccoagm.co.ke",
    "HN11200138@kusccoagm.co.ke",
    "HO11204440@kusccoagm.co.ke",
    "HO11206312@kusccoagm.co.ke",
    "HO11205268@kusccoagm.co.ke",
    "HM11205236@kusccoagm.co.ke",
    "IM11205273@kusccoagm.co.ke",
    "IG11211266@kusccoagm.co.ke",
    "IM16215706@kusccoagm.co.ke",
    "JK11206532@kusccoagm.co.ke",
    "JM11207701@kusccoagm.co.ke",
    "JO11200209@kusccoagm.co.ke",
    "JO11214448@kusccoagm.co.ke",
    "JK10215852@kusccoagm.co.ke",
    "JN11212095@kusccoagm.co.ke",
    "JI11216296@kusccoagm.co.ke",
    "JM11213435@kusccoagm.co.ke",
    "JN11210142@kusccoagm.co.ke",
    "JN11215549@kusccoagm.co.ke",
    "JO11200092@kusccoagm.co.ke",
    "JO11216322@kusccoagm.co.ke",
    "JR11207313@kusccoagm.co.ke",
    "JK11216249@kusccoagm.co.ke",
    "JA17215751@kusccoagm.co.ke",
    "JW11215843@kusccoagm.co.ke",
    "JS11200210@kusccoagm.co.ke",
    "JO11215813@kusccoagm.co.ke",
    "JA11213163@kusccoagm.co.ke",
    "JG11201825@kusccoagm.co.ke",
    "JG11214082@kusccoagm.co.ke",
    "JI11209463@kusccoagm.co.ke",
    "JO11216263@kusccoagm.co.ke",
    "JW11203905@kusccoagm.co.ke",
    "JW12216391@kusccoagm.co.ke",
    "JK11211132@kusccoagm.co.ke",
    "JM11200048@kusccoagm.co.ke",
    "JN11207775@kusccoagm.co.ke",
    "JO10214526@kusccoagm.co.ke",
    "JO11315213@kusccoagm.co.ke",
    "JN11213706@kusccoagm.co.ke",
    "JO11204591@kusccoagm.co.ke",
    "JM11215660@kusccoagm.co.ke",
    "JW11205311@kusccoagm.co.ke",
    "JK11213637@kusccoagm.co.ke",
    "JO11216449@kusccoagm.co.ke",
    "JM11202689@kusccoagm.co.ke",
    "JK11209053@kusccoagm.co.ke",
    "JO11200007@kusccoagm.co.ke",
    "JO11216445@kusccoagm.co.ke",
    "JT11200905@kusccoagm.co.ke",
    "KN11207893@kusccoagm.co.ke",
    "KO16216536@kusccoagm.co.ke",
    "KW11207970@kusccoagm.co.ke",
    "KA11215724@kusccoagm.co.ke",
    "KM112002761@kusccoagm.co.ke",
    "LN11215916@kusccoagm.co.ke",
    "LA11214580@kusccoagm.co.ke",
    "LM11200012@kusccoagm.co.ke",
    "LM11207432@kusccoagm.co.ke",
    "LK11201032@kusccoagm.co.ke",
    "LM11215842@kusccoagm.co.ke",
    "LL11211644@kusccoagm.co.ke",
    "LO11206233@kusccoagm.co.ke",
    "LW11202358@kusccoagm.co.ke",
    "LK11208189@kusccoagm.co.ke",
    "LN11216246@kusccoagm.co.ke",
    "LN11200270@kusccoagm.co.ke",
    "LK11216132@kusccoagm.co.ke",
    "LN11200050@kusccoagm.co.ke",
    "LA11207405@kusccoagm.co.ke",
    "LK11213448@kusccoagm.co.ke",
    "LO11202073@kusccoagm.co.ke",
    "MK11203882@kusccoagm.co.ke",
    "MM16216498@kusccoagm.co.ke",
    "MM11204449@kusccoagm.co.ke",
    "MN11215600@kusccoagm.co.ke",
    "MO11200003@kusccoagm.co.ke",
    "MA11208194@kusccoagm.co.ke",
    "MK11200367@kusccoagm.co.ke",
    "MK18216481@kusccoagm.co.ke",
    "MM11204524@kusccoagm.co.ke",
    "MM11215881@kusccoagm.co.ke",
    "MN11216425@kusccoagm.co.ke",
    "MO11216328@kusccoagm.co.ke",
    "MW11205312@kusccoagm.co.ke",
    "MM11200016@kusccoagm.co.ke",
    "MB11215830@kusccoagm.co.ke",
    "MG11200736@kusccoagm.co.ke",
    "MM11201607@kusccoagm.co.ke",
    "MG11200242@kusccoagm.co.ke",
    "MI10215833@kusccoagm.co.ke",
    "MN10211823@kusccoagm.co.ke",
    "MN11215884@kusccoagm.co.ke",
    "MO16216500@kusccoagm.co.ke",
    "MW11215077@kusccoagm.co.ke",
    "MG11215444@kusccoagm.co.ke",
    "MM11215582@kusccoagm.co.ke",
    "MK18207412@kusccoagm.co.ke",
    "MM11205617@kusccoagm.co.ke",
    "MO11200880@kusccoagm.co.ke",
    "MO11208138@kusccoagm.co.ke",
    "MJ11216400@kusccoagm.co.ke",
    "MK11214859@kusccoagm.co.ke",
    "MO11208397@kusccoagm.co.ke",
    "MW11200035@kusccoagm.co.ke",
    "NH12213123@kusccoagm.co.ke",
    "NR11207593@kusccoagm.co.ke",
    "NM11200109@kusccoagm.co.ke",
    "NW11216128@kusccoagm.co.ke",
    "NK16216439@kusccoagm.co.ke",
    "NK11207232@kusccoagm.co.ke",
    "NK11200729@kusccoagm.co.ke",
    "NK11215406@kusccoagm.co.ke",
    "NM11207300@kusccoagm.co.ke",
    "NN11202573@kusccoagm.co.ke",
    "NN11205749@kusccoagm.co.ke",
    "NN17215723@kusccoagm.co.ke",
    "NN11207804@kusccoagm.co.ke",
    "OD11215804@kusccoagm.co.ke",
    "ON11216426@kusccoagm.co.ke",
    "PK11209017@kusccoagm.co.ke",
    "PO11213464@kusccoagm.co.ke",
    "PB11211496@kusccoagm.co.ke",
    "PI11200041@kusccoagm.co.ke",
    "PM11216347@kusccoagm.co.ke",
    "PN11213364@kusccoagm.co.ke",
    "PO11207226@kusccoagm.co.ke",
    "PA11203764@kusccoagm.co.ke",
    "PJ11208529@kusccoagm.co.ke",
    "PM11216405@kusccoagm.co.ke",
    "PN11200008@kusccoagm.co.ke",
    "PN11213758@kusccoagm.co.ke",
    "P11190134@kusccoagm.co.ke",
    "P11204510@kusccoagm.co.ke",
    "PK11200208@kusccoagm.co.ke",
    "PK11207574@kusccoagm.co.ke",
    "PM11200409@kusccoagm.co.ke",
    "RR11212520@kusccoagm.co.ke",
    "RO17215728@kusccoagm.co.ke",
    "RN11207546@kusccoagm.co.ke",
    "RN11200412@kusccoagm.co.ke",
    "RK11214917@kusccoagm.co.ke",
    "RO11215518@kusccoagm.co.ke",
    "RN11212217@kusccoagm.co.ke",
    "RN11215894@kusccoagm.co.ke",
    "RO1128877@kusccoagm.co.ke",
    "RO11216346@kusccoagm.co.ke",
    "RM11205315@kusccoagm.co.ke",
    "RM18211242@kusccoagm.co.ke",
    "RP11027011@kusccoagm.co.ke",
    "RO11210183@kusccoagm.co.ke",
    "RS10215836@kusccoagm.co.ke",
    "SM11202226@kusccoagm.co.ke",
    "SA11211665@kusccoagm.co.ke",
    "SA16216045@kusccoagm.co.ke",
    "SG11212822@kusccoagm.co.ke",
    "SK11201165@kusccoagm.co.ke",
    "SK11215774@kusccoagm.co.ke",
    "SN11215657@kusccoagm.co.ke",
    "SM11214635@kusccoagm.co.ke",
    "SK11210402@kusccoagm.co.ke",
    "SO11216058@kusccoagm.co.ke",
    "SM11203818@kusccoagm.co.ke",
    "SJ11215985@kusccoagm.co.ke",
    "SM11200114@kusccoagm.co.ke",
    "SO11213994@kusccoagm.co.ke",
    "SK11204511@kusccoagm.co.ke",
    "SI11216251@kusccoagm.co.ke",
    "SO11200044@kusccoagm.co.ke",
    "SN11205414@kusccoagm.co.ke",
    "S11200164@kusccoagm.co.ke",
    "SM18200347@kusccoagm.co.ke",
    "SK11215910@kusccoagm.co.ke",
    "SM11215744@kusccoagm.co.ke",
    "TM11200059@kusccoagm.co.ke",
    "TN11215201@kusccoagm.co.ke",
    "TE11200045@kusccoagm.co.ke",
    "TM11210691@kusccoagm.co.ke",
    "TM11216382@kusccoagm.co.ke",
    "TM11209330@kusccoagm.co.ke",
    "TG11208334@kusccoagm.co.ke",
    "TV11205063@kusccoagm.co.ke",
    "TN11208265@kusccoagm.co.ke",
    "VO11310354@kusccoagm.co.ke",
    "VO11215986@kusccoagm.co.ke",
    "VM11211355@kusccoagm.co.ke",
    "VK11200220@kusccoagm.co.ke",
    "VM11206313@kusccoagm.co.ke",
    "VO11216464@kusccoagm.co.ke",
    "WM11215486@kusccoagm.co.ke",
    "WM11215550@kusccoagm.co.ke",
    "WA11108107@kusccoagm.co.ke",
    "WA11200004@kusccoagm.co.ke",
    "W10190156@kusccoagm.co.ke",
    "YI11215672@kusccoagm.co.ke",
    "ZN18216131@kusccoagm.co.ke",
    "ZC11200211@kusccoagm.co.ke",
    "Z18190142@kusccoagm.co.ke",
]
N = 1

for name in usernames:
    imap = imaplib.IMAP4_SSL("kusccoagm.co.ke")

    password = "hiltonagm2021??"
    imap.login(name, password)
    status, emails = imap.select(mailbox="INBOX.spam")
    emails = int(emails[0])
    if emails == 0:
        print('{} has no password'.format(name))
        with open('passwordsUpdated.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ', quotechar='"')
            writer.writerow(name)
        continue

    for i in range(emails, emails - N, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)

                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode()

                if content_type == "text/html":
                    expression = re.compile(r'Password:\s{1}\w+',
                                            re.IGNORECASE)
                    results = expression.search(body)
                    if results:
                        password = results.group()
                        # password = password[10:]
                        with open('passwordsUpdated.csv', 'a') as csv_file:
                            writer = csv.writer(csv_file,
                                                delimiter=' ',
                                                quotechar='"')
                            writer.writerow(password[10:])
                            imap.logout()

    print("_" * 50)

imap.close()
