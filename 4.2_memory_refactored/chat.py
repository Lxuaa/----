from api import call_zhipu_api
from roles import get_role_prompt
from logic import get_break_message

# 生成ASCII头像
PORTRAIT = """
....'..............'........''''''''''''''''''''''''''''''''''''''''''
'.'................'........''''''''''''''''''''''''''''''''''''''''''
'...................''''....''''.......'''''''''''''''''''''''''''''''
''..''..............'..''''.............'''''''''''''''''''''''''''''''
''...'.........'.....''''................''''''''''''''''''''''''''''''
.''..''..''..'..'.....'....................'',''',''''''''''''''''''''
.''...''.'''..'.............................''',,,,,,''''''''''',,,,,,
'.'...''..''..'..............................',,,,,,,,,,,,,,,,,,,,,,,,
...'..''..'''.................................'',,,,,,,,,,,,,,,,,,,,,,
'..''..'...'....................................'',,,,,,,,,,,,,,,,,,,,
'..'''.''..............................'...........',,,,,,,,,,,,,,,,,,
'...''.''..............................'............',,,,,,,,,,,,,,,,,
''..'''.'.............',..;:;;;;;'..'................''',,,,,,,,,,,,,,
''...''.'..........'..;c;'colccol:,','..... ..........''''',,,,,,;,,,,
''...'...........,;;,,:oo:lxxddxdocc;'.................'''''',,;;;;,,,
'''.............;cc::cldxdlokkkkkxxdoc,..................'''..',;;;;;;
''...........'',clccoddkOkdodkOOOOkkkdl:'...............'''''..',;;;;;
''.........'',,;coodxkkOOOkddxk00OOOOkxd;........... ........''',;;;;;
'..........',;;:coddxxxkOOOkxxk0K0000Okd;............ .........'',;;;;
'.........';:::clloodxxxkkkOkOO0KKKK00Od;..  ..',.... ..........'',;;;
'.........,;:;:codxO00K00OOOO000KKK00Oko;............ ...........'',;;
'.........,:::ldkkO000KK0kkkOO00KK0Okxol;........................'',,;
..........,:ccoxkkxxooddooloxkOO00Okxoc:,'...................'...',;;;
..........,:cldkkkkkkkOOkxxxxkkkOOkxdlc;;,,'.............''..'...',;;;
......,:;',:coxO00000000OOOOOOOOOOkkxolc:::;,'.........',,'''''...'',,
.....'cxd:,;cokO00KKKKKKKK0KK0OOOO0OOkoccllc::,'........';'''.''....',
......cxdl;;cdkO00KKXXXXXKKK0OOO0KKXK0klcoxolc:;,........,'....'.....'
......'cddc:cdkO0KKXXNXXXKKK000KKKKK0Okxodkxdc;,,,'..,,...'''.........
........cxocldxk0KKXXXXKKKKXKKKKKK00OOOkxxkkkd:'',,..',......'........
.........'',oxkOO0KKXKK0KKKKKKKKKK0000Okxddxkd:,'';'.........,,'......
............cxkOO0KKK00000000OOOOkkxkxdollldkd;'.';,.........',,''....
............'lxkO00000OOkddkOOO0KK0O00Oxccdxko,...';............,,'...
...''''......'lxOOO000OOOxddk0KXXXXKKKkocldxdc.....,'............',,..
':oxkkkdc,.''.'cdxkOOO0000Okxxxkkkkkkxoollol;.......'..'''........','.
k0KKKK00Oxcco;.;codxkkOOO000OOkkkxxxdddoooc'...........',;,........,,.
NNXXXXXXX0ddkl,,:looodxkOO000000OOkkkkOkxc..............',,,'......,;,
XXNNXXKKXX0OOkc,:lodddddxk000KKKKKKKK00kl'...........''''''.'........;
XNNNNNXK0XXK00x::codxxxdddxO00KKK0000Okc..............,;,,'.......''..
NNNWWWNNXK0KXXOc:lodxxxkxxxxxxkkkxool;............''...,::,'..........
NNNNNNWWNNK00KKklcodxxxxxxxxddolc;... ............''''..;c;'......... 
WWWNNNXNWWNXK0OKOlldxxxdddddooll:'... .............,,....,,...........
MWWWWNNXXNWWXKOOX0lcdxxddooollc:,.;:'...............,,................
WWWWWWWWNNNNNXKO0X0lcdddoolccc;'.':l:...............,;'...............
WWWWWWWNNNWNNNX0O0X0ccoollc:;,'';,;c:...............':,...............
MMWWWNWWWXXNNNNX0OKXOl:llc:,''',:;,:;................,,...............
MMMMMWNNNNXXNWNX0OOKXOl:c:;'',,;::'..................''...............
MMMMMMWNXXX0KNWXKOO0KXO:,:;',;;:cc,......','.........''...............

"""


def start_chat(role_name="妹妹"):
    # 加载角色prompt和结束规则
    role_prompt = get_role_prompt(role_name)
    break_message = get_break_message()
    system_message = f"{role_prompt}\n\n{break_message}"
    
    # 初始化对话历史
    conversation_history = [{"role": "system", "content": system_message}]
    print("✓ 已加载初始记忆，开始对话（对话记录不会保存）")
    
    try:
        while True:
            user_input = input("\n请输入你要说的话（输入\"再见\"退出）：")
            if user_input in ['再见']:
                print("对话结束")
                break
            
            # 追加用户输入到对话历史
            conversation_history.append({"role": "user", "content": user_input})
            
            # 调用API获取回复
            result = call_zhipu_api(conversation_history)
            assistant_reply = result['choices'][0]['message']['content']
            
            # 追加AI回复到对话历史
            conversation_history.append({"role": "assistant", "content": assistant_reply})
            
            # 显示回复
            print(PORTRAIT + "\n" + assistant_reply)
            
            # 检查AI回复是否结束对话
            reply_cleaned = assistant_reply.strip().replace(" ", "").replace("！", "").replace("!", "").replace("，", "").replace(",", "").replace("。", "").replace("~", "")
            if reply_cleaned == "再见" or (len(reply_cleaned) <= 5 and "再见" in reply_cleaned):
                print("\n对话结束")
                break
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n\n发生错误：{e}")

