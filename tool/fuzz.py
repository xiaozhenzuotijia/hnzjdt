from fuzzywuzzy import fuzz
# list = ["下列不属于我国宗教特征的是（  ）。*****['单一性']","迷信本质上是一种世界观，宗教则是少数迷信职业者骗取钱财坑害百姓的手段*****['错误']","中华民族和各民族的关系是（  ）。*****['大家庭和家庭成员的关系']","宗教信仰自由是宪法赋予公民的权利，就是说共产党员*****['错误']","下列说法正确的是（  ）。*****['中国共产党曾经多次作出明确规定：共产党员不得信仰宗教，不得参加宗教活动，长期坚持不改的要劝其退党']","积极引导宗教与社会主义社会相适应，是要引导信教群众（  ）。*****['维护祖国统一', '拥护中国共产党领导', '积极践行社会主义核心价值观', '投身改革开放和社会主义现代化建设']","下列不属于新时代党的治疆方略内容的是（）*****['坚持生态保护第一。']","《中国共产主义青年团章程》规定：“中国共产主义青年团坚决拥护中国共产党的纲领，以马克思列宁主义、（ ）、（ ）、（ ）、科学发展观、（ ）。”*****['毛泽东思想', '邓小平理论', '“三个代表”重要思想', '习近平新时代中国特色社会主义思想']","(  )是社会主义民族关系的基石。*****['平等']","境外利用宗教对我国进行渗透，是宗教问题，不是政治问题*****['错误']","在新修订《宗教事务条例》中，哪两项对从事互联网宗教信息服务作出了规定？*****['第四十七、四十八条']","西藏工作对党和国家工作大局的影响不大*****['错误']","关于“大藏区”的说法，错误的是（  ）。*****['“大藏区”是十四世达赖提出的']","依《宗教事务条例》第四十四条规定，禁止在宗教院校以外的学校及其他教育机构进行（  ）。*****['传教', '设立宗教活动场所', '成立宗教组织', '举行宗教活动']","下列属于新时代党的治藏方略“十个必须”的基本内容的是（  ）。*****['必须统筹国内国际两个大局', '必须促进各民族交往交流交融,', '必须坚持我国宗教中国化方向、依法管理宗教事务', '必须坚持生态保护第一']","习近平总书记在参加十三届全国人大一次会议内蒙古代表团审议时指出，我国是统一的多民族国家，民族团结是各族人民的生命线。加强民族团结，根本在于（ ）。*****['坚持和完善民族区域自治制度']","新修订《宗教事务条例》规定，宗教教职人员经宗教团体认定，报（  ）人民政府宗教事务部门备案，可以从事宗教教务活动。*****['县级以上']","宗教和迷信都是对支配人们日常生活的人间力量采取的超人间形式的反映，密切联系，但并不相同。*****['正确']","我国的宗教政策是（  ）。*****['宗教信仰自由']","我国宪法第（  ）条明确规定：“宗教团体和宗教事务不受国外势力的支配”。*****['三十六']","各民族要始终把（ ）的利益放在首位。*****['中华民族']","中华民族共同体意识是（ ）*****['国家统一之基', '民族团结之本', '精神力量之魂']","我国的民族区域自治是指在国家的统一领导下，各少数民族聚居地方实行区域自治，设立自治机关，行使自治权。*****['正确']","用法律来保障民族团结，要做到（  ）。*****['增强各族群众法律意识', '严格区分两类不同性质的矛盾', '坚决依法打击蓄意挑拨民族关系、破坏民族团结的犯罪分子', '坚决依法打击搞民族分裂和暴恐活动的犯罪分子']","公民有宗教信仰自由，就是说：每个公民（  ）。*****['有信仰宗教的自由，也有不信仰宗教的自由', '有信仰这种宗教的自由，也有信仰那种宗教的自由', '有过去不信教而现在信教的自由', '有过去信教而现在不信教的自由']","马克思主义认为，宗教对于现实世界的反映是（  ）。*****['虚幻的 ']","2021年中央民族工作会议指出，必须坚持和完善（ ），确保党中央政令畅通，确保国家法律法规实施，支持各民族发展经济*****['民族区域自治制度']","党的十九大报告指出：“全面贯彻党的宗教工作基本方针，坚持我国宗教的中国化方向，积极引导宗教与社会主义社会（  ）。”*****['相适应']","(  )是社会主义民族关系的本质。*****['和谐']","《学校招收和培养国际学生管理办法》第二十九条规定，高等学校应当尊重国际学生的民族习俗和宗教信仰，并为其提供宗教活动场所。*****['正确']","宗教有着悠久的历史，邪教则都是短期内冒出来的极端功利化的社会组织，往往会对社会进步产生极为严重的破坏作用。*****['正确']","关于民族区域自治制度，下列说法正确的是(  )。*****['民族区域自治是在国家统一领导下的自治', '各民族自治地方都是国家不可分离的部分', '各民族中自治地方的自治机关都必须服从中央的领导', '民族区域自治制度是我国的一项基本政治制度']","“三交”的基本内涵是（  ）*****['促进各民族广泛交往交流交融']","坚持我国宗教中国化方向，下列说法错误的是（  ）。*****['要求宗教界在经济上自觉吻合']","对超自然力量的肯定和否定，决定了宗教与科学在本质上的对立是不可调和的*****['错误']","世界上的邪教五花八门，名称各异，但它们却有着共同的特点。下列不属于邪教特点的是（  ）。*****['集体活动一般在依法登记的宗教活动场所内进行']","下列属于《中华人民共和国境内外国人宗教活动管理规定》及其实施细则规定内容的是（ ）。*****['外国人不得干涉和支配中国宗教团体、宗教活动场所的其他内部事务', '外国人不得干涉中国宗教团体、宗教活动场所的设立和变更', '外国人不得干涉中国宗教团体对宗教教职人员的选任和变更', '外国人不得在中国境内成立宗教组织、设立宗教办事机构、设立宗教活动场所或者开办宗教院校']","1950年11月，四川广元县天主教神甫王良佐和500多名教徒，联名发表了《天主教自立革新运动宣言》，号召中国天主教徒“基于爱祖国*****['自治、自养、自传']","民族区域自治制度在下列哪些方面起到了重要作用（  ）。*****['维护国家统一、领土完整', '加强民族平等团结、促进民族地区发展', '增强中华民族凝聚力']","宗教工作的本质是（  ）*****['群众工作 ']","第三次中央新疆工作座谈会于2020年8月召开*****['错误']","中央第七次西藏工作座谈会于2020年9月召开*****['错误']","2015年8月24日，习近平总书记在中央第六次西藏工作座谈会上指出，必须全面正确贯彻党的民族政策和宗教政策，加强民族团结，不断增进各族群众对（  ）的认同。*****['伟大祖国、中华民族、中华文化、中国共产党、中国特色社会主义']","宗教与科学在本质上是（  ）的关系。*****['对立的']","宗教认识其信仰对象的基本方法是（  ）。*****[' 信仰主义']","《教育法》（  ）规定：国家施行教育与宗教相分离。任何组织和个人不得利用宗教进行妨碍国家教育制度的活动*****['第八条']","关于社会主义民族关系，《宪法》第四条规定（  ）。*****['中华人民共和国各民族一律平等', '国家保障各少数民族的合法的权利和利益', '禁止对任何民族的歧视和压迫', '禁止破坏民族团结和制造民族分裂的行为']","关于中华文化和各民族文化的关系，下列说法正确的是（ ）。*****['各民族优秀传统文化都是中华文化的组成部分', '中华文化是主干', '各民族文化是枝叶', '中华文化是各民族共同创造的']","据《宗教事务条例》第五条规定，各宗教坚持(   )的原则，宗教团体*****['独立自主自办']","下列属于我国多元一体格局内容的是（  ）。*****['文化上的兼收并蓄', '分布上的交错杂居', '经济上的相互依存', '情感上的相互亲近']","习近平总书记在参加十三届全国人大一次会议内蒙古代表团审议时指出，要高举（ ）旗帜，全面贯彻党的民族区域自治制度这一理论根源越扎越深*****['各民族大团结']","如何理解我国的宗教信仰自由政策，下面观点中正确的是（  ）。*****['宗教信仰自由包括不信仰宗教的自由']","宗教工作的本质是（  ）工作。*****['群众']","党的十八大以来，以习近平同志为核心的党中央高度重视民族工作，着眼培育中华民族共同体意识，创新推进（ ），取得显著成绩。*****['民族团结进步创建']","宗教院校以外的学校及其他教育机构传教*****['改正']","2021年中央民族工作会议提出，必须构筑中华民族共有精神家园，使各族人民（ ）*****['人心归聚', '精神相依']","根据《中华人民共和国电信条例》第五十六条中第五款规定，任何组织或者个人不得利用电信网络制作*****['宣扬邪教和封建迷信']","我们的高校是党领导下的高校，是中国特色社会主义高校。办好我们的高校，必须坚持（  ），全面贯彻党的教育方针。*****['以马克思主义为指导']","改革开放以来,我国的民族关系为（  ）。*****['汉族离不开少数民族', '少数民族离不开汉族', '各少数民族之间也相互离不开']","《学校招收和培养国际学生管理办法》第二十九条规定，高等学校应当尊重国际学生的民族习俗和宗教信仰，但在学校内不得进行任何传教*****['正确']","“全面贯彻党的宗教工作基本方针，坚持我国宗教的中国化方向，积极引导宗教与社会主义社会相适应。”这是党的（  ）对宗教工作的重要论述。*****['十九大']","不属于民族团结进步“七进”的基本内容的是（  ）。*****['进家庭']","除经政府批准设立的宗教院校外，在各级各类学校中，以下做法正确的是（）。*****['不得强迫、诱使学生信仰宗教']","必须从（ ）战略高度把握新时代党的民族工作的历史方位。*****['中华民族伟大复兴']","2021年中央民族工作会议指出，必须坚决维护国家主权*****['爱国主义']","《互联网信息服务管理办法》第十五条规定，互联网信息服务提供者不得（ ）含有煽动民族仇恨*****['制作', '复制', '发布', '传播']","根据《中华人民共和国反恐怖主义法》第八十一条规定，利用极端主义，以恐吓、骚扰等方式驱赶其他民族或者有其他信仰的人员离开居住地，情节轻微，尚不构成犯罪的，由公安机关处十五日以上三十日以下拘留，可以并处一万元以下罚款*****['错误']","坚持我国宗教中国化方向，要求宗教界在（  ）上自觉融合。*****['文化']","（  ）是党的宗教工作基本方针的根本方向和目的，是宗教工作的重点。*****['坚持独立自主自办原则']","新时代西藏工作的着眼点和着力点是（ ）*****['维护祖国统一', '加强民族团结']","正确处理涉及民族因素的矛盾纠纷要做到（  ）。*****['教育引导各族群众树立对法律的信仰，自觉按法律办事', '要增强各族群众法律意识，懂得法律面前人人平等，谁都没有超越法律的特权', '要严格区分两类不同性质的矛盾，是什么问题就按什么问题处置。不能因为当事人身份证上写着“某某民族”就犯嘀咕、绕着走，处理起来进退失据', '对极少数蓄意挑拨民族关系、破坏民族团结的犯罪分子，对搞民族分裂和暴恐活动的犯罪分子，不论什么民族出身、信仰哪种宗教，都要坚决依法打击']","(  )是社会主义民族关系的主线。*****['团结']","实行宗教信仰自由政策，出发点和落脚点是（  ）。*****['要最大限度把广大信教群众和不信教群众团结起来']","根据2019年发表的《新疆的若干历史问题》白皮书，下列说法错误的是（）。*****['维吾尔族是隋唐时期突厥人的后裔']","《中华人民共和国反恐怖主义法》第八十一条规定，利用极端主义，实施下列（  ）行为，情节轻微，尚不构成犯罪的，由公安机关处五日以上十五日以下拘留，可以并处一万元以下罚款。*****['强迫他人参加宗教活动，或者强迫他人向宗教活动场所、宗教教职人员提供财物或者劳务的', '以恐吓、骚扰等方式驱赶其他民族或者有其他信仰的人员离开居住地的', '以恐吓、骚扰等方式干涉他人与其他民族或者有其他信仰的人员交往、共同生活的', '阻碍国家机关工作人员依法执行职务的']","要正确认识和把握宗教社会作用的（  ），最大限度发挥宗教的积极作用，最大限度抑制宗教的消极作用，因势利导*****['两重性']","坚持我国宗教中国化方向，要求宗教界在（  ）上自觉适应。*****['社会']","（ ）是最深层次的认同，是民族团结之根*****['文化认同']","下列不属于党关于加强和改进民族工作的重要思想的是（ ）*****['必须坚持政教分离原则，任何宗教都没有超越宪法和法律的特权，都不能干预行政、司法和教育等国家职能的实施。']","以下选项中符合我国宗教信仰自由政策的是（  ）。*****['我国公民有信仰宗教和不信仰宗教的自由']","下列不属于“五爱”的基本内容的是（  ）。*****['爱集体']","党的宗教工作基本方针是：全面贯彻党的宗教信仰自由政策，依法管理宗教事务，坚持（  ）原则，积极引导宗教与社会主义社会相适应。*****['独立自主自办']","我国实行政教分离的原则，任何宗教都没有超越（  ）的特权，都不能干预国家行政*****['宪法和法律']","回顾党的百年历史，党的民族工作取得的最大成就，就是走出了一条（ ）解决民族问题的正确道路*****['中国特色']","实践充分证明，党的民族理论和方针政策是正确的，中国特色解决民族问题的道路是正确的，只有中国共产党才能实现中华民族的大团结，只有（ ）才能凝聚各民族*****['中国特色社会主义']","习近平总书记在中央第（ ）次西藏工作座谈会上指出，要重视加强学校思想政治教育，把爱国主义精神贯穿各级各类学校教育全过程，把爱我中华的种子埋入每个青少年的心灵深处。*****['七']","习近平总书记在第二次中央新疆工作座谈会上指出，各民族要（  ），像石榴籽那样紧紧抱在一起。*****['相互了解、相互尊重']","构建各民族共有精神家园，要以（ ）为引领。*****['社会主义核心价值观']","改革开放特别是党的十八大以来，我们党强调（ ）、（ ）、（ ）等理念，既一脉相承又与时俱进贯彻党的民族理论和民族政策，积累了把握民族问题、做好民族工作的宝贵经验，形成了党关于加强和改进民族工作的重要思想。*****['中华民族大家庭', '中华民族共同体', '铸牢中华民族共同体意识']","在《中华人民共和国海关进出境印刷品及音像制品监管办法》第十二条规定中，符合下列（ ）情况的宗教印刷品、宗教音像制品和其他宗教用品不得人境*****['超出个人自用、合理数量', '危害中国国家安全', '危害社会公共利益内容']","严禁国民教育各级各类师生在学校中穿戴宗教服饰*****['正确']","2014年5月29日，习近平总书记在第二次中央新疆工作座谈会上指出，各族群众要（  ），像石榴籽那样紧紧抱在一起。*****['相互了解、相互尊重、相互包容、相互欣赏、相互学习、相互帮助']","《宪法》第（  ）条规定：中华人民共和国公民有宗教信仰自由。*****['三十六']","我国宪法第三十六条明确规定：“宗教团体和宗教事务不受（  ）的支配”。*****['外国势力']","坚决抵御境外利用宗教进行渗透要求我们（  ）。*****['始终坚持我国宗教团体和宗教事务不受外国势力支配这一宪法原则', '要支持我国宗教独立自主办好教务，坚持中国化方向', '要规范宗教对外交流活动', '要规范互联网宗教信息服务']","习近平总书记在十三届全国人大四次会议内蒙古代表团审议时指出，要围绕共同团结奋斗*****['汉族离不开少数民族', '少数民族离不开汉族', '各少数民族之间也相互离不开']","新中国成立后，我们党创造性地把马克思主义民族理论同中国民族问题具体实际相结合，走出一条中国特色解决民族问题的正确道路，确立了党的民族理论和民族政策，（ ），（ ），各族人民在历史上第一次真正获得了平等的政治权利*****['把民族平等作为立国的根本原则之一', '确立了民族区域自治制度']","宗教的消亡是事物本身矛盾运动的结果，是社会历史发展的自然过程。*****['正确']","《刑法》第三百条规定:组织、利用会道门、邪教组织或者利用迷信破坏国家法律、行政法规实施的，情节特别严重的，处（  ）以上有期徒刑,并处罚金或者没收财产。*****['7年']","马克思恩格斯认为宗教的根源有（  ）。*****['自然根源', '社会根源', '认识根源']","教育法（  ）规定，国家实行教育和宗教相分离。*****['第八条']","新时代党的治藏方略“十个必须”必须中，西藏工作的着眼点和着力点是（）*****['维护祖国统一', '加强民族团结']","信教公民举行集体宗教活动一般应在经登记的寺院*****['其他固定宗教活动场所']","马克思主义哲学课的一项重要内容是：要切实加强青少年的科学世界观，其中包括（  ）的宣传教育。*****['无神论']","我国支持各宗教在保持基本信仰、核心教义、礼仪制度的同时，对教规教义作出符合当代中国发展进步要求、符合（ ）的阐释。*****['中华优秀传统文化']","马克思认为，宗教是人的异化形式，宗教的本质就是人的本质，是“人创造了宗教，而不是宗教创造了人”。*****['正确']","“一体”指中华民族是由56个民族组成的统一体。*****['正确']","要积极推进（），形成共学共进的氛围和条件，避免各民族学生到了学校还是各抱各的团*****['民汉合校、混合编班']","习近平总书记在（  ）上明确强调，共产党员要做坚定的马克思主义无神论者，严守党章规定，坚定理想信念，牢记党的宗旨，决不能在宗教中寻找自己的价值和信念。*****['全国宗教工作会议']","2015年9月在会见基层民族团结优秀代表时，习近平总书记指出，（ ），这是全体中华儿女的共同心愿，也是全国各族人民的共同目标。*****['中华民族一家亲，同心共筑中国梦']","(  )是社会主义民族关系的保障。*****['互助']","马克思、恩格斯运用辩证唯物主义和历史唯物主义观察分析宗教现象和宗教问题，创立了（ ），为马克思主义政党正确认识和处理宗教问题提供了理论基础。*****['马克思主义宗教观']","国家要（  ）对宗教事务进行管理*****['依法']","习近平总书记在参加十三届全国人大四次会议内蒙古代表团审议时强调，要认真做好推广普及（）工作，全面推行使用国家统编教材。*****['国家通用语言文字']","政治传统的大一统，各民族多元一体，是历史留给我们的一笔重要财富，也是我们国家的一个重要优势。*****['正确']","我国民族关系的真实写照是汉族离不开少数民族*****['正确']","下列说法错误的是（  ）*****['中华文化就是汉族文化。']","根据新修订《宗教事务条例》第七十条规定，擅自组织公民出境参加宗教方面的培训*****['2万元以上20万元以下']","新时代党的民族工作的主线是（ ）。*****['铸牢中华民族共同体意识']","党的十八以来，民族工作的显著成绩体现在(  )。*****['各民族交往交流交融广泛拓展', '中华民族共同体意识不断增强', '平等团结互助和谐的社会主义民族关系不断巩固和发展']","《学校招收和培养国际学生管理办法》是由教育部、外交部、公安部、司法部联合颁布的。*****['正确']","下列属于新时代党的治疆方略内容的是（ ）。*****['坚持从战略上审视和谋划新疆工作', '坚持以凝聚人心为根本', '坚持紧贴民生推动高质量发展', '坚持加强党对新疆工作的领导']","宗教事务管理坚持的基本原则是（  ）。*****['保护合法', '制止非法', '遏制极端', '抵御渗透']","大汉族主义和狭隘民族主义的危害在于*****['容易产生民族歧视', '容易滋生离心倾向', '造成民族隔阂和对立', '严重的会被敌对势力利用']","2017年6月14日，国务院常务会议审议通过了《宗教事务条例（修订草案）》,2017年8月26日，李克强总理签署国务院令公布条例，自（  ）起施行。*****['2018-2-1']","《宪法》序言指出，维护民族团结，既要反对大汉族主义，也要反对地方民族主义。*****['正确']","马克思认为，宗教是人的异化形式，宗教的本质是（  ）。*****['人的本质']","“三股势力”是指（ ）*****['暴力恐怖势力', '民族分裂势力', '宗教极端势力']","新时代新疆工作的总目标是（  ）。*****['社会稳定和长治久安']","涉及民族因素的矛盾和问题，有不少是由于群众不懂法或者不守法酿成的。这些矛盾和问题，虽然带着“民族”字样，但不都是民族问题。*****['正确']","《宗教事务条例》第三条规定，宗教事务管理坚持的原则是（  ）。*****['保护合法，制止非法，遏制极端，抵御渗透，打击犯罪']","处理我国宗教关系要（  ）。*****['牢牢把握坚持党的领导、巩固党的执政地位、强化党的执政基础这个根本', '坚持政府依法对涉及国家利益和社会公共利益的宗教事务进行管理', '必须坚持政教分离', '坚持宗教不得干预行政、司法、教育等国家职能实施']","依据《宗教事务条例》规定，下列哪项（ ）不是宗教团体、宗教院校、宗教活动场所、宗教教职人员上开展对外交往的基础。*****['互惠互利']","习近平总书记在中央第七次西藏工作座谈会上指出，要培育和践行（ ），不断增强各族群众对伟大祖国*****['社会主义核心价值观']","恩格斯关于宗教的发展曾提出过三种图式，下列说法错误的是（  ）。*****['从原始社会的“自发宗教”到阶级社会的“自觉宗教”']","本民族意识要服从和服务于（ ）意识。*****['中华民族共同体']","党的十九大把“铸牢中华民族共同体意识”写入党章”*****['正确']","宗教工作在党和国家工作全局中具有特殊重要性，关系到（  ）。*****['中国特色社会主义事业发展', '党同人民群众的血肉联系', '社会和谐、民族团结', '国家安全和祖国统一']","宗教信仰从本质上说属于意识形态范畴，反映的是人们精神世界的问题，是人们的一种思想认识。*****['正确']","“大藏区”的概念根源于西藏历史*****['错误']","我国实行宗教与教育（  ）的原则。*****['相分离']","按照《中华人民共和国海关进出境印刷品及音像制品监管办法》规定，一切宗教类印刷品及音像制品都禁止入境。*****['错误']","各高校利用课堂主渠道对在校学生进行马克思主义宗教观和党的宗教政策宣传教育要做到（  ）。*****['在学校德育课程、思想政治理论课中加强科学无神论教育、培养唯物主义思想认识', '把马克思主义宗教观、党的宗教政策和国家相关法律法规教育融入到人文素养和科学精神教育体系']","实行宗教信仰自由政策，出发点和落脚点是要最大限度把广大信教和不信教群众团结起来。*****['正确']","习近平总书记指出，积极引导宗教与社会主义社会相适应，一个重要的任务就是（  ）。*****['支持我国宗教坚持中国化方向']","“多元”指中华民族的人口众多是多元的*****['错误']","任何组织和个人不得在以下场所（  ）进行宗教活动。*****['学校']","平等团结互助和谐，这是新时代我国民族团结进步事业的生动写照，也是新时代民族工作创新推进的鲜明特征。*****['错误']","新时代党的治藏方略“十个必须”必须中，西藏经济社会发展的出发点和落脚点是（ ）*****['改善民生', '凝聚人心']","文化认同是民族团结的（ ）*****['根脉']","宗教极端主义一般是宗教中的某一派别。*****['错误']","正确把握中华民族共同体意识和各民族意识的关系包括：（  ）。*****['引导各民族始终把中华民族利益放在首位', '本民族意识要服从和服务于中华民族共同体意识', '在实现好中华民族整体利益进程中实现好各民族具体利益', '反对大汉族主义和地方民族主义']","《宪法》第（  ）条规定，各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。*****['四']","增进共同性、尊重和包容差异性是民族工作的（）*****['重要原则']","习近平总书记在2019年全国民族团结进步表彰大会上指出，（ ），是中华民族伟大复兴必定要实现的根本保证。*****['各族人民亲如一家']","宪法规定:国家保护正常的宗教活动，正常的宗教活动是指（  ）。*****['在宪法、法律和政策范围内进行的宗教活动']","国家应保护一切宗教活动。*****['错误']","在《中外合作办学条例》中第七条规定中，（  ）不得在中国境内从事合作办学活动。*****['外国宗教组织', '外国宗教教职人员', '外国宗教院校', '外国宗教机构']","《中华人民共和国电信条例》第六十六条规定，违反本条例（  ）的规定，构成犯罪的，依法追究刑事责任；尚不构成犯罪的，由公安机关*****['第五十六、五十七条']","习近平总书记鲜明提出（  ），这是我们党关于宗教工作理论的系统总结和重大创新，是中国特色社会主义理论体系的“宗教篇”。*****['中国特色社会主义宗教理论']","下列（  ）不是社会主义核心价值观的内容。*****['爱国', '诚信', '敬业']","依法对宗教事务进行管理，是世界大多数国家的通行做法，也是引导宗教与社会主义社会相适应的必由之路。*****['正确']","下列关于民族区域自治制度的说法正确的是（  ）。*****['民族区域自治制度保证了国家团结统一', '民族区域自治制度实现了各民族共同当家作主', '民族区域自治不是某个民族独享的自治', '民族自治地方不是某个民族独有的地方']","关于中华民族各民族之间的关系，下列说法正确的是(  )。*****['中华民族各民族是一荣俱荣、一损俱损的命运共同体', '你中有我、我中有你、谁也离不开谁的多元一体格局是在历史发展中逐步形成的', '中华民族和各民族的关系是一个大家庭和家庭成员的关系', '各民族之间的关系是一个大家庭里不同成员的关系']","信仰宗教的党员，经组织教育仍然没有转变，应当（  ）。*****['劝其退党']","《宗教事务条例》第四十七条规定，从事互联网宗教信息服务，应当经(   )以上人民政府宗教事务部门审核同意后，按照国家互联网信息服务管理有关规定办理。*****['省级']","下列说法错误的是（  ）。*****['公民不能信仰宗教']","（  ）是中国特色解决民族问题的正确道路的重要内容和制度保障*****['民族区域自治制度']","下列关于中华民族多元一体格局中，多元与一体的关系不正确的是（  ）。*****['一体是要素和动力']","中华民族是多元一体的大家庭，是在长期历史演进中形成的（）。*****['命运共同体']","马克思认为，宗教是人的异化形式，宗教的本质就是人的本质，是“人创造了宗教，而不是宗教创造了人”。*****['正确']","下列关于民族区域自治制度的说法正确的是（  ）。*****['是我国解决民族问题的基本政策']","《宪法》第三十六条规定，中华人民共和国公民有宗教信仰自由。*****['正确']","正常的宗教活动主要有两层含义：一是宗教活动要在（  ）允许的范围内进行；二是宗教活动要严格按照宗教教义*****['法律、法规']","根据《宗教事务条例》第四十一条规定，下列地点中（  ）不得组织、举行宗教活动的是。*****['高等院校']","目前，全国共建立了156个民族区域自治地方，其中包括（  ）自治区*****['5个']","民族团结是我国各族人民的生命线，各民族共同团结进步*****['民族团结是实现各民族繁荣的前提条件，是中华民族伟大复兴的保证', '民族团结有利于维护国家统一和领土完整']","我国是统一的多民族国家，（ ）是各族人民的生命线*****['民族团结']","在《刑法》第三百条规定，组织利用会道门、邪教组织或者利用迷信破坏国家法律、行政法规实施的，关于处罚下列说法错误的是（  ）。*****['处三年以上七年以下有期徒刑，并处罚金']","2021年中央民族工作会议提出，必须促进各民族（ ）（ ）（ ），促进各民族在理想*****['交往', '交流', '交融']","《宪法》第二十四条规定，国家通过普及（  ），在城乡不同范围的群众中制定和执行各种守则*****['理想教育', '道德教育', '文化教育', '纪律和法制教育']","习近平总书记在全国民族团结进步表彰大会上指出，各民族在文化上要（ ）*****['相互尊重', '相互欣赏', '相互学习', '相互借鉴']","党员不能信仰宗教，但可以参加宗教活动*****['正确', '错误']","关于抵御利用宗教对学校进行渗透和防范校园传教的意义，下列说法不正确的是（  ）。*****['关系到教育与宗教关系的和谐']","宗教极端主义的危害在于(  )。*****['将宗教的教义绝对化', '以歪曲宗教教义或者其他方法煽动仇恨、煽动歧视、鼓吹暴力', '其本质反人类、反社会、反文明，是对宗教的恶意歪曲利用', '具有欺骗性和煽动性，诱惑、误导一些不明真相的人从事暴力恐怖活动']","依法管理宗教事务的要旨是保护合法、制止非法、遏制极端、抵御渗透、打击犯罪*****['正确']","新时代党的民族工作的重要任务是（ ）。*****['推动各民族为全面建设社会主义现代化共同奋斗']","宗教极端主义在本质上（ ）*****['反人类', '反社会', '反文明', '反科学']","习近平总书记在2021年中央民族工作会议上指出，要正确把握物质和精神的关系，要赋予所有改革发展（ ），（ ），（ ），让中华民族共同体牢不可破。*****['以彰显中华民族共同体意识的意义', '以维护统一、反对分裂的意义', '以改善民生、凝聚人心的意义']","习近平总书记在第三次中央新疆工作座谈会上强调，要加强（ ）*****['中华民族共同体历史', '中华民族多元一体格局']","坚持我国宗教中国化方向，是积极引导宗教与社会主义社会相适应的必然要求，也是我国宗教发展的必由之路。*****['正确']","民族分裂势力企图破坏民族团结，极个别民族地区发生民族隔阂的现象，这是支流，不是主流*****['正确']","民族习俗从本质上说属于意识形态范畴，反映的是人们精神世界的问题，是人们的一种思想认识。宗教信仰属于某种社会群体的行为方式和生活方式。*****['错误']","习近平总书记在全国民族团结进步表彰大会上指出，我们要全面贯彻党的（ ）和（ ），坚持共同团结奋斗*****['民族理论', '民族政策']","2014年4月，习近平总书记考察新疆时强调，要把民族团结紧紧抓在手上，坚持正确的祖国观*****['和睦相处、和衷共济、和谐发展']","宗教必须在宪法和法律规定的权利和义务范围内活动，任何人不得利用宗教反对党的领导和社会主义制度，宗教活动不得妨碍社会秩序和生活秩序。*****['正确']","宗教对于国家来说是私人的事情，实行政教分离，宗教信仰自由政策；宗教对于工人阶级政党来说，也是个人的私事。*****['错误']","宪法第（ ）条规定，中华人民共和国公民有维护国家统一和全国各民族团结的义务。*****['五十二']","关于“大藏区”的表述，以下说法正确的是（  ）。*****['“大藏区”纯属虚构，不符合中国历史和国情', '“大藏区”是典型的极端民族主义和种族主义的表现', '“大藏区”是西方殖民者侵略中国、企图分裂中国的产物', ' 按照十四世达赖集团的假想，“大藏区”总面积超过中国国土面积的四分之一']","《教育法》第八条规定，国家实行教育与宗教相分离。任何组织和个人不得利用宗教进行妨碍国家教育制度的活动。*****['正确']","我国宗教工作形势总体向好，表现在（  ）。*****['党的宗教工作基本方针得到贯彻', '宗教工作法治化明显加强', '党同宗教界的爱国统一战线不断巩固', '宗教活动总体平稳有序']","习近平总书记在全国民族团结进步表彰大会上指出，要把民族团结进步创建全面深入持久开展起来，创新方式载体，推动进机关*****['乡镇', '学校', '宗教活动场所']","要加强向干部群众和青少年进行辩证唯物主义和历史唯物主义的科学世界观的教育，宣传（  ），加强有关自然现象*****['宗教知识']","党的十九大对民族工作的重要论述包括(  )。*****['全面贯彻党的民族政策', '深化民族团结进步教育', '铸牢中华民族共同体意识', '坚决反对一切分裂祖国、破坏民族团结和社会和谐稳定的行为']","《宪法》中关于民族关系的规定包括（  ）。*****['中华人民共和国是全国各族人民共同缔造的统一的多民族国家', '中华人民共和国各民族一律平等', '禁止对任何民族的歧视和压迫，禁止破坏民族团结和制造民族分裂的行为']","(  )是积极引导宗教与社会主义社会相适应的必然要求，也是我国宗教发展的必由之路。*****['坚持我国宗教中国化方向']","（ ）是习近平总书记关于民族工作的重大原创性论断，是新时代党的民族工作的主线。*****['铸牢中华民族共同体意识']","以下叙述不正确的是（  ）。*****['国家保护所有的宗教活动']","习近平总书记在参加十三届全国人大四次会议内蒙古代表团审议时指出，要在各族干部群众中深入开展中华民族共同体意识教育，特别是要从青少年教育抓起，引导广大干部群众全面理解党的民族政策，树立正确的（ ）*****['国家观', '历史观', '文化观']","假冒宗教教职人员进行宗教活动的，由宗教事务部门责令（  ），有违法所得的，没收违法所得;有违反治安管理行为的，依法给予治安管理处罚;构成犯罪的，依法追究刑事责任。*****['停止活动 ']","习近平总书记在第三次中央新疆工作座谈会上强调，要促进各民族（ ）*****['广泛交往', '全面交流', '深度交融']","宗教信仰自由等于宗教活动可以不受任何约束。*****['错误']","在《网络出版服务管理规定》第二十四条规定中，网络出版物不得含有以下（  ）内容。*****['反对宪法确定的基本原则的', '危害国家统一、主权和领土完整的', '宣扬邪教、迷信的', '侮辱或者诽谤他人，侵害他人合法权益的']","宗教信仰从本质上说属于意识形态范畴，反映的是人们（  ）的问题，是人们的一种思想认识。*****[' 精神世界']","中国特色社会主义宗教理论，以（  ）为指导，对我国社会主义特别是初级阶段的宗教进行理论阐述，分析宗教在我国社会主义时期的特征和作用，明确党和国家在社会主义条件下处理宗教问题的方针政策。*****['马克思主义']","多民族大一统格局是我国自（  ）以来就基本形成的历史传统和独特优势*****['秦汉']","对中华民族共同体的认识。下列说法正确的是（ ）*****['各民族交融汇聚成多元一体中华民族', '各民族共同缔造、发展、巩固统一的伟大祖国', '中华民族多元一体是先人们留给我们的丰厚遗产', '中华民族多元一体是我国发展的巨大优势']","下列不属于宗教产生的根源的是（  ）。*****['文化根源']","习近平总书记在全国民族团结进步表彰大会强调，（ ）和（ ）都是民族团结的大敌，要坚决反对。*****['大汉族主义', '地方民族主义']","自成立起，中国共产党就积极探索适合我国国情的解决民族问题的道路。*****['正确']","坚持我国宗教中国化方向，要求宗教界在（  ）上自觉认同；坚持我国宗教中国化方向，要求宗教界在（  ）上自觉融合；坚持我国宗教中国化方向，要求宗教界在（  ）上自觉适应。*****['政治']","邪教的本质及危害性是（  ）。*****['反人类', '反科学', '反社会']","下列行为中（  ）违反《宗教事务条例》。*****['基督教信徒在路边散发宗教传单', '某寺院参加赈灾活动并向灾民宣讲佛法','学生在学校组织佛学社团']","坚持我国宗教中国化方向，要求宗教界在（  ）上自觉认同。*****['政治']","新时代党的民族工作的出发点和落脚点是*****['实现中华民族伟大复兴']","中央第七次西藏工作座谈会提出，要培育和践行社会主义核心价值观，不断增强各族群众对伟大祖国、中华民族、中华文化、中国共产党、中国特色社会主义的认同。*****['正确']","《宗教事务条例》第五十六条规定，宗教团体*****['正确', '错误']","习近平总书记在第三次中央新疆工作座谈会上指出，新疆自古以来就是（ ），新疆各民族是中华民族血脉相连的家庭成员。*****['多民族聚居地区']","下列不属于党的十九大对民族工作的重要论述的是（  ）。*****['同心共筑中国梦']","共产党员和 （  ）不能信仰宗教*****['共青团员']","下列有关新疆的说法不正确的是（  ）。*****['新疆地区各族居民历史上一直信仰伊斯兰教']","关于邪教的危害，以下说法错误的是（  ）。*****['精神寄托']","2017年9月召开的新疆若干历史问题研究座谈会,明确阐明（  ）。*****['新疆是我国领土不可分割的一部分，多民族大一统格局是我国自秦汉以来就基本形成的历史传统和独特优势', '新疆各民族是中华民族血脉相连的家庭成员，实现中华民族伟大复兴的中国梦是各族人民的共同利益', '新疆各民族文化扎根于中华文明沃土，是中华文化不可分割的一部分', '新疆是多种宗教并存地区，促进宗教关系和谐是新疆稳定繁荣的历史经验等等']","铸牢中华民族共同体意识要从孩子抓起，青少年首先要知道自己是中华民族，树立中华民族一员的意识，不能只知道自己是哪个民族的人。*****['正确']","习近平总书记在中央第七次西藏工作座谈会上指出，要挖掘、整理、宣传西藏自古以来各民族交往交流交融的历史事实，引导各族群众看到民族的走向和未来，深刻认识到*****['中华民族是命运共同体']","坚持和发展中国特色社会主义宗教理论要做到（  ）。*****['辩证看待我国宗教的社会作用', '坚持我国宗教中国化方向', '构建积极健康的宗教关系', '提高宗教工作法治化水平']","“六个相互”是习近平总书记在第一次中央新疆工作座谈会上提出的*****['错误']","按照中央民族工作会议精神，坚持依法治理民族事务，做到法律面前人人平等，就要做到（ ），（ ），（ ）。*****['依法保障各族群众合法权益', '依法妥善处理涉民族因素的案事件', '依法打击各类违法犯罪行为']","党的十九大把（  ）写入党章，成为全党全国各族人民实现中国梦新征程上的共同意志和根本遵循。*****['铸牢中华民族共同体意识']","2021年中央民族工作会议指出，必须坚持正确的中华民族历史观，增强对中华民族的（ ）和（ ）。*****['认同感', '自豪感']","我国实行（  ）的原则，任何宗教都没有超越宪法和法律的特权，都不能干预国家行政*****['宗教自由']","“四个共同”是指我国（  ）。*****['辽阔的疆域是各民族共同开拓的', '悠久的历史是各民族共同书写的', '灿烂的文化是各民族共同创造的', '伟大的精神是各民族共同培育的。']","依《宗教事务条例》第四十八条规定，互联网宗教信息服务的内容应当符合（  ）的相关规定*****['有关法律', '有关法规', '宗教事务管理']","党的宗教工作基本方针是（  ）。*****['全面贯彻党的宗教信仰自由政策', '依法管理宗教事务', '坚持独立自主自办原则', '积极引导宗教与社会主义社会相适应']","中国宗教的特征是（  ）。*****['长期性、群众性、民族性、国际性、复杂性']","党的十九大报告指出：“全面贯彻党的民族政策，深化民族团结进步教育，铸牢中华民族共同体意识，加强各民族（  ），促进各民族像石榴籽一样紧紧抱在一起，共同团结奋斗*****['交往交流交融']","《中华人民共和国海关进出境印刷品及音像制品监管办法》规定，个人携带、邮寄进境的宗教类出版物及印刷品，在自用、合理范围内的数量不超过（  ），是可以进境的。*****['3本']","必须坚持（ ），推进民族事务治理体系和治理能力现代化。*****['依法治理民族事务']","以下说法不正确的是（  ）。*****['在校学生可以参加宗教组织和教徒在宗教场所以外的地方进行的宗教活动']","《教育法》第九条规定，公民除宗教信仰外不分民族*****['错误']","根据《宗教事务条例》有关规定，任何组织或者个人不得利用宗教进行（  ）等违法活动。*****['危害国家安全', '破坏社会秩序', '损害公民身体健康', '妨碍国家教育制度']","做好民族工作要正确把握（ ）。*****['共同性和差异性的关系', '中华民族共同体意识和各民族意识的关系', '中华文化和各民族文化的关系', '物质和精神的关系']","在恩格斯提出的宗教发展和宗教历史形态图示中，宗教经历了从原始社会的（  ）到阶级社会的（  ）的发展过程。*****['自发宗教、人为宗教']","封建迷信和宗教信仰的区别在于（  ）。*****['宗教是依法成立的社会组织']","全面正确地贯彻宗教信仰自由政策包含有（  ）两个方面的内容。*****['要求尊重每个公民信仰宗教的自由和不信仰宗教的自由', '要求权利与义务的统一']","《宪法》第三十六条规定，中华人民共和国公民有宗教信仰自由，任何国家机关*****['个人']","信教公民举行集体宗教活动一般应在经登记的宗教活动场所内举行，下列（  ）属于违法宗教活动处所。*****['信教学生宿舍']","在社会主义条件下，信教群众与不信教群众在政治上、经济上的根本利益是一致的，都是我们党执政的重要基础，都是建设中国特色社会主义的重要力量。*****['正确']","（  ）在《反杜林论》中指出：“一切宗教都不过是支配着人们日常生活的外部力量在人们头脑中的幻想的反映，在这种反映中，人间的力量采取了超人间的力量的形式。”*****['恩格斯']","宗教在社会主义社会将（  ）。*****['长期存在']","铸牢中华民族共同体意识，就是要引导各族人民牢固树立（ ）*****['休戚与共', '荣辱与共', '生死与共', '命运与共']","中华民族主要分布在(  )。*****['中国大陆']","高校在教育教学过程中，要发挥课堂主渠道作用，在学校德育课程*****['无神论']","科学无神论的教育，并不仅仅限于单纯否定神灵的存在。它的最主要的内容是（  ），还包括（  ）和（  ）。*****['运用马克思主义的科学世界观认识宗教的本质及其发展规律', '自然科学知识的普及，社会进化', '人的生老病死、吉凶祸福的科学文化和社会科学知识的宣传']","关于如何区分邪教和宗教，下列说法错误的是（  ）。*****['看看宗教领袖是谁']","实现中华民族伟大复兴的中国梦，就要以铸牢中华民族共同体意识为主线，把（ ）作为基础性事业抓紧抓好。*****['民族团结进步事业']","下列属于新时代党的治藏方略“十个必须”的基本内容的是（  ）。*****['必须坚持中国共产党领导、中国特色社会主义制度、民族区域自治制度', '必须坚持治国必治边、治边先稳藏的战略思想', '必须坚持依法治藏、富民兴藏、长期建藏、凝聚人心、夯实基础的重要原则', '必须加强党的建设特别是政治建设']","下列（  ）不是“五个认同”的内容。*****['无神论']","马克思主义对宗教的批判的目的是要（ ）。*****['废除作为人们幻想的幸福的宗教，也就是要求实现人民的现实的幸福']","下列关于依法管理宗教事务的说法，正确的是（ )。*****['依法进行管理，就是要切实保障宗教信仰自由，保证正常宗教活动的有序进行，保护宗教团体的合法权益。', '依法管理宗教事务的要旨是保护合法、制止非法、遏制极端、抵御渗透、打击犯罪。',  '依法管理宗教事务，要规范那些以“宗教信仰自由”为借口，违背宪法、法律和政策的事情，防止和制止不法分子利用宗教活动制造混乱，违法犯罪，以及境外敌对势力的渗透活动。']","我国的民族区域自治是指在国家的统一领导下，各少数民族聚居地方实行区域自治，设立（ ），行使（ ）。*****['自治机关', '自治权']","《宪法》序言指出，中华人民共和国是全国各族人民共同缔造的统一的多民族国家。（  ）的社会主义民族关系已经确立，并将继续加强。*****['平等团结互助和谐']","下列说法正确的是（  ）。*****['各民族首先要树立中华民族的一员的意识。']","我国某地一寺庙佛门弟子积极参加当地架桥修路、捐资助学等活动，方丈还以80万元巨资买到了电视台黄金时段前15秒公益广告权，宣传保护野生动物和禁止毒品。以上事实说明，在我国（ ）。*****['信教群众与不信教群众的根本利益是一致的']"]
# json = {'《宗教事务条例》第五十六条规定，宗教团体、宗教院校、宗教活动场所、信教群众可以依法兴办公益慈善事业。':['错误'],'根据新修订《宗教事务条例》第七十条规定，擅自组织公民出境参加宗教方面的培训、会议、朝觐等活动的，或者擅自开展宗教教育培训的，由宗教事务部门会同有关部门责令停止活动，可以并处（ ）的罚款。':['2万元以上20万元以下'],'下列不属于我国宗教特征的是（  ）。': ['单一性'], '迷信本质上是一种世界观，宗教则是少数迷信职业者骗取钱财坑害百姓的手段': ['错误'], '中华民族和各民族的关系是（  ）。': ['大家庭和家庭成员的关系'], '宗教信仰自由是宪法赋予公民的权利，就是说共产党员': ['错误'], '下列说法正确的是（  ）。': ['各民族首先要树立中华民族的一员的意识。'], '积极引导宗教与社会主义社会相适应，是要引导信教群众（  ）。': ['维护祖国统一', '拥护中国共产党领导', '积极践行社会主义核心价值观', '投身改革开放和社会主义现代化建设'], '下列不属于新时代党的治疆方略内容的是（）': ['坚持生态保护第一。'], '《中国共产主义青年团章程》规定：“中国共产主义青年团坚决拥护中国共产党的纲领，以马克思列宁主义、（ ）、（ ）、（ ）、科学发展观、（ ）。”': ['毛泽东思想', '邓小平理论', '“三个代表”重要思想', '习近平新时代中国特色社会主义思想'], '(  )是社会主义民族关系的基石。': ['平等'], '境外利用宗教对我国进行渗透，是宗教问题，不是政治问题': ['错误'], '在新修订《宗教事务条例》中，哪两项对从事互联网宗教信息服务作出了规定？': ['第四十七、四十八条'], '西藏工作对党和国家工作大局的影响不大': ['错误'], '关于“大藏区”的说法，错误的是（  ）。': ['“大藏区”是十四世达赖提出的'], '依《宗教事务条例》第四十四条规定，禁止在宗教院校以外的学校及其他教育机构进行（  ）。': ['传教', '设立宗教活动场所', '成立宗教组织', '举行宗教活动'], '下列属于新时代党的治藏方略“十个必须”的基本内容的是（  ）。': ['必须坚持中国共产党领导、中国特色社会主义制度、民族区域自治制度', '必须坚持治国必治边、治边先稳藏的战略思想', '必须坚持依法治藏、富民兴藏、长期建藏、凝聚人心、夯实基础的重要原则', '必须加强党的建设特别是政治建设'], '习近平总书记在参加十三届全国人大一次会议内蒙古代表团审议时指出，我国是统一的多民族国家，民族团结是各族人民的生命线。加强民族团结，根本在于（ ）。': ['坚持和完善民族区域自治制度'], '新修订《宗教事务条例》规定，宗教教职人员经宗教团体认定，报（  ）人民政府宗教事务部门备案，可以从事宗教教务活动。': ['县级以上'], '宗教和迷信都是对支配人们日常生活的人间力量采取的超人间形式的反映，密切联系，但并不相同。': ['正确'], '我国的宗教政策是（  ）。': ['宗教信仰自由'], '我国宪法第（  ）条明确规定：“宗教团体和宗教事务不受国外势力的支配”。': ['三十六'], '各民族要始终把（ ）的利益放在首位。': ['中华民族'], '中华民族共同体意识是（ ）': ['国家统一之基', '民族团结之本', '精神力量之魂'], '我国的民族区域自治是指在国家的统一领导下，各少数民族聚居地方实行区域自治，设立自治机关，行使自治权。': ['正确'], '用法律来保障民族团结，要做到（  ）。': ['增强各族群众法律意识', '严格区分两类不同性质的矛盾', '坚决依法打击蓄意挑拨民族关系、破坏民族团结的犯罪分子', '坚决依法打击搞民族分裂和暴恐活动的犯罪分子'], '公民有宗教信仰自由，就是说：每个公民（  ）。': ['有信仰宗教的自由，也有不信仰宗教的自由', '有信仰这种宗教的自由，也有信仰那种宗教的自由', '有过去不信教而现在信教的自由', '有过去信教而现在不信教的自由'], '马克思主义认为，宗教对于现实世界的反映是（  ）。': ['虚幻的 '], '2021年中央民族工作会议指出，必须坚持和完善（ ），确保党中央政令畅通，确保国家法律法规实施，支持各民族发展经济': ['民族区域自治制度'], '党的十九大报告指出：“全面贯彻党的宗教工作基本方针，坚持我国宗教的中国化方向，积极引导宗教与社会主义社会（  ）。”': ['相适应'], '(  )是社会主义民族关系的本质。': ['和谐'], '《学校招收和培养国际学生管理办法》第二十九条规定，高等学校应当尊重国际学生的民族习俗和宗教信仰，并为其提供宗教活动场所。': ['正确'], '宗教有着悠久的历史，邪教则都是短期内冒出来的极端功利化的社会组织，往往会对社会进步产生极为严重的破坏作用。': ['正确'], '关于民族区域自治制度，下列说法正确的是(  )。': ['民族区域自治是在国家统一领导下的自治', '各民族自治地方都是国家不可分离的部分', '各民族中自治地方的自治机关都必须服从中央的领导', '民族区域自治制度是我国的一项基本政治制度'], '“三交”的基本内涵是（  ）': ['促进各民族广泛交往交流交融'], '坚持我国宗教中国化方向，下列说法错误的是（  ）。': ['要求宗教界在经济上自觉吻合'], '对超自然力量的肯定和否定，决定了宗教与科学在本质上的对立是不可调和的': ['错误'], '世界上的邪教五花八门，名称各异，但它们却有着共同的特点。下列不属于邪教特点的是（  ）。': ['集体活动一般在依法登记的宗教活动场所内进行'], '下列属于《中华人民共和国境内外国人宗教活动管理规定》及其实施细则规定内容的是（ ）。': ['外国人不得干涉和支配中国宗教团体、宗教活动场所的其他内部事务', '外国人不得干涉中国宗教团体、宗教活动场所的设立和变更', '外国人不得干涉中国宗教团体对宗教教职人员的选任和变更', '外国人不得在中国境内成立宗教组织、设立宗教办事机构、设立宗教活动场所或者开办宗教院校'], '1950年11月，四川广元县天主教神甫王良佐和500多名教徒，联名发表了《天主教自立革新运动宣言》，号召中国天主教徒“基于爱祖国': ['自治、自养、自传'], '民族区域自治制度在下列哪些方面起到了重要作用（  ）。': ['维护国家统一、领土完整', '加强民族平等团结、促进民族地区发展', '增强中华民族凝聚力'], '宗教工作的本质是（  ）': ['群众工作 '], '第三次中央新疆工作座谈会于2020年8月召开': ['错误'], '中央第七次西藏工作座谈会于2020年9月召开': ['错误'], '2015年8月24日，习近平总书记在中央第六次西藏工作座谈会上指出，必须全面正确贯彻党的民族政策和宗教政策，加强民族团结，不断增进各族群众对（  ）的认同。': ['伟大祖国、中华民族、中华文化、中国共产党、中国特色社会主义'], '宗教与科学在本质上是（  ）的关系。': ['对立的'], '宗教认识其信仰对象的基本方法是（  ）。': [' 信仰主义'], '《教育法》（  ）规定：国家施行教育与宗教相分离。任何组织和个人不得利用宗教进行妨碍国家教育制度的活动': ['第八条'], '关于社会主义民族关系，《宪法》第四条规定（  ）。': ['中华人民共和国各民族一律平等', '国家保障各少数民族的合法的权利和利益', '禁止对任何民族的歧视和压迫', '禁止破坏民族团结和制造民族分裂的行为'], '关于中华文化和各民族文化的关系，下列说法正确的是（ ）。': ['各民族优秀传统文化都是中华文化的组成部分', '中华文化是主干', '各民族文化是枝叶', '中华文化是各民族共同创造的'], '据《宗教事务条例》第五条规定，各宗教坚持(   )的原则，宗教团体': ['独立自主自办'], '下列属于我国多元一体格局内容的是（  ）。': ['文化上的兼收并蓄', '分布上的交错杂居', '经济上的相互依存', '情感上的相互亲近'], '习近平总书记在参加十三届全国人大一次会议内蒙古代表团审议时指出，要高举（ ）旗帜，全面贯彻党的民族区域自治制度这一理论根源越扎越深': ['各民族大团结'], '如何理解我国的宗教信仰自由政策，下面观点中正确的是（  ）。': ['宗教信仰自由包括不信仰宗教的自由'], '宗教工作的本质是（  ）工作。': ['群众'], '党的十八大以来，以习近平同志为核心的党中央高度重视民族工作，着眼培育中华民族共同体意识，创新推进（ ），取得显著成绩。': ['民族团结进步创建'], '宗教院校以外的学校及其他教育机构传教': ['改正'], '2021年中央民族工作会议提出，必须构筑中华民族共有精神家园，使各族人民（ ）': ['人心归聚', '精神相依'], '根据《中华人民共和国电信条例》第五十六条中第五款规定，任何组织或者个人不得利用电信网络制作': ['宣扬邪教和封建迷信'], '我们的高校是党领导下的高校，是中国特色社会主义高校。办好我们的高校，必须坚持（  ），全面贯彻党的教育方针。': ['以马克思主义为指导'], '改革开放以来,我国的民族关系为（  ）。': ['汉族离不开少数民族', '少数民族离不开汉族', '各少数民族之间也相互离不开'], '《学校招收和培养国际学生管理办法》第二十九条规定，高等学校应当尊重国际学生的民族习俗和宗教信仰，但在学校内不得进行任何传教': ['正确'], '“全面贯彻党的宗教工作基本方针，坚持我国宗教的中国化方向，积极引导宗教与社会主义社会相适应。”这是党的（  ）对宗教工作的重要论述。': ['十九大'], '不属于民族团结进步“七进”的基本内容的是（  ）。': ['进家庭'], '除经政府批准设立的宗教院校外，在各级各类学校中，以下做法正确的是（）。': ['不得强迫、诱使学生信仰宗教'], '必须从（ ）战略高度把握新时代党的民族工作的历史方位。': ['中华民族伟大复兴'], '2021年中央民族工作会议指出，必须坚决维护国家主权': ['爱国主义'], '《互联网信息服务管理办法》第十五条规定，互联网信息服务提供者不得（ ）含有煽动民族仇恨': ['制作', '复制', '发布', '传播'], '根据《中华人民共和国反恐怖主义法》第八十一条规定，利用极端主义，以恐吓、骚扰等方式驱赶其他民族或者有其他信仰的人员离开居住地，情节轻微，尚不构成犯罪的，由公安机关处十五日以上三十日以下拘留，可以并处一万元以下罚款': ['错误'], '坚持我国宗教中国化方向，要求宗教界在（  ）上自觉融合。': ['文化'], '（  ）是党的宗教工作基本方针的根本方向和目的，是宗教工作的重点。': ['坚持独立自主自办原则'], '新时代西藏工作的着眼点和着力点是（ ）': ['维护祖国统一', '加强民族团结'], '正确处理涉及民族因素的矛盾纠纷要做到（  ）。': ['教育引导各族群众树立对法律的信仰，自觉按法律办事', '要增强各族群众法律意识，懂得法律面前人人平等，谁都没有超越法律的特权', '要严格区分两类不同性质的矛盾，是什么问题就按什么问题处置。不能因为当事人身份证上写着“某某民族”就犯嘀咕、绕着走，处理起来进退失据', '对极少数蓄意挑拨民族关系、破坏民族团结的犯罪分子，对搞民族分裂和暴恐活动的犯罪分子，不论什么民族出身、信仰哪种宗教，都要坚决依法打击'], '(  )是社会主义民族关系的主线。': ['团结'], '实行宗教信仰自由政策，出发点和落脚点是（  ）。': ['要最大限度把广大信教群众和不信教群众团结起来'], '根据2019年发表的《新疆的若干历史问题》白皮书，下列说法错误的是（）。': ['维吾尔族是隋唐时期突厥人的后裔'], '《中华人民共和国反恐怖主义法》第八十一条规定，利用极端主义，实施下列（  ）行为，情节轻微，尚不构成犯罪的，由公安机关处五日以上十五日以下拘留，可以并处一万元以下罚款。': ['强迫他人参加宗教活动，或者强迫他人向宗教活动场所、宗教教职人员提供财物或者劳务的', '以恐吓、骚扰等方式驱赶其他民族或者有其他信仰的人员离开居住地的', '以恐吓、骚扰等方式干涉他人与其他民族或者有其他信仰的人员交往、共同生活的', '阻碍国家机关工作人员依法执行职务的'], '要正确认识和把握宗教社会作用的（  ），最大限度发挥宗教的积极作用，最大限度抑制宗教的消极作用，因势利导': ['两重性'], '坚持我国宗教中国化方向，要求宗教界在（  ）上自觉适应。': ['社会'], '（ ）是最深层次的认同，是民族团结之根': ['文化认同'], '下列不属于党关于加强和改进民族工作的重要思想的是（ ）': ['必须坚持政教分离原则，任何宗教都没有超越宪法和法律的特权，都不能干预行政、司法和教育等国家职能的实施。'], '以下选项中符合我国宗教信仰自由政策的是（  ）。': ['我国公民有信仰宗教和不信仰宗教的自由'], '下列不属于“五爱”的基本内容的是（  ）。': ['爱集体'], '党的宗教工作基本方针是：全面贯彻党的宗教信仰自由政策，依法管理宗教事务，坚持（  ）原则，积极引导宗教与社会主义社会相适应。': ['独立自主自办'], '我国实行政教分离的原则，任何宗教都没有超越（  ）的特权，都不能干预国家行政': ['宪法和法律'], '回顾党的百年历史，党的民族工作取得的最大成就，就是走出了一条（ ）解决民族问题的正确道路': ['中国特色'], '实践充分证明，党的民族理论和方针政策是正确的，中国特色解决民族问题的道路是正确的，只有中国共产党才能实现中华民族的大团结，只有（ ）才能凝聚各民族': ['中国特色社会主义'], '习近平总书记在中央第（ ）次西藏工作座谈会上指出，要重视加强学校思想政治教育，把爱国主义精神贯穿各级各类学校教育全过程，把爱我中华的种子埋入每个青少年的心灵深处。': ['七'], '习近平总书记在第二次中央新疆工作座谈会上指出，各民族要（  ），像石榴籽那样紧紧抱在一起。': ['相互了解、相互尊重'], '构建各民族共有精神家园，要以（ ）为引领。': ['社会主义核心价值观'], '改革开放特别是党的十八大以来，我们党强调（ ）、（ ）、（ ）等理念，既一脉相承又与时俱进贯彻党的民族理论和民族政策，积累了把握民族问题、做好民族工作的宝贵经验，形成了党关于加强和改进民族工作的重要思想。': ['中华民族大家庭', '中华民族共同体', '铸牢中华民族共同体意识'], '在《中华人民共和国海关进出境印刷品及音像制品监管办法》第十二条规定中，符合下列（ ）情况的宗教印刷品、宗教音像制品和其他宗教用品不得人境': ['超出个人自用、合理数量', '危害中国国家安全', '危害社会公共利益内容'], '严禁国民教育各级各类师生在学校中穿戴宗教服饰': ['正确'], '2014年5月29日，习近平总书记在第二次中央新疆工作座谈会上指出，各族群众要（  ），像石榴籽那样紧紧抱在一起。': ['相互了解、相互尊重、相互包容、相互欣赏、相互学习、相互帮助'], '《宪法》第（  ）条规定：中华人民共和国公民有宗教信仰自由。': ['三十六'], '我国宪法第三十六条明确规定：“宗教团体和宗教事务不受（  ）的支配”。': ['外国势力'], '坚决抵御境外利用宗教进行渗透要求我们（  ）。': ['始终坚持我国宗教团体和宗教事务不受外国势力支配这一宪法原则', '要支持我国宗教独立自主办好教务，坚持中国化方向', '要规范宗教对外交流活动', '要规范互联网宗教信息服务'], '习近平总书记在十三届全国人大四次会议内蒙古代表团审议时指出，要围绕共同团结奋斗': ['汉族离不开少数民族', '少数民族离不开汉族', '各少数民族之间也相互离不开'], '新中国成立后，我们党创造性地把马克思主义民族理论同中国民族问题具体实际相结合，走出一条中国特色解决民族问题的正确道路，确立了党的民族理论和民族政策，（ ），（ ），各族人民在历史上第一次真正获得了平等的政治权利': ['把民族平等作为立国的根本原则之一', '确立了民族区域自治制度'], '宗教的消亡是事物本身矛盾运动的结果，是社会历史发展的自然过程。': ['正确'], '《刑法》第三百条规定:组织、利用会道门、邪教组织或者利用迷信破坏国家法律、行政法规实施的，情节特别严重的，处（  ）以上有期徒刑,并处罚金或者没收财产。': ['7年'], '马克思恩格斯认为宗教的根源有（  ）。': ['自然根源', '社会根源', '认识根源'], '教育法（  ）规定，国家实行教育和宗教相分离。': ['第八条'], '新时代党的治藏方略“十个必须”必须中，西藏工作的着眼点和着力点是（）': ['维护祖国统一', '加强民族团结'], '信教公民举行集体宗教活动一般应在经登记的寺院': ['其他固定宗教活动场所'], '马克思主义哲学课的一项重要内容是：要切实加强青少年的科学世界观，其中包括（  ）的宣传教育。': ['无神论'], '我国支持各宗教在保持基本信仰、核心教义、礼仪制度的同时，对教规教义作出符合当代中国发展进步要求、符合（ ）的阐释。': ['中华优秀传统文化'], '马克思认为，宗教是人的异化形式，宗教的本质就是人的本质，是“人创造了宗教，而不是宗教创造了人”。': ['正确'], '“一体”指中华民族是由56个民族组成的统一体。': ['正确'], '要积极推进（），形成共学共进的氛围和条件，避免各民族学生到了学校还是各抱各的团': ['民汉合校、混合编班'], '习近平总书记在（  ）上明确强调，共产党员要做坚定的马克思主义无神论者，严守党章规定，坚定理想信念，牢记党的宗旨，决不能在宗教中寻找自己的价值和信念。': ['全国宗教工作会议'], '2015年9月在会见基层民族团结优秀代表时，习近平总书记指出，（ ），这是全体中华儿女的共同心愿，也是全国各族人民的共同目标。': ['中华民族一家亲，同心共筑中国梦'], '(  )是社会主义民族关系的保障。': ['互助'], '马克思、恩格斯运用辩证唯物主义和历史唯物主义观察分析宗教现象和宗教问题，创立了（ ），为马克思主义政党正确认识和处理宗教问题提供了理论基础。': ['马克思主义宗教观'], '国家要（  ）对宗教事务进行管理': ['依法'], '习近平总书记在参加十三届全国人大四次会议内蒙古代表团审议时强调，要认真做好推广普及（）工作，全面推行使用国家统编教材。': ['国家通用语言文字'], '政治传统的大一统，各民族多元一体，是历史留给我们的一笔重要财富，也是我们国家的一个重要优势。': ['正确'], '我国民族关系的真实写照是汉族离不开少数民族': ['正确'], '下列说法错误的是（  ）': ['中华文化就是汉族文化。'], '根据新修订《宗教事务条例》第七十条规定，擅自组织公民出境参加宗教方面的培训': ['2万元以上20万元以下'], '新时代党的民族工作的主线是（ ）。': ['铸牢中华民族共同体意识'], '党的十八以来，民族工作的显著成绩体现在(  )。': ['各民族交往交流交融广泛拓展', '中华民族共同体意识不断增强', '平等团结互助和谐的社会主义民族关系不断巩固和发展'], '《学校招收和培养国际学生管理办法》是由教育部、外交部、公安部、司法部联合颁布的。': ['正确'], '下列属于新时代党的治疆方略内容的是（ ）。': ['坚持从战略上审视和谋划新疆工作', '坚持以凝聚人心为根本', '坚持紧贴民生推动高质量发展', '坚持加强党对新疆工作的领导'], '宗教事务管理坚持的基本原则是（  ）。': ['保护合法', '制止非法', '遏制极端', '抵御渗透'], '大汉族主义和狭隘民族主义的危害在于': ['容易产生民族歧视', '容易滋生离心倾向', '造成民族隔阂和对立', '严重的会被敌对势力利用'], '2017年6月14日，国务院常务会议审议通过了《宗教事务条例（修订草案）》,2017年8月26日，李克强总理签署国务院令公布条例，自（  ）起施行。': ['2018-2-1'], '《宪法》序言指出，维护民族团结，既要反对大汉族主义，也要反对地方民族主义。': ['正确'], '马克思认为，宗教是人的异化形式，宗教的本质是（  ）。': ['人的本质'], '“三股势力”是指（ ）': ['暴力恐怖势力', '民族分裂势力', '宗教极端势力'], '新时代新疆工作的总目标是（  ）。': ['社会稳定和长治久安'], '涉及民族因素的矛盾和问题，有不少是由于群众不懂法或者不守法酿成的。这些矛盾和问题，虽然带着“民族”字样，但不都是民族问题。': ['正确'], '《宗教事务条例》第三条规定，宗教事务管理坚持的原则是（  ）。': ['保护合法，制止非法，遏制极端，抵御渗透，打击犯罪'], '处理我国宗教关系要（  ）。': ['牢牢把握坚持党的领导、巩固党的执政地位、强化党的执政基础这个根本', '坚持政府依法对涉及国家利益和社会公共利益的宗教事务进行管理', '必须坚持政教分离', '坚持宗教不得干预行政、司法、教育等国家职能实施'], '依据《宗教事务条例》规定，下列哪项（ ）不是宗教团体、宗教院校、宗教活动场所、宗教教职人员上开展对外交往的基础。': ['互惠互利'], '习近平总书记在中央第七次西藏工作座谈会上指出，要培育和践行（ ），不断增强各族群众对伟大祖国': ['社会主义核心价值观'], '恩格斯关于宗教的发展曾提出过三种图式，下列说法错误的是（  ）。': ['从原始社会的“自发宗教”到阶级社会的“自觉宗教”'], '本民族意识要服从和服务于（ ）意识。': ['中华民族共同体'], '党的十九大把“铸牢中华民族共同体意识”写入党章”': ['正确'], '宗教工作在党和国家工作全局中具有特殊重要性，关系到（  ）。': ['中国特色社会主义事业发展', '党同人民群众的血肉联系', '社会和谐、民族团结', '国家安全和祖国统一'], '宗教信仰从本质上说属于意识形态范畴，反映的是人们精神世界的问题，是人们的一种思想认识。': ['正确'], '“大藏区”的概念根源于西藏历史': ['错误'], '我国实行宗教与教育（  ）的原则。': ['相分离'], '按照《中华人民共和国海关进出境印刷品及音像制品监管办法》规定，一切宗教类印刷品及音像制品都禁止入境。': ['错误'], '各高校利用课堂主渠道对在校学生进行马克思主义宗教观和党的宗教政策宣传教育要做到（  ）。': ['在学校德育课程、思想政治理论课中加强科学无神论教育、培养唯物主义思想认识', '把马克思主义宗教观、党的宗教政策和国家相关法律法规教育融入到人文素养和科学精神教育体系'], '实行宗教信仰自由政策，出发点和落脚点是要最大限度把广大信教和不信教群众团结起来。': ['正确'], '习近平总书记指出，积极引导宗教与社会主义社会相适应，一个重要的任务就是（  ）。': ['支持我国宗教坚持中国化方向'], '“多元”指中华民族的人口众多是多元的': ['错误'], '任何组织和个人不得在以下场所（  ）进行宗教活动。': ['学校'], '平等团结互助和谐，这是新时代我国民族团结进步事业的生动写照，也是新时代民族工作创新推进的鲜明特征。': ['错误'], '新时代党的治藏方略“十个必须”必须中，西藏经济社会发展的出发点和落脚点是（ ）': ['改善民生', '凝聚人心'], '文化认同是民族团结的（ ）': ['根脉'], '宗教极端主义一般是宗教中的某一派别。': ['错误'], '正确把握中华民族共同体意识和各民族意识的关系包括：（  ）。': ['引导各民族始终把中华民族利益放在首位', '本民族意识要服从和服务于中华民族共同体意识', '在实现好中华民族整体利益进程中实现好各民族具体利益', '反对大汉族主义和地方民族主义'], '《宪法》第（  ）条规定，各少数民族聚居的地方实行区域自治，设立自治机关，行使自治权。': ['四'], '增进共同性、尊重和包容差异性是民族工作的（）': ['重要原则'], '习近平总书记在2019年全国民族团结进步表彰大会上指出，（ ），是中华民族伟大复兴必定要实现的根本保证。': ['各族人民亲如一家'], '宪法规定:国家保护正常的宗教活动，正常的宗教活动是指（  ）。': ['在宪法、法律和政策范围内进行的宗教活动'], '国家应保护一切宗教活动。': ['错误'], '在《中外合作办学条例》中第七条规定中，（  ）不得在中国境内从事合作办学活动。': ['外国宗教组织', '外国宗教教职人员', '外国宗教院校', '外国宗教机构'], '《中华人民共和国电信条例》第六十六条规定，违反本条例（  ）的规定，构成犯罪的，依法追究刑事责任；尚不构成犯罪的，由公安机关': ['第五十六、五十七条'], '习近平总书记鲜明提出（  ），这是我们党关于宗教工作理论的系统总结和重大创新，是中国特色社会主义理论体系的“宗教篇”。': ['中国特色社会主义宗教理论'], '下列（  ）不是社会主义核心价值观的内容。': ['爱国', '诚信', '敬业'], '依法对宗教事务进行管理，是世界大多数国家的通行做法，也是引导宗教与社会主义社会相适应的必由之路。': ['正确'], '下列关于民族区域自治制度的说法正确的是（  ）。': ['是我国解决民族问题的基本政策'], '关于中华民族各民族之间的关系，下列说法正确的是(  )。': ['中华民族各民族是一荣俱荣、一损俱损的命运共同体', '你中有我、我中有你、谁也离不开谁的多元一体格局是在历史发展中逐步形成的', '中华民族和各民族的关系是一个大家庭和家庭成员的关系', '各民族之间的关系是一个大家庭里不同成员的关系'], '信仰宗教的党员，经组织教育仍然没有转变，应当（  ）。': ['劝其退党'], '《宗教事务条例》第四十七条规定，从事互联网宗教信息服务，应当经(   )以上人民政府宗教事务部门审核同意后，按照国家互联网信息服务管理有关规定办理。': ['省级'], '下列说法错误的是（  ）。': ['公民不能信仰宗教'], '（  ）是中国特色解决民族问题的正确道路的重要内容和制度保障': ['民族区域自治制度'], '下列关于中华民族多元一体格局中，多元与一体的关系不正确的是（  ）。': ['一体是要素和动力'], '中华民族是多元一体的大家庭，是在长期历史演进中形成的（）。': ['命运共同体'], '《宪法》第三十六条规定，中华人民共和国公民有宗教信仰自由。': ['正确'], '正常的宗教活动主要有两层含义：一是宗教活动要在（  ）允许的范围内进行；二是宗教活动要严格按照宗教教义': ['法律、法规'], '根据《宗教事务条例》第四十一条规定，下列地点中（  ）不得组织、举行宗教活动的是。': ['高等院校'], '目前，全国共建立了156个民族区域自治地方，其中包括（  ）自治区': ['5个'], '民族团结是我国各族人民的生命线，各民族共同团结进步': ['民族团结是实现各民族繁荣的前提条件，是中华民族伟大复兴的保证', '民族团结有利于维护国家统一和领土完整'], '我国是统一的多民族国家，（ ）是各族人民的生命线': ['民族团结'], '在《刑法》第三百条规定，组织利用会道门、邪教组织或者利用迷信破坏国家法律、行政法规实施的，关于处罚下列说法错误的是（  ）。': ['处三年以上七年以下有期徒刑，并处罚金'], '2021年中央民族工作会议提出，必须促进各民族（ ）（ ）（ ），促进各民族在理想': ['交往', '交流', '交融'], '《宪法》第二十四条规定，国家通过普及（  ），在城乡不同范围的群众中制定和执行各种守则': ['理想教育', '道德教育', '文化教育', '纪律和法制教育'], '习近平总书记在全国民族团结进步表彰大会上指出，各民族在文化上要（ ）': ['相互尊重', '相互欣赏', '相互学习', '相互借鉴'], '党员不能信仰宗教，但可以参加宗教活动': ['正确', '错误'], '关于抵御利用宗教对学校进行渗透和防范校园传教的意义，下列说法不正确的是（  ）。': ['关系到教育与宗教关系的和谐'], '宗教极端主义的危害在于(  )。': ['将宗教的教义绝对化', '以歪曲宗教教义或者其他方法煽动仇恨、煽动歧视、鼓吹暴力', '其本质反人类、反社会、反文明，是对宗教的恶意歪曲利用', '具有欺骗性和煽动性，诱惑、误导一些不明真相的人从事暴力恐怖活动'], '依法管理宗教事务的要旨是保护合法、制止非法、遏制极端、抵御渗透、打击犯罪': ['正确'], '新时代党的民族工作的重要任务是（ ）。': ['推动各民族为全面建设社会主义现代化共同奋斗'], '宗教极端主义在本质上（ ）': ['反人类', '反社会', '反文明', '反科学'], '习近平总书记在2021年中央民族工作会议上指出，要正确把握物质和精神的关系，要赋予所有改革发展（ ），（ ），（ ），让中华民族共同体牢不可破。': ['以彰显中华民族共同体意识的意义', '以维护统一、反对分裂的意义', '以改善民生、凝聚人心的意义'], '习近平总书记在第三次中央新疆工作座谈会上强调，要加强（ ）': ['中华民族共同体历史', '中华民族多元一体格局'], '坚持我国宗教中国化方向，是积极引导宗教与社会主义社会相适应的必然要求，也是我国宗教发展的必由之路。': ['正确'], '民族分裂势力企图破坏民族团结，极个别民族地区发生民族隔阂的现象，这是支流，不是主流': ['正确'], '民族习俗从本质上说属于意识形态范畴，反映的是人们精神世界的问题，是人们的一种思想认识。宗教信仰属于某种社会群体的行为方式和生活方式。': ['错误'], '习近平总书记在全国民族团结进步表彰大会上指出，我们要全面贯彻党的（ ）和（ ），坚持共同团结奋斗': ['民族理论', '民族政策'], '2014年4月，习近平总书记考察新疆时强调，要把民族团结紧紧抓在手上，坚持正确的祖国观': ['和睦相处、和衷共济、和谐发展'], '宗教必须在宪法和法律规定的权利和义务范围内活动，任何人不得利用宗教反对党的领导和社会主义制度，宗教活动不得妨碍社会秩序和生活秩序。': ['正确'], '宗教对于国家来说是私人的事情，实行政教分离，宗教信仰自由政策；宗教对于工人阶级政党来说，也是个人的私事。': ['错误'], '宪法第（ ）条规定，中华人民共和国公民有维护国家统一和全国各民族团结的义务。': ['五十二'], '关于“大藏区”的表述，以下说法正确的是（  ）。': ['“大藏区”纯属虚构，不符合中国历史和国情', '“大藏区”是典型的极端民族主义和种族主义的表现', '“大藏区”是西方殖民者侵略中国、企图分裂中国的产物', ' 按照十四世达赖集团的假想，“大藏区”总面积超过中国国土面积的四分之一'], '《教育法》第八条规定，国家实行教育与宗教相分离。任何组织和个人不得利用宗教进行妨碍国家教育制度的活动。': ['正确'], '我国宗教工作形势总体向好，表现在（  ）。': ['党的宗教工作基本方针得到贯彻', '宗教工作法治化明显加强', '党同宗教界的爱国统一战线不断巩固', '宗教活动总体平稳有序'], '习近平总书记在全国民族团结进步表彰大会上指出，要把民族团结进步创建全面深入持久开展起来，创新方式载体，推动进机关': ['乡镇', '学校', '宗教活动场所'], '要加强向干部群众和青少年进行辩证唯物主义和历史唯物主义的科学世界观的教育，宣传（  ），加强有关自然现象': ['宗教知识'], '党的十九大对民族工作的重要论述包括(  )。': ['全面贯彻党的民族政策', '深化民族团结进步教育', '铸牢中华民族共同体意识', '坚决反对一切分裂祖国、破坏民族团结和社会和谐稳定的行为'], '《宪法》中关于民族关系的规定包括（  ）。': ['中华人民共和国是全国各族人民共同缔造的统一的多民族国家', '中华人民共和国各民族一律平等', '禁止对任何民族的歧视和压迫，禁止破坏民族团结和制造民族分裂的行为'], '(  )是积极引导宗教与社会主义社会相适应的必然要求，也是我国宗教发展的必由之路。': ['坚持我国宗教中国化方向'], '（ ）是习近平总书记关于民族工作的重大原创性论断，是新时代党的民族工作的主线。': ['铸牢中华民族共同体意识'], '以下叙述不正确的是（  ）。': ['国家保护所有的宗教活动'], '习近平总书记在参加十三届全国人大四次会议内蒙古代表团审议时指出，要在各族干部群众中深入开展中华民族共同体意识教育，特别是要从青少年教育抓起，引导广大干部群众全面理解党的民族政策，树立正确的（ ）': ['国家观', '历史观', '文化观'], '假冒宗教教职人员进行宗教活动的，由宗教事务部门责令（  ），有违法所得的，没收违法所得;有违反治安管理行为的，依法给予治安管理处罚;构成犯罪的，依法追究刑事责任。': ['停止活动 '], '习近平总书记在第三次中央新疆工作座谈会上强调，要促进各民族（ ）': ['广泛交往', '全面交流', '深度交融'], '宗教信仰自由等于宗教活动可以不受任何约束。': ['错误'], '在《网络出版服务管理规定》第二十四条规定中，网络出版物不得含有以下（  ）内容。': ['反对宪法确定的基本原则的', '危害国家统一、主权和领土完整的', '宣扬邪教、迷信的', '侮辱或者诽谤他人，侵害他人合法权益的'], '宗教信仰从本质上说属于意识形态范畴，反映的是人们（  ）的问题，是人们的一种思想认识。': [' 精神世界'], '中国特色社会主义宗教理论，以（  ）为指导，对我国社会主义特别是初级阶段的宗教进行理论阐述，分析宗教在我国社会主义时期的特征和作用，明确党和国家在社会主义条件下处理宗教问题的方针政策。': ['马克思主义'], '多民族大一统格局是我国自（  ）以来就基本形成的历史传统和独特优势': ['秦汉'], '对中华民族共同体的认识。下列说法正确的是（ ）': ['各民族交融汇聚成多元一体中华民族', '各民族共同缔造、发展、巩固统一的伟大祖国', '中华民族多元一体是先人们留给我们的丰厚遗产', '中华民族多元一体是我国发展的巨大优势'], '下列不属于宗教产生的根源的是（  ）。': ['文化根源'], '习近平总书记在全国民族团结进步表彰大会强调，（ ）和（ ）都是民族团结的大敌，要坚决反对。': ['大汉族主义', '地方民族主义'], '自成立起，中国共产党就积极探索适合我国国情的解决民族问题的道路。': ['正确'], '坚持我国宗教中国化方向，要求宗教界在（  ）上自觉认同；坚持我国宗教中国化方向，要求宗教界在（  ）上自觉融合；坚持我国宗教中国化方向，要求宗教界在（  ）上自觉适应。': ['政治'], '邪教的本质及危害性是（  ）。': ['反人类', '反科学', '反社会'], '下列行为中（  ）违反《宗教事务条例》。': ['基督教信徒在路边散发宗教传单', '某寺院参加赈灾活动并向灾民宣讲佛法', '学生在学校组织佛学社团'], '坚持我国宗教中国化方向，要求宗教界在（  ）上自觉认同。': ['政治'], '新时代党的民族工作的出发点和落脚点是': ['实现中华民族伟大复兴'], '中央第七次西藏工作座谈会提出，要培育和践行社会主义核心价值观，不断增强各族群众对伟大祖国、中华民族、中华文化、中国共产党、中国特色社会主义的认同。': ['正确'], '《宗教事务条例》第五十六条规定，宗教团体': ['正确', '错误'], '习近平总书记在第三次中央新疆工作座谈会上指出，新疆自古以来就是（ ），新疆各民族是中华民族血脉相连的家庭成员。': ['多民族聚居地区'], '下列不属于党的十九大对民族工作的重要论述的是（  ）。': ['同心共筑中国梦'], '共产党员和 （  ）不能信仰宗教': ['共青团员'], '下列有关新疆的说法不正确的是（  ）。': ['新疆地区各族居民历史上一直信仰伊斯兰教'], '关于邪教的危害，以下说法错误的是（  ）。': ['精神寄托'], '2017年9月召开的新疆若干历史问题研究座谈会,明确阐明（  ）。': ['新疆是我国领土不可分割的一部分，多民族大一统格局是我国自秦汉以来就基本形成的历史传统和独特优势', '新疆各民族是中华民族血脉相连的家庭成员，实现中华民族伟大复兴的中国梦是各族人民的共同利益', '新疆各民族文化扎根于中华文明沃土，是中华文化不可分割的一部分', '新疆是多种宗教并存地区，促进宗教关系和谐是新疆稳定繁荣的历史经验等等'], '铸牢中华民族共同体意识要从孩子抓起，青少年首先要知道自己是中华民族，树立中华民族一员的意识，不能只知道自己是哪个民族的人。': ['正确'], '习近平总书记在中央第七次西藏工作座谈会上指出，要挖掘、整理、宣传西藏自古以来各民族交往交流交融的历史事实，引导各族群众看到民族的走向和未来，深刻认识到': ['中华民族是命运共同体'], '坚持和发展中国特色社会主义宗教理论要做到（  ）。': ['辩证看待我国宗教的社会作用', '坚持我国宗教中国化方向', '构建积极健康的宗教关系', '提高宗教工作法治化水平'], '“六个相互”是习近平总书记在第一次中央新疆工作座谈会上提出的': ['错误'], '按照中央民族工作会议精神，坚持依法治理民族事务，做到法律面前人人平等，就要做到（ ），（ ），（ ）。': ['依法保障各族群众合法权益', '依法妥善处理涉民族因素的案事件', '依法打击各类违法犯罪行为'], '党的十九大把（  ）写入党章，成为全党全国各族人民实现中国梦新征程上的共同意志和根本遵循。': ['铸牢中华民族共同体意识'], '2021年中央民族工作会议指出，必须坚持正确的中华民族历史观，增强对中华民族的（ ）和（ ）。': ['认同感', '自豪感'], '我国实行（  ）的原则，任何宗教都没有超越宪法和法律的特权，都不能干预国家行政': ['宗教自由'], '“四个共同”是指我国（  ）。': ['辽阔的疆域是各民族共同开拓的', '悠久的历史是各民族共同书写的', '灿烂的文化是各民族共同创造的', '伟大的精神是各民族共同培育的。'], '依《宗教事务条例》第四十八条规定，互联网宗教信息服务的内容应当符合（  ）的相关规定': ['有关法律', '有关法规', '宗教事务管理'], '党的宗教工作基本方针是（  ）。': ['全面贯彻党的宗教信仰自由政策', '依法管理宗教事务', '坚持独立自主自办原则', '积极引导宗教与社会主义社会相适应'], '中国宗教的特征是（  ）。': ['长期性、群众性、民族性、国际性、复杂性'], '党的十九大报告指出：“全面贯彻党的民族政策，深化民族团结进步教育，铸牢中华民族共同体意识，加强各民族（  ），促进各民族像石榴籽一样紧紧抱在一起，共同团结奋斗': ['交往交流交融'], '《中华人民共和国海关进出境印刷品及音像制品监管办法》规定，个人携带、邮寄进境的宗教类出版物及印刷品，在自用、合理范围内的数量不超过（  ），是可以进境的。': ['3本'], '必须坚持（ ），推进民族事务治理体系和治理能力现代化。': ['依法治理民族事务'], '以下说法不正确的是（  ）。': ['在校学生可以参加宗教组织和教徒在宗教场所以外的地方进行的宗教活动'], '《教育法》第九条规定，公民除宗教信仰外不分民族': ['错误'], '根据《宗教事务条例》有关规定，任何组织或者个人不得利用宗教进行（  ）等违法活动。': ['危害国家安全', '破坏社会秩序', '损害公民身体健康', '妨碍国家教育制度'], '做好民族工作要正确把握（ ）。': ['共同性和差异性的关系', '中华民族共同体意识和各民族意识的关系', '中华文化和各民族文化的关系', '物质和精神的关系'], '在恩格斯提出的宗教发展和宗教历史形态图示中，宗教经历了从原始社会的（  ）到阶级社会的（  ）的发展过程。': ['自发宗教、人为宗教'], '封建迷信和宗教信仰的区别在于（  ）。': ['宗教是依法成立的社会组织'], '全面正确地贯彻宗教信仰自由政策包含有（  ）两个方面的内容。': ['要求尊重每个公民信仰宗教的自由和不信仰宗教的自由', '要求权利与义务的统一'], '《宪法》第三十六条规定，中华人民共和国公民有宗教信仰自由，任何国家机关': ['个人'], '信教公民举行集体宗教活动一般应在经登记的宗教活动场所内举行，下列（  ）属于违法宗教活动处所。': ['信教学生宿舍'], '在社会主义条件下，信教群众与不信教群众在政治上、经济上的根本利益是一致的，都是我们党执政的重要基础，都是建设中国特色社会主义的重要力量。': ['正确'], '（  ）在《反杜林论》中指出：“一切宗教都不过是支配着人们日常生活的外部力量在人们头脑中的幻想的反映，在这种反映中，人间的力量采取了超人间的力量的形式。”': ['恩格斯'], '宗教在社会主义社会将（  ）。': ['长期存在'], '铸牢中华民族共同体意识，就是要引导各族人民牢固树立（ ）': ['休戚与共', '荣辱与共', '生死与共', '命运与共'], '中华民族主要分布在(  )。': ['中国大陆'], '高校在教育教学过程中，要发挥课堂主渠道作用，在学校德育课程': ['无神论'], '科学无神论的教育，并不仅仅限于单纯否定神灵的存在。它的最主要的内容是（  ），还包括（  ）和（  ）。': ['运用马克思主义的科学世界观认识宗教的本质及其发展规律', '自然科学知识的普及，社会进化', '人的生老病死、吉凶祸福的科学文化和社会科学知识的宣传'], '关于如何区分邪教和宗教，下列说法错误的是（  ）。': ['看看宗教领袖是谁'], '实现中华民族伟大复兴的中国梦，就要以铸牢中华民族共同体意识为主线，把（ ）作为基础性事业抓紧抓好。': ['民族团结进步事业'], '下列（  ）不是“五个认同”的内容。': ['无神论'], '马克思主义对宗教的批判的目的是要（ ）。': ['废除作为人们幻想的幸福的宗教，也就是要求实现人民的现实的幸福'], '下列关于依法管理宗教事务的说法，正确的是（ )。': ['依法进行管理，就是要切实保障宗教信仰自由，保证正常宗教活动的有序进行，保护宗教团体的合法权益。', '依法管理宗教事务的要旨是保护合法、制止非法、遏制极端、抵御渗透、打击犯罪。', '依法管理宗教事务，要规范那些以“宗教信仰自由”为借口，违背宪法、法律和政策的事情，防止和制止不法分子利用宗教活动制造混乱，违法犯罪，以及境外敌对势力的渗透活动。'], '我国的民族区域自治是指在国家的统一领导下，各少数民族聚居地方实行区域自治，设立（ ），行使（ ）。': ['自治机关', '自治权'], '《宪法》序言指出，中华人民共和国是全国各族人民共同缔造的统一的多民族国家。（  ）的社会主义民族关系已经确立，并将继续加强。': ['平等团结互助和谐'], '我国某地一寺庙佛门弟子积极参加当地架桥修路、捐资助学等活动，方丈还以80万元巨资买到了电视台黄金时段前15秒公益广告权，宣传保护野生动物和禁止毒品。以上事实说明，在我国（ ）。': ['信教群众与不信教群众的根本利益是一致的']}
def simpleMatching(title,tiku,option):
    num = 1
    dataList = []
    checkList = {}
    #一个标题可能搜到多个答案，进行相似度比对
    like = 0
    for i in tiku:
        like = fuzz.ratio(title, i)
        #题目相似度
        if like >68:
            #如果遇到题目相似，答案不同。  做相似度对比 取最大相似度对应的信息，
            #例如遇到题目为：下面说法正确的是:()。
            # 这样的就需要再写逻辑进行对比 比如选项模糊匹配累计相似度
            #即答案与答案匹配，有时间再写吧
            checkList[i] = like
        else:
            pass
    try:
        #一个题目匹配到多个答案就检查答案存在否
        for oo in checkList:
            checkAns = tiku[oo]
            if checkAns[0] in option:
                return [oo, like, checkAns]
        # checkedTitle = max(checkList, key=checkList.get)
    except:
        pass

