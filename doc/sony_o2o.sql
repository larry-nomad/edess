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

SELECT pg_catalog.setval('dict_sony_store_id_seq', 1, false);


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

SELECT pg_catalog.setval('map_guest_reviews_id_seq', 234, true);


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

SELECT pg_catalog.setval('map_product_img_id_seq', 1, false);


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
    status character varying(64)
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

SELECT pg_catalog.setval('table_guest_id_seq', 18, true);


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
    year character varying
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

SELECT pg_catalog.setval('table_product_id_seq', 6, true);


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
227	2	14	f	334\n	\N	\N
228	2	14	f	334\n	\N	\N
229	2	14	t	ddddd	\N	\N
230	\N	\N	\N	\N	\N	\N
231	\N	\N	\N	\N	\N	\N
232	2	14	f	ddddd	\N	\N
233	2	14	f	ddddd	\N	\N
234	2	16	f	ddddd	\N	\N
\.


--
-- Data for Name: map_product_img; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_product_img (id, product_id, small, medium, large) FROM stdin;
\.


--
-- Data for Name: table_guest; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_guest (id, name, gender, birthday, telephone, register_date, last_active_date, email, qq, qq_openid, wechat, twitter, weibo, facebook, google_plus, alipay, credit_points, influence_point, status) FROM stdin;
17	等六方3	test	2013-12-11	13800138000	2014-12-11	\N	lfd@qunar.com	12345	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
16	等六方3	test	2013-12-11	13800138000	2014-12-11	\N	lfd@qunar.com	12345	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
18	availabletest	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3904348426	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: table_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_product (id, name, category, manufacturer, brief, invisible, year) FROM stdin;
3	头戴显示器 HMZ-T3W	display	SONY	WirelessHD™无线技术\n便携设计，方便外出携带\n电池盒有线连接主机，可连续播放约5部电影\n电池盒无线连接主机，可连续播放约2部电影\n电池盒MHL连接手机、平板，可连续播放约2部电影\n电池盒通过MHL线连接手机、平板，可给手机、平板充电\n头戴设备较HMZ-T1轻约25%，佩戴更舒适\n750英寸3D巨幕\n7.1虚拟声道\n高速响应，低延迟画面	f	2013
4	佩戴式高清数码摄像机 HDR-AS15	dv	SONY	Exmor R CMOS影像传感器 / 卡尔·蔡司®Tessar®镜头 / 170°广角拍摄* / WIFI影像传输 / 5种录制模式 / 电子防抖	f	2013
5	摄录望远镜 DEV-30	telescope	SONY	15倍放大倍率*1 / 3D/2D高清视频拍摄 / 约2040万像素静态图像拍摄*2 / 光学防抖（增强模式）*3/ 以记忆棒*4或SD/SDHC存储卡*5为存储介质 / 标配电池持续拍摄时长约3小时*6	\N	2013
6	NFC无线扬声器 SRS-BTV5	speaker	SONY	手机连接扬声器？赶快抛弃那些繁琐的蓝牙匹配步骤吧，就是要让听音乐变得更加简单！SRS-BTV5 的一触即听功能，只需将智能手机和扬声器轻轻一触*，通过 NFC（近场通讯技术），可快速实现一对一蓝牙匹配，让 SRS-BTV5 播放手机中的音乐。一触即听，让音乐满屋、亲友同享，就是这么简单！	\N	2013
2	防水耳机 NWZ-W273	player	SONY	NWZ-W273防水性能得到显著提升：达到相当于防水等级IPX5/8*1标准，实现水深2米的防水保护。您可以在游泳、雨中跑步时使用,让音乐伴随您放松地运动。	f	2013
1	浮潜拍照手机 Xperia™ Z1 L39h	mobile	SONY	约2070万像素高清晰成像\n1/2.3英寸索尼 Exmor RS™ 积层型影像传感器\n索尼G镜头，BIONZ影像处理器\n智能AR、局部彩色等多种相机效果\nTimeshift burst时光平移(2秒内可拍下61张照片)\n5英寸屏幕，1080p高清晰屏幕\nX-Reality™ 迅锐图像处理引擎\n索尼TRILUMINOS™ 特丽魅彩移动显示技术\n高通骁龙800四核处理器\nIP55/IP58精密防尘、防水\n支持NFC近场通信技术	\N	2013
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

