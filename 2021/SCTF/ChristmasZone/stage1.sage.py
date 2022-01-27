
# This file was *autogenerated* from the file stage1.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_101769519193859897825320245156959434921913983350473060882286349485865984317847870491404933879093953844043746336727206024576370530292354093815863023816706246500298401622086226447269280268616579093359838092177566300422450268807805764053269666406661746447216430803672425368187850241035951924968282837212195122009661837881639260394408377769780736894355913339761124951087878683112341579831203537690452068872325361085194676246398043353830320116631731052775233562373473466987587868005268581813479779347680063366303017713536066445950119653273801655986218864523290954405450118867912084493204633639794887212799992251732430784674488402713909794174876005671995596180233507663769534324478247169857849296242438419851584731760109867502433723889003163357912826164605761440076107391415859710270107208238788343003197401241164218906390765598034607381603748260135711929915310061018442294577268048174890825217788770406998063119050836051489078273 = Integer(101769519193859897825320245156959434921913983350473060882286349485865984317847870491404933879093953844043746336727206024576370530292354093815863023816706246500298401622086226447269280268616579093359838092177566300422450268807805764053269666406661746447216430803672425368187850241035951924968282837212195122009661837881639260394408377769780736894355913339761124951087878683112341579831203537690452068872325361085194676246398043353830320116631731052775233562373473466987587868005268581813479779347680063366303017713536066445950119653273801655986218864523290954405450118867912084493204633639794887212799992251732430784674488402713909794174876005671995596180233507663769534324478247169857849296242438419851584731760109867502433723889003163357912826164605761440076107391415859710270107208238788343003197401241164218906390765598034607381603748260135711929915310061018442294577268048174890825217788770406998063119050836051489078273); _sage_const_19398712966389173067515660342342371376171822855077792430320907920482468319034356508473830699130119726502328267606091971072624658237697431558761718296916369668202230512807622341524837789641448767802361925545348467904711602267688826344269930586157457184165009996779745720616560780946563277776544719243932403743 = Integer(19398712966389173067515660342342371376171822855077792430320907920482468319034356508473830699130119726502328267606091971072624658237697431558761718296916369668202230512807622341524837789641448767802361925545348467904711602267688826344269930586157457184165009996779745720616560780946563277776544719243932403743); _sage_const_267000359463890957717294351755470395775719644789429663372393934597886269585220011545044241458534045359371297184551277070963234405275020426197366492869314542709770069940218775927729656563824049000861637672019261914763255535102368549189717138802777857362338800063261799093471863140383233839337323951256030092519904238160488078801775094231309854037045776322975374136086721587475321461865395766598044725287653610465988931031232528714170443934495346597507225059138123723217195600699010690404724751765768947671633341548919663197287149388174745361423892142684664502757004981595130275477628185542483487720787553731056377755612968232532486236222531976930567469450118630574878461610221412520855639284541260477254335811263503618354963929644259420215673854617684859387440666537678991106163811693608705830080085992199446733965897982586004566211695950749580230294269802861047464077650537072587582866785357191599817136214300826353340261120 = Integer(267000359463890957717294351755470395775719644789429663372393934597886269585220011545044241458534045359371297184551277070963234405275020426197366492869314542709770069940218775927729656563824049000861637672019261914763255535102368549189717138802777857362338800063261799093471863140383233839337323951256030092519904238160488078801775094231309854037045776322975374136086721587475321461865395766598044725287653610465988931031232528714170443934495346597507225059138123723217195600699010690404724751765768947671633341548919663197287149388174745361423892142684664502757004981595130275477628185542483487720787553731056377755612968232532486236222531976930567469450118630574878461610221412520855639284541260477254335811263503618354963929644259420215673854617684859387440666537678991106163811693608705830080085992199446733965897982586004566211695950749580230294269802861047464077650537072587582866785357191599817136214300826353340261120); _sage_const_13560918884675796397422230974896753903564514060544004622609605573166124357809803049342207856908237157989458174631058128913271365699175849042916944962684319362603309646697695167167430136068004838289739138033112696576679443996914506782400912475705559889360576361738784125657707992917972167925405463413645788482 = Integer(13560918884675796397422230974896753903564514060544004622609605573166124357809803049342207856908237157989458174631058128913271365699175849042916944962684319362603309646697695167167430136068004838289739138033112696576679443996914506782400912475705559889360576361738784125657707992917972167925405463413645788482); _sage_const_64392795853847475796939596948374573513341136006013188358665448316305707477998438325517993586430100318003625505157712138814030987620038360820900112359350226402638642419396935215229157012026467896203963294845355310085476165076942465877433408205263068546705226319393063008332679430070032638523530045872344446063 = Integer(64392795853847475796939596948374573513341136006013188358665448316305707477998438325517993586430100318003625505157712138814030987620038360820900112359350226402638642419396935215229157012026467896203963294845355310085476165076942465877433408205263068546705226319393063008332679430070032638523530045872344446063)#! /usr/bin/sage
from sage.all import *
from Crypto.Util.number import *
from util import Complex
import random