#数据对撞
def dataCollision(ansList,quesList):
    if len(ansList) > 1:
        rightList = dataCollision2(ansList,quesList)
        return ','.join(set(rightList))
    elif len(ansList) == 1:
        rightList = dataCollision1(ansList,quesList)
        return ','.join(set(rightList))
    else:
        print("答案选择器出错")
#单选
def dataCollision1(ansList,quesList):
    num = 1
    rightKeyList = []
    for i in ansList:
        contrastList = {}
        for o in quesList:
            like = fuzz.ratio(i, o)
            if like > 68:
                index = quesList.index(str(o))
                rightKey = str(index+1).replace('1','A').replace('2','B').replace('3','C').replace('4','D')
                contrastList[str(i)+f'&&&{rightKey}&&&'+str(o)] = like
            else:
                pass
        num+=1
        try:
            a = max(contrastList,key = contrastList.get)
            rightKey = a.split("&&&")[1]
            rightKeyList.append(rightKey)
        except:
            pass

    return rightKeyList
#多选
def dataCollision2(ansList,quesList):
    num = 1
    rightKeyList = []
    for i in ansList:
        for o in quesList:
            like = fuzz.ratio(i, o)
            if like > 68:
                rightKey = str(num).replace('1','A').replace('2','B').replace('3','C').replace('4','D')
                rightKeyList.append(rightKey)
            else:
                pass
        num+=1
    return rightKeyList





