# Syrup and the Ultimate Sweet 视觉观察与生图规范

观察日期：2026-10-17。本文依据官方 itch.io 的五张公开游戏截图、封面，以及 `analysis/reference/unpacked/game/images`、`gui` 内原图的只读观察。已经用 `view_image` 查看全部背景、全部 35 张 `sb` 插画、主要角色各服装状态、主要 GUI、所有 concept/extra 图集；不是仅依据搜索摘要。本文描述外观与素材结构，不复制剧情文本。

## 1. 总体结论

需要统一的是三种相互配合的视觉语言，而不是把所有图片都画成同一种精细插画：

1. **角色立绘**：约 3–3.5 头身的可爱卡通，粗黑圆润外轮廓、大眼、小嘴、明显剪影，纯色块和一层清晰赛璐璐阴影。头发有两三个白色圆点高光。站姿大多正面或轻微 3/4，表情夸张，躯体结构简化。透明底，不能带场景。
2. **场景背景**：淡彩的简化室内/街景线稿，使用背景主色的较深同色线条，不用角色那样粗黑的边。大量背景只用两三种颜色，几何形的大块斜切光照，几乎没有材质渲染和景深。场景细节可识别，但饱和度、对比度低于角色。
3. **故事书 CG**：竖椭圆 vignette，纯色块、几何形轮廓、细节很少，多数不画粗黑边；人物比例可以更小、更简化。它们是用于故事书左半页的插画，不是全屏写实 CG。

画布统计已核实：背景 17 张均为 1280×720；`sb` 插画 35 张均为 640×720 RGBA；大多数角色槽位 621×673，Toffee 606×657。角色槽位总计 151：Syrup 40、Gumdrop 长发 29 / 短发 13、Pastille 16、Butterscotch 37、Toffee 8、Chocolate 双人 2、Treat 3、Wolf 3。

建议生图共同基础描述：

> Whimsical candy-fantasy visual novel art, compact chibi proportions, round expressive faces, large simple oval eyes, very clean bold rounded outlines for characters, flat pastel color blocks with one crisp cel-shadow layer, a few round white highlights on hair, readable silhouettes, playful hand-drawn charm, simple shapes, no photorealism, no 3D rendering, no painterly textures, no text or watermark.

背景和故事书插画要覆盖上述 character outline 条款，分别使用下面的专用规范。配色名称是肉眼观察；下述十六进制色值若用作提示词应视为近似方向，最终以新主设定图为准。

## 2. 主要角色：已观察外观

