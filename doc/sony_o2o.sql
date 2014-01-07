--
-- PostgreSQL database dump
--

-- Dumped from database version 9.2.0
-- Dumped by pg_dump version 9.3beta2
-- Started on 2014-01-07 16:45:59 CST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- TOC entry 2858 (class 0 OID 44961)
-- Dependencies: 181
-- Data for Name: dict_sony_store; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (1, 'Sony Store 北京东方广场店', '北京市东长安街1号东方新天地商场首层 AA06C&AA08号店铺', NULL, '010-58116080');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (2, 'Sony Store 北京悠唐广场店', '北京市朝阳区三丰北里五号悠唐中央广场2-101', NULL, '010-85611336');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (3, 'Sony Store 上海淮海路店', '上海市淮海中路901-909号1-3楼', NULL, '021-64721212');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (4, 'Sony Store 上海美罗城店', '徐汇区肇嘉浜路1111号美罗城第一层A区1-23单元', NULL, '021-34692625');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (5, 'Sony Store 上海南京东路店 ', '上海市黄浦区南京东路233号102铺位', NULL, '021-63216677');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (6, 'Sony Store 广州太古汇店', '广州市天河路385号太古汇一座3楼', NULL, '020-38682903');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (7, 'Sony Store 成都来福士店', '成都市人民南路四段3号成都来福士广场L2层2001号', NULL, '028-64041580');
INSERT INTO dict_sony_store (id, name, address, gps_location, telephone) VALUES (8, 'Sony Store 成都银石店', '四川省成都市锦江区红星路三段99号银石广场第二层第2001-2003号商铺', NULL, '028-86729718');


--
-- TOC entry 2873 (class 0 OID 0)
-- Dependencies: 180
-- Name: dict_sony_store_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('dict_sony_store_id_seq', 8, true);


--
-- TOC entry 2848 (class 0 OID 43485)
-- Dependencies: 171
-- Data for Name: map_guest_likes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO map_guest_likes (id, product_id, guest_id, like_date) VALUES (37, 2, 45, '2013-12-05 14:39:29.58668');
INSERT INTO map_guest_likes (id, product_id, guest_id, like_date) VALUES (36, 1, 45, '2013-12-05 12:42:08.813451');


--
-- TOC entry 2874 (class 0 OID 0)
-- Dependencies: 170
-- Name: map_guest_likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('map_guest_likes_id_seq', 39, true);


--
-- TOC entry 2850 (class 0 OID 43493)
-- Dependencies: 173
-- Data for Name: map_guest_manuals; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2875 (class 0 OID 0)
-- Dependencies: 172
-- Name: map_guest_manuals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('map_guest_manuals_id_seq', 3, true);


--
-- TOC entry 2854 (class 0 OID 43512)
-- Dependencies: 177
-- Data for Name: map_guest_reviews; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (227, 2, 29, true, '这个我就喜欢', 5, '2013-11-26');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (228, 1, 29, true, '确实不错', 4, '2013-11-11');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (229, 2, 30, true, '手感细腻', 5, '2013-11-11');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (230, 1, 30, true, '朋友推荐的，不错', 4, '2013-11-12');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (231, 2, 31, true, '颜色很正，做工不错', 4, '2013-11-10');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (232, 2, 32, true, 'Great Value!', 4, '2013-11-13');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (233, 1, 33, true, '真不怕水！！', 3, '2013-11-09');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (234, 1, 34, true, '防水处理真好', 5, '2013-11-09');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (235, 1, 36, true, 'Nice quanlity', 5, '2013-11-07');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (236, 1, 37, true, '果然超值！', 4, '2013-11-07');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (237, 9, 0, true, '好', 3, '2013-12-05');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (238, 13, 0, true, '太贵', 3, '2013-12-05');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (239, 13, 46, true, '价格太高了', 5, '2013-12-05');
INSERT INTO map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) VALUES (240, 3, 46, true, 'sdfsdfsdfsdf', 4, '2013-12-18');


--
-- TOC entry 2876 (class 0 OID 0)
-- Dependencies: 176
-- Name: map_guest_reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('map_guest_reviews_id_seq', 240, true);


--
-- TOC entry 2877 (class 0 OID 0)
-- Dependencies: 178
-- Name: map_product_img_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('map_product_img_id_seq', 16, true);


