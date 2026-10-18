# Syrup and the Ultimate Sweet 网页公开构建视觉资产清单

## 结论

逐个覆盖 **407 个图像文件**（383 PNG + 24 JPG），没有只计主目录而漏掉 GUI、画廊或语言替换图。
原包 SHA256：`3b01e88b68be2f41e8305215c30863c6ee4063bea6fe72b0a6f496841c8edf9a`。REA 归档证据：`ev_8e5d4de3c042817e24abd04ae3ccfbc41adc264b16b149e573d5e4ff40685a02`。

文件内容唯一数：369；归一化 RGBA 像素唯一数：369。
哈希相同才认定重复；其他语言图是用途上的语言替换，不能默认认定字节或像素相同。

## 按用途统计

| 类别 | 文件数 |
|---|---:|
| background | 16 |
| character_sprite | 151 |
| gallery_concept | 9 |
| gallery_extra | 9 |
| gallery_thumbnail | 6 |
| gallery_ui | 4 |
| gui_component | 141 |
| localized_image | 11 |
| menu_animation | 3 |
| menu_portrait | 10 |
| screen_art | 3 |
| solid_background | 1 |
| story_cg | 34 |
| title_art | 1 |
| visual_effect | 8 |

## 角色与服装/状态

| 角色 | 服装/状态 | 独立表情/姿势图数 |
|---|---|---:|
| Butterscotch | witch | 14 |
| Butterscotch | chubby_witch | 9 |
| Butterscotch | snowy_witch | 8 |
| Butterscotch | borrowed_wintercoat | 6 |
| Chocolate Twins | default | 2 |
| Gumdrop | long_hair_candy_body | 29 |
| Gumdrop | short_hair_shop_uniform | 13 |
| Pastille | winter_outfit | 3 |
| Pastille | shop_uniform | 13 |
| Syrup | labcoat | 22 |
| Syrup | wintercoat | 12 |
| Syrup | labcoat_after_lending_wintercoat | 6 |
| Toffee | default | 8 |
| Treat | default | 3 |
| Wolf | pink_fur | 2 |
| Wolf | gray_white_fur | 1 |

`sy cold*` 是灰色毛领防寒外套；`sy colder*` 是借出外套后冻红的白大褂。
`bs warm*` 是借穿灰色外套；`bs cold*` 是淋雪的巫师装。两类服装不能仅靠 cold/warm 字面合并。
Gumdrop 有长发常态 29 图、短发店员制服 13 图；新图长发常态采用完整糖霜连衣裙。Wolf 3 图是四足狼，Treat 3 图是人形，分别保留。

## 去重、中文及使用点判据

- `sha256` 按原文件字节计算；`pixel_sha256` 按尺寸+RGBA 像素计算，忽略 PNG 元数据差异。
- `duplicate_of` 只表示像素完全相同，可共用一张新图。不得据此删除原逻辑槽位或悬停状态。
- `automatic_image_name` 记录 Ren'Py images/ 自动图片名；使用点包含直接路径、自动图片名、show/scene、角色对白表情属性、GUI 状态模板。
- 无静态命中的文件标为 packaged_no_static_reference。它们仍列入完整重绘计划；不伪造运行时触达证据。
- 简中本地化图只有 `tl/chinese/images/title.png`；简中剧情、菜单、名字翻译位于文本源码，非图片。另 10 个语言图保留盘点但中文版不加载。
- `gui/phone/` 是移动端变体；GUI 家族由 `gui.button_properties` 与屏幕样式按状态选图，部分打包旧版状态未被源码实际引用。

## 最少完整生成任务分组

角色按身份合并图集、每个表情/服装独立格；背景每组 4 图、剧情 CG 每组 6 图。其余美术按用途进入 UI/概念/额外插画图集。
这是槽位不遗漏的最少分组方案；如图像模型分辨率限制导致小格细节不足，可拆页，不能合并原表情。UV 坐标随 JSON 给出，前端可直接按图集选格，无需裁图。

### character_syrup · character · 7×6 · 40 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/sy aww.png` — Syrup / labcoat / 温柔怜惜
- 01（0,1）：`images/sy cold.png` — Syrup / wintercoat / 基础
- 02（0,2）：`images/sy coldcomfort.png` — Syrup / wintercoat / 安抚
- 03（0,3）：`images/sy colder.png` — Syrup / labcoat_after_lending_wintercoat / 基础
- 04（0,4）：`images/sy colderawkward.png` — Syrup / labcoat_after_lending_wintercoat / 尴尬
- 05（0,5）：`images/sy colderhey.png` — Syrup / labcoat_after_lending_wintercoat / 打招呼
- 06（0,6）：`images/sy coldersmile.png` — Syrup / labcoat_after_lending_wintercoat / 微笑
- 07（1,0）：`images/sy colderstop.png` — Syrup / labcoat_after_lending_wintercoat / 制止
- 08（1,1）：`images/sy colderyeah.png` — Syrup / labcoat_after_lending_wintercoat / 应答
- 09（1,2）：`images/sy coldhey.png` — Syrup / wintercoat / 打招呼
- 10（1,3）：`images/sy coldhmm.png` — Syrup / wintercoat / 思考
- 11（1,4）：`images/sy coldhuh.png` — Syrup / wintercoat / 疑惑
- 12（1,5）：`images/sy coldsass.png` — Syrup / wintercoat / 吐槽
- 13（1,6）：`images/sy coldscared.png` — Syrup / wintercoat / 害怕
- 14（2,0）：`images/sy coldsmirk.png` — Syrup / wintercoat / 得意笑
- 15（2,1）：`images/sy coldstop.png` — Syrup / wintercoat / 制止
- 16（2,2）：`images/sy coldthought.png` — Syrup / wintercoat / 沉思
- 17（2,3）：`images/sy coldyeah.png` — Syrup / wintercoat / 应答
- 18（2,4）：`images/sy coldyell.png` — Syrup / wintercoat / 喊叫
- 19（2,5）：`images/sy cool.png` — Syrup / labcoat / 淡定
- 20（2,6）：`images/sy crystalball.png` — Syrup / labcoat / 手持水晶球
- 21（3,0）：`images/sy dakara.png` — Syrup / labcoat / 解释
- 22（3,1）：`images/sy embarrassed.png` — Syrup / labcoat / 害羞
- 23（3,2）：`images/sy frick.png` — Syrup / labcoat / 懊恼
- 24（3,3）：`images/sy grr.png` — Syrup / labcoat / 恼怒
- 25（3,4）：`images/sy grr2.png` — Syrup / labcoat / 另一种恼怒
- 26（3,5）：`images/sy hahano.png` — Syrup / labcoat / 尴尬拒绝
- 27（3,6）：`images/sy heeey.png` — Syrup / labcoat / 高声招呼
- 28（4,0）：`images/sy heh.png` — Syrup / labcoat / 轻笑
- 29（4,1）：`images/sy hmm.png` — Syrup / labcoat / 思考
- 30（4,2）：`images/sy indifferent.png` — Syrup / labcoat / 冷淡
- 31（4,3）：`images/sy oh.png` — Syrup / labcoat / 察觉
- 32（4,4）：`images/sy point.png` — Syrup / labcoat / 指向
- 33（4,5）：`images/sy proud.png` — Syrup / labcoat / 自豪
- 34（4,6）：`images/sy reg.png` — Syrup / labcoat / 平常
- 35（5,0）：`images/sy smirk.png` — Syrup / labcoat / 得意笑
- 36（5,1）：`images/sy tch.png` — Syrup / labcoat / 不耐烦
- 37（5,2）：`images/sy thanks.png` — Syrup / labcoat / 感谢
- 38（5,3）：`images/sy um.png` — Syrup / labcoat / 迟疑
- 39（5,4）：`images/sy yo.png` — Syrup / labcoat / 随意招呼

### character_gumdrop · character · 7×6 · 42 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/gum aw.png` — Gumdrop / long_hair_candy_body / 轻声安慰
- 01（0,1）：`images/gum baw.png` — Gumdrop / long_hair_candy_body / 大哭
- 02（0,2）：`images/gum broken.png` — Gumdrop / long_hair_candy_body / 身体破损
- 03（0,3）：`images/gum determined.png` — Gumdrop / long_hair_candy_body / 坚定
- 04（0,4）：`images/gum doll.png` — Gumdrop / long_hair_candy_body / 玩偶状态
- 05（0,5）：`images/gum dress.png` — Gumdrop / long_hair_candy_body / 展示衣服
- 06（0,6）：`images/gum eaten.png` — Gumdrop / long_hair_candy_body / 被吃掉后的状态
- 07（1,0）：`images/gum friendlier.png` — Gumdrop / long_hair_candy_body / 更亲近
- 08（1,1）：`images/gum frozen.png` — Gumdrop / long_hair_candy_body / 冻结
- 09（1,2）：`images/gum happy.png` — Gumdrop / long_hair_candy_body / 开心
- 10（1,3）：`images/gum hey.png` — Gumdrop / long_hair_candy_body / 打招呼
- 11（1,4）：`images/gum hey2.png` — Gumdrop / long_hair_candy_body / 另一种招呼姿势
- 12（1,5）：`images/gum lost.png` — Gumdrop / long_hair_candy_body / 迷茫
- 13（1,6）：`images/gum mad.png` — Gumdrop / long_hair_candy_body / 生气
- 14（2,0）：`images/gum noo.png` — Gumdrop / long_hair_candy_body / 拒绝
- 15（2,1）：`images/gum nooo.png` — Gumdrop / long_hair_candy_body / 强烈抗拒
- 16（2,2）：`images/gum ooh.png` — Gumdrop / long_hair_candy_body / 好奇惊喜
- 17（2,3）：`images/gum pls.png` — Gumdrop / long_hair_candy_body / 请求
- 18（2,4）：`images/gum shutdown.png` — Gumdrop / long_hair_candy_body / 失去反应
- 19（2,5）：`images/gum surprise.png` — Gumdrop / long_hair_candy_body / 惊讶
- 20（2,6）：`images/gum surprise2.png` — Gumdrop / long_hair_candy_body / 另一种惊讶
- 21（3,0）：`images/gum umm.png` — Gumdrop / long_hair_candy_body / 犹豫
- 22（3,1）：`images/gum worry.png` — Gumdrop / long_hair_candy_body / 担忧
- 23（3,2）：`images/gum yay.png` — Gumdrop / long_hair_candy_body / 欢呼
- 24（3,3）：`images/gum yay2.png` — Gumdrop / long_hair_candy_body / 另一种欢呼
- 25（3,4）：`images/gum yayyy.png` — Gumdrop / long_hair_candy_body / 非常兴奋
- 26（3,5）：`images/gum yayyy2.png` — Gumdrop / long_hair_candy_body / 另一种兴奋
- 27（3,6）：`images/gum yes.png` — Gumdrop / long_hair_candy_body / 肯定
- 28（4,0）：`images/gum yes2.png` — Gumdrop / long_hair_candy_body / 另一种肯定
- 29（4,1）：`images/gums aw.png` — Gumdrop / short_hair_shop_uniform / 轻声安慰
- 30（4,2）：`images/gums baw.png` — Gumdrop / short_hair_shop_uniform / 大哭
- 31（4,3）：`images/gums dress.png` — Gumdrop / short_hair_shop_uniform / 展示衣服
- 32（4,4）：`images/gums frozen.png` — Gumdrop / short_hair_shop_uniform / 冻结
- 33（4,5）：`images/gums hey2.png` — Gumdrop / short_hair_shop_uniform / 另一种招呼姿势
- 34（4,6）：`images/gums mad.png` — Gumdrop / short_hair_shop_uniform / 生气
- 35（5,0）：`images/gums ooh.png` — Gumdrop / short_hair_shop_uniform / 好奇惊喜
- 36（5,1）：`images/gums surprise2.png` — Gumdrop / short_hair_shop_uniform / 另一种惊讶
- 37（5,2）：`images/gums worry.png` — Gumdrop / short_hair_shop_uniform / 担忧
- 38（5,3）：`images/gums yay2.png` — Gumdrop / short_hair_shop_uniform / 另一种欢呼
- 39（5,4）：`images/gums yayyy2.png` — Gumdrop / short_hair_shop_uniform / 另一种兴奋
- 40（5,5）：`images/gums yes.png` — Gumdrop / short_hair_shop_uniform / 肯定
- 41（5,6）：`images/gums yes2.png` — Gumdrop / short_hair_shop_uniform / 另一种肯定