| 角色 / 文件前缀 | 造型和配色 | 必须保持的识别点 | 服装/状态分组建议 |
|---|---|---|---|
| Syrup / `sy` | 棕色皮肤，明亮蓝眼；薄荷绿长侧刘海、同色长侧马尾，一侧短剃发；蓝色透明护目镜置于头顶；黑小方耳饰；白色长实验服，灰蓝背心、深色裤装；常含或拿蓝色棒棒糖 | 不对称薄荷发型、护目镜、白大褂、略冷淡/自信表情 | 常规大褂；灰蓝毛绒连帽厚外套；卸下厚外套仍戴护目镜的大褂状态；水晶球手持状态。表情包含抱臂、思考、指向、怒吼、得意、害羞、感谢等 |
| Gumdrop / `gum`、`gums` | 莓粉色皮肤、草莓粉长发，发尾偏奶白/极浅粉；两侧红白旋纹薄荷糖圆发饰，粉色大椭圆眼、圆形螺旋腮红；白衬衫、粉色围裙、深巧克力色裙摆、粉糖果领结 | 全身糖果配色、薄荷糖双发饰、粉肤、螺旋腮红 | 长发着制服；长发无制服的简化糖果身体；短发着制服；受损/破裂；冻结/沉默；玩偶姿态。原图的糖果身体是平滑符号形，没有写实解剖细节。新图可用同色无接缝糖果连体造型保持含义 |
| Pastille / `pas` | 浅肤、粉色蓬松短发、金黄眼；白色三角头巾，白衬衫、粉围裙和糖果领结；常拿长扫帚，表情温和或紧张 | 粉短发、白头巾、粉围裙、扫帚、金眼；角色是男生，不应因服装误标成女仆少女 | 糖果店制服＋扫帚；粉色毛线护耳帽、粉白厚外套、围巾/手套的冬装；少量不同手势 |
| Butterscotch / `bs` | 浅肤、橙色平刘海和两条短辫、鼻侧雀斑、橙红色眼；巨大深紫软尖巫师帽，帽尖歪折，帽冠有两道像眼睛的深色竖缝；紫色披肩、蝴蝶结、长裙、深色鞋 | 巨帽构成最宽剪影、橙辫、雀斑、紫黑服装 | 常规巫师装；帽檐覆雪/冻得发抖；披借来的灰蓝毛绒大衣；施法动作；鼓腮/吃糖/陶醉/哭泣。表情幅度较大，眼睛有时变成小圆点 |
| Toffee / `tof` | 棕肤、金黄色猫眼、黑/深巧克力色蓬松乱短发；头顶尖猫耳、长大猫尾；黑色无袖连衣造型和深色短裤/裙摆；大金铃黑项圈、手腕小铃，猫爪手势 | 猫耳、长尾、金铃、金眼、调皮懒散神态 | 常规一套服装；歪头、抱爪、惊讶、偷笑、害羞、思考等。不要将其尾巴画成细绳 |
| Dark Chocolate + Milk Chocolate / `choco` | 同一透明双人图中并立、棕肤、深色大眼。Dark 是深棕/黑发、黑色燕尾礼服和迷你黑礼帽；Milk 是白灰色头发向一侧翘、棕色礼服和迷你棕帽；白衬衫、领结、金色腰封，Milk 的帽子还可装花 | 一黑一白头发对照，迷你礼帽、礼服、并排相近身高；**黑发 Dark / 白发 Milk** 已由 concept 图标签核实 | 双人寒暄；双人送花/帽中花。保持两个角色在同一槽位内 |
| Treat / `treat` | 浅灰/白色毛发和长狼耳，金色眼；灰蓝大衣，白毛绒领、袖口、下摆，毛球扣；深色裤袜、靴子，帽子有白色毛绒帽檐和护耳；有尾巴 | 白灰狼耳与尾、寒冷地区毛绒衣装 | 常规、淡然、担心三表情 |
| Wolf / `wolf` | 非人形的圆润狼头/肩部剪影，夸张长嘴、小椭圆黑眼、尖耳、锯齿状毛边，灰白色毛发；另有粉色染色版 | 它与 Treat 的人形立绘不同，属于动物头像式轮廓 | 灰白原色；粉色版；粉色神态变体 |

所有表达槽位可以使用精灵图集，但应按「角色 × 服装/发型状态」建立图集，不要仅按人名混合。每格都需要一致的头部大小、脚/腰基线和透明留边。先固定一张主设定，再派生表情；不要让图集自动重新设计服装和发型。

## 3. 全部背景：17 槽

背景通用提示词应采用：

> Simplified 2D candy-fantasy visual novel background, monochrome colored line art on a pale pastel base, two or three flat color families, a large diagonal shaft of light, clean slightly whimsical perspective, sparse texture, low contrast, no people, no foreground character, clear central staging area, 16:9.

| 原文件名 | 已观察地点 / 画面 | 主色与关系 |
|---|---|---|
| `bg black.png` | 纯深蓝灰过场底 | 单一深蓝灰；可用确定性纯色重建 |
| `bg cabin.jpg` | 木屋室内，左壁炉、中央窗、窗旁摇椅、右门/木柜 | 冰冷灰青，较深灰青细线；斜块光 |
| `bg cottage.jpg` | 林间圆润小女巫屋外景，门两侧圆窗、烟囱、花草和树篱 | 薄荷青天空/树、奶黄前景，明亮对角光 |
| `bg cottagedoor.jpg` | 同小屋的拱形门近景，右侧巨大门框、左侧小窗和植物 | 奶黄与薄荷青，亮区在右侧 |
| `bg cottageint.jpg` | 温暖女巫屋内，大锅炉/坩埚、左凳、中央书架、右侧回旋楼梯、墙上海报 | 杏橙与奶油黄，棕橙线稿 |
| `bg icecave.jpg` | 冰洞内狭长通道，大量垂挂冰棱，深处留白 | 极浅青与白、冰蓝线稿 |
| `bg icecave2.jpg` | 更宽冰洞、中央一棵结晶样树/枝状冰体、地面浅水或裂纹 | 薰衣草紫和浅冰蓝 |
| `bg lab.png` | 糖果实验室，左上储物柜、中央长工作桌和试管烧瓶、凳子、右侧白板与箱子 | 浅紫/粉紫，斜切光照 |
| `bg library.jpg` | 图书馆四周高书架、满架书籍、中央低书桌 | 奶油黄、浅驼棕，背景整体暖色 |
| `bg market.jpg` | 魔法小镇露天集市、左右遮棚、石板路、简化顾客白色剪影 | 粉紫/薰衣草紫，顾客保留符号剪影 |
| `bg mountain.jpg` | 从冰洞或峡口望向雪山远景；前景左右冰刺框景 | 极浅冰蓝/白 |
| `bg nightcottage.jpg` | 与 cottage 构图同源的夜间小屋外景 | 深蓝青、极低亮度 |
| `bg nightshop.jpg` | 与 shop 构图同源的夜间糖果店内 | 靛蓝/深紫，低亮度 |
| `bg shop.jpg` | 糖果店内，前景左右玻璃糖果柜、后方收银台、墙上海报、货架 | 极浅粉/白，桃粉线稿 |
| `bg shop2.jpg` | 与 shop 同构图的暖色糖果店内 | 焦糖/杏黄/米黄，棕橙线稿 |
| `bg shopext.jpg` | 糖果店外近景，门在右，左边窗/墙海报，右窗能见糖果，石板门前路 | 蜜桃粉/奶黄，斜切光 |
| `bg snow.jpg` | 空旷雪原、远处雪丘和小冰岩、低矮云层 | 白与淡蓝，线稿极简 |

