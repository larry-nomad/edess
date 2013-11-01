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

SELECT pg_catalog.setval('map_guest_likes_id_seq', 1, false);


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

SELECT pg_catalog.setval('map_guest_manuals_id_seq', 1, false);


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
    review_date time without time zone
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

SELECT pg_catalog.setval('map_guest_reviews_id_seq', 1, false);


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

SELECT pg_catalog.setval('table_guest_id_seq', 1, false);


--
-- Name: table_product; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE table_product (
    id integer NOT NULL,
    name character varying(256),
    category character varying(128),
    manufacturer character varying(256),
    brief text,
    invisible boolean
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

SELECT pg_catalog.setval('table_product_id_seq', 1, false);


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

ALTER TABLE ONLY table_guest ALTER COLUMN id SET DEFAULT nextval('table_guest_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY table_product ALTER COLUMN id SET DEFAULT nextval('table_product_id_seq'::regclass);


--
-- Data for Name: map_guest_likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_likes (id, product_id, guest_id, like_date) FROM stdin;
\.


--
-- Data for Name: map_guest_manuals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_manuals (id, product_id, guest_id) FROM stdin;
\.


--
-- Data for Name: map_guest_reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY map_guest_reviews (id, product_id, guest_id, is_approved, comment, ranked_stars, review_date) FROM stdin;
\.


--
-- Data for Name: table_guest; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_guest (id, name, gender, birthday, telephone, register_date, last_active_date, email, qq, qq_openid, wechat, twitter, weibo, facebook, google_plus, alipay, credit_points, influence_point, status) FROM stdin;
\.


--
-- Data for Name: table_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY table_product (id, name, category, manufacturer, brief, invisible) FROM stdin;
\.


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

