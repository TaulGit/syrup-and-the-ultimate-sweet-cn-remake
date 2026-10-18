# 《希乐普与终极糖果》公开网页版玩法与剧情结构分析

结论：公开网页构建是 **3.1.0**，原生分辨率 **1280×720**，由 **Ren’Py 8.5.2** 构建。主脚本含 **49 个 label、19 个 menu、40 个选项、48 条显式 jump、10 个结局**。简中剧本、选项、结局名称和字体均已随公开包发行；原生网页版隐藏画廊入口，虽然资源和画廊脚本仍在包内。

## 证据与边界

- 源目录：`analysis/reference/unpacked/game`。本报告只读随公开网页版交付的明文 `.rpy` 和配置，不执行原作脚本，不访问付费 PC/Mac 包。
- 源包 SHA-256：`3b01e88b68be2f41e8305215c30863c6ee4063bea6fe72b0a6f496841c8edf9a`。REA 归档证据：`ev_8e5d4de3c042817e24abd04ae3ccfbc41adc264b16b149e573d5e4ff40685a02`。
- 公开构建：[入口](https://html-classic.itch.zone/html/18611204/index.html?v=1785467169)、[game.zip](https://html-classic.itch.zone/html/18611204/game.zip)、[pwa_catalog.json](https://html-classic.itch.zone/html/18611204/pwa_catalog.json)。
- 游戏版本：`options.rpy:26` 与 `cache/build_info.json:1` 均为 `3.1.0`；`script_version.txt:1` 为 `(8, 5, 2)`；`gui.rpy:12` 调用 `gui.init(1280, 720)`。build_info 的时间戳为 `1785466772.7617974`，对应 2026-07-31 UTC。
- 以下结局条件属于静态观察；示例路径通过独立控制流模型枚举验证，不等于在浏览器逐条实际通关。分镜、台词与完整剧本未复制到交付文件。

## 简中标题、角色和本地化

正式译名为 **希乐普与终极糖果**（`tl/chinese/options.rpy:41–42`），语言标识 `chinese`，选单名称“汉语”，译者 **Yuriatelier**（`tl.rpy:15`；`tl/chinese/options.rpy:60–61`）。

| 英文标识 | 简中译名 |
|---|---|
| Syrup | 希乐普 |
| Gumdrop | 甘姆德洛普 |
| Pastille | 帕斯提耶 |
| Butterscotch | 巴塔斯可琪 |
| Toffee | 托菲 |
| Treat | 德莉特 |
| Milk Chocolate | 米尔克查克利 |
| Dark Chocolate | 达克查克利 |
| Chocolate Twins | 查克利双子 |

主要地点：Atelier Sweets＝糖果工坊；Syrup’s Candy Laboratory＝希乐普的糖果实验室；Butterscotch’s Cottage＝巴塔斯可琪的小屋；Choco Library＝巧克力图书馆；Mount Sorbet＝索尔贝山；Treat’s Cabin＝德莉特的木屋。译文在 `tl/chinese/script.rpy:8494–8699` 的 strings 段。

简中提供 `script.rpy`、`screens.rpy`、`options.rpy`、`definitions.rpy`、`gallery.rpy`、`common.rpy`，并有本地化标题图 `tl/chinese/images/title.png`。字体为 `ZCOOLKuaiLe-Regular.ttf`；简中正文/历史文字32、界面/按钮36、选项34（`tl/chinese/options.rpy:3–31`）。这证明相关资源和翻译存在；未逐句实机检查所有翻译的显示效果。

## 状态模型

`start` 每次开新局将下列关系和标记重置（`script.rpy:50–84`）。分数不在界面明示。对话身份名、地点 `save_name` 也随流程更新。

| 变量 | 用途 |
|---|---|
| `bp` | 魔女关系分数；0开始，最高5，决定夜谈和最终魔女/托菲分支 |
| `gp` | 糖果女孩关系分数；0开始，最高5；>=4且非candyslave时抢占其他角色结局 |
| `pp` | 帕斯提耶关系分数；0开始，最高4；救援至少1，专属结局至少3 |
| `biopsy` | 取样检查身体；主要改变后续对白 |
| `nopets` | 曾拒绝接纳并带女孩到魔女家；后续对白分流 |
| `candyslave` | 曾将女孩留给魔女；保留外观变体并阻断女孩好结局和同伴救援 |
| `candydate` | 共同采购经历；后续对白分流 |
| `gotlost` | 记录女孩走失；当前主脚本仅写入，未见条件读取 |
| `foundcandy` | 共同寻找女孩；后续对白分流 |
| `paranoid` | 独自购物后对魔女怀疑；后续对白分流 |
| `salesman` | 曾议价出售女孩；图书馆对白分流 |
| `gentlelady` | 把外套借给魔女；姿态/对白变化，同时该选择bp+1 |
| `forgiven` | 先拒绝和解、获救后原谅魔女；bp+1并允许无前置通关进入托菲线 |
| `forgotit` | 不看水晶球；最终强制希乐普结局 |

`persistent.*end` 是跨周目结局记录；`persistent.endclear` 控制已通关入口；`persistent.setlanguage` 控制首次语言选择。它们不在 `start` 中重置。`persistent.toffeeend` 仅解锁第二次托菲问答中的“都不是”，并非首通托菲结局的必需条件。

## 全部选择与状态影响

选项序号依当前菜单从上到下编号。这里只保留按钮文案和结构，不收录上下文台词。未列加分的选项不会自动扣分。

| Menu 行 / 所属 label | 选择内容 | 代码影响与去向 |
|---|---|---|
| `140` / `start` | 1. 既然这样的话…… | biopsy = True；jump candybiopsy |
| `140` / `start` | 2. 不要吃这个可爱的糖果女孩 | jump continued |
| `195` / `candybiopsy` | 1. ……好吧，你说得有理 | pp += 1；jump newassistant |
| `195` / `candybiopsy` | 2. 反正我就是要吃掉她 | jump candibal |
| `471` / `newassistant` | 1. 好吧，我们可以留她在这里。 | gp += 1；pp += 1；jump adopted |
| `471` / `newassistant` | 2. 我还是不喜欢她。 | nopets = True |
| `560` / `nopetsallowed` | 1. 我已经下定决心了。 | jump abandonher |
| `560` / `nopetsallowed` | 2. 容我三思…… | jump keepher |
| `630` / `candyslave` | 1. 答应帮忙 | pp += 1；jump rescuemission |
| `630` / `candyslave` | 2. 无视他 | jump lonelystore |
| `771` / `adopted` | 1. 你开心就好。 | gp += 1；jump shoppingduo |
| `771` / `adopted` | 2. 别烦我。 | gotlost = True；jump shoppingalone |
| `869` / `shoppingduo` | 1. 带她回家 | gp += 1；jump homesweethome |
| `869` / `shoppingduo` | 2. 把她丢弃在这里 | gotlost = True；jump lostcandy |
| `998` / `lostcandy` | 1. ……他说得对 | pp += 1；jump search |
| `998` / `lostcandy` | 2. 管他呢，再见。 | jump lonelystore |
| `1098` / `lonelystore` | 1. 雇用猫 | jump parttimecat |
| `1098` / `lonelystore` | 2. 我还没绝望到那种地步 | 当前选择不改关系分数；按下一流程继续 |
| `1318` / `customers` | 1. 她是非卖品 | gp += 1 |
| `1318` / `customers` | 2. ……我们可以谈谈价钱。 | salesman = True；不增加关系分数，按下一流程继续 |
| `1394` / `customers` | 1. 监督甘姆德洛普 | gp += 1；jump withgumdrop |
| `1394` / `customers` | 2. 和你一起工作 | pp += 1；jump withpastille |
| `1394` / `customers` | 3. 外出 | jump butterscotchvisit |
| `2084` / `missingcandy` | 1. 让她帮忙 | bp += 1 |
| `2084` / `missingcandy` | 2. 这是个糟糕的主意 | 当前选择不改关系分数；按下一流程继续 |
| `2262` / `adventure` | 1. 把外套给她 | bp += 1；gentlelady = True |
| `2262` / `adventure` | 2. 她能搞定的 | 当前选择不改关系分数；按下一流程继续 |
| `2353` / `thecave` | 1. 有多少拿多少 | 当前选择不改关系分数；按下一流程继续 |
| `2353` / `thecave` | 2. 只拿你需要的份量 | bp += 1 |
| `2485` / `trapped` | 1. 我不讨厌你。 | bp += 2；jump hearttoheart |
| `2485` / `trapped` | 2. 是的，我讨厌你。 | jump thingsgonesour |
| `2608` / `saved` | 1. ……没关系的。 | forgiven = True；bp += 1；jump backhome |
| `2608` / `saved` | 2. 我还是很讨厌你。 | return |
| `2860` / `makethething` | 1. 观看水晶球里的内容 | jump creation |
| `2860` / `makethething` | 2. 还是算了吧 | forgotit = True；jump ultimatesweet |
| `3540` / `toffeeend` | 1. 当然 | 当前选择不改关系分数；按下一流程继续 |
| `3540` / `toffeeend` | 2. 听起来很费劲…… | jump butterscotchend |
| `3632` / `toffeeend` | 1. 男孩？ | 当前选择不改关系分数；按下一流程继续 |
| `3632` / `toffeeend` | 2. 女孩？ | 当前选择不改关系分数；按下一流程继续 |
| `3632` / `toffeeend` | 3. 都不是；仅当 `persistent.toffeeend` 可见 | jump toffeeend2 |

补充：`candyslave` 在 `script.rpy:607` 写入；`candydate` 在796行；`paranoid` 在953行；`foundcandy` 在1227行。主剧情中一些“跳转”依赖 label 之间自然贯通，不能只抓显式 jump：例如 `continued → newassistant`、`withpastille → butterscotchvisit`、`hearttoheart → backhome`。JSON 同时记录了条件、选项与这些贯通边。

## 十个结局的精确条件

五个较好结局的分发位于 `ultimatesweet`（`script.rpy:3206–3246`），按顺序执行，**较早条件优先覆盖较晚条件**：先 `forgotit`，再甘姆德洛普，再魔女/托菲，再帕斯提耶，最后默认希乐普。

令 `G = (gp >= 4 and not candyslave)`。下表默认已活着走到相应判断点；早期坏结局会提前退出。

| 简中结局 | achievement / 标记 | 进入条件 |
|---|---|---|
| 食人结局 | `CANDIBAL_END / persistent.candibalend` | 首个菜单选1，检查后仍选“反正我就是要吃掉她”（menu 195的2）；直接到candibal。 |
| 坏结局1 | `BAD1_END / persistent.badend1` | 丢下女孩后拒绝接回/寻找，进入lonelystore；menu 1098选2，不雇用托菲。 |
| 坏结局2 | `BAD2_END / persistent.badend2` | 同样到lonelystore；menu 1098选1，雇用托菲。 |
| 冻僵结局 | `FROZEN_END / persistent.frozenend` | menu 2485选2，拒绝和解；且不满足 `pp>=1 and gp>=2 and not candyslave` 的获救条件。 |
| 最坏的结局 | `WORST_END / persistent.worstend` | menu 2485选2；满足获救条件；获救后menu 2608仍选2，第二次拒绝魔女。 |
| 希乐普结局 | `SYRUP_END / persistent.syrupend` | `forgotit=True` 强制进入；否则 `not G and bp<4 and pp<3`，从ultimatesweet自然落入syrupend。 |
| 甘姆德洛普结局 | `GUMDROP_END / persistent.gumdropend` | `not forgotit and G`；即使bp或pp也达标仍优先进入本结局。 |
| 帕斯提耶结局 | `PASTILLE_END / persistent.pastilleend` | `not forgotit and not G and bp<4 and pp>=3`。 |
| 巴塔斯可琪结局 | `BS_END / persistent.butterscotchend` | `not forgotit and not G and bp>=4`，且 `not forgiven and not persistent.butterscotchend`；或已进托菲线却在menu 3540选2。 |
| 托菲结局 | `TOFFEE_END / persistent.toffeeend` | `not forgotit and not G and bp>=4 and (forgiven or persistent.butterscotchend)`；进入toffeeend后menu 3540选1。menu 3632的所有可见答案均能最终抵达toffeeend2。 |

简中结局名由 `tl/chinese/screens.rpy:350–463` 核对。来源代码的实际终点为 `candibal`、`thentherewasone`、`parttimecat`、`thingsgonesour`、`saved`、`syrupend`、`pastilleend`、`gumdropend`、`butterscotchend`、`toffeeend2`；并非每个坏结局都有同名 label。

托菲存在两条进入办法：通常先拿到巴塔斯可琪结局，再以魔女关系分数达标重玩；也能在全新持久化状态下先于冰洞说讨厌她、满足同伴救援，再在获救后原谅她（`forgiven=True`）。只要之前帮助、借外套、只拿所需材料三次都加分，获救后的原谅再加1，即 `bp=4`，无需先通魔女结局。JSON 保留了这条完整可行路径。翻译文件中的旧攻略提示未被当作当前版本的判定依据。

## 完整 label 结构

表中后继为保留控制流的压缩结果，包含条件分支和自然贯通；精确守卫条件以 `story-graph.json` 的节点、边和嵌套 body 为准。

| label / 行 | 摘要 | 可达的下一 label 或 return |
|---|---|---|
| `splashscreen` / 35 | 首次语言设置、成就同步与启动画面 | `return` |
| `start` / 49 | 初始化关系分数与标记，发现糖果女孩 | `candybiopsy`, `continued` |
| `candybiopsy` / 146 | 检查糖果身体后决定是否继续吃掉她 | `candibal`, `newassistant` |
| `candibal` / 242 | 食人结局 | `return` |
| `continued` / 295 | 未取食时与糖果女孩初次交谈 | `newassistant` |
| `newassistant` / 424 | 决定接纳或拒绝新助手 | `adopted`, `nopetsallowed` |
| `nopetsallowed` / 479 | 将糖果女孩带到魔女家 | `abandonher`, `keepher` |
| `abandonher` / 567 | 决定把糖果女孩留给魔女 | `candyslave` |
| `candyslave` / 603 | 糖果女孩被改造成服从魔女的外观状态 | `lonelystore`, `rescuemission` |
| `rescuemission` / 646 | 回应帕斯提耶请求去接回女孩 | `homesweethome` |
| `keepher` / 698 | 在魔女家反悔并带女孩回家 | `homesweethome` |
| `adopted` / 737 | 接纳女孩后决定是否一起采购 | `shoppingalone`, `shoppingduo` |
| `shoppingduo` / 795 | 同行采购并决定是否带她回家 | `homesweethome`, `lostcandy` |
| `shoppingalone` / 917 | 独自采购并增加对魔女的怀疑 | `lostcandy` |
| `lostcandy` / 965 | 发现女孩走失并决定是否寻找 | `lonelystore`, `search` |
| `lonelystore` / 1008 | 帕斯提耶离开后独自经营的支线 | `parttimecat`, `thentherewasone` |
| `thentherewasone` / 1114 | 坏结局1：经营失败 | `return` |
| `parttimecat` / 1133 | 坏结局2：托菲与魔女接管商店 | `return` |
| `search` / 1194 | 与帕斯提耶找回女孩 | `homesweethome` |
| `homesweethome` / 1242 | 回店并为女孩命名 | `customers` |
| `customers` / 1285 | 巧克力双子来店，之后选择与谁共度工作时间 | `butterscotchvisit`, `withgumdrop`, `withpastille` |
| `withgumdrop` / 1449 | 与女孩相处的分支 | `butterscotchvisit` |
| `withpastille` / 1527 | 与帕斯提耶相处的分支 | `butterscotchvisit` |
| `butterscotchvisit` / 1605 | 魔女初次来店，按此前经历分流对白 | `butterscotchvisit2` |
| `butterscotchvisit2` / 1678 | 魔女来访后向山区任务过渡 | `mission` |
| `mission` / 1802 | 次日准备终极糖果的材料任务 | `libraryvisit` |
| `libraryvisit` / 1901 | 进入巧克力图书馆寻找线索 | `missingcandy` |
| `missingcandy` / 2015 | 女孩失踪后邀请魔女帮助 | `adventure` |
| `adventure` / 2107 | 登山途中与魔女、德莉特互动 | `thecave` |
| `thecave` / 2311 | 进入冰洞并决定取多少材料 | `trapped` |
| `trapped` / 2379 | 被冰墙困住后决定如何回应魔女 | `hearttoheart`, `thingsgonesour` |
| `thingsgonesour` / 2496 | 拒绝和解，按同伴关系判断能否获救 | `return`, `saved` |
| `saved` / 2539 | 获救后再决定是否原谅魔女 | `backhome`, `return` |
| `hearttoheart` / 2656 | 主动和解使魔女恢复行动能力 | `backhome` |
| `backhome` / 2714 | 离开山区回到魔女家 | `missioncomplete` |
| `missioncomplete` / 2792 | 回到商店完成材料任务 | `makethething` |
| `makethething` / 2831 | 决定是否查看水晶球揭示真相 | `creation`, `ultimatesweet` |
| `creation` / 2882 | 水晶球揭示糖果女孩的创生经过 | `afterwards`, `lonelygumdrop` |
| `lonelygumdrop` / 2980 | 关系足够亲密时与女孩深夜交流 | `ultimatesweet` |
| `afterwards` / 3072 | 查看真相后按魔女关系分数进入夜谈 | `toffeetalk`, `ultimatesweet` |
| `toffeetalk` / 3107 | 托菲说明魔女的背景 | `ultimatesweet` |
| `ultimatesweet` / 3178 | 终极糖果完成，按优先级分发五种好结局 | `butterscotchend`, `gumdropend`, `pastilleend`, `syrupend`, `toffeeend` |
| `syrupend` / 3246 | 希乐普结局：投入制糖事业 | `credits` |
| `pastilleend` / 3299 | 帕斯提耶结局：结伴研究与冒险 | `credits` |
| `gumdropend` / 3372 | 甘姆德洛普结局：共同旅行 | `credits` |
| `butterscotchend` / 3424 | 巴塔斯可琪结局：共享制糖技艺 | `credits` |
| `toffeeend` / 3510 | 托菲支线邀请与身份选择 | `butterscotchend`, `toffeeend2` |
| `toffeeend2` / 3657 | 托菲结局：形成新的陪伴关系 | `credits` |
| `credits` / 3694 | 结算、持久化与制作人员画面 | `return` |

## 存档、通关记录与操作

- 桌面快捷栏支持回退、历史、快进、自动、保存、设置；Q.Save/Q.Load按钮已被注释（`screens.rpy:251–273`）。触摸版换成回退、快进、自动、隐藏文本框、菜单（1727–1745）。历史容量100条（`gui.rpy:364`），默认文本速度60字符/秒、自动翻页时间15（`options.rpy:131、137`）。
- 保存/读取使用同一个 `file_slots` 页面，每页2列×2行，共4槽（`gui.rpy:265–266`）；槽中显示截图、时间、地点名，支持删除和前后翻页（`screens.rpy:692–745`）。存在自动/快速存档页名称支持，但未在主脚本观察到定制自动存档触发逻辑，不据此宣称它们关闭或已实机验证。
- 保存目录配置是 `syrup-1555791336`（`options.rpy:154`）。公开网页引擎包装层把 `/home/web_user/.renpy` 挂载到浏览器IDBFS，外层菜单另提供导入/导出保存文件；这是公开 `renpy-pre.js` 的实现，不是自建服务器存档。
- 五个较好结局进入 `credits`，显式调用 `renpy.save_persistent()`；同时临时关闭快捷栏和游戏菜单。PC variant还设置MultiPersistent的 `mp.candyvn=True`；网页不执行该PC专属分支（`script.rpy:3694–3703`）。五个坏结局也设置自己的persistent标记和endclear后return，但没有同位置的显式save_persistent调用。
- 首次启动 `splashscreen` 显示语言页，再设 `persistent.setlanguage=True`（35–39）。之后设置中的语言页用 `Language(i[0])` 即时切换；`preferences.language` 决定制作人员字幕是否显示翻译署名（3705）。
- 任意结局设置endclear后，游戏菜单出现“结局”；十个条目分别由各自persistent标记解锁，未见条目显示“？？？”（`screens.rpy:329–330、1516–1607`）。主菜单的已通关角色展示也按五个好结局标记变化（374–397）。

## 图鉴与画廊

- **原生网页版主菜单不显示画廊**：`screens.rpy:413–414` 用 `if not renpy.variant("web")` 包围Gallery按钮，非web版还要求 `persistent.endclear`。不要因为文件存在就描述成网页版已有可点入口。
- `gallery.rpy` 实现背景、角色、插画、追加四类。背景6组共16幅；部分采用Gallery的已见图解锁。角色页7组，可切换预设姿势；追加页9幅。图鉴列表在 `definitions.rpy:382–484`。
- 插画有34个 `sb_list` 条目；`g_illust` 以 `renpy.seen_image()` 判断显示原图还是锁定图，收集数也实时按seen_image统计（`gallery.rpy:260–313`）。包内另有 `persistent.sb_seen` 与collect辅助函数，但当前插画界面使用的是Ren’Py的seen-image记录，不能混为两个独立的实际收藏系统。
- 主菜单风味提示会读取未解锁/已解锁的结局标记，给出提示或额外短句（`definitions.rpy:34–88`），这是多周目引导。

## 机器可读结构与验证

`analysis/story-graph.json` 包含元信息、所有49个label的结构化body、353个控制/状态节点、417条边、19个menu、40个选择、48条显式jump、初始状态、10结局守卫与一条示例路径。节点以源码行号稳定标识；仅保存流程与短按钮文本，不保存原作完整对白。

验证已完成：label、menu和jump数量与原脚本逐项比对；所有图边目标存在；十个结局均在静态结构枚举中可达。枚举分别取 `persistent.butterscotchend=False/True`，`persistent.toffeeend=False`，网页variant，无需执行原作。对已通关托菲才显示的第三个身份选项，已在结构图中保留其守卫；其行为只影响短对白，仍跳到同一结局终点。