构图同源的 day/night、shop/shop2 应从同一张新底图派生调色，避免几何关系漂移。`icecave` 和 `icecave2` 是不同构图，不只是调色。

## 4. 全部故事书 CG：35 槽

共同画面规律：竖椭圆透明图框；人物和场景采用无纹理的色块剪纸感；曲线和少量棱角混合；主体被完整放在椭圆里；外部透明。以书页布局展示，周围不要自动添加文字或额外厚边框。

专用提示词：

> A vertical oval storybook vignette on a transparent canvas, whimsical candy fantasy, very simple flat geometric cut-paper color shapes, minimal line work, soft pastel palette, simplified tiny chibi characters with readable silhouettes, limited details, all scenery clipped inside one clean upright oval, no words, no captions, no rectangular background.

下表的主题均来自已看过的缩略图；事件因果和正式结局名称不在此推断。`working/working2` 等画面差异很小的双槽仍要保留槽位。

| 分组 | 原文件槽位 | 可见画面 / 生图主题 |
|---|---|---|
| 小镇与店铺建立镜头 | `sb shop.png` | 暖桃粉小糖果屋外景，窗、拱门、小糖果招牌 |
| 夜间空店 | `sb badend1.png` | 深蓝紫夜色糖果屋正面，窗几乎无光 |
| 夜间寻找 | `sb search.png` | Syrup 和 Pastille 持扫帚/篮子走过月亮下的紫蓝小镇 |
| 独自归家 | `sb homealone.png` | 紫粉色小镇街道，Syrup 独自走过 |
| 结伴归家 | `sb hometogether.png` | 与 homealone 同一小镇构图，多出 Gumdrop 结伴 |
| 睡眠/醒来双槽 | `sb sleep.png`, `sb unsleep.png` | Syrup 斜躺床上，薄荷发铺开、白被、周边糖果；两张的眼睛状态不同 |
| 店内工作双槽 | `sb working.png`, `sb working2.png` | Syrup 在实验桌左侧，发光的 Gumdrop 在右侧，浅紫底；小表情/姿势变化 |
| 修复糖果女孩 | `sb fixd.png` | Syrup 面向坐在工作台边的 Gumdrop，近距离照顾/修复动作 |
| 新助手双槽 | `sb newassistant.png`, `sb newassistant2.png` | Gumdrop 着粉围裙站在中央，后方金黄人形剪影/欢呼形状，两张小差异 |
| 糖果女孩暗影双槽 | `sb eatenaway1.png`, `sb eatenaway2.png` | 同一个女孩轮廓；一张只剩深色剪影，一张能见粉肤与短发围裙；酒红暗底 |
| 糖果残余 | `sb candibal.png` | 灰暗椭圆中红白旋纹糖果碎块；原画无写实血肉 |
| 对峙/孤影 | `sb badend2.png` | 深紫灰地平线上小小单人剪影，简化横向风/光形状 |
| 被聚光的柜台 | `sb counter.png` | 深蓝舞台感空间，一束浅紫聚光灯照向柜台后小剪影 |
| 雪原攀登 | `sb climb.png` | Syrup 与 Butterscotch 在雪坡前行，浅紫天和白云/雪点 |
| 雪原相遇 | `sb hitreat.png` | 左侧 Toffee、中央远处 Syrup，右侧树林边 Treat 的雪地相遇 |
| 雪地告别 | `sb byetreat.png` | 队伍在深蓝灰雪地小屋/树林前告别，数个人物并排 |
| 冰洞冻结 | `sb frozen.png` | 巨大冰棱深处，小小 Syrup 与 Butterscotch 在左右下角；冷深青蓝 |
| 冰洞返回 | `sb happyreturn.png` | 青蓝椭圆通道、中央白色亮出口，极少人物细节 |
| 冰崩逃离双槽 | `sb escape.png`, `sb escape2.png` | 大片白色冰雪、深蓝三角冰刺、左下小人物向外逃离；两张小差异 |
| 特殊食材 | `sb creamilla.png` | 冰蓝色枝叶植物，像透明糖霜叶片/白色缎带缠绕枝条 |
| 终极甜点 | `sb ultimatesweet.png` | 青绿色高脚玻璃杯、巨大金黄奶油层、顶上红樱桃、蓝紫光底 |
| Syrup 成就插画 | `sb syrupend.png` | Syrup 戴夸张王冠和眼镜，背景绿色飞散纸币，兴奋得意姿态 |
| Gumdrop 结伴插画 | `sb gumend.png` | Syrup 和 Gumdrop 在夕阳草地/篱笆前牵手或并肩，粉橙天空 |
| Butterscotch 插画 | `sb bsend.png` | 巨帽女巫站在右前方，Syrup 在左后，暖金黄炼锅/碗形前景 |
| Pastille 插画 | `sb pasend.png` | Pastille 戴尖巫师帽在空中，Syrup 位于下方；蓝粉云、飞鸟/蝙蝠剪影 |
| Toffee 插画 | `sb tofend.png` | Syrup 与 Toffee 近距离同框，粉色圆形背景，猫耳和金铃突出 |
| 猫咪占据画面 | `sb cattakeover.png` | 深紫色 Toffee 轮廓置于紫红底，周围橙色糖果/小符号 |
| 夜间挥手 | `sb byetoffee.png` | Syrup 在左前方挥手，远处右侧 Toffee，深青星空与弯曲小路 |
| 黑暗心形 | `sb worstend.png` | 深蓝黑椭圆、女孩全黑剪影、胸前一颗明亮冰蓝心 |
| 锁定占位 | `sb locked.png` | 浅粉椭圆与中央酒红色挂锁；可确定性绘制以保证清晰 |