### character_pastille · character · 4×4 · 16 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/pas cold.png` — Pastille / winter_outfit / 基础
- 01（0,1）：`images/pas coldnervous.png` — Pastille / winter_outfit / 紧张
- 02（0,2）：`images/pas coldpatient.png` — Pastille / winter_outfit / 耐心
- 03（0,3）：`images/pas dang.png` — Pastille / shop_uniform / 懊恼
- 04（1,0）：`images/pas eheh.png` — Pastille / shop_uniform / 不好意思地笑
- 05（1,1）：`images/pas heh.png` — Pastille / shop_uniform / 轻笑
- 06（1,2）：`images/pas hmhm.png` — Pastille / shop_uniform / 胸有成竹
- 07（1,3）：`images/pas mad.png` — Pastille / shop_uniform / 生气
- 08（2,0）：`images/pas patient.png` — Pastille / shop_uniform / 耐心
- 09（2,1）：`images/pas ready.png` — Pastille / shop_uniform / 准备就绪
- 10（2,2）：`images/pas sad.png` — Pastille / shop_uniform / 难过
- 11（2,3）：`images/pas smile.png` — Pastille / shop_uniform / 微笑
- 12（3,0）：`images/pas sorry.png` — Pastille / shop_uniform / 歉意
- 13（3,1）：`images/pas wahh.png` — Pastille / shop_uniform / 惊慌叫喊
- 14（3,2）：`images/pas worry.png` — Pastille / shop_uniform / 担忧
- 15（3,3）：`images/pas yum.png` — Pastille / shop_uniform / 品尝美味

### character_butterscotch · character · 7×6 · 37 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/bs aaa.png` — Butterscotch / witch / 惊叫
- 01（0,1）：`images/bs awchub.png` — Butterscotch / chubby_witch / 轻声安慰
- 02（0,2）：`images/bs bawchub.png` — Butterscotch / chubby_witch / 大哭
- 03（0,3）：`images/bs brag.png` — Butterscotch / witch / 炫耀
- 04（0,4）：`images/bs castin.png` — Butterscotch / witch / 施法
- 05（0,5）：`images/bs chub.png` — Butterscotch / chubby_witch / 基础
- 06（0,6）：`images/bs chubtears.png` — Butterscotch / chubby_witch / 流泪
- 07（1,0）：`images/bs cold.png` — Butterscotch / snowy_witch / 基础
- 08（1,1）：`images/bs coldeheh.png` — Butterscotch / snowy_witch / 不好意思地笑
- 09（1,2）：`images/bs coldfreakinout.png` — Butterscotch / snowy_witch / 慌乱
- 10（1,3）：`images/bs coldgrr.png` — Butterscotch / snowy_witch / 恼怒
- 11（1,4）：`images/bs coldmad.png` — Butterscotch / snowy_witch / 生气
- 12（1,5）：`images/bs coldpathetic.png` — Butterscotch / snowy_witch / 可怜委屈
- 13（1,6）：`images/bs coldtch.png` — Butterscotch / snowy_witch / 不耐烦
- 14（2,0）：`images/bs coldtears.png` — Butterscotch / snowy_witch / 流泪
- 15（2,1）：`images/bs doll.png` — Butterscotch / witch / 玩偶状态
- 16（2,2）：`images/bs drool.png` — Butterscotch / witch / 馋嘴
- 17（2,3）：`images/bs ehehchub.png` — Butterscotch / chubby_witch / 不好意思地笑
- 18（2,4）：`images/bs freakinout.png` — Butterscotch / witch / 慌乱
- 19（2,5）：`images/bs happychub.png` — Butterscotch / chubby_witch / 开心
- 20（2,6）：`images/bs hey.png` — Butterscotch / witch / 打招呼
- 21（3,0）：`images/bs mad.png` — Butterscotch / witch / 生气
- 22（3,1）：`images/bs madchub.png` — Butterscotch / chubby_witch / 生气
- 23（3,2）：`images/bs magics.png` — Butterscotch / witch / 魔法动作
- 24（3,3）：`images/bs ohno.png` — Butterscotch / witch / 不妙
- 25（3,4）：`images/bs shock.png` — Butterscotch / witch / 震惊
- 26（3,5）：`images/bs shychub.png` — Butterscotch / chubby_witch / 羞怯
- 27（3,6）：`images/bs smirk.png` — Butterscotch / witch / 得意笑
- 28（4,0）：`images/bs takeit.png` — Butterscotch / witch / 递出物品
- 29（4,1）：`images/bs umai.png` — Butterscotch / witch / 觉得美味
- 30（4,2）：`images/bs warm.png` — Butterscotch / borrowed_wintercoat / 基础
- 31（4,3）：`images/bs warmeheh.png` — Butterscotch / borrowed_wintercoat / 不好意思地笑
- 32（4,4）：`images/bs warmgrr.png` — Butterscotch / borrowed_wintercoat / 恼怒
- 33（4,5）：`images/bs warmpathetic.png` — Butterscotch / borrowed_wintercoat / 可怜委屈
- 34（4,6）：`images/bs warmscared.png` — Butterscotch / borrowed_wintercoat / 害怕
- 35（5,0）：`images/bs warmtch.png` — Butterscotch / borrowed_wintercoat / 不耐烦
- 36（5,1）：`images/bs wehchub.png` — Butterscotch / chubby_witch / 委屈

### character_toffee · character · 3×3 · 8 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/tof fret.png` — Toffee / default / 焦虑
- 01（0,1）：`images/tof heh.png` — Toffee / default / 轻笑
- 02（0,2）：`images/tof help.png` — Toffee / default / 求助
- 03（1,0）：`images/tof hmm.png` — Toffee / default / 思考
- 04（1,1）：`images/tof myow.png` — Toffee / default / 喵叫
- 05（1,2）：`images/tof nyan.png` — Toffee / default / 猫式招呼
- 06（2,0）：`images/tof sly.png` — Toffee / default / 狡黠
- 07（2,1）：`images/tof tsun.png` — Toffee / default / 傲娇

### character_chocolate_twins · character · 2×1 · 2 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/choco flowers.png` — Chocolate Twins / default / 手持花束
- 01（0,1）：`images/choco hello.png` — Chocolate Twins / default / 双人招呼

### character_treat · character · 2×2 · 3 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/treat aw.png` — Treat / default / 轻声安慰
- 01（0,1）：`images/treat meh.png` — Treat / default / 无所谓
- 02（1,0）：`images/treat.png` — Treat / default / 基础

### character_wolf · character · 2×2 · 3 槽

逐表情独立格；保留服装、体型和状态差异。Gumdrop 长发常态新图采用完整糖霜连衣裙。

- 00（0,0）：`images/wolf pink.png` — Wolf / pink_fur / 被魔法染成粉色
- 01（0,1）：`images/wolf pink2.png` — Wolf / pink_fur / 粉色状态惊慌
- 02（1,0）：`images/wolf.png` — Wolf / gray_white_fur / 基础

### background_01 · background · 2×2 · 4 槽

2×2；每格 16:9，无人物，不合并白天/夜晚和场景变体。

- 00（0,0）：`images/bg cabin.jpg` — 雪山木屋室内
- 01（0,1）：`images/bg cottage.jpg` — 女巫小屋外景
- 02（1,0）：`images/bg cottagedoor.jpg` — 女巫小屋门口近景
- 03（1,1）：`images/bg cottageint.jpg` — 女巫小屋室内

### background_02 · background · 2×2 · 4 槽

2×2；每格 16:9，无人物，不合并白天/夜晚和场景变体。

- 00（0,0）：`images/bg icecave.jpg` — 冰洞
- 01（0,1）：`images/bg icecave2.jpg` — 冰洞第二状态
- 02（1,0）：`images/bg lab.png` — 糖果炼金实验室
- 03（1,1）：`images/bg library.jpg` — 图书馆

### background_03 · background · 2×2 · 4 槽

2×2；每格 16:9，无人物，不合并白天/夜晚和场景变体。

- 00（0,0）：`images/bg market.jpg` — 城镇集市
- 01（0,1）：`images/bg mountain.jpg` — 雪山远景
- 02（1,0）：`images/bg nightcottage.jpg` — 夜晚女巫小屋
- 03（1,1）：`images/bg nightshop.jpg` — 夜晚糖果店内

### background_04 · background · 2×2 · 4 槽

2×2；每格 16:9，无人物，不合并白天/夜晚和场景变体。

- 00（0,0）：`images/bg shop.jpg` — 糖果店内
- 01（0,1）：`images/bg shop2.jpg` — 糖果店第二状态
- 02（1,0）：`images/bg shopext.jpg` — 糖果店外街道
- 03（1,1）：`images/bg snow.jpg` — 雪地山路

### story_cg_01 · cg · 3×2 · 6 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb badend1.png` — 剧情故事书插画：badend1
- 01（0,1）：`images/sb badend2.png` — 剧情故事书插画：badend2
- 02（0,2）：`images/sb bsend.png` — 剧情故事书插画：bsend
- 03（1,0）：`images/sb byetoffee.png` — 剧情故事书插画：byetoffee
- 04（1,1）：`images/sb byetreat.png` — 剧情故事书插画：byetreat
- 05（1,2）：`images/sb candibal.png` — 剧情故事书插画：candibal

