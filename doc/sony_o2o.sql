--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dict_sony_store; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE dict_sony_store (
    id integer NOT NULL,
    name character varying(1024),
    address character varying(1024),
    gps_location character varying(1024),
    telephone character varying(32)
);


ALTER TABLE public.dict_sony_store OWNER TO postgres;

--
-- Name: dict_sony_store_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE dict_sony_store_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dict_sony_store_id_seq OWNER TO postgres;

--
-- Name: dict_sony_store_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE dict_sony_store_id_seq OWNED BY dict_sony_store.id;


--
-- Name: dict_sony_store_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('dict_sony_store_id_seq', 8, true);


--
-- Name: map_guest_likes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE map_guest_likes (
    id integer NOT NULL,
    product_id integer,
    guest_id integer,
    like_date timestamp without time zone
);


ALTER TABLE public.map_guest_likes OWNER TO postgres;

--
-- Name: map_guest_likes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_guest_likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_guest_likes_id_seq OWNER TO postgres;

--
-- Name: map_guest_likes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE map_guest_likes_id_seq OWNED BY map_guest_likes.id;


--
-- Name: map_guest_likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_guest_likes_id_seq', 27, true);


--
-- Name: map_guest_manuals; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE map_guest_manuals (
    id integer NOT NULL,
    product_id integer,
    guest_id integer
);


ALTER TABLE public.map_guest_manuals OWNER TO postgres;

--
-- Name: map_guest_manuals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_guest_manuals_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_guest_manuals_id_seq OWNER TO postgres;

--
-- Name: map_guest_manuals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE map_guest_manuals_id_seq OWNED BY map_guest_manuals.id;


--
-- Name: map_guest_manuals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_guest_manuals_id_seq', 3, true);


--
-- Name: map_guest_reviews; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE map_guest_reviews (
    id integer NOT NULL,
    product_id integer,
    guest_id integer,
    is_approved boolean,
    comment text,
    ranked_stars smallint,
    review_date date
);


ALTER TABLE public.map_guest_reviews OWNER TO postgres;

--
-- Name: map_guest_reviews_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_guest_reviews_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_guest_reviews_id_seq OWNER TO postgres;

--
-- Name: map_guest_reviews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE map_guest_reviews_id_seq OWNED BY map_guest_reviews.id;


--
-- Name: map_guest_reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_guest_reviews_id_seq', 236, true);


--
-- Name: map_product_img; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE map_product_img (
    id integer NOT NULL,
    product_id integer,
    small character varying(1024),
    medium character varying(1024),
    large character varying(1024)
);


ALTER TABLE public.map_product_img OWNER TO postgres;

--
-- Name: map_product_img_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_product_img_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_product_img_id_seq OWNER TO postgres;

--
-- Name: map_product_img_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE map_product_img_id_seq OWNED BY map_product_img.id;


--
-- Name: map_product_img_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_product_img_id_seq', 1, true);


--
-- Name: table_guest; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE table_guest (
    id integer NOT NULL,
    name character varying(1024),
    gender character varying(12),
    birthday date,
    telephone character varying(64),
    register_date date,
    last_active_date date,
    email character varying(1024),
    qq character varying(64),
    qq_openid character varying(64),
    wechat character varying(256),
    twitter character varying(256),
    weibo character varying(256),
    facebook character varying(256),
    google_plus character varying(256),
    alipay character varying(256),
    credit_points integer,
    influence_point integer,
    status character varying(64),
    weibo_uid character varying(1024)
);


ALTER TABLE public.table_guest OWNER TO postgres;

--
-- Name: table_guest_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE table_guest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.table_guest_id_seq OWNER TO postgres;

--
-- Name: table_guest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE table_guest_id_seq OWNED BY table_guest.id;


--
-- Name: table_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('table_guest_id_seq', 37, true);


--
-- Name: table_product; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE table_product (
    id integer NOT NULL,
    name character varying(256),
    category character varying(128),
    manufacturer character varying(256),
    brief text,
    invisible boolean,
    year character varying,
    tmall_link character varying(2048)
);