--
-- TOC entry 2856 (class 0 OID 44950)
-- Dependencies: 179
-- Data for Name: map_product_video; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (3, 1, 'http://xperia.qunar.com/videos/1/b.mp4', '索尼智能手机 Xperia Z1 L39h 官方宣传视频 因出色 而出众');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (4, 3, 'http://xperia.qunar.com/videos/3/a.mp4', '索尼智能手机 Xperia C S39h 单车篇');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (5, 3, 'http://xperia.qunar.com/videos/3/b.mp4', '索尼智能手机 Xperia C S39h 画画篇');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (6, 3, 'http://xperia.qunar.com/videos/3/c.mp4', '索尼智能手机 Xperia C S39h 武功篇');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (2, 1, 'http://xperia.qunar.com/videos/1/a.mp4', '索尼智能手机 Xperia Z1 L39h 官方宣传视频');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (7, 4, 'http://xperia.qunar.com/videos/4/a.mp4', 'Sony QX100 and QX10 attachable Lenses 镜头相机官方宣传视频');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (9, 7, 'http://xperia.qunar.com/videos/7/a.mp4', '80后 内心强大，要你好看——索尼“黑卡”RX100');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (8, 6, 'http://xperia.qunar.com/videos/6/a.mp4', '索尼NEX7微单广告');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (10, 8, 'http://xperia.qunar.com/videos/8/a.mp4', 'SONY Action Cam HDR-AS30V 官方宣传片');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (11, 8, 'http://xperia.qunar.com/videos/8/b.mp4', '索尼酷拍AS30V极限影片-肆城记');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (12, 9, 'http://xperia.qunar.com/videos/9/a.mp4', 'Sony HMZ T1 3D');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (13, 10, 'http://xperia.qunar.com/videos/10/a.mp4', '索尼数码望远镜 DEV-50');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (14, 11, 'http://xperia.qunar.com/videos/11/a.mp4', 'Sony VAIO Pro 13 宣传篇');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (15, 11, 'http://xperia.qunar.com/videos/11/b.mp4', 'Sony VAIO Pro 13 工艺篇');
INSERT INTO map_product_video (id, product_id, video_url, description) VALUES (16, 14, 'http://xperia.qunar.com/videos/14/a.mp4', '索尼2013年超高清电视宣传片“美的感受”');


