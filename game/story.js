// Fresh Chinese adaptation. Branch rules reconstructed from the public 3.1.0 build.
export const NAMES = {sy:'希乐普',gum:'甘姆德洛普',pas:'帕斯提耶',bs:'巴塔斯可琪',tof:'托菲',treat:'德莉特',choco:'查克利双子',n:''};
const L=(who,text,pose)=>({who,text,pose});
const C=(text,to,effect={},when)=>({text,to,effect,when});
const scene=(title,bg,cast,lines,next,extra={})=>({title,bg,cast,lines,next,...extra});
export const ENDINGS={
 candibal:{name:'食人结局',subtitle:'甜味的代价',cg:'candibal',text:'实验笔记记录下了味道，却再也没有人回答希乐普的问题。'},
 bad1:{name:'坏结局 1',subtitle:'空荡荡的糖果店',cg:'badend1',text:'独自完成所有工作并不等于独自过得很好。糖果工坊的灯，最终还是熄灭了。'},
 bad2:{name:'坏结局 2',subtitle:'猫的经营哲学',cg:'badend2',text:'新店员很擅长招揽顾客，也很擅长把招牌换成魔女的名字。希乐普成了自己店里的客人。'},
 frozen:{name:'冻僵结局',subtitle:'没能融化的话语',cg:'frozen',text:'风雪盖住了洞口。比冰更难融化的，是那句始终没有收回的话。'},
 worst:{name:'最坏的结局',subtitle:'第二次转身',cg:'worstend',text:'同伴救回了希乐普，却没能替她修复所有关系。没有人再来敲那扇门。'},
 syrup:{name:'希乐普结局',subtitle:'下一份配方',cg:'syrupend',text:'终极糖果只是新的起点。希乐普翻开空白的一页，写下下一次实验的标题。'},
 gumdrop:{name:'甘姆德洛普结局',subtitle:'世界上的每一种甜',cg:'gumend',text:'一张地图、两只行李箱。她们要亲自去尝遍这个世界，而第一站还没有名字。'},
 pastille:{name:'帕斯提耶结局',subtitle:'并肩的明天',cg:'pasend',text:'有人整理配方，有人记下灵感。实验室之外还有很大的世界，两个人决定一起去看。'},
 butterscotch:{name:'巴塔斯可琪结局',subtitle:'科学与魔法之间',cg:'bsend',text:'魔女带来新的材料，制糖师拿出新的工具。争论依然热闹，但桌子的另一边不再空着。'},
 toffee:{name:'托菲结局',subtitle:'给自由留一扇窗',cg:'tofend',text:'铃铛声每天准时响起。有人来蹭茶，也有人终于学会为意外来客多留一把椅子。'},
};
export const initialVars=()=>Object.fromEntries(['bp','gp','pp'].map(k=>[k,0]).concat(['biopsy','nopets','candyslave','candydate','gotlost','foundcandy','paranoid','salesman','gentlelady','forgiven','forgotit'].map(k=>[k,false])));
const finalRoute=(v,p)=>v.forgotit?'syrupend':v.gp>=4&&!v.candyslave?'gumdropend':v.bp>=4?(v.forgiven||p.endings?.includes('butterscotch')?'toffeeend':'butterscotchend'):v.pp>=3?'pastilleend':'syrupend';
export const scenes={
 start:scene('会说话的糖果','lab',['sy hmm','gum ooh'],[
 L('n','在只相信配方与温度计的糖果工坊里，今天出现了一项无法解释的实验结果。'),
 L('sy','我很确定，昨天这只烧杯里还没有一个人。','sy oh'),
 L('gum','早上好！请问，你就是做出最棒糖果的人吗？'),
 L('pas','她有自己的声音，也会感到害怕。先把取样刀放下，好吗？','pas worry'),
 L('sy','糖会说话……我需要更多证据。')],null,{menu:'m140',options:[C('检查一下她的糖果身体','candybiopsy',{biopsy:true}),C('先听听她想说什么','continued')]}),
 candybiopsy:scene('实验的边界','lab',['sy hmm','gum worry'],[
 L('n','希乐普取下一小块糖片。女孩缩了缩手，仍努力保持笑容。'),L('gum','如果这能帮到你，我可以忍耐。'),L('pas','研究不应该让愿意信任我们的人受伤。'),L('sy','……她不只是一个样品。')],null,{menu:'m195',options:[C('停下来，听帕斯提耶的意见','newassistant',{pp:1}),C('继续，只要知道味道就够了','candibal')]}),
 candibal:scene('甜味的代价','black',[],[L('n','这一次，希乐普得到了她要求的证据。桌边却永远少了一个声音。')],null,{cg:'candibal',ending:'candibal'}),
 continued:scene('意外的访客','lab',['sy um','gum happy'],[L('sy','先说清楚，我没用魔法造你。'),L('gum','那我就帮你找出答案！在那之前，能让我待在这里吗？'),L('pas','正好，店里总有做不完的事情。')],'newassistant'),
 newassistant:scene('新的助手','shop',['sy reg','pas smile','gum pls'],[L('n','女孩把糖罐摆成一条歪歪扭扭的直线。帕斯提耶假装没看见，重新排了一遍。'),L('gum','我会慢慢学。只要你肯告诉我该怎么做。'),L('pas','每个人都有第一天，对吧？')],null,{cg:'newassistant',menu:'m471',options:[C('给她一个留下来的机会','adopted',{gp:1,pp:1}),C('去找魔女问个清楚','nopetsallowed',{nopets:true})]}),
 nopetsallowed:scene('魔女的小屋','cottage',['sy reg','bs smirk','gum worry'],[L('bs','哎呀，稀客。你终于承认自己需要魔法了？'),L('sy','我是来解决问题的。你愿意照顾她吗？'),L('gum','我可以很安静。也可以帮忙……请别急着决定。')],null,{menu:'m560',options:[C('把她留在这里','abandonher'),C('改变主意，带她回去','keepher')]}),
 abandonher:scene('留下的背影','cottage',['bs hey','gum worry'],[L('n','门关上时，铃铛轻轻响了一声。希乐普告诉自己，这只是一次合理的安排。')],'candyslave',{cg:'homealone'}),
 candyslave:scene('不该被替代的意愿','shop',['sy reg','pas worry'],[L('pas','我去看过她了。魔女给她换了衣服，也替她安排了所有事情。'),L('pas','她说，只要你来接，她随时愿意回来。和我一起去吧。')],null,{enter:{candyslave:true},menu:'m630',options:[C('陪他去接回女孩','rescuemission',{pp:1}),C('继续手里的实验','lonelystore')]}),
 rescuemission:scene('重新伸出的手','cottage',['sy um','pas smile','gums happy'],[L('sy','店里的工作还没结束。你愿意回来继续吗？'),L('gum','这一次，是在问我的意思？那我的答案是：愿意！')],'homesweethome',{cg:'happyreturn'}),
 keepher:scene('带你回家','cottage',['sy thanks','gum happy'],[L('sy','我还没有弄明白你。但这不是把你推给别人的理由。'),L('gum','那我们可以边走边想。回家的路很长呢。')],'homesweethome',{cg:'hometogether'}),
 adopted:scene('采购清单','shopext',['sy reg','gum yay'],[L('gum','店门外的世界，比糖罐上的画还大！'),L('sy','我们只是去买原料。别忘了清单。'),L('gum','我会记得的。也会记得今天可以和你一起出门。')],null,{menu:'m771',options:[C('让她享受这趟出门','shoppingduo',{gp:1}),C('让她别再跟着自己','shoppingalone',{gotlost:true})]}),
 shoppingduo:scene('集市上的甜味','market',['sy smirk','gum happy'],[L('n','她们在集市尝到了酸莓、焦糖和温热的牛奶。女孩把每一种味道都认真记住。'),L('gum','最好吃的是哪一种？我觉得，是有人陪着尝的那一种。')],null,{enter:{candydate:true},menu:'m869',options:[C('采购结束，一起回家','homesweethome',{gp:1}),C('趁人群拥挤独自离开','lostcandy',{gotlost:true})]}),
 shoppingalone:scene('独自采购','market',['sy tch','bs smirk'],[L('bs','你身边那个粉红色的小家伙呢？'),L('sy','我不用向你汇报。'),L('n','希乐普加快脚步。等她回头，熟悉的身影已经不在人群中。')],'lostcandy',{enter:{paranoid:true}}),
 lostcandy:scene('空出来的位置','shop',['sy hmm','pas worry'],[L('pas','她没有回来。你真的打算让她一个人留在外面？'),L('sy','我……'),L('pas','至少，再去找一次。不是每个人都知道怎么回家。')],null,{menu:'m998',options:[C('和帕斯提耶一起去找','search',{pp:1}),C('她会有自己的去处','lonelystore')]}),
 lonelystore:scene('一个人的店','shop',['sy indifferent','tof sly'],[L('n','帕斯提耶留下钥匙，去做他认为更重要的事。'),L('tof','听说你缺个店员？我会看店、会招客，还会在柜台上打盹。'),L('sy','最后那一项不算技能。')],null,{menu:'m1098',options:[C('雇用这只猫','parttimecat'),C('自己就能应付','thentherewasone')]}),
 thentherewasone:scene('没有帮手的日子','nightshop',[],[L('n','订单越堆越高。希乐普做出了许多糖果，却再也腾不出时间点亮橱窗。')],null,{cg:'badend1',ending:'bad1'}),
 parttimecat:scene('猫接管了柜台','shop',['tof nyan','bs smirk'],[L('tof','营业额涨了。只是，经营方针稍微变了一点。'),L('bs','现在买糖还附送小魔法！是不是很划算？'),L('sy','等一下，我的招牌呢？')],null,{cg:'cattakeover',ending:'bad2'}),
 search:scene('寻找粉红色的身影','market',['sy um','pas smile','gum happy'],[L('n','他们在最后一盏路灯下找到了女孩。她抱着采购袋，连一颗糖都没有弄丢。'),L('gum','我怕你回来时，找不到我。'),L('sy','下次……直接喊我的名字。')],'homesweethome',{cg:'search',enter:{foundcandy:true}}),
 homesweethome:scene('属于你的名字','shop',['sy aww','gum happy','pas smile'],[L('pas','总不能一直叫她“那个糖果女孩”。'),L('sy','甘姆德洛普。这个名字怎么样？'),L('gum','甘姆德洛普……我喜欢！因为这是你叫我的名字。')],'customers',{cg:'newassistant2'}),
 customers:scene('非卖品','shop',['sy reg','choco hello','gum worry'],[L('choco','多么精巧的作品！橱窗里的糖果能卖，这位呢？'),L('gum','我也……有一个价钱吗？'),L('sy','你们的问题问错对象了。')],null,{menu:'m1318',options:[C('她是店员，也是我们的同伴','afternoon',{gp:1}),C('先听听他们打算出多少','afternoon',{salesman:true})]}),
 afternoon:scene('午后的安排','shop',['sy reg','pas smile','gum happy'],[L('pas','客人走了。今天余下的时间，你准备做什么？')],null,{menu:'m1394',options:[C('陪甘姆德洛普练习工作','withgumdrop',{gp:1}),C('和帕斯提耶研究新配方','withpastille',{pp:1}),C('到外面整理思路','butterscotchvisit')]}),
 withgumdrop:scene('一起练习','shop',['sy thanks','gum yay'],[L('gum','这次我把每个标签都贴对了。你看！'),L('sy','嗯。做得不错。'),L('gum','你笑了。这个也能记在今天的成果里吗？')],'butterscotchvisit',{cg:'working'}),
 withpastille:scene('实验桌的另一边','lab',['sy hmm','pas eheh'],[L('pas','你负责那些大胆的点子，我负责提醒你记得吃饭。'),L('sy','你也可以提点子。'),L('pas','那我希望，下一次实验结束后，我们能去看看远一点的地方。')],'butterscotchvisit',{cg:'working2'}),
 butterscotchvisit:scene('不请自来的魔女','shopext',['sy tch','bs hey','tof nyan'],[L('bs','你的店太安静了。我给你带来了一个值得动心的配方。'),L('sy','如果“值得动心”意味着会爆炸，我不需要。'),L('bs','终极糖果。听完名字再拒绝也不迟。')],'butterscotchvisit2'),
 butterscotchvisit2:scene('一张旧配方','cottageint',['sy hmm','bs takeit'],[L('bs','普通的糖只能留下味道。这份配方，能留住制作它时最重要的东西。'),L('sy','听起来毫无科学依据。'),L('bs','那你就亲自验证。索尔贝山上的冰晶，是最后一味材料。')],'mission'),
 mission:scene('出发前','shop',['sy proud','pas smile','gum pls'],[L('sy','先查资料，再准备装备。不许任何人空着肚子上山。'),L('gum','我会把店看好。也会等你回来。'),L('n','希乐普把那张配方折好，放进口袋。')],'libraryvisit'),
 libraryvisit:scene('巧克力图书馆','library',['sy hmm','choco hello'],[L('choco','传说中的冰晶只生长在最深的洞穴。带走太多，山就会醒来。'),L('sy','我更愿意称它为环境失稳。'),L('choco','怎么称呼都好。请记住：只拿你需要的。')],'missingcandy'),
 missingcandy:scene('不见的糖果','cottage',['sy oh','bs shock'],[L('n','返回时，甘姆德洛普不见了。线索指向雪山，魔女也露出了少有的严肃神情。'),L('bs','我的魔法能帮你找到路。这次别急着赶我走。')],null,{menu:'m2084',options:[C('接受她的帮助','adventure',{bp:1}),C('只把她当作带路的人','adventure')]}),
 adventure:scene('索尔贝山','snow',['sy cold','bs cold','treat reg'],[L('treat','天黑以前找到避风的地方。山里的天气从不等人。'),L('bs','我、我才没有冷得发抖。'),L('sy','你的帽子已经在替你发抖了。')],null,{cg:'climb',menu:'m2262',options:[C('把外套借给魔女','thecave',{bp:1,gentlelady:true}),C('提醒她继续向前走','thecave')]}),
 thecave:scene('冰晶的回声','icecave',['sy coldhmm','bs cold'],[L('n','蓝色冰晶照亮洞穴深处。每一次敲击，都传来细细的回声。'),L('bs','这里的材料够做一整年的糖果。'),L('sy','配方只需要一小块。')],null,{menu:'m2353',options:[C('尽可能多取一些','trapped'),C('取够这次所需就停手','trapped',{bp:1})]}),
 trapped:scene('冰墙之后','icecave2',['sy coldscared','bs coldtears'],[L('n','一声闷响，回去的路被冰墙封住。魔女的咒语散成了微弱的光点。'),L('bs','你是不是一直都讨厌我？我只是想……让你觉得我也有用。'),L('sy','现在不是讨论配方的时候。')],null,{menu:'m2485',options:[C('告诉她：我并不讨厌你','hearttoheart',{bp:2}),C('承认自己不想再见到她','thingsgonesour')]}),
 hearttoheart:scene('融化的第一层冰','icecave2',['sy coldcomfort','bs coldeheh'],[L('sy','你的帮助有用。你本人也有用。这是两件事。'),L('bs','那你能不能……再说一遍？'),L('n','魔法重新在指尖亮起。坚硬的冰墙终于裂开一条缝。')],'backhome',{cg:'escape'}),
 thingsgonesour:scene('雪中的等待','icecave2',['sy coldscared','bs coldtears'],[L('n','没有人再说话。洞口的光一点点暗下去。'),L('sy','如果有人来找我们……')],(v)=>v.pp>=1&&v.gp>=2&&!v.candyslave?'saved':'frozenend'),
 frozenend:scene('未被听见的声音','black',[],[L('n','这一次，没有脚步声从雪地传来。')],null,{cg:'frozen',ending:'frozen'}),
 saved:scene('熟悉的呼喊','snow',['sy coldhey','pas coldworry','gum happy'],[L('pas','我们找到你了！甘姆德洛普一直坚持往这边走。'),L('gum','你叫我回家时，我记住了。所以这次轮到我来接你。'),L('bs','如果还能重来，我会做得好一些。')],null,{cg:'escape2',menu:'m2608',options:[C('给魔女一次重新开始的机会','backhome',{forgiven:true,bp:1}),C('依然拒绝与她和解','worstend')]}),
 worstend:scene('没有回应的门','nightcottage',[],[L('n','希乐普的确离开了冰洞。但还有一些东西，永远留在了那里。')],null,{cg:'worstend',ending:'worst'}),
 backhome:scene('温暖的屋檐','cabin',['sy coldyeah','bs coldeheh','treat reg'],[L('treat','先把手暖过来，再谈别的。'),L('n','热茶升起白雾。希乐普第一次觉得，配方之外的事情也值得认真记下。')],'missioncomplete',{cg:'byetreat'}),
 missioncomplete:scene('终于回到工坊','shop',['sy thanks','gum happy','pas smile'],[L('gum','欢迎回来！我把每一个糖罐都擦干净了。'),L('pas','炉子也准备好了。现在，轮到你完成最后一步。')],'makethething',{cg:'happyreturn'}),
 makethething:scene('水晶球里的答案','lab',['sy crystalball','gum worry'],[L('n','材料旁边放着一颗水晶球。里面闪过女孩诞生之前的影像。'),L('sy','答案可能就在这里。也可能，我们已经有了继续生活所需的一切。')],null,{menu:'m2860',options:[C('看一看她诞生时的记忆','creation'),C('把水晶球放回抽屉','ultimatesweet',{forgotit:true})]}),
 creation:scene('一个愿望的形状','lab',[],[L('n','水晶里，没说出口的愿望与尚未完成的糖浆相遇。一次孤独的实验，变成了想要陪伴他人的生命。'),L('sy','所以，这就是你来到这里的原因。'),L('gum','原因是起点。现在想留下来，是我自己的愿望。')],(v)=>v.gp>=4&&!v.candyslave?'lonelygumdrop':'afterwards',{cg:'creamilla'}),
 lonelygumdrop:scene('灯熄灭以后','nightshop',['sy aww','gum worry'],[L('gum','如果我不再是一颗特别的糖，你还愿意叫我的名字吗？'),L('sy','你的名字不是实验编号。它不会因为实验结束就失效。'),L('n','女孩靠在窗边，终于放心地闭上了眼睛。')],'ultimatesweet',{cg:'sleep'}),
 afterwards:scene('夜晚的敲门声','nightshop',['sy um','tof hello'],[L('n','配方的最后一行还空着。窗外传来铃铛的轻响。')],(v)=>v.bp>=4?'toffeetalk':'ultimatesweet'),
 toffeetalk:scene('魔女没说的话','nightcottage',['sy hmm','tof sly'],[L('tof','她不擅长直接说“陪陪我”。所以总把事情弄得很复杂。'),L('sy','你倒是看得清楚。'),L('tof','猫很擅长找温暖的地方。也擅长发现谁在逞强。')],'ultimatesweet'),
 ultimatesweet:scene('终极糖果','lab',[],[L('n','冰晶溶进糖浆，锅中盛开细小的彩色光点。没有仪器能替希乐普描述此刻的味道。'),L('sy','我想，我终于知道最后一味材料是什么了。')],finalRoute,{cg:'ultimatesweet'}),
 syrupend:scene('下一次实验','shop',['sy proud'],[L('sy','配方已经验证成功。接下来，试试完全不同的方向吧。'),L('n','清晨的门铃响起，工坊又开始了忙碌的一天。')],null,{cg:'syrupend',ending:'syrup'}),
 gumdropend:scene('一起去远方','market',['sy thanks','gum yay'],[L('gum','地图上还有这么多我们没去过的地方。'),L('sy','那就从离家最近的那一站开始。带上笔记本。'),L('gum','还有两个人的糖果！')],null,{cg:'gumend',ending:'gumdrop'}),
 pastilleend:scene('并肩而行','mountain',['sy smirk','pas smile'],[L('pas','以前，我总是在你身后整理桌子。'),L('sy','以后走在旁边吧。看见什么有趣的，记得告诉我。'),L('n','两本旅行笔记，从同一页开始。')],null,{cg:'pasend',ending:'pastille'}),
 butterscotchend:scene('新的合作伙伴','cottageint',['sy thanks','bs hey'],[L('bs','这次换你来我的实验室。不是请求，是正式邀请。'),L('sy','如果你肯把材料贴上标签，我会考虑。'),L('bs','那你可要常来检查。')],null,{cg:'bsend',ending:'butterscotch'}),
 toffeeend:scene('窗边的新客人','nightshop',['sy reg','tof nyan'],[L('tof','你店里的窗台很舒服。我能不能常来？也许还顺便帮点忙。'),L('sy','“顺便”听起来很值得怀疑。')],null,{menu:'m3540',options:[C('给托菲留一把椅子','toffeeidentity'),C('让魔女来谈正式合作','butterscotchend')]}),
 toffeeidentity:scene('如何称呼你','shop',['sy hmm','tof sly'],[L('tof','在成为常客之前，你还有什么想问的吗？'),L('sy','我该怎样介绍你？'),L('tof','你可以先猜猜看。')],null,{menu:'m3632',options:[C('一位男孩？','toffeeend2'),C('一位女孩？','toffeeend2'),C('都不是，只是托菲','toffeeend2',{},(_,p)=>p.endings?.includes('toffee'))]}),
 toffeeend2:scene('留下来就好','shop',['sy thanks','tof myow'],[L('tof','答案可以慢慢了解。现在，先喝茶吧。'),L('sy','这次你负责洗杯子。'),L('n','铃铛响了一声，像是答应了。')],null,{cg:'tofend',ending:'toffee'}),
};
export function getOptions(state,persistent={endings:[]}) {return (scenes[state.label].options||[]).filter(o=>!o.when||o.when(state.vars,persistent));}
export function createState(){return {schemaVersion:1,label:'start',line:0,vars:initialVars(),history:[],undo:[],seen:[],ending:null};}
function checkpoint(s){return {label:s.label,line:s.line,vars:{...s.vars},historyLength:s.history.length,ending:s.ending};}
function apply(s,e={}){for(const[k,v]of Object.entries(e))s.vars[k]=typeof v==='number'?s.vars[k]+v:v;}
function enter(s,label){if(!scenes[label])throw Error('Unknown scene: '+label);s.label=label;s.line=0;s.ending=null;apply(s,scenes[label].enter);}
export function current(s){const sc=scenes[s.label];return {scene:sc,line:sc.lines[s.line],menu:!s.ending&&s.line>=sc.lines.length&&!!sc.options,ending:s.ending};}
export function advance(s,p={endings:[]},choice){if(s.ending)return false;const sc=scenes[s.label];if(s.line>=sc.lines.length&&sc.options&&choice===undefined)return false;
 s.undo.push(checkpoint(s));if(s.undo.length>100)s.undo.shift();
 if(s.line<sc.lines.length){const l=sc.lines[s.line];s.history.push({who:l.who,text:l.text,title:sc.title});s.line++;return true;}
 if(sc.ending){s.ending=sc.ending;return true;}
 if(sc.options){const o=getOptions(s,p)[choice];if(!o){s.undo.pop();throw Error('Invalid choice');}apply(s,o.effect);enter(s,o.to);return true;}
 const to=typeof sc.next==='function'?sc.next(s.vars,p):sc.next;if(to)enter(s,to);return true;
}
export function back(s){const old=s.undo.pop();if(!old)return false;Object.assign(s,{label:old.label,line:old.line,vars:old.vars,ending:old.ending});s.history.length=old.historyLength;return true;}
export function snapshot(s){return JSON.parse(JSON.stringify(s));}
export function restore(value){if(value?.schemaVersion!==1||!scenes[value.label]||!Number.isInteger(value.line)||value.line<0||value.line>scenes[value.label].lines.length)throw Error('存档格式不兼容');const s=createState();s.label=value.label;s.line=value.line;s.vars={...initialVars(),...value.vars};for(const k of ['bp','gp','pp'])if(!Number.isFinite(s.vars[k]))throw Error('存档分数无效');s.history=Array.isArray(value.history)?value.history.slice(-400):[];s.undo=Array.isArray(value.undo)?value.undo.slice(-100):[];s.seen=Array.isArray(value.seen)?value.seen:[];s.ending=ENDINGS[value.ending]?value.ending:null;return s;}