### story_cg_02 · cg · 3×2 · 6 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb cattakeover.png` — 剧情故事书插画：cattakeover
- 01（0,1）：`images/sb climb.png` — 剧情故事书插画：climb
- 02（0,2）：`images/sb counter.png` — 剧情故事书插画：counter
- 03（1,0）：`images/sb creamilla.png` — 剧情故事书插画：creamilla
- 04（1,1）：`images/sb eatenaway1.png` — 剧情故事书插画：eatenaway1
- 05（1,2）：`images/sb eatenaway2.png` — 剧情故事书插画：eatenaway2

### story_cg_03 · cg · 3×2 · 6 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb escape.png` — 剧情故事书插画：escape
- 01（0,1）：`images/sb escape2.png` — 剧情故事书插画：escape2
- 02（0,2）：`images/sb fixd.png` — 剧情故事书插画：fixd
- 03（1,0）：`images/sb frozen.png` — 剧情故事书插画：frozen
- 04（1,1）：`images/sb gumend.png` — 剧情故事书插画：gumend
- 05（1,2）：`images/sb happyreturn.png` — 剧情故事书插画：happyreturn

### story_cg_04 · cg · 3×2 · 6 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb hitreat.png` — 剧情故事书插画：hitreat
- 01（0,1）：`images/sb homealone.png` — 剧情故事书插画：homealone
- 02（0,2）：`images/sb hometogether.png` — 剧情故事书插画：hometogether
- 03（1,0）：`images/sb newassistant.png` — 剧情故事书插画：newassistant
- 04（1,1）：`images/sb newassistant2.png` — 剧情故事书插画：newassistant2
- 05（1,2）：`images/sb pasend.png` — 剧情故事书插画：pasend

### story_cg_05 · cg · 3×2 · 6 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb search.png` — 剧情故事书插画：search
- 01（0,1）：`images/sb shop.png` — 剧情故事书插画：shop
- 02（0,2）：`images/sb sleep.png` — 剧情故事书插画：sleep
- 03（1,0）：`images/sb syrupend.png` — 剧情故事书插画：syrupend
- 04（1,1）：`images/sb tofend.png` — 剧情故事书插画：tofend
- 05（1,2）：`images/sb ultimatesweet.png` — 剧情故事书插画：ultimatesweet

### story_cg_06 · cg · 3×2 · 4 槽

3×2；每格保留独立剧情构图。最后不足 6 格留空，不减少原图。

- 00（0,0）：`images/sb unsleep.png` — 剧情故事书插画：unsleep
- 01（0,1）：`images/sb working.png` — 剧情故事书插画：working
- 02（0,2）：`images/sb working2.png` — 剧情故事书插画：working2
- 03（1,0）：`images/sb worstend.png` — 剧情故事书插画：worstend

### gallery_character_concepts · character · 3×3 · 9 槽

全新角色设计概念图；概念原稿仍逐项映射。

- 00（0,0）：`images/gallery/concept assistant.png` — 画廊角色概念设计图：assistant
- 01（0,1）：`images/gallery/concept candyalchemist.png` — 画廊角色概念设计图：candyalchemist
- 02（0,2）：`images/gallery/concept candygirl.png` — 画廊角色概念设计图：candygirl
- 03（1,0）：`images/gallery/concept cat.png` — 画廊角色概念设计图：cat
- 04（1,1）：`images/gallery/concept chocolate.png` — 画廊角色概念设计图：chocolate
- 05（1,2）：`images/gallery/concept saveher.png` — 画廊角色概念设计图：saveher
- 06（2,0）：`images/gallery/concept treat.png` — 画廊角色概念设计图：treat
- 07（2,1）：`images/gallery/concept uniform.png` — 画廊角色概念设计图：uniform
- 08（2,2）：`images/gallery/concept witch.png` — 画廊角色概念设计图：witch

### gallery_extra_01 · cg · 3×2 · 6 槽

附加插画亦重新创作；原 rough/doodle 保留草图语汇。

- 00（0,0）：`images/gallery/extra albumart.png` — 画廊附加插画：albumart
- 01（0,1）：`images/gallery/extra candyprint.png` — 画廊附加插画：candyprint
- 02（0,2）：`images/gallery/extra doodles.png` — 画廊附加插画：doodles
- 03（1,0）：`images/gallery/extra promo.png` — 画廊附加插画：promo
- 04（1,1）：`images/gallery/extra rough.png` — 画廊附加插画：rough
- 05（1,2）：`images/gallery/extra roughpromo.png` — 画廊附加插画：roughpromo

### gallery_extra_02 · cg · 3×2 · 3 槽

附加插画亦重新创作；原 rough/doodle 保留草图语汇。

- 00（0,0）：`images/gallery/extra shirt.png` — 画廊附加插画：shirt
- 01（0,1）：`images/gallery/extra toffee1.png` — 画廊附加插画：toffee1
- 02（0,2）：`images/gallery/extra toffee2.png` — 画廊附加插画：toffee2

### ui_bars_and_sliders · ui · 7×6 · 40 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。通用几何/字母细节可运行时绘制，生图负责统一装饰风格。

- 00（0,0）：`gui/bar/bottom.png` — 进度条分段
- 01（0,1）：`gui/bar/left.png` — 进度条分段
- 02（0,2）：`gui/bar/right.png` — 进度条分段
- 03（0,3）：`gui/bar/top.png` — 进度条分段
- 04（0,4）：`gui/phone/bar/bottom.png` — 进度条分段
- 05（0,5）：`gui/phone/bar/left.png` — 进度条分段
- 06（0,6）：`gui/phone/bar/right.png` — 进度条分段
- 07（1,0）：`gui/phone/bar/top.png` — 进度条分段
- 08（1,1）：`gui/phone/scrollbar/horizontal_hover_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 09（1,2）：`gui/phone/scrollbar/horizontal_hover_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 10（1,3）：`gui/phone/scrollbar/horizontal_idle_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 11（1,4）：`gui/phone/scrollbar/horizontal_idle_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 12（1,5）：`gui/phone/scrollbar/vertical_hover_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 13（1,6）：`gui/phone/scrollbar/vertical_hover_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 14（2,0）：`gui/phone/scrollbar/vertical_idle_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 15（2,1）：`gui/phone/scrollbar/vertical_idle_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 16（2,2）：`gui/phone/slider/horizontal_hover_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 17（2,3）：`gui/phone/slider/horizontal_hover_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 18（2,4）：`gui/phone/slider/horizontal_idle_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 19（2,5）：`gui/phone/slider/horizontal_idle_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 20（2,6）：`gui/phone/slider/vertical_hover_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 21（3,0）：`gui/phone/slider/vertical_hover_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 22（3,1）：`gui/phone/slider/vertical_idle_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 23（3,2）：`gui/phone/slider/vertical_idle_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 24（3,3）：`gui/scrollbar/horizontal_hover_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 25（3,4）：`gui/scrollbar/horizontal_hover_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 26（3,5）：`gui/scrollbar/horizontal_idle_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 27（3,6）：`gui/scrollbar/horizontal_idle_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 28（4,0）：`gui/scrollbar/vertical_hover_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 29（4,1）：`gui/scrollbar/vertical_hover_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 30（4,2）：`gui/scrollbar/vertical_idle_bar.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 31（4,3）：`gui/scrollbar/vertical_idle_thumb.png` — 滚动条的横/竖、悬停/静止、轨道/滑块
- 32（4,4）：`gui/slider/horizontal_hover_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 33（4,5）：`gui/slider/horizontal_hover_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 34（4,6）：`gui/slider/horizontal_idle_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 35（5,0）：`gui/slider/horizontal_idle_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 36（5,1）：`gui/slider/vertical_hover_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 37（5,2）：`gui/slider/vertical_hover_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 38（5,3）：`gui/slider/vertical_idle_bar.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块
- 39（5,4）：`gui/slider/vertical_idle_thumb.png` — 设置滑条的横/竖、悬停/静止、轨道/滑块

### ui_buttons · ui · 7×6 · 39 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。

- 00（0,0）：`gui/button/check_foreground.png` — 按钮背景、选中标记或导航图标
- 01（0,1）：`gui/button/check_selected_foreground.png` — 按钮背景、选中标记或导航图标
- 02（0,2）：`gui/button/choice_hover_background.png` — 按钮背景、选中标记或导航图标
- 03（0,3）：`gui/button/choice_idle_background.png` — 按钮背景、选中标记或导航图标
- 04（0,4）：`gui/button/filepagebuttonl_hover.png` — 按钮背景、选中标记或导航图标
- 05（0,5）：`gui/button/filepagebuttonl_idle.png` — 按钮背景、选中标记或导航图标
- 06（0,6）：`gui/button/filepagebuttonl_insensitive.png` — 按钮背景、选中标记或导航图标
- 07（1,0）：`gui/button/filepagebuttonr_hover.png` — 按钮背景、选中标记或导航图标
- 08（1,1）：`gui/button/filepagebuttonr_idle.png` — 按钮背景、选中标记或导航图标
- 09（1,2）：`gui/button/filepagebuttonr_insensitive.png` — 按钮背景、选中标记或导航图标
- 10（1,3）：`gui/button/hebrew_hover.png` — 按钮背景、选中标记或导航图标
- 11（1,4）：`gui/button/hebrew_idle.png` — 按钮背景、选中标记或导航图标
- 12（1,5）：`gui/button/hebrew_selected_hover.png` — 按钮背景、选中标记或导航图标
- 13（1,6）：`gui/button/hebrew_selected_idle.png` — 按钮背景、选中标记或导航图标
- 14（2,0）：`gui/button/helpme_hover.png` — 按钮背景、选中标记或导航图标
- 15（2,1）：`gui/button/helpme_idle.png` — 按钮背景、选中标记或导航图标
- 16（2,2）：`gui/button/hover_background.png` — 按钮背景、选中标记或导航图标
- 17（2,3）：`gui/button/idle_background.png` — 按钮背景、选中标记或导航图标
- 18（2,4）：`gui/button/mute_hover.png` — 按钮背景、选中标记或导航图标
- 19（2,5）：`gui/button/mute_idle.png` — 按钮背景、选中标记或导航图标
- 20（2,6）：`gui/button/mute_selected_idle.png` — 按钮背景、选中标记或导航图标
- 21（3,0）：`gui/button/quick_hover_background.png` — 按钮背景、选中标记或导航图标
- 22（3,1）：`gui/button/quick_idle_background.png` — 按钮背景、选中标记或导航图标
- 23（3,2）：`gui/button/radio_foreground.png` — 按钮背景、选中标记或导航图标
- 24（3,3）：`gui/button/radio_selected_foreground.png` — 按钮背景、选中标记或导航图标
- 25（3,4）：`gui/button/slot_hover_background.png` — 按钮背景、选中标记或导航图标
- 26（3,5）：`gui/button/slot_idle_background.png` — 按钮背景、选中标记或导航图标
- 27（3,6）：`gui/phone/button/check_foreground.png` — 按钮背景、选中标记或导航图标
- 28（4,0）：`gui/phone/button/check_selected_foreground.png` — 按钮背景、选中标记或导航图标
- 29（4,1）：`gui/phone/button/choice_hover_background.png` — 按钮背景、选中标记或导航图标
- 30（4,2）：`gui/phone/button/choice_idle_background.png` — 按钮背景、选中标记或导航图标
- 31（4,3）：`gui/phone/button/hover_background.png` — 按钮背景、选中标记或导航图标
- 32（4,4）：`gui/phone/button/idle_background.png` — 按钮背景、选中标记或导航图标
- 33（4,5）：`gui/phone/button/mygames_idle.png` — 按钮背景、选中标记或导航图标
- 34（4,6）：`gui/phone/button/mygames_idle0.png` — 按钮背景、选中标记或导航图标
- 35（5,0）：`gui/phone/button/radio_foreground.png` — 按钮背景、选中标记或导航图标
- 36（5,1）：`gui/phone/button/radio_selected_foreground.png` — 按钮背景、选中标记或导航图标
- 37（5,2）：`gui/phone/button/slot_hover_background.png` — 按钮背景、选中标记或导航图标
- 38（5,3）：`gui/phone/button/slot_idle_background.png` — 按钮背景、选中标记或导航图标

