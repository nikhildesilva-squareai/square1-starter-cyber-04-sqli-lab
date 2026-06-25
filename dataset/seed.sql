-- Square 1 AI - synthetic seed for the SQL Injection Lab.
-- Synthetic, Square 1-owned, free for learners. Rebuild app.db from this.
BEGIN TRANSACTION;
CREATE TABLE products (
            id       INTEGER PRIMARY KEY,
            name     TEXT NOT NULL,
            category TEXT NOT NULL,
            price    REAL NOT NULL,
            listed   INTEGER NOT NULL  -- 1 public, 0 internal-only (must stay hidden)
        );
INSERT INTO "products" VALUES(1,'Gadget Model 598','Gadgets',336.76,1);
INSERT INTO "products" VALUES(2,'Widget Model 319','Stationery',363.86,1);
INSERT INTO "products" VALUES(3,'Gadget Model 196','Stationery',117.96,0);
INSERT INTO "products" VALUES(4,'Hardwar Model 226','Tools',187.61,1);
INSERT INTO "products" VALUES(5,'Tool Model 826','Hardware',475.69,1);
INSERT INTO "products" VALUES(6,'Gadget Model 659','Tools',130.7,1);
INSERT INTO "products" VALUES(7,'Widget Model 247','Tools',219.37,1);
INSERT INTO "products" VALUES(8,'Widget Model 236','Hardware',374.56,1);
INSERT INTO "products" VALUES(9,'Gadget Model 903','Widgets',160.38,1);
INSERT INTO "products" VALUES(10,'Tool Model 401','Stationery',188.96,0);
INSERT INTO "products" VALUES(11,'Stationer Model 771','Gadgets',467.72,1);
INSERT INTO "products" VALUES(12,'Gadget Model 128','Widgets',415.4,0);
INSERT INTO "products" VALUES(13,'Stationer Model 261','Gadgets',436.91,0);
INSERT INTO "products" VALUES(14,'Tool Model 352','Gadgets',388.82,1);
INSERT INTO "products" VALUES(15,'Tool Model 550','Tools',10.9,1);
INSERT INTO "products" VALUES(16,'Widget Model 351','Widgets',339.44,0);
INSERT INTO "products" VALUES(17,'Gadget Model 555','Hardware',291.65,0);
INSERT INTO "products" VALUES(18,'Stationer Model 877','Hardware',358.13,1);
INSERT INTO "products" VALUES(19,'Hardwar Model 217','Tools',463.14,1);
INSERT INTO "products" VALUES(20,'Widget Model 974','Gadgets',245.85,1);
INSERT INTO "products" VALUES(21,'Gadget Model 959','Tools',461.78,0);
INSERT INTO "products" VALUES(22,'Gadget Model 636','Tools',317.82,0);
INSERT INTO "products" VALUES(23,'Stationer Model 226','Stationery',482.28,1);
INSERT INTO "products" VALUES(24,'Tool Model 263','Hardware',402.16,1);
INSERT INTO "products" VALUES(25,'Stationer Model 805','Hardware',58.03,1);
INSERT INTO "products" VALUES(26,'Widget Model 325','Stationery',119.16,1);
INSERT INTO "products" VALUES(27,'Stationer Model 644','Hardware',302.54,1);
INSERT INTO "products" VALUES(28,'Hardwar Model 206','Gadgets',214.81,1);
INSERT INTO "products" VALUES(29,'Hardwar Model 879','Gadgets',126.68,1);
INSERT INTO "products" VALUES(30,'Tool Model 994','Stationery',408.2,0);
INSERT INTO "products" VALUES(31,'Hardwar Model 159','Tools',76.36,1);
INSERT INTO "products" VALUES(32,'Tool Model 386','Gadgets',75.22,1);
INSERT INTO "products" VALUES(33,'Tool Model 248','Widgets',80.04,0);
INSERT INTO "products" VALUES(34,'Gadget Model 585','Widgets',31.42,0);
INSERT INTO "products" VALUES(35,'Hardwar Model 147','Tools',340.95,1);
INSERT INTO "products" VALUES(36,'Tool Model 844','Gadgets',253.74,1);
INSERT INTO "products" VALUES(37,'Stationer Model 865','Tools',93.84,1);
INSERT INTO "products" VALUES(38,'Widget Model 305','Gadgets',286.76,1);
INSERT INTO "products" VALUES(39,'Gadget Model 144','Widgets',263.26,0);
INSERT INTO "products" VALUES(40,'Gadget Model 183','Hardware',29.72,1);
CREATE TABLE users (
            id       INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,   -- plaintext on purpose: this is the lab's bad app
            role     TEXT NOT NULL,   -- 'user' or 'admin'
            secret   TEXT             -- only the admin row carries the planted flag
        );
INSERT INTO "users" VALUES(1,'admin','S0meAdminPass!42','admin','FLAG_sq1_EXAMPLE_admin_secret_not_a_real_key_REPLACE');
INSERT INTO "users" VALUES(2,'liam.murphy','qq5cygct9z','user',NULL);
INSERT INTO "users" VALUES(3,'jack.singh','sd5qsnf73wp','user',NULL);
INSERT INTO "users" VALUES(4,'emma.reyes','qhcu6b54j','user',NULL);
INSERT INTO "users" VALUES(5,'ruby.patel','ymc9q6y32gn','user',NULL);
INSERT INTO "users" VALUES(6,'eli.adler','te2y72n8','user',NULL);
INSERT INTO "users" VALUES(7,'nora.lopez','ncr3freyrmh','user',NULL);
INSERT INTO "users" VALUES(8,'finn.obrien','qe4wydk24q3','user',NULL);
INSERT INTO "users" VALUES(9,'emma.walsh','jhywe4g3a33','user',NULL);
INSERT INTO "users" VALUES(10,'jack.obrien','yj3ursube','user',NULL);
INSERT INTO "users" VALUES(11,'zoe.smith','xxr5uc2uw','user',NULL);
INSERT INTO "users" VALUES(12,'finn.reyes','u3kvamq9','user',NULL);
INSERT INTO "users" VALUES(13,'zoe.kim','95bh4b5j7','user',NULL);
INSERT INTO "users" VALUES(14,'kai.walsh','dus39xppp4','user',NULL);
INSERT INTO "users" VALUES(15,'ivy.patel','adc2zyrze','user',NULL);
INSERT INTO "users" VALUES(16,'sara.reyes','esysqfnhkyw','user',NULL);
INSERT INTO "users" VALUES(17,'ruby.lopez','cmdm8n7syrj','user',NULL);
INSERT INTO "users" VALUES(18,'jack.wood','3jz3qzjcc','user',NULL);
INSERT INTO "users" VALUES(19,'nora.diaz','rygzk4ut','user',NULL);
INSERT INTO "users" VALUES(20,'noah.adler','a2szxqkwevc','user',NULL);
INSERT INTO "users" VALUES(21,'ruby.obrien','2p3bfsfm','user',NULL);
INSERT INTO "users" VALUES(22,'owen.patel','dfv3fk79vq','user',NULL);
INSERT INTO "users" VALUES(23,'ivy.cohen','kae8prr3cc','user',NULL);
INSERT INTO "users" VALUES(24,'kai.adler','sq8eutr4j8','user',NULL);
INSERT INTO "users" VALUES(25,'ivy.reyes','5qjan4a6te','user',NULL);
COMMIT;