--
-- TOC entry 2846 (class 0 OID 43473)
-- Dependencies: 169
-- Data for Name: table_guest; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO table_guest (id, name, gender, birthday, telephone, register_date, last_active_date, email, qq, qq_openid, wechat, twitter, weibo, facebook, google_plus, alipay, credit_points, influence_point, status, weibo_uid) VALUES (46, '你好', 'm', '1982-12-01', '13800138000', '2013-12-04', '2013-12-18', 'hhh@ht.com', '55689857', '15E8858F592DBCE6BB4C2CD646FA49A3', '', NULL, 'zsjforcn', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO table_guest (id, name, gender, birthday, telephone, register_date, last_active_date, email, qq, qq_openid, wechat, twitter, weibo, facebook, google_plus, alipay, credit_points, influence_point, status, weibo_uid) VALUES (45, 'HakunaMatata', 'm', '1988-08-01', '18618189555', '2013-12-04', '2013-12-04', 'hhh@hot.com', '12331111111', 'FEBD4A0F4EE4A7A5EEC6B2BB04E766E1', 'sdfsdf', NULL, 'sdfsdf', NULL, NULL, NULL, NULL, NULL, NULL, NULL);


--
-- TOC entry 2878 (class 0 OID 0)
-- Dependencies: 168
-- Name: table_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('table_guest_id_seq', 46, true);


--
-- TOC entry 2852 (class 0 OID 43501)
-- Dependencies: 175
-- Data for Name: table_product; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (11, '超级本 VAIO® Pro13', 'laptop', 'SONY', '512GB PCIE高速固态硬盘
非触控屏，轻仅约940g
正版windows 8 专业版
大容量充电电池支持约17小时续航
背光键盘
内置摄像头有效像素约1280x720
工厂精心定制
激光刻印服务
专业配送上门', NULL, '2013', 'http://m.jd.com/product/928758.html', NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (18, 'Xperia™ SP M35t TD-LTE 4G智能手机', 'mobile', 'SONY', '4.6英寸1280*720分辨率显示屏, 搭载Sony Mobile Bravia® Engine 2图像处理引擎，画面更加鲜艳逼真，影像呈现更加细腻，无论是观看电影还是欣赏照片都能更真实地还原现场效果。NFC（近场通讯技术）触刷功能，一触之间即可无线输出音乐、照片、视频等内容到其他终端*，轻松连接，即刻分享。内置高通骁龙S4 pro 1.7GHz MSM8960T双核处理器，即使多任务操作也游刃有余。配备Sony Walkman™ 播放器 ，时刻享受听觉的饕餮盛宴。此外，炫彩SBH20蓝牙耳机、NTI NFC智触卡等更多可选配件**。多色的蓝牙耳机满足消费者的个性化需求，时刻闪亮专属于自己的色彩。', NULL, '2013', NULL, NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (13, '弧面屏液晶电视 KDL-65S990A', 'display', 'SONY', '弧面屏设计 / 多角度扬声器 / 迅锐图像处理引擎PRO / 特丽魅彩显示技术 / Motionflow XR 400 / 偏振式3D / 一触TM功能 / 屏幕镜像 / 智能连接 / 多屏遥控 / 标配3D眼镜3副 / 标配一触遥控器 / *产品图仅为展示，具体以实物为主', NULL, '2013', NULL, 'http://a.m.tmall.com/i35529055090.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (12, '超级本 VAIO® RED Edition 红', 'laptop', 'SONY', 'VAIO® | red edition 红 限量版的艳丽外表，带来强烈视觉冲击。多重精致涂层，凝结了VAIO®的先进技术，趋近完美。经过手工作业多次研磨打造，并根据不同材质采用不同的涂层，才能创造出如此耀眼的色彩。', NULL, '2013', NULL, NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (6, '一镜走天下微单 NEX-7', 'dc', 'SONY', '标准机身NEX-7
约2430万有效像素
出色的低光照环境拍摄能力
XGA OLED电子取景器
镁合金机身
索尼镜头E 18-200mm F3.5-6.3 OSS LE
小巧、紧凑，具有11倍变焦倍率，
焦段覆盖从广角到长焦，适合各种场景拍', NULL, '2013', NULL, 'http://a.m.tmall.com/i16780046511.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (17, 'Xperia™ Z Ultra XL39h/B(黑色)', 'mobile', 'SONY', '6.44英寸大屏幕，1080p高清晰显示
6.5毫米锐薄机身
X-Reality™ 迅锐图像处理引擎
索尼TRILUMINOS™ 特丽魅彩移动显示技术
约800万像素拍摄
索尼 Exmor RS™ 积层型影像传感器
高通骁龙800四核处理器
IP55/IP58精密防尘、防水
支持NFC近场通信技术', NULL, '2013', NULL, 'http://a.m.tmall.com/i21873691546.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (14, '4K高清电视 KD-65X8500A', 'display', 'SONY', '4K分辨率 / 4K迅锐图像处理引擎PRO / 特丽魅彩显示技术 / 低频反射扬声器 / 一触TM功能 / 标配3D眼镜3副 / 标配一触遥控器', NULL, '2013', NULL, 'http://a.m.tmall.com/i35593210635.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (1, '浮潜拍照 商务旗舰 Xperia™ Z1 L39h', 'mobile', 'SONY', '约2070万像素高清晰成像
1/2.3英寸索尼 Exmor RS™ 积层型影像传感器
索尼G镜头，BIONZ影像处理器
智能AR、局部彩色等多种相机效果
Timeshift burst时光平移(2秒内可拍下61张照片)
5英寸屏幕，1080p高清晰屏幕
X-Reality™ 迅锐图像处理引擎
索尼TRILUMINOS™ 特丽魅彩移动显示技术
高通骁龙800四核处理器
IP55/IP58精密防尘、防水
支持NFC近场通信技术', NULL, '2013', NULL, 'http://a.m.tmall.com/i20025165904.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (3, '联通双卡双待 Xperia™ C S39h', 'mobile', 'SONY', '中国联通定制
WCDMA+GSM双卡双待
5英寸，1600万色，960×540显示屏
索尼音乐独家首发
3,000,000首在线音乐库
2个月高品质音乐免费下载
1年免费 VIP 特权服务
索尼Walkman™ 领先音乐技术
21M 网络', false, '2013', NULL, 'http://a.m.tmall.com/i26813432346.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (2, 'SONY 爆款三防机王  原价 3599 – 活动惊爆价 2788', 'mobile', 'SONY', '5英寸，1080p高清晰屏幕
约7.9mm 防尘、防水双玻璃镜面机身
索尼BRAVIA® Engine 2 图像处理引擎
约1300万像素拍摄
索尼 Exmor RS™ 积层型影像传感器
高通 APQ8064 四核处理器
支持NFC近场通信技术', false, '2013', NULL, 'http://a.m.tmall.com/i36082171308.htm?sid=01442ff98c075ead');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (7, '黑卡 DSC-RX100', 'dc', 'SONY', '1英寸Exmor CMOS影像传感器
2020万有效像素
卡尔·蔡司Vario-Sonnar T*镜头
F1.8大光圈 焦距f=28-100mm
附带8GB 东芝FlashAir SD存储卡', NULL, '2013', 'http://m.jd.com/product/676676.html', NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (8, '头戴式高清DV HDR-AS15', 'dv', 'SONY', 'Exmor R CMOS影像传感器 / 卡尔·蔡司®Tessar®镜头 / 170°广角拍摄* / WIFI影像传输 / 5种录制模式 / 电子防抖  颜', NULL, '2013', 'http://m.jd.com/product/886164.html', NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (9, '头戴式3D影院 HMZ-T1', 'display', 'SONY', '750英寸3D巨幕/45度广视角/5.1虚拟声道', NULL, '2013', 'http://m.jd.com/product/958258.html', NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (4, 'NFC镜头 DSC-QX100', 'len', 'SONY', '卡尔∙蔡斯Vario-Sonnar T*镜头
1英寸Exmor R CMOS影像传感器
支持NFC（近场通信）
支持WiFi链接', false, '2013', NULL, 'http://a.m.tmall.com/i20237394444.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (16, 'Xperia™ ZR M36h黑特供套装', 'mobile', 'SONY', 'IP55/IP58 精密防尘、防水
黑、白、珊瑚粉及土耳其绿四种个性配色
4.6英寸，1280x720显示屏
索尼BRAVIA® Engine 2 图像处理引擎
1300万像素摄像头
索尼 Exmor RS™ 积层型影像传感器
支持NFC近场通信技术
2GB 内存', NULL, '2013', NULL, 'http://a.m.tmall.com/i21406879590.htm');
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (10, '摄录望远镜 DEV-50', 'telescope', 'SONY', '25倍放大倍率*1 / 3D/2D高清视频拍摄 / 约2040万像素静态图像拍摄*2 / 光学防抖（增强模式）*3/ 以记忆棒*4或SD/SDHC存储卡*5为存储介质 / 标配电池持续拍摄时长约3小时*6', NULL, '2013', NULL, NULL);
INSERT INTO table_product (id, name, category, manufacturer, brief, invisible, year, jd_link, tmall_link) VALUES (15, 'SONY 4G 旗舰防水 原价4599 － 活动惊爆价3999', 'mobile', 'SONY', '4G，飞一般自由
快，就是感受到血液的燃烧。装配4G移动网络技术的索尼Xperia™ Z1 4G移动版，呈现超越想象的上网体验。高达百兆级的下载速度*，1首MV在1秒间即刻到达手机，下载1部高清电影仅需60秒。在线浏览一扫卡屏延时的窘况，任你在剧情中跌宕，为比赛持续喝彩，与游戏同步激情。更快的网络速度总是能创造更多可能——有了4G，你可以即时进入工作状态，自如收发邮件，第一时间坐享高效。你能感受到，自由在加速。', NULL, '2013', NULL, 'http://a.m.tmall.com/i36793868229.htm?sid=01442ff98c075ead');


--
-- TOC entry 2879 (class 0 OID 0)
-- Dependencies: 174
-- Name: table_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('table_product_id_seq', 18, true);


-- Completed on 2014-01-07 16:46:01 CST

--
-- PostgreSQL database dump complete
--