## 5. GUI、主菜单、特效与图鉴

### GUI 已观察

- 主菜单底为极浅薰衣草紫，底沿有紫色魔法小镇剪影；顶部细白横线。标题是白底黑描边的手绘气泡字。新标题文字建议在代码层排版，避免生图拼写错误。
- 五位主角在主菜单使用更小的 Q 版半身/全身卡片，存在普通/变化两态 `mm*` 图，每张 240×390 左右。其角色设计要与立绘一致。
- 对话框是横向超宽奶白半透明圆角框，两侧糖果包装扭结，桃粉双描边；名字牌是独立的小圆角白牌，粉色边。对白字体是粗圆手绘体，外描边、颜色随说话者变化。下沿快捷菜单也是深莓粉圆体字。
- 选择项也是白底粉框圆角胶囊，hover 改金黄色外框，不用强烈立体投影。
- 设置/存读档页底为浅奶油黄，四周金黄色糖果/叶子/螺旋图案装饰。存档格为粉白圆角小卡，中间包装糖果剪影，hover 轻微切换粉白层次。
- 确认框使用酒红边和粉色内填充。通知条是桃粉色细线加一侧小糖果卷草。
- 勾选、单选、滑块、滚动条和 console 按键属于小尺寸功能控件，形状/状态要可读；适合确定性裁切/矢量/代码绘制，不应每个状态随机生图。
- 手机目录主要是同套控件的适配版本。颜色、糖果符号和描边宽度应共用规范。

### 故事书底页和特殊层