### ui_controller_glyphs · ui · 7×6 · 42 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。通用几何/字母细节可运行时绘制，生图负责统一装饰风格。

- 00（0,0）：`gui/button/console/face_empty.png` — 手柄按键提示图标
- 01（0,1）：`gui/button/console/ps4_L1.png` — 手柄按键提示图标
- 02（0,2）：`gui/button/console/ps4_L2.png` — 手柄按键提示图标
- 03（0,3）：`gui/button/console/ps4_opt.png` — 手柄按键提示图标
- 04（0,4）：`gui/button/console/ps4_R1.png` — 手柄按键提示图标
- 05（0,5）：`gui/button/console/ps4_R2.png` — 手柄按键提示图标
- 06（0,6）：`gui/button/console/ps4_touch.png` — 手柄按键提示图标
- 07（1,0）：`gui/button/console/ps_dpad.png` — 手柄按键提示图标
- 08（1,1）：`gui/button/console/ps_o.png` — 手柄按键提示图标
- 09（1,2）：`gui/button/console/ps_sq.png` — 手柄按键提示图标
- 10（1,3）：`gui/button/console/ps_tri.png` — 手柄按键提示图标
- 11（1,4）：`gui/button/console/ps_x.png` — 手柄按键提示图标
- 12（1,5）：`gui/button/console/switch_a.png` — 手柄按键提示图标
- 13（1,6）：`gui/button/console/switch_b.png` — 手柄按键提示图标
- 14（2,0）：`gui/button/console/switch_dpad.png` — 手柄按键提示图标
- 15（2,1）：`gui/button/console/switch_l.png` — 手柄按键提示图标
- 16（2,2）：`gui/button/console/switch_minus.png` — 手柄按键提示图标
- 17（2,3）：`gui/button/console/switch_plus.png` — 手柄按键提示图标
- 18（2,4）：`gui/button/console/switch_r.png` — 手柄按键提示图标
- 19（2,5）：`gui/button/console/switch_x.png` — 手柄按键提示图标
- 20（2,6）：`gui/button/console/switch_y.png` — 手柄按键提示图标
- 21（3,0）：`gui/button/console/switch_zl.png` — 手柄按键提示图标
- 22（3,1）：`gui/button/console/switch_zr.png` — 手柄按键提示图标
- 23（3,2）：`gui/button/console/vita_l.png` — 手柄按键提示图标
- 24（3,3）：`gui/button/console/vita_o.png` — 手柄按键提示图标
- 25（3,4）：`gui/button/console/vita_r.png` — 手柄按键提示图标
- 26（3,5）：`gui/button/console/vita_select.png` — 手柄按键提示图标
- 27（3,6）：`gui/button/console/vita_sq.png` — 手柄按键提示图标
- 28（4,0）：`gui/button/console/vita_start.png` — 手柄按键提示图标
- 29（4,1）：`gui/button/console/vita_tri.png` — 手柄按键提示图标
- 30（4,2）：`gui/button/console/vita_x.png` — 手柄按键提示图标
- 31（4,3）：`gui/button/console/xbox_a.png` — 手柄按键提示图标
- 32（4,4）：`gui/button/console/xbox_b.png` — 手柄按键提示图标
- 33（4,5）：`gui/button/console/xbox_dpad.png` — 手柄按键提示图标
- 34（4,6）：`gui/button/console/xbox_lb.png` — 手柄按键提示图标
- 35（5,0）：`gui/button/console/xbox_lt.png` — 手柄按键提示图标
- 36（5,1）：`gui/button/console/xbox_menu.png` — 手柄按键提示图标
- 37（5,2）：`gui/button/console/xbox_nav.png` — 手柄按键提示图标
- 38（5,3）：`gui/button/console/xbox_rb.png` — 手柄按键提示图标
- 39（5,4）：`gui/button/console/xbox_rt.png` — 手柄按键提示图标
- 40（5,5）：`gui/button/console/xbox_x.png` — 手柄按键提示图标
- 41（5,6）：`gui/button/console/xbox_y.png` — 手柄按键提示图标

### ui_panels_and_screens · ui · 6×5 · 28 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。

- 00（0,0）：`gui/confirm_frame.png` — 确认弹窗边框
- 01（0,1）：`gui/frame.png` — 通用边框
- 02（0,2）：`gui/frame2.png` — 第二种通用边框
- 03（0,3）：`gui/game_menu.png` — 存读档/设置通用菜单底图
- 04（0,4）：`gui/history.png` — 历史/图库面板纹理
- 05（0,5）：`gui/main_menu.png` — 主菜单底图
- 06（1,0）：`gui/namebox.png` — 说话者姓名框
- 07（1,1）：`gui/notify.png` — 通知条
- 08（1,2）：`gui/nvl.png` — 整屏叙述框
- 09（1,3）：`gui/overlay/confirm.png` — 菜单或确认框遮罩
- 10（1,4）：`gui/overlay/game_menu.png` — 菜单或确认框遮罩
- 11（1,5）：`gui/overlay/main_menu.png` — 菜单或确认框遮罩
- 12（2,0）：`gui/phone/nvl.png` — 整屏叙述框
- 13（2,1）：`gui/phone/overlay/game_menu.png` — 菜单或确认框遮罩
- 14（2,2）：`gui/phone/overlay/main_menu.png` — 菜单或确认框遮罩
- 15（2,3）：`gui/phone/textbox.png` — 底部对话框
- 16（2,4）：`gui/phone/textbox0.png` — 旧版移动端对话框
- 17（2,5）：`gui/skip.png` — 快进提示框
- 18（3,0）：`gui/textbox.png` — 底部对话框
- 19（3,1）：`gui/window_icon.png` — 程序图标
- 20（3,2）：`images/bg black.png` — 深蓝灰转场底
- 21（3,3）：`images/gallery/galframe_hover.png` — 背景画廊边框/锁定图
- 22（3,4）：`images/gallery/galframe_idle.png` — 背景画廊边框/锁定图
- 23（3,5）：`images/gallery/galframe_insensitive.png` — 背景画廊边框/锁定图
- 24（4,0）：`images/sb locked.png` — 未解锁剧情插画占位图
- 25（4,1）：`images/splash.jpg` — 启动画面
- 26（4,2）：`images/storybook.jpg` — 故事书/画廊背景
- 27（4,3）：`images/storybook2.jpg` — 故事书另一背景

### ui_menu_animation · ui · 2×2 · 3 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。

- 00（0,0）：`images/ani1.png` — 主菜单循环底部动画第 1 帧
- 01（0,1）：`images/ani2.png` — 主菜单循环底部动画第 2 帧
- 02（1,0）：`images/ani3.png` — 主菜单循环底部动画第 3 帧

### ui_effects · ui · 3×3 · 8 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。

- 00（0,0）：`images/clouds.png` — 主菜单平移云层
- 01（0,1）：`images/flowers1.png` — 花瓣魔法粒子
- 02（0,2）：`images/flowers2.png` — 花瓣魔法粒子
- 03（1,0）：`images/flowers3.png` — 花瓣魔法粒子
- 04（1,1）：`images/light1.png` — 光芒魔法粒子
- 05（1,2）：`images/light2.png` — 光芒魔法粒子
- 06（2,0）：`images/light3.png` — 光芒魔法粒子
- 07（2,1）：`images/pastfilter.png` — 回忆场景全屏滤镜

### ui_gallery_thumbnails_derived · ui · 3×2 · 6 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。从新背景同 UV 派生，无需另一次生图。

- 00（0,0）：`images/gallery/gal_cabin.jpg` — 背景画廊缩略图：cabin
- 01（0,1）：`images/gallery/gal_cottage.jpg` — 背景画廊缩略图：cottage
- 02（0,2）：`images/gallery/gal_lab.jpg` — 背景画廊缩略图：lab
- 03（1,0）：`images/gallery/gal_market.jpg` — 背景画廊缩略图：market
- 04（1,1）：`images/gallery/gal_mountain.jpg` — 背景画廊缩略图：mountain
- 05（1,2）：`images/gallery/gal_shop.jpg` — 背景画廊缩略图：shop

### ui_menu_portraits · ui · 4×3 · 10 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。

- 00（0,0）：`images/mmbs.png` — 主菜单 Butterscotch 默认立绘
- 01（0,1）：`images/mmbs2.png` — 主菜单 Butterscotch 结局完成立绘
- 02（0,2）：`images/mmgum.png` — 主菜单 Gumdrop 默认立绘
- 03（0,3）：`images/mmgum2.png` — 主菜单 Gumdrop 结局完成立绘
- 04（1,0）：`images/mmpas.png` — 主菜单 Pastille 默认立绘
- 05（1,1）：`images/mmpas2.png` — 主菜单 Pastille 结局完成立绘
- 06（1,2）：`images/mmsyrup.png` — 主菜单 Syrup 默认立绘
- 07（1,3）：`images/mmsyrup2.png` — 主菜单 Syrup 结局完成立绘
- 08（2,0）：`images/mmtof.png` — 主菜单 Toffee 默认立绘
- 09（2,1）：`images/mmtof2.png` — 主菜单 Toffee 结局完成立绘

### ui_title_and_locale_text · ui · 4×3 · 12 槽

保留全部源路径/状态；完全相同像素可映射同一新图格。统一新标题装饰底，简中文字用运行时字体绘制；其他语言只保留清单，中文版不加载。