def PowPlus(msg,k):
    c=Complex(msg[_sage_const_0 ],msg[_sage_const_1 ])
    while k>_sage_const_0 :
        if k%_sage_const_2 :
            k-=_sage_const_1 
            c.OnePlus()
        else:
            k//=_sage_const_2 
            c.Double()
    return c.val()

n =  _sage_const_64392795853847475796939596948374573513341136006013188358665448316305707477998438325517993586430100318003625505157712138814030987620038360820900112359350226402638642419396935215229157012026467896203963294845355310085476165076942465877433408205263068546705226319393063008332679430070032638523530045872344446063 
enc = (_sage_const_19398712966389173067515660342342371376171822855077792430320907920482468319034356508473830699130119726502328267606091971072624658237697431558761718296916369668202230512807622341524837789641448767802361925545348467904711602267688826344269930586157457184165009996779745720616560780946563277776544719243932403743 , _sage_const_13560918884675796397422230974896753903564514060544004622609605573166124357809803049342207856908237157989458174631058128913271365699175849042916944962684319362603309646697695167167430136068004838289739138033112696576679443996914506782400912475705559889360576361738784125657707992917972167925405463413645788482 )
phi = _sage_const_267000359463890957717294351755470395775719644789429663372393934597886269585220011545044241458534045359371297184551277070963234405275020426197366492869314542709770069940218775927729656563824049000861637672019261914763255535102368549189717138802777857362338800063261799093471863140383233839337323951256030092519904238160488078801775094231309854037045776322975374136086721587475321461865395766598044725287653610465988931031232528714170443934495346597507225059138123723217195600699010690404724751765768947671633341548919663197287149388174745361423892142684664502757004981595130275477628185542483487720787553731056377755612968232532486236222531976930567469450118630574878461610221412520855639284541260477254335811263503618354963929644259420215673854617684859387440666537678991106163811693608705830080085992199446733965897982586004566211695950749580230294269802861047464077650537072587582866785357191599817136214300826353340261120 

d = _sage_const_101769519193859897825320245156959434921913983350473060882286349485865984317847870491404933879093953844043746336727206024576370530292354093815863023816706246500298401622086226447269280268616579093359838092177566300422450268807805764053269666406661746447216430803672425368187850241035951924968282837212195122009661837881639260394408377769780736894355913339761124951087878683112341579831203537690452068872325361085194676246398043353830320116631731052775233562373473466987587868005268581813479779347680063366303017713536066445950119653273801655986218864523290954405450118867912084493204633639794887212799992251732430784674488402713909794174876005671995596180233507663769534324478247169857849296242438419851584731760109867502433723889003163357912826164605761440076107391415859710270107208238788343003197401241164218906390765598034607381603748260135711929915310061018442294577268048174890825217788770406998063119050836051489078273 

msg = PowPlus(enc, d)
flag = bytes_to_long(long_to_bytes(msg[_sage_const_0 ]) + long_to_bytes(msg[_sage_const_1 ]))
print(flag)