ALTER TABLE public.table_product OWNER TO postgres;

--
-- Name: table_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE table_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.table_product_id_seq OWNER TO postgres;

--
-- Name: table_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE table_product_id_seq OWNED BY table_product.id;


--
-- Name: table_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('table_product_id_seq', 14, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY dict_sony_store ALTER COLUMN id SET DEFAULT nextval('dict_sony_store_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY map_guest_likes ALTER COLUMN id SET DEFAULT nextval('map_guest_likes_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY map_guest_manuals ALTER COLUMN id SET DEFAULT nextval('map_guest_manuals_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY map_guest_reviews ALTER COLUMN id SET DEFAULT nextval('map_guest_reviews_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY map_product_img ALTER COLUMN id SET DEFAULT nextval('map_product_img_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY table_guest ALTER COLUMN id SET DEFAULT nextval('table_guest_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY table_product ALTER COLUMN id SET DEFAULT nextval('table_product_id_seq'::regclass);


--
-- Data for Name: dict_sony_store; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY dict_sony_store (id, name, address, gps_location, telephone) FROM stdin;
1	Sony Store 北京东方广场店	北京市东长安街1号东方新天地商场首层 AA06C&AA08号店铺	\N	010-58116080
2	Sony Store 北京悠唐广场店	北京市朝阳区三丰北里五号悠唐中央广场2-101	\N	010-85611336
3	Sony Store 上海淮海路店	上海市淮海中路901-909号1-3楼	\N	021-64721212
4	Sony Store 上海美罗城店	徐汇区肇嘉浜路1111号美罗城第一层A区1-23单元	\N	021-34692625
5	Sony Store 上海南京东路店 	上海市黄浦区南京东路233号102铺位	\N	021-63216677
6	Sony Store 广州太古汇店	广州市天河路385号太古汇一座3楼	\N	020-38682903
7	Sony Store 成都来福士店	成都市人民南路四段3号成都来福士广场L2层2001号	\N	028-64041580
8	Sony Store 成都银石店	四川省成都市锦江区红星路三段99号银石广场第二层第2001-2003号商铺	\N	028-86729718
\.


--
-- Data for Name: map_guest_likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_likes (id, product_id, guest_id, like_date) FROM stdin;
1	\N	\N	\N
2	\N	\N	\N
3	\N	\N	\N
4	\N	\N	\N
5	\N	\N	\N
12	2	1	\N
13	0	\N	\N
14	1	1	\N
15	2	3	\N
19	2	14	\N
20	0	16	2013-11-15 18:13:23.350176
21	0	16	2013-11-15 18:22:17.075818
22	0	16	2013-11-15 18:23:28.069601
23	0	16	2013-11-15 18:25:34.984616
24	0	16	2013-11-15 18:25:56.852149
25	0	16	2013-11-15 18:28:09.529762
26	0	16	2013-11-15 18:29:24.805794
27	20	16	2013-11-15 18:30:05.218105
\.


--
-- Data for Name: map_guest_manuals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_manuals (id, product_id, guest_id) FROM stdin;
2	2	1
\.


--
-- Data for Name: map_guest_reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) FROM stdin;
227	2	29	t	这个我就喜欢	5	2013-11-26
228	1	29	t	确实不错	4	2013-11-11
229	2	30	t	手感细腻	5	2013-11-11
230	1	30	t	朋友推荐的，不错	4	2013-11-12
231	2	31	t	颜色很正，做工不错	4	2013-11-10
232	2	32	t	Great Value!	4	2013-11-13
233	1	33	t	真不怕水！！	3	2013-11-09
234	1	34	t	防水处理真好	5	2013-11-09
235	1	36	t	Nice quanlity	5	2013-11-07
236	1	37	t	果然超值！	4	2013-11-07
\.


--
-- Data for Name: map_product_img; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_product_img (id, product_id, small, medium, large) FROM stdin;
1	2	s	m	l
\.


--
-- Data for Name: table_guest; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_guest (id, name, gender, birthday, telephone, register_date, last_active_date, email, qq, qq_openid, wechat, twitter, weibo, facebook, google_plus, alipay, credit_points, influence_point, status, weibo_uid) FROM stdin;
30	availabletest	f	\N	\N	2013-11-21	2013-11-21	\N	\N	\N	\N	\N	3904348426	\N	\N	\N	\N	\N	\N	\N
29	HakunaMatata	f	\N	\N	2013-11-21	2013-11-25	\N	HakunaMatata	FEBD4A0F4EE4A7A5EEC6B2BB04E766E1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
31	小毛	m	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
34	大师傅	m	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
33	007是我	m	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
32	黑影	m	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
35	我爱人民币	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
36	薛必群	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
37	Cherry王	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: table_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_product (id, name, category, manufacturer, brief, invisible, year, tmall_link) FROM stdin;
6	一镜走天下微单 NEX-7	dc	SONY	标准机身NEX-7\n约2430万有效像素\n出色的低光照环境拍摄能力\nXGA OLED电子取景器\n镁合金机身\n索尼镜头E 18-200mm F3.5-6.3 OSS LE\n小巧、紧凑，具有11倍变焦倍率，\n焦段覆盖从广角到长焦，适合各种场景拍	\N	2013	http://a.m.tmall.com/i15602227906.htm
11	超级本 VAIO® Pro13	laptop	SONY	512GB PCIE高速固态硬盘\n非触控屏，轻仅约940g\n正版windows 8 专业版\n大容量充电电池支持约17小时续航\n背光键盘\n内置摄像头有效像素约1280x720\n工厂精心定制\n激光刻印服务\n专业配送上门	\N	2013	\N
7	黑卡 DSC-RX100	dc	SONY	1英寸Exmor CMOS影像传感器\n2020万有效像素\n卡尔·蔡司Vario-Sonnar T*镜头\nF1.8大光圈 焦距f=28-100mm\n附带8GB 东芝FlashAir SD存储卡	\N	2013	http://a.m.tmall.com/i16016543793.htm
12	超级本 VAIO® RED Edition 红	laptop	SONY	VAIO® | red edition 红 限量版的艳丽外表，带来强烈视觉冲击。多重精致涂层，凝结了VAIO®的先进技术，趋近完美。经过手工作业多次研磨打造，并根据不同材质采用不同的涂层，才能创造出如此耀眼的色彩。	\N	2013	\N
9	头戴式3D影院 HMZ-T1	display	SONY	750英寸3D巨幕/45度广视角/5.1虚拟声道	\N	2013	http://a.m.tmall.com/i15193917914.htm
8	头戴式高清DV HDR-AS15	dv	SONY	Exmor R CMOS影像传感器 / 卡尔·蔡司®Tessar®镜头 / 170°广角拍摄* / WIFI影像传输 / 5种录制模式 / 电子防抖  颜	\N	2013	\N
13	弧面屏液晶电视 KDL-65S990A	display	SONY	弧面屏设计 / 多角度扬声器 / 迅锐图像处理引擎PRO / 特丽魅彩显示技术 / Motionflow XR 400 / 偏振式3D / 一触TM功能 / 屏幕镜像 / 智能连接 / 多屏遥控 / 标配3D眼镜3副 / 标配一触遥控器 / *产品图仅为展示，具体以实物为主	\N	2013	http://a.m.tmall.com/i35529055090.htm
14	4K高清电视 KD-65X8500A	display	SONY	4K分辨率 / 4K迅锐图像处理引擎PRO / 特丽魅彩显示技术 / 低频反射扬声器 / 一触TM功能 / 标配3D眼镜3副 / 标配一触遥控器	\N	2013	http://a.m.tmall.com/i35593210635.htm
1	浮潜拍照 移动4G Xperia™ Z1 L39h	mobile	SONY	约2070万像素高清晰成像\n1/2.3英寸索尼 Exmor RS™ 积层型影像传感器\n索尼G镜头，BIONZ影像处理器\n智能AR、局部彩色等多种相机效果\nTimeshift burst时光平移(2秒内可拍下61张照片)\n5英寸屏幕，1080p高清晰屏幕\nX-Reality™ 迅锐图像处理引擎\n索尼TRILUMINOS™ 特丽魅彩移动显示技术\n高通骁龙800四核处理器\nIP55/IP58精密防尘、防水\n支持NFC近场通信技术	\N	2013	http://a.m.tmall.com/i20025165904.htm
10	摄录望远镜 DEV-50	telescope	SONY	25倍放大倍率*1 / 3D/2D高清视频拍摄 / 约2040万像素静态图像拍摄*2 / 光学防抖（增强模式）*3/ 以记忆棒*4或SD/SDHC存储卡*5为存储介质 / 标配电池持续拍摄时长约3小时*6	\N	2013	\N
2	防水防尘 联通合约 Xperia™ Z L36h	mobile	SONY	5英寸，1080p高清晰屏幕\n约7.9mm 防尘、防水双玻璃镜面机身\n索尼BRAVIA® Engine 2 图像处理引擎\n约1300万像素拍摄\n索尼 Exmor RS™ 积层型影像传感器\n高通 APQ8064 四核处理器\n支持NFC近场通信技术	f	2013	http://a.m.tmall.com/i17200558607.htm
3	联通双卡双待 Xperia™ C S39h	mobile	SONY	中国联通定制\nWCDMA+GSM双卡双待\n5英寸，1600万色，960×540显示屏\n索尼音乐独家首发\n3,000,000首在线音乐库\n2个月高品质音乐免费下载\n1年免费 VIP 特权服务\n索尼Walkman™ 领先音乐技术\n21M 网络	f	2013	http://a.m.tmall.com/i26813432346.htm
4	NFC镜头 DSC-QX100	len	SONY	卡尔∙蔡斯Vario-Sonnar T*镜头\n1英寸Exmor R CMOS影像传感器\n支持NFC（近场通信）\n支持WiFi链接	f	2013	http://a.m.tmall.com/i20237394444.htm
5	全画幅 ILCE-7R	dc	SONY	标准机身ILCE-7R\n约3640万有效像素\nBIONZ X影像处理器\n小巧的镁合金机身\nXGA OLED电子取景器\n一触TM功能和WiFi功能\n支持特丽魅彩色彩技术和4K静态影像输出\n卡口适配器 LA-EA4\n只有使用LA-EA4卡口适配器，\n才可直接搭载您现有的索尼A卡口全画幅镜头	\N	2013	http://a.m.tmall.com/i35519637462.htm
\.


--
-- Name: dict_sony_store_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY dict_sony_store
    ADD CONSTRAINT dict_sony_store_idx PRIMARY KEY (id);


--
-- Name: map_guest_likes_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY map_guest_likes
    ADD CONSTRAINT map_guest_likes_idx PRIMARY KEY (id);


--
-- Name: map_guest_manuals_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY map_guest_manuals
    ADD CONSTRAINT map_guest_manuals_idx PRIMARY KEY (id);


--
-- Name: map_guest_review_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY map_guest_reviews
    ADD CONSTRAINT map_guest_review_idx PRIMARY KEY (id);


--
-- Name: map_product_img_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY map_product_img
    ADD CONSTRAINT map_product_img_idx PRIMARY KEY (id);


--
-- Name: table_guest_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY table_guest
    ADD CONSTRAINT table_guest_idx PRIMARY KEY (id);


--
-- Name: table_product_idx; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY table_product
    ADD CONSTRAINT table_product_idx PRIMARY KEY (id);


--
-- Name: qq_openid; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX qq_openid ON table_guest USING btree (qq_openid);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