- 00（0,0）：`images/title.png` — 英文主标题装饰字图
- 01（0,1）：`tl/chinese/images/title.png` — 简体中文标题字图
- 02（0,2）：`tl/de/images/cred2.png` — de 本地化制作人员名单图
- 03（0,3）：`tl/es/images/cred.png` — es 本地化制作人员名单图
- 04（1,0）：`tl/es/images/cred2.png` — es 本地化制作人员名单图
- 05（1,1）：`tl/es/images/title.png` — es 本地化标题图
- 06（1,2）：`tl/fr/images/cred2.png` — fr 本地化制作人员名单图
- 07（1,3）：`tl/fr/images/title.png` — fr 本地化标题图
- 08（2,0）：`tl/japanese/images/title.png` — japanese 本地化标题图
- 09（2,1）：`tl/kr/images/title.png` — kr 本地化标题图
- 10（2,2）：`tl/por/images/cred2.png` — por 本地化制作人员名单图
- 11（2,3）：`tl/por/images/title.png` — por 本地化标题图

## 完整逐文件清单

更完整的模式、尺寸、SHA256、像素哈希、所有源码使用点与图集 UV 坐标见同名 JSON。

| 路径 | 用途分类 | 尺寸/模式 | 使用点（首个） | 重复/派生 |
|---|---|---|---|---|
| `gui/bar/bottom.png` | gui_component/bar | 25×350 RGBA | screens.rpy:57 `explicit_file` | `` |
| `gui/bar/left.png` | gui_component/bar | 350×25 RGBA | screens.rpy:51 `explicit_file` | `` |
| `gui/bar/right.png` | gui_component/bar | 350×25 RGBA | screens.rpy:52 `explicit_file` | `` |
| `gui/bar/top.png` | gui_component/bar | 25×350 RGBA | screens.rpy:56 `explicit_file` | `` |
| `gui/button/check_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:938 `gui_state_pattern` | `` |
| `gui/button/check_selected_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:938 `gui_state_pattern` | `` |
| `gui/button/choice_hover_background.png` | gui_component/button | 272×60 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/button/choice_idle_background.png` | gui_component/button | 272×60 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/button/console/face_empty.png` | gui_component/controller_glyph | 32×32 RGBA | packaged_no_static_reference | `` |
| `gui/button/console/ps4_L1.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:498 `explicit_file` | `` |
| `gui/button/console/ps4_L2.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:499 `explicit_file` | `` |
| `gui/button/console/ps4_opt.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:502 `explicit_file` | `` |
| `gui/button/console/ps4_R1.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:500 `explicit_file` | `` |
| `gui/button/console/ps4_R2.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:501 `explicit_file` | `` |
| `gui/button/console/ps4_touch.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:503 `explicit_file` | `` |
| `gui/button/console/ps_dpad.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:492 `explicit_file` | `` |
| `gui/button/console/ps_o.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:494 `explicit_file` | `` |
| `gui/button/console/ps_sq.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:496 `explicit_file` | `` |
| `gui/button/console/ps_tri.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:495 `explicit_file` | `` |
| `gui/button/console/ps_x.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:493 `explicit_file` | `` |
| `gui/button/console/switch_a.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:516 `explicit_file` | `` |
| `gui/button/console/switch_b.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:517 `explicit_file` | `` |
| `gui/button/console/switch_dpad.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:515 `explicit_file` | `` |
| `gui/button/console/switch_l.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:521 `explicit_file` | `` |
| `gui/button/console/switch_minus.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:526 `explicit_file` | `` |
| `gui/button/console/switch_plus.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:525 `explicit_file` | `` |
| `gui/button/console/switch_r.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:523 `explicit_file` | `` |
| `gui/button/console/switch_x.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:518 `explicit_file` | `` |
| `gui/button/console/switch_y.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:519 `explicit_file` | `` |
| `gui/button/console/switch_zl.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:522 `explicit_file` | `` |
| `gui/button/console/switch_zr.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:524 `explicit_file` | `` |
| `gui/button/console/vita_l.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:510 `explicit_file` | `` |
| `gui/button/console/vita_o.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:506 `explicit_file` | `` |
| `gui/button/console/vita_r.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:511 `explicit_file` | `` |
| `gui/button/console/vita_select.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:513 `explicit_file` | `` |
| `gui/button/console/vita_sq.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:508 `explicit_file` | `` |
| `gui/button/console/vita_start.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:512 `explicit_file` | `` |
| `gui/button/console/vita_tri.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:507 `explicit_file` | `` |
| `gui/button/console/vita_x.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:505 `explicit_file` | `` |
| `gui/button/console/xbox_a.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:535 `explicit_file` | `` |
| `gui/button/console/xbox_b.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:536 `explicit_file` | `` |
| `gui/button/console/xbox_dpad.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:530 `explicit_file` | `` |
| `gui/button/console/xbox_lb.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:531 `explicit_file` | `` |
| `gui/button/console/xbox_lt.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:533 `explicit_file` | `` |
| `gui/button/console/xbox_menu.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:528 `explicit_file` | `` |
| `gui/button/console/xbox_nav.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:529 `explicit_file` | `` |
| `gui/button/console/xbox_rb.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:532 `explicit_file` | `` |
| `gui/button/console/xbox_rt.png` | gui_component/controller_glyph | 42×32 RGBA | definitions.rpy:534 `explicit_file` | `` |
| `gui/button/console/xbox_x.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:537 `explicit_file` | `` |
| `gui/button/console/xbox_y.png` | gui_component/controller_glyph | 32×32 RGBA | definitions.rpy:538 `explicit_file` | `` |
| `gui/button/filepagebuttonl_hover.png` | gui_component/button | 78×413 RGBA | gallery.rpy:287 `gui_state_pattern` | `` |
| `gui/button/filepagebuttonl_idle.png` | gui_component/button | 78×413 RGBA | gallery.rpy:287 `gui_state_pattern` | `` |
| `gui/button/filepagebuttonl_insensitive.png` | gui_component/button | 78×413 RGBA | gallery.rpy:287 `gui_state_pattern` | `` |
| `gui/button/filepagebuttonr_hover.png` | gui_component/button | 78×413 RGBA | gallery.rpy:297 `gui_state_pattern` | `` |
| `gui/button/filepagebuttonr_idle.png` | gui_component/button | 78×413 RGBA | gallery.rpy:297 `gui_state_pattern` | `` |
| `gui/button/filepagebuttonr_insensitive.png` | gui_component/button | 78×413 RGBA | gallery.rpy:297 `gui_state_pattern` | `` |
| `gui/button/hebrew_hover.png` | gui_component/button | 136×52 RGBA | tl.rpy:21 `gui_state_pattern` | `` |
| `gui/button/hebrew_idle.png` | gui_component/button | 136×52 RGBA | tl.rpy:21 `gui_state_pattern` | `` |
| `gui/button/hebrew_selected_hover.png` | gui_component/button | 136×52 RGBA | tl.rpy:21 `gui_state_pattern` | `` |
| `gui/button/hebrew_selected_idle.png` | gui_component/button | 136×52 RGBA | tl.rpy:21 `gui_state_pattern` | `` |
| `gui/button/helpme_hover.png` | gui_component/button | 55×54 RGBA | screens.rpy:337 `gui_state_pattern` | `` |
| `gui/button/helpme_idle.png` | gui_component/button | 55×54 RGBA | screens.rpy:337 `gui_state_pattern` | `` |
| `gui/button/hover_background.png` | gui_component/button | 300×33 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/button/idle_background.png` | gui_component/button | 300×33 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/hover_background.png` |
| `gui/button/mute_hover.png` | gui_component/button | 62×63 RGBA | screens.rpy:872 `gui_state_pattern` | `` |
| `gui/button/mute_idle.png` | gui_component/button | 62×63 RGBA | screens.rpy:872 `gui_state_pattern` | `` |
| `gui/button/mute_selected_idle.png` | gui_component/button | 62×63 RGBA | screens.rpy:872 `gui_state_pattern` | `` |
| `gui/button/quick_hover_background.png` | gui_component/button | 100×30 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/button/quick_idle_background.png` | gui_component/button | 100×30 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/quick_hover_background.png` |
| `gui/button/radio_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:925 `gui_state_pattern` | `gui/button/check_foreground.png` |
| `gui/button/radio_selected_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:925 `gui_state_pattern` | `gui/button/check_selected_foreground.png` |
| `gui/button/slot_hover_background.png` | gui_component/button | 276×206 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/button/slot_idle_background.png` | gui_component/button | 276×206 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/confirm_frame.png` | gui_component/panel_frame | 600×250 RGBA | screens.rpy:1286 `explicit_file` | `` |
| `gui/frame.png` | gui_component/panel_frame | 600×250 RGBA | screens.rpy:82 `explicit_file` | `` |
| `gui/frame2.png` | gui_component/panel_frame | 600×250 RGBA | gallery.rpy:61 `explicit_file` | `` |
| `gui/game_menu.png` | gui_component/menu_background | 1280×720 RGBA | gui.rpy:101 `explicit_file` | `` |
| `gui/history.png` | gui_component/panel_tile | 55×48 RGBA | gallery.rpy:106 `explicit_file` | `` |
| `gui/main_menu.png` | gui_component/menu_background | 1280×720 RGBA | gui.rpy:100 `explicit_file` | `` |
| `gui/namebox.png` | gui_component/name_box | 272×60 RGBA | screens.rpy:154 `explicit_file` | `gui/button/choice_idle_background.png` |
| `gui/notify.png` | gui_component/notification | 526×66 RGBA | screens.rpy:1372 `explicit_file` | `` |
| `gui/nvl.png` | gui_component/nvl_background | 1280×720 RGBA | screens.rpy:1474 `explicit_file` | `` |
| `gui/overlay/confirm.png` | gui_component/overlay | 1280×720 RGBA | screens.rpy:1255 `explicit_file` | `gui/game_menu.png` |
| `gui/overlay/game_menu.png` | gui_component/overlay | 1280×720 RGBA | packaged_no_static_reference | `gui/nvl.png` |
| `gui/overlay/main_menu.png` | gui_component/overlay | 1280×720 RGBA | screens.rpy:431 `explicit_file` | `gui/nvl.png` |
| `gui/phone/bar/bottom.png` | gui_component/bar | 25×350 RGBA | screens.rpy:1781 `explicit_file` | `gui/bar/bottom.png` |
| `gui/phone/bar/left.png` | gui_component/bar | 350×25 RGBA | screens.rpy:1774 `explicit_file` | `gui/bar/left.png` |
| `gui/phone/bar/right.png` | gui_component/bar | 350×25 RGBA | screens.rpy:1775 `explicit_file` | `gui/bar/right.png` |
| `gui/phone/bar/top.png` | gui_component/bar | 25×350 RGBA | screens.rpy:1780 `explicit_file` | `gui/bar/top.png` |
| `gui/phone/button/check_foreground.png` | gui_component/button | 18×43 RGBA | screens.rpy:1757 `gui_state_pattern` | `` |
| `gui/phone/button/check_selected_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:1757 `gui_state_pattern` | `` |
| `gui/phone/button/choice_hover_background.png` | gui_component/button | 272×60 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/choice_hover_background.png` |
| `gui/phone/button/choice_idle_background.png` | gui_component/button | 272×60 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/choice_idle_background.png` |
| `gui/phone/button/hover_background.png` | gui_component/button | 220×43 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/phone/button/idle_background.png` | gui_component/button | 220×43 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/phone/button/hover_background.png` |
| `gui/phone/button/mygames_idle.png` | gui_component/button | 120×120 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/phone/button/mygames_idle0.png` | gui_component/button | 120×120 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `` |
| `gui/phone/button/radio_foreground.png` | gui_component/button | 18×43 RGBA | screens.rpy:1753 `gui_state_pattern` | `gui/phone/button/check_foreground.png` |
| `gui/phone/button/radio_selected_foreground.png` | gui_component/button | 18×33 RGBA | screens.rpy:1753 `gui_state_pattern` | `gui/phone/button/check_selected_foreground.png` |
| `gui/phone/button/slot_hover_background.png` | gui_component/button | 276×206 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/slot_hover_background.png` |
| `gui/phone/button/slot_idle_background.png` | gui_component/button | 276×206 RGBA | screens.rpy:30 `implicit_gui_style_or_packaged_variant` | `gui/button/slot_idle_background.png` |
| `gui/phone/nvl.png` | gui_component/nvl_background | 1280×720 RGBA | screens.rpy:1761 `explicit_file` | `gui/nvl.png` |
| `gui/phone/overlay/game_menu.png` | gui_component/overlay | 1280×720 RGBA | packaged_no_static_reference | `gui/nvl.png` |
| `gui/phone/overlay/main_menu.png` | gui_component/overlay | 1280×720 RGBA | screens.rpy:1765 `explicit_file` | `gui/nvl.png` |
| `gui/phone/scrollbar/horizontal_hover_bar.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:1786 `gui_state_pattern` | `` |
| `gui/phone/scrollbar/horizontal_hover_thumb.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:1787 `gui_state_pattern` | `` |
| `gui/phone/scrollbar/horizontal_idle_bar.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:1786 `gui_state_pattern` | `` |
| `gui/phone/scrollbar/horizontal_idle_thumb.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:1787 `gui_state_pattern` | `gui/phone/scrollbar/horizontal_hover_thumb.png` |
| `gui/phone/scrollbar/vertical_hover_bar.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:1792 `gui_state_pattern` | `` |
| `gui/phone/scrollbar/vertical_hover_thumb.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:1793 `gui_state_pattern` | `` |
| `gui/phone/scrollbar/vertical_idle_bar.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:1792 `gui_state_pattern` | `gui/phone/scrollbar/vertical_hover_bar.png` |
| `gui/phone/scrollbar/vertical_idle_thumb.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:1793 `gui_state_pattern` | `` |
| `gui/phone/slider/horizontal_hover_bar.png` | gui_component/slider | 350×36 RGBA | screens.rpy:1798 `gui_state_pattern` | `` |
| `gui/phone/slider/horizontal_hover_thumb.png` | gui_component/slider | 15×36 RGBA | screens.rpy:1799 `gui_state_pattern` | `` |
| `gui/phone/slider/horizontal_idle_bar.png` | gui_component/slider | 350×36 RGBA | screens.rpy:1798 `gui_state_pattern` | `` |
| `gui/phone/slider/horizontal_idle_thumb.png` | gui_component/slider | 15×36 RGBA | screens.rpy:1799 `gui_state_pattern` | `gui/phone/slider/horizontal_hover_thumb.png` |
| `gui/phone/slider/vertical_hover_bar.png` | gui_component/slider | 36×350 RGBA | screens.rpy:1804 `gui_state_pattern` | `` |
| `gui/phone/slider/vertical_hover_thumb.png` | gui_component/slider | 36×15 RGBA | screens.rpy:1805 `gui_state_pattern` | `` |
| `gui/phone/slider/vertical_idle_bar.png` | gui_component/slider | 36×350 RGBA | screens.rpy:1804 `gui_state_pattern` | `` |
| `gui/phone/slider/vertical_idle_thumb.png` | gui_component/slider | 36×15 RGBA | screens.rpy:1805 `gui_state_pattern` | `gui/phone/slider/vertical_hover_thumb.png` |
| `gui/phone/textbox.png` | gui_component/dialogue_box | 1280×185 RGBA | screens.rpy:1749 `explicit_file` | `` |
| `gui/phone/textbox0.png` | gui_component/dialogue_box_legacy | 1280×240 RGBA | packaged_no_static_reference | `` |
| `gui/scrollbar/horizontal_hover_bar.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:61 `gui_state_pattern` | `gui/phone/scrollbar/horizontal_hover_bar.png` |
| `gui/scrollbar/horizontal_hover_thumb.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:62 `gui_state_pattern` | `gui/phone/scrollbar/horizontal_hover_thumb.png` |
| `gui/scrollbar/horizontal_idle_bar.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:61 `gui_state_pattern` | `gui/phone/scrollbar/horizontal_idle_bar.png` |
| `gui/scrollbar/horizontal_idle_thumb.png` | gui_component/scrollbar | 700×12 RGBA | screens.rpy:62 `gui_state_pattern` | `gui/phone/scrollbar/horizontal_hover_thumb.png` |
| `gui/scrollbar/vertical_hover_bar.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:66 `gui_state_pattern` | `gui/phone/scrollbar/vertical_hover_bar.png` |
| `gui/scrollbar/vertical_hover_thumb.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:67 `gui_state_pattern` | `gui/phone/scrollbar/vertical_hover_thumb.png` |
| `gui/scrollbar/vertical_idle_bar.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:66 `gui_state_pattern` | `gui/phone/scrollbar/vertical_hover_bar.png` |
| `gui/scrollbar/vertical_idle_thumb.png` | gui_component/scrollbar | 12×700 RGBA | screens.rpy:67 `gui_state_pattern` | `gui/phone/scrollbar/vertical_idle_thumb.png` |
| `gui/skip.png` | gui_component/skip_indicator | 240×43 RGBA | screens.rpy:1349 `explicit_file` | `` |
| `gui/slider/horizontal_hover_bar.png` | gui_component/slider | 224×40 RGBA | screens.rpy:71 `gui_state_pattern` | `` |
| `gui/slider/horizontal_hover_thumb.png` | gui_component/slider | 36×42 RGBA | screens.rpy:72 `gui_state_pattern` | `` |
| `gui/slider/horizontal_idle_bar.png` | gui_component/slider | 224×40 RGBA | screens.rpy:71 `gui_state_pattern` | `` |
| `gui/slider/horizontal_idle_thumb.png` | gui_component/slider | 36×42 RGBA | screens.rpy:72 `gui_state_pattern` | `gui/slider/horizontal_hover_thumb.png` |
| `gui/slider/vertical_hover_bar.png` | gui_component/slider | 25×350 RGBA | screens.rpy:76 `gui_state_pattern` | `` |
| `gui/slider/vertical_hover_thumb.png` | gui_component/slider | 25×10 RGBA | screens.rpy:77 `gui_state_pattern` | `` |
| `gui/slider/vertical_idle_bar.png` | gui_component/slider | 25×350 RGBA | screens.rpy:76 `gui_state_pattern` | `gui/bar/top.png` |
| `gui/slider/vertical_idle_thumb.png` | gui_component/slider | 25×10 RGBA | screens.rpy:77 `gui_state_pattern` | `gui/slider/vertical_hover_thumb.png` |
| `gui/textbox.png` | gui_component/dialogue_box | 1280×185 RGBA | screens.rpy:145 `explicit_file` | `gui/phone/textbox.png` |
| `gui/window_icon.png` | gui_component/app_icon | 250×250 RGBA | options.rpy:161 `explicit_file` | `` |
| `images/ani1.png` | menu_animation/animated_landscape_strip | 1280×219 P | definitions.rpy:25 `automatic_image_name` | `` |
| `images/ani2.png` | menu_animation/animated_landscape_strip | 1280×219 P | definitions.rpy:27 `automatic_image_name` | `` |
| `images/ani3.png` | menu_animation/animated_landscape_strip | 1280×219 P | definitions.rpy:29 `automatic_image_name` | `` |
| `images/bg black.png` | solid_background/transition | 1280×720 P | script.rpy:94 `show_scene` | `` |
| `images/bg cabin.jpg` | background/scene | 1280×720 RGB | gallery.rpy:35 `automatic_image_name` | `` |
| `images/bg cottage.jpg` | background/scene | 1280×720 RGB | gallery.rpy:18 `automatic_image_name` | `` |
| `images/bg cottagedoor.jpg` | background/scene | 1280×720 RGB | gallery.rpy:19 `automatic_image_name` | `` |
| `images/bg cottageint.jpg` | background/scene | 1280×720 RGB | gallery.rpy:20 `automatic_image_name` | `` |
| `images/bg icecave.jpg` | background/scene | 1280×720 RGB | gallery.rpy:31 `automatic_image_name` | `` |
| `images/bg icecave2.jpg` | background/scene | 1280×720 RGB | gallery.rpy:32 `automatic_image_name` | `` |
| `images/bg lab.png` | background/scene | 1280×720 RGB | gallery.rpy:10 `automatic_image_name` | `` |
| `images/bg library.jpg` | background/scene | 1280×720 RGB | gallery.rpy:26 `automatic_image_name` | `` |
| `images/bg market.jpg` | background/scene | 1280×720 RGB | gallery.rpy:25 `automatic_image_name` | `` |
| `images/bg mountain.jpg` | background/scene | 1280×720 RGB | gallery.rpy:29 `automatic_image_name` | `` |
| `images/bg nightcottage.jpg` | background/scene | 1280×720 RGB | gallery.rpy:21 `automatic_image_name` | `` |
| `images/bg nightshop.jpg` | background/scene | 1280×720 RGB | gallery.rpy:15 `automatic_image_name` | `` |
| `images/bg shop.jpg` | background/scene | 1280×720 RGB | gallery.rpy:13 `automatic_image_name` | `` |
| `images/bg shop2.jpg` | background/scene | 1280×720 RGB | gallery.rpy:14 `automatic_image_name` | `` |
| `images/bg shopext.jpg` | background/scene | 1280×720 RGB | gallery.rpy:24 `automatic_image_name` | `` |
| `images/bg snow.jpg` | background/scene | 1280×720 RGB | gallery.rpy:30 `automatic_image_name` | `` |
| `images/bs aaa.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:685 `show_scene` | `` |
| `images/bs awchub.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:446 `automatic_image_name` | `` |
| `images/bs bawchub.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2772 `dialogue_image_attribute` | `` |
| `images/bs brag.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:439 `automatic_image_name` | `` |
| `images/bs castin.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:441 `automatic_image_name` | `` |
| `images/bs chub.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2459 `dialogue_image_attribute` | `` |
| `images/bs chubtears.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2512 `dialogue_image_attribute` | `` |
| `images/bs cold.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:146 `automatic_image_name` | `` |
| `images/bs coldeheh.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:149 `automatic_image_name` | `` |
| `images/bs coldfreakinout.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2225 `show_scene` | `` |
| `images/bs coldgrr.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:140 `automatic_image_name` | `` |
| `images/bs coldmad.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2259 `show_scene` | `` |
| `images/bs coldpathetic.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:137 `automatic_image_name` | `` |
| `images/bs coldtch.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:143 `automatic_image_name` | `` |
| `images/bs coldtears.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2434 `dialogue_image_attribute` | `` |
| `images/bs doll.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1645 `dialogue_image_attribute` | `` |
| `images/bs drool.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:536 `dialogue_image_attribute` | `` |
| `images/bs ehehchub.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2742 `dialogue_image_attribute` | `` |
| `images/bs freakinout.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2140 `show_scene` | `` |
| `images/bs happychub.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2618 `dialogue_image_attribute` | `` |
| `images/bs hey.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2191 `dialogue_image_attribute` | `` |
| `images/bs mad.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:553 `show_scene` | `` |
| `images/bs madchub.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:444 `automatic_image_name` | `` |
| `images/bs magics.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2237 `dialogue_image_attribute` | `` |
| `images/bs ohno.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1607 `show_scene` | `` |
| `images/bs shock.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:540 `dialogue_image_attribute` | `` |
| `images/bs shychub.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:445 `automatic_image_name` | `` |
| `images/bs smirk.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:438 `automatic_image_name` | `` |
| `images/bs takeit.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2758 `dialogue_image_attribute` | `` |
| `images/bs umai.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:447 `automatic_image_name` | `` |
| `images/bs warm.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:145 `automatic_image_name` | `` |
| `images/bs warmeheh.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:148 `automatic_image_name` | `` |
| `images/bs warmgrr.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:139 `automatic_image_name` | `` |
| `images/bs warmpathetic.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:136 `automatic_image_name` | `` |
| `images/bs warmscared.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2290 `show_scene` | `` |
| `images/bs warmtch.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:142 `automatic_image_name` | `` |
| `images/bs wehchub.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2660 `dialogue_image_attribute` | `` |
| `images/choco flowers.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:455 `automatic_image_name` | `` |
| `images/choco hello.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:454 `automatic_image_name` | `` |
| `images/clouds.png` | visual_effect/parallax_clouds | 1725×152 P | definitions.rpy:14 `automatic_image_name` | `` |
| `images/flowers1.png` | visual_effect/magic_particle | 80×80 RGBA | definitions.rpy:162 `automatic_image_name` | `` |
| `images/flowers2.png` | visual_effect/magic_particle | 80×80 P | definitions.rpy:176 `automatic_image_name` | `` |
| `images/flowers3.png` | visual_effect/magic_particle | 80×80 RGBA | definitions.rpy:190 `automatic_image_name` | `` |
| `images/gallery/concept assistant.png` | gallery_concept/character_design | 184×380 RGBA | gallery.rpy:163 `automatic_image_name` | `` |
| `images/gallery/concept candyalchemist.png` | gallery_concept/character_design | 211×380 RGBA | gallery.rpy:154 `automatic_image_name` | `` |
| `images/gallery/concept candygirl.png` | gallery_concept/character_design | 346×380 RGBA | gallery.rpy:159 `automatic_image_name` | `` |
| `images/gallery/concept cat.png` | gallery_concept/character_design | 196×380 RGBA | gallery.rpy:172 `automatic_image_name` | `` |
| `images/gallery/concept chocolate.png` | gallery_concept/character_design | 251×380 RGBA | gallery.rpy:177 `automatic_image_name` | `` |
| `images/gallery/concept saveher.png` | gallery_concept/character_design | 203×380 RGBA | packaged_no_static_reference | `` |
| `images/gallery/concept treat.png` | gallery_concept/character_design | 240×380 RGBA | gallery.rpy:181 `automatic_image_name` | `` |
| `images/gallery/concept uniform.png` | gallery_concept/character_design | 184×380 RGBA | packaged_no_static_reference | `` |
| `images/gallery/concept witch.png` | gallery_concept/character_design | 194×380 RGBA | gallery.rpy:168 `automatic_image_name` | `` |
| `images/gallery/extra albumart.png` | gallery_extra/bonus_illustration | 640×500 RGBA | definitions.rpy:477 `automatic_image_name` | `` |
| `images/gallery/extra candyprint.png` | gallery_extra/bonus_illustration | 640×720 RGBA | definitions.rpy:478 `automatic_image_name` | `` |
| `images/gallery/extra doodles.png` | gallery_extra/bonus_illustration | 640×380 RGBA | definitions.rpy:482 `automatic_image_name` | `` |
| `images/gallery/extra promo.png` | gallery_extra/bonus_illustration | 640×720 RGBA | definitions.rpy:476 `automatic_image_name` | `` |
| `images/gallery/extra rough.png` | gallery_extra/bonus_illustration | 640×720 RGBA | definitions.rpy:483 `automatic_image_name` | `` |
| `images/gallery/extra roughpromo.png` | gallery_extra/bonus_illustration | 640×384 RGBA | definitions.rpy:484 `automatic_image_name` | `` |
| `images/gallery/extra shirt.png` | gallery_extra/bonus_illustration | 640×720 RGBA | definitions.rpy:479 `automatic_image_name` | `` |
| `images/gallery/extra toffee1.png` | gallery_extra/bonus_illustration | 640×619 RGBA | definitions.rpy:480 `automatic_image_name` | `` |
| `images/gallery/extra toffee2.png` | gallery_extra/bonus_illustration | 640×720 RGBA | definitions.rpy:481 `automatic_image_name` | `` |
| `images/gallery/gal_cabin.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:117 `automatic_image_name` | `images/bg cabin.jpg` |
| `images/gallery/gal_cottage.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:113 `automatic_image_name` | `images/bg cottage.jpg` |
| `images/gallery/gal_lab.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:111 `automatic_image_name` | `images/bg lab.png` |
| `images/gallery/gal_market.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:115 `automatic_image_name` | `images/bg market.jpg` |
| `images/gallery/gal_mountain.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:116 `automatic_image_name` | `images/bg mountain.jpg` |
| `images/gallery/gal_shop.jpg` | gallery_thumbnail/background_preview | 256×144 RGB | gallery.rpy:112 `automatic_image_name` | `images/bg shop.jpg` |
| `images/gallery/galframe_hover.png` | gallery_ui/gallery_frame | 276×164 RGBA | gallery.rpy:40 `automatic_image_name` | `` |
| `images/gallery/galframe_idle.png` | gallery_ui/gallery_frame | 276×164 RGBA | gallery.rpy:41 `automatic_image_name` | `` |
| `images/gallery/galframe_insensitive.png` | gallery_ui/gallery_frame | 256×144 RGBA | gallery.rpy:39 `automatic_image_name` | `` |
| `images/gum aw.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:97 `explicit_file` | `` |
| `images/gum baw.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:100 `explicit_file` | `` |
| `images/gum broken.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2946 `show_scene` | `` |
| `images/gum determined.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:327 `dialogue_image_attribute` | `` |
| `images/gum doll.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2895 `dialogue_image_attribute` | `` |
| `images/gum dress.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:103 `explicit_file` | `` |
| `images/gum eaten.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:652 `show_scene` | `` |
| `images/gum friendlier.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2917 `dialogue_image_attribute` | `` |
| `images/gum frozen.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:133 `explicit_file` | `` |
| `images/gum happy.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:424 `explicit_file` | `` |
| `images/gum hey.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:121 `show_scene` | `` |
| `images/gum hey2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:106 `explicit_file` | `` |
| `images/gum lost.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2939 `dialogue_image_attribute` | `` |
| `images/gum mad.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:109 `explicit_file` | `` |
| `images/gum noo.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:321 `dialogue_image_attribute` | `` |
| `images/gum nooo.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:425 `explicit_file` | `` |
| `images/gum ooh.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:112 `explicit_file` | `` |
| `images/gum pls.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:300 `show_scene` | `` |
| `images/gum shutdown.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2886 `show_scene` | `` |
| `images/gum surprise.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:126 `dialogue_image_attribute` | `` |
| `images/gum surprise2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:115 `explicit_file` | `` |
| `images/gum umm.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:361 `dialogue_image_attribute` | `` |
| `images/gum worry.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:118 `explicit_file` | `` |
| `images/gum yay.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:134 `dialogue_image_attribute` | `` |
| `images/gum yay2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:121 `explicit_file` | `` |
| `images/gum yayyy.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:116 `dialogue_image_attribute` | `` |
| `images/gum yayyy2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:124 `explicit_file` | `` |
| `images/gum yes.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:127 `explicit_file` | `` |
| `images/gum yes2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:130 `explicit_file` | `` |
| `images/gums aw.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:96 `explicit_file` | `` |
| `images/gums baw.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:99 `explicit_file` | `` |
| `images/gums dress.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:102 `explicit_file` | `` |
| `images/gums frozen.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:132 `explicit_file` | `` |
| `images/gums hey2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:105 `explicit_file` | `` |
| `images/gums mad.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:108 `explicit_file` | `` |
| `images/gums ooh.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:111 `explicit_file` | `` |
| `images/gums surprise2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:114 `explicit_file` | `` |
| `images/gums worry.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:117 `explicit_file` | `` |
| `images/gums yay2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:120 `explicit_file` | `` |
| `images/gums yayyy2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:123 `explicit_file` | `` |
| `images/gums yes.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:126 `explicit_file` | `` |
| `images/gums yes2.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:129 `explicit_file` | `` |
| `images/light1.png` | visual_effect/magic_particle | 200×200 RGBA | definitions.rpy:218 `automatic_image_name` | `` |
| `images/light2.png` | visual_effect/magic_particle | 200×200 RGBA | definitions.rpy:224 `automatic_image_name` | `` |
| `images/light3.png` | visual_effect/magic_particle | 200×200 RGBA | definitions.rpy:230 `automatic_image_name` | `` |
| `images/mmbs.png` | menu_portrait/default | 240×390 RGBA | screens.rpy:391 `automatic_image_name` | `` |
| `images/mmbs2.png` | menu_portrait/ending_unlocked | 240×390 RGBA | screens.rpy:389 `automatic_image_name` | `` |
| `images/mmgum.png` | menu_portrait/default | 240×390 RGBA | screens.rpy:382 `automatic_image_name` | `` |
| `images/mmgum2.png` | menu_portrait/ending_unlocked | 240×390 RGBA | screens.rpy:380 `automatic_image_name` | `` |
| `images/mmpas.png` | menu_portrait/default | 240×390 RGBA | screens.rpy:387 `automatic_image_name` | `` |
| `images/mmpas2.png` | menu_portrait/ending_unlocked | 240×390 RGBA | screens.rpy:385 `automatic_image_name` | `` |
| `images/mmsyrup.png` | menu_portrait/default | 240×390 RGBA | screens.rpy:377 `automatic_image_name` | `` |
| `images/mmsyrup2.png` | menu_portrait/ending_unlocked | 240×390 RGBA | screens.rpy:375 `automatic_image_name` | `` |
| `images/mmtof.png` | menu_portrait/default | 240×390 RGBA | screens.rpy:396 `automatic_image_name` | `` |
| `images/mmtof2.png` | menu_portrait/ending_unlocked | 240×390 RGBA | screens.rpy:394 `automatic_image_name` | `` |
| `images/pas cold.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2578 `dialogue_image_attribute` | `` |
| `images/pas coldnervous.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2594 `dialogue_image_attribute` | `` |
| `images/pas coldpatient.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:436 `automatic_image_name` | `` |
| `images/pas dang.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:255 `dialogue_image_attribute` | `` |
| `images/pas eheh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:220 `dialogue_image_attribute` | `` |
| `images/pas heh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:313 `dialogue_image_attribute` | `` |
| `images/pas hmhm.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:381 `dialogue_image_attribute` | `` |
| `images/pas mad.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:185 `dialogue_image_attribute` | `` |
| `images/pas patient.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:200 `dialogue_image_attribute` | `` |
| `images/pas ready.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:214 `show_scene` | `` |
| `images/pas sad.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:251 `dialogue_image_attribute` | `` |
| `images/pas smile.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:433 `automatic_image_name` | `` |
| `images/pas sorry.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:434 `automatic_image_name` | `` |
| `images/pas wahh.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:435 `automatic_image_name` | `` |
| `images/pas worry.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:158 `dialogue_image_attribute` | `` |
| `images/pas yum.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:3190 `dialogue_image_attribute` | `` |
| `images/pastfilter.png` | visual_effect/memory_overlay | 1280×720 P | script.rpy:2887 `show_scene` | `` |
| `images/sb badend1.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:391 `automatic_image_name` | `` |
| `images/sb badend2.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:393 `automatic_image_name` | `` |
| `images/sb bsend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:414 `automatic_image_name` | `` |
| `images/sb byetoffee.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:410 `automatic_image_name` | `` |
| `images/sb byetreat.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:404 `automatic_image_name` | `` |
| `images/sb candibal.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:384 `automatic_image_name` | `` |
| `images/sb cattakeover.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:392 `automatic_image_name` | `` |
| `images/sb climb.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:399 `automatic_image_name` | `` |
| `images/sb counter.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:390 `automatic_image_name` | `` |
| `images/sb creamilla.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:398 `automatic_image_name` | `` |
| `images/sb eatenaway1.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:385 `automatic_image_name` | `` |
| `images/sb eatenaway2.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:386 `automatic_image_name` | `` |
| `images/sb escape.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:400 `automatic_image_name` | `` |
| `images/sb escape2.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:401 `automatic_image_name` | `` |
| `images/sb fixd.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:387 `automatic_image_name` | `` |
| `images/sb frozen.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:402 `automatic_image_name` | `` |
| `images/sb gumend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:413 `automatic_image_name` | `` |
| `images/sb happyreturn.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:405 `automatic_image_name` | `` |
| `images/sb hitreat.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:415 `automatic_image_name` | `` |
| `images/sb homealone.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:388 `automatic_image_name` | `` |
| `images/sb hometogether.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:389 `automatic_image_name` | `` |
| `images/sb locked.png` | gallery_ui/locked_story_cg | 640×720 RGBA | gallery.rpy:284 `automatic_image_name` | `` |
| `images/sb newassistant.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:395 `automatic_image_name` | `` |
| `images/sb newassistant2.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:396 `automatic_image_name` | `` |
| `images/sb pasend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:412 `automatic_image_name` | `` |
| `images/sb search.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:394 `automatic_image_name` | `` |
| `images/sb shop.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:383 `automatic_image_name` | `` |
| `images/sb sleep.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:408 `automatic_image_name` | `` |
| `images/sb syrupend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:411 `automatic_image_name` | `` |
| `images/sb tofend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:416 `automatic_image_name` | `` |
| `images/sb ultimatesweet.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:397 `automatic_image_name` | `` |
| `images/sb unsleep.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:409 `automatic_image_name` | `` |
| `images/sb working.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:406 `automatic_image_name` | `` |
| `images/sb working2.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:407 `automatic_image_name` | `` |
| `images/sb worstend.png` | story_cg/storybook_illustration | 640×720 RGBA | definitions.rpy:403 `automatic_image_name` | `` |
| `images/splash.jpg` | screen_art/splash | 1280×720 RGB | script.rpy:43 `show_scene` | `` |
| `images/storybook.jpg` | screen_art/storybook_page | 1280×720 RGB | gallery.rpy:54 `automatic_image_name` | `` |
| `images/storybook2.jpg` | screen_art/storybook_page_variant | 1280×720 RGB | script.rpy:277 `show_scene` | `` |
| `images/sy aww.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1489 `dialogue_image_attribute` | `` |
| `images/sy cold.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:421 `automatic_image_name` | `` |
| `images/sy coldcomfort.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2436 `dialogue_image_attribute` | `` |
| `images/sy colder.png` | character_sprite/expression_pose | 621×673 RGBA | packaged_no_static_reference | `` |
| `images/sy colderawkward.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2566 `dialogue_image_attribute` | `` |
| `images/sy colderhey.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:152 `automatic_image_name` | `` |
| `images/sy coldersmile.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2596 `dialogue_image_attribute` | `` |
| `images/sy colderstop.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:155 `automatic_image_name` | `` |
| `images/sy colderyeah.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:158 `automatic_image_name` | `` |
| `images/sy coldhey.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:153 `automatic_image_name` | `` |
| `images/sy coldhmm.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2471 `dialogue_image_attribute` | `` |
| `images/sy coldhuh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2444 `dialogue_image_attribute` | `` |
| `images/sy coldsass.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2125 `dialogue_image_attribute` | `` |
| `images/sy coldscared.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2233 `dialogue_image_attribute` | `` |
| `images/sy coldsmirk.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2135 `dialogue_image_attribute` | `` |
| `images/sy coldstop.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:156 `automatic_image_name` | `` |
| `images/sy coldthought.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2481 `dialogue_image_attribute` | `` |
| `images/sy coldyeah.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:159 `automatic_image_name` | `` |
| `images/sy coldyell.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2428 `dialogue_image_attribute` | `` |
| `images/sy cool.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:469 `dialogue_image_attribute` | `` |
| `images/sy crystalball.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:422 `automatic_image_name` | `` |
| `images/sy dakara.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:156 `dialogue_image_attribute` | `` |
| `images/sy embarrassed.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1476 `dialogue_image_attribute` | `` |
| `images/sy frick.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1173 `show_scene` | `` |
| `images/sy grr.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:176 `show_scene` | `` |
| `images/sy grr2.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:542 `dialogue_image_attribute` | `` |
| `images/sy hahano.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:136 `dialogue_image_attribute` | `` |
| `images/sy heeey.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:119 `show_scene` | `` |
| `images/sy heh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:160 `dialogue_image_attribute` | `` |
| `images/sy hmm.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:419 `automatic_image_name` | `` |
| `images/sy indifferent.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:418 `automatic_image_name` | `` |
| `images/sy oh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1277 `dialogue_image_attribute` | `` |
| `images/sy point.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:420 `automatic_image_name` | `` |
| `images/sy proud.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:721 `dialogue_image_attribute` | `` |
| `images/sy reg.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:99 `show_scene` | `` |
| `images/sy smirk.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:703 `dialogue_image_attribute` | `` |
| `images/sy tch.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:1783 `dialogue_image_attribute` | `` |
| `images/sy thanks.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:3016 `dialogue_image_attribute` | `` |
| `images/sy um.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:108 `dialogue_image_attribute` | `` |
| `images/sy yo.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:216 `show_scene` | `` |
| `images/title.png` | title_art/english_title | 1046×116 LA | screens.rpy:369 `automatic_image_name` | `` |
| `images/tof fret.png` | character_sprite/expression_pose | 606×657 RGBA | definitions.rpy:452 `automatic_image_name` | `` |
| `images/tof heh.png` | character_sprite/expression_pose | 606×657 RGBA | definitions.rpy:450 `automatic_image_name` | `` |
| `images/tof help.png` | character_sprite/expression_pose | 606×657 RGBA | script.rpy:2719 `show_scene` | `` |
| `images/tof hmm.png` | character_sprite/expression_pose | 606×657 RGBA | script.rpy:1617 `dialogue_image_attribute` | `` |
| `images/tof myow.png` | character_sprite/expression_pose | 606×657 RGBA | definitions.rpy:451 `automatic_image_name` | `` |
| `images/tof nyan.png` | character_sprite/expression_pose | 606×657 RGBA | script.rpy:502 `show_scene` | `` |
| `images/tof sly.png` | character_sprite/expression_pose | 606×657 RGBA | definitions.rpy:449 `automatic_image_name` | `` |
| `images/tof tsun.png` | character_sprite/expression_pose | 606×657 RGBA | script.rpy:2104 `dialogue_image_attribute` | `` |
| `images/treat aw.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:458 `automatic_image_name` | `` |
| `images/treat meh.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2185 `dialogue_image_attribute` | `` |
| `images/treat.png` | character_sprite/expression_pose | 621×673 RGBA | definitions.rpy:457 `automatic_image_name` | `` |
| `images/wolf pink.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2242 `dialogue_image_attribute` | `` |
| `images/wolf pink2.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:2285 `show_scene` | `` |
| `images/wolf.png` | character_sprite/expression_pose | 621×673 RGBA | script.rpy:31 `automatic_image_name` | `` |
| `tl/chinese/images/title.png` | localized_image/chinese_title | 1050×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/de/images/cred2.png` | localized_image/other_language_image | 660×720 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/es/images/cred.png` | localized_image/other_language_image | 660×720 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/es/images/cred2.png` | localized_image/other_language_image | 660×720 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/es/images/title.png` | localized_image/other_language_image | 1046×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/fr/images/cred2.png` | localized_image/other_language_image | 660×720 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/fr/images/title.png` | localized_image/other_language_image | 1046×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/japanese/images/title.png` | localized_image/other_language_image | 1046×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/kr/images/title.png` | localized_image/other_language_image | 1046×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/por/images/cred2.png` | localized_image/other_language_image | 660×720 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
| `tl/por/images/title.png` | localized_image/other_language_image | 1046×116 RGBA | Ren'Py localization resolver:None `localized_image_substitution` | `` |