- `storybook.jpg`：奶油白纸页，细棕色四边框，四角糖果旋纹花饰，轻微纸粒；中间和右侧留白用于正文。`storybook2.jpg` 是同构图深灰暗色版本。
- `splash.jpg`：白底的小型彩色作者标识；新交付应使用本项目自己的署名/标识排版，不把原作者标识混入新素材。
- `clouds.png`：细长紫色云剪影，用作菜单水平运动层。
- `ani1/2/3.png`：主菜单底部符号式小动物/人物剪影动画三帧。
- `flowers1/2/3.png`：浅金黄色六瓣花/星形小粒子，尺寸不同但造型语言一致。
- `light1/2.png`：粉色能量轮廓线及碎片，`light3.png` 是白色柔光；`pastfilter.png` 为柔白/灰淡化叠层。这些是特效层，不是完整场景。

### 图鉴素材已观察

- `concept` 图有 9 张，分别展示 assistant、candyalchemist、candygirl、cat、chocolate、saveher、treat、uniform、witch 的全身主设定。白底，角色站姿，有少量简单阴影。
- `extra` 图有 9 张：albumart（Gumdrop 肖像和音符）、candyprint（五人彩色群像）、doodles（彩色简笔人物头像）、promo（五人动态海报）、rough（群像草稿）、roughpromo（分色粗线群像）、shirt（深莓色底 Gumdrop 装饰图）、toffee1/2（两张暖橙底猫角色独立插画）。
- `gal_*` 六张是背景的小图鉴预览，构图与背景相同；应从新背景缩略生成，不必再次生图。`galframe_*` 是普通/hover/锁定三种边框状态。

## 6. 素材生成批次建议

1. 先生成一张统一角色主设定板，覆盖五主角和 Chocolate/Treat/Wolf；确认粗线条、3–3.5 头身、配色后再派生表情。角色不能和背景同图生成。
2. 角色表情图集按上文角色/服装状态拆组。每格明确数量、网格、姿态和无文字，保留透明底；图集若无法稳定透明，应先白底再统一处理，不允许靠近白色大褂/头巾的边缘被误删。
3. 先生成糖果店、实验室、集市、图书馆四张背景作为场景视觉基准，再生成野外/冰洞/小屋。昼夜同构图由同一底图派生。
4. CG 先生成一张暖色日常与一张冰蓝冒险的椭圆样张，之后按上表情景生成 35 槽。双槽应沿用同一母图，只改变眼睛、表情或必要道具，不能整张重画成不同场景。
5. GUI 生成糖果边框/纸页/小镇剪影等装饰母版；文字、按钮尺寸、hover、滚动条等由代码和确定性绘制保证一致。每个原视觉槽位仍需有映射和产物，但不代表每个像素控件都需单独发起生图。
6. 图鉴 concept/extra 保持角色身份一致，按明确用途生成新设定板/群像/草图。素材输出必须与 `analysis/reference` 的原作只读参考分离。

## 7. 官方公开参考链接

- 官方游戏页：https://nomnomnami.itch.io/syrup-and-the-ultimate-sweet
- 官方封面：https://img.itch.zone/aW1hZ2UvNDEzOTkvODIxMTI3LnBuZw%3D%3D/original/p4TI7q.png
- 故事书/糖果店建立镜头：https://img.itch.zone/aW1hZ2UvNDEzOTkvMjE3MDM3MC5wbmc%3D/original/%2FtJ%2Fk%2B.png
- 糖果店三主角：https://img.itch.zone/aW1hZ2UvNDEzOTkvMjE3MDM3MS5wbmc%3D/original/7airn4.png
- 集市三角色：https://img.itch.zone/aW1hZ2UvNDEzOTkvMjE3MDM3Mi5wbmc%3D/original/iFTebv.png
- 店外女巫/猫角色：https://img.itch.zone/aW1hZ2UvNDEzOTkvMjE3MDM3My5wbmc%3D/original/gbT7hc.png
- 图书馆 Chocolate 双人：https://img.itch.zone/aW1hZ2UvNDEzOTkvMjE3MDM3NC5wbmc%3D/original/JMYlYs.png
- 官方图鉴说明：https://nomnomnami.itch.io/syrup-and-the-ultimate-sweet/devlog/128302/syrup-and-the-ultimate-sweet-console-release

只读参考与分析联系图位于 `analysis/reference/style/`：`contact_characters.jpg`、`contact_backgrounds.jpg`、`contact_cg.jpg`、`contact_gui.jpg`、`contact_gallery.jpg`、`contact_storybook_effects.jpg`。这些是观察证据，不是游戏交付素材。
