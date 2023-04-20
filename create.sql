
CREATE OR REPLACE TYPE adres AS OBJECT (
    miejscowosc VARCHAR2(50),
    ulica       VARCHAR2(50),
    numer_domu  INTEGER,
    wojewodztwo VARCHAR2(50)
) NOT FINAL;
/

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE choroba (
    id_choroba INTEGER NOT NULL,
    nazwa      VARCHAR2(50)
);

ALTER TABLE choroba ADD CONSTRAINT choroba_pk PRIMARY KEY ( id_choroba );

CREATE TABLE choroba_historia (
    id_ch INTEGER NOT NULL,
    historia_chorob_id_historia INTEGER NOT NULL,
    choroba_id_choroba          INTEGER NOT NULL
);

ALTER TABLE choroba_historia ADD CONSTRAINT choroba_historia_pk PRIMARY KEY ( id_ch,historia_chorob_id_historia,choroba_id_choroba );

CREATE TABLE gatunek (
    id_gatunku INTEGER NOT NULL,
    nazwa      VARCHAR2(30)
);

ALTER TABLE gatunek ADD CONSTRAINT gatunek_pk PRIMARY KEY ( id_gatunku );

CREATE TABLE historia_chorob (
    id_historia             INTEGER NOT NULL,
    data_diagnozy           DATE,
    zalecane_leczenie       CLOB,
    zwierzeta_id_zwierzecia INTEGER NOT NULL
    
);

ALTER TABLE historia_chorob ADD CONSTRAINT historia_chorob_pk PRIMARY KEY ( id_historia );

CREATE TABLE lekarze (
    id_lekarz                      INTEGER NOT NULL,
    imie                           VARCHAR2(30),
    nazwisko                       VARCHAR2(30),
    nr_tel                         VARCHAR2(9),
    specjalizacja_id_specjalizacja INTEGER NOT NULL
);

ALTER TABLE lekarze ADD CONSTRAINT lekarze_pk PRIMARY KEY ( id_lekarz );

CREATE TABLE magazyn (
    id_magazyn INTEGER NOT NULL,
    nazwa      VARCHAR2(30),
    ilosc      INTEGER,
    producent  VARCHAR2(50),
    cena       NUMBER
);

ALTER TABLE magazyn ADD CONSTRAINT magazyn_pk PRIMARY KEY ( id_magazyn );

CREATE TABLE magazyn_recepta (
    id_mag INTEGER NOT NULL,
    magazyn_id_magazyn INTEGER NOT NULL,
    recepty_id_recepty INTEGER NOT NULL
);

ALTER TABLE magazyn_recepta ADD CONSTRAINT magazyn_recepta_pk PRIMARY KEY ( id_mag,magazyn_id_magazyn,recepty_id_recepty );

CREATE TABLE recepty (
    id_recepty        INTEGER NOT NULL,
    data              DATE,
    stan_platnosci    NUMBER,
    lekarze_id_lekarz INTEGER NOT NULL
);

ALTER TABLE recepty ADD CONSTRAINT recepty_pk PRIMARY KEY ( id_recepty );

CREATE TABLE rodzaj_wizyty (
    id_rodz_wiz INTEGER NOT NULL,
    nazwa       VARCHAR2(30),
    cena	NUMBER
);

ALTER TABLE rodzaj_wizyty ADD CONSTRAINT rodzaj_wizyty_pk PRIMARY KEY ( id_rodz_wiz );

CREATE TABLE rodzaj_zabiegu (
    id_rodz_zab INTEGER NOT NULL,
    nazwa       VARCHAR2(30)
);

ALTER TABLE rodzaj_zabiegu ADD CONSTRAINT rodzaj_zabiegu_pk PRIMARY KEY ( id_rodz_zab );

CREATE TABLE specjalizacja (
    id_specjalizacja    INTEGER NOT NULL,
    nazwa_specjalizacji VARCHAR2(30)
);

ALTER TABLE specjalizacja ADD CONSTRAINT specjalizacja_pk PRIMARY KEY ( id_specjalizacja );

CREATE TABLE wizyty (
    id_wizyt                 INTEGER NOT NULL,
    data                     DATE,
    koszt                    NUMBER,
    stan_tranzakcji          NUMBER,
    zwierzeta_id_zwierzecia  INTEGER NOT NULL,
    zabiegi_id_zabieg        INTEGER,
    rodzaj_wizyty_id_rodz_wiz INTEGER NOT NULL
);



ALTER TABLE wizyty ADD CONSTRAINT wizyty_pk PRIMARY KEY ( id_wizyt );

CREATE TABLE wlasciciele (
    id_wlasciciela INTEGER NOT NULL,
    imie           VARCHAR2(30),
    nazwisko       VARCHAR2(30),
    adres          adres,
    nr_tel         VARCHAR2(9)
);

ALTER TABLE wlasciciele ADD CONSTRAINT wlasciciele_pk PRIMARY KEY ( id_wlasciciela );

CREATE TABLE zabiegi (
    id_zabieg                  INTEGER NOT NULL,
    data                       DATE,
    czas                       INTEGER,
    znieczulenie               NUMBER,
    zwierzeta_id_zwierzecia    INTEGER NOT NULL,
    lekarze_id_lekarz          INTEGER NOT NULL,
    rodzaj_zabiegu_id_rodz_zab INTEGER NOT NULL,
    id_wizyt                   INTEGER NOT NULL
);

ALTER TABLE zabiegi ADD CONSTRAINT zabiegi_pk PRIMARY KEY ( id_zabieg );

CREATE TABLE zwierzeta (
    id_zwierzecia              INTEGER NOT NULL,
    imie                       VARCHAR2(30),
    wiek                       FLOAT(4),
    waga                       INTEGER,
    samica                     NUMBER,
    wlasciciele_id_wlasciciela INTEGER NOT NULL,
    gatunek_id_gatunku         INTEGER NOT NULL
);

ALTER TABLE zwierzeta ADD CONSTRAINT zwierzeta_pk PRIMARY KEY ( id_zwierzecia );
ALTER TABLE choroba_historia
    ADD CONSTRAINT choroba_historia_choroba_fk FOREIGN KEY ( id_ch )
        REFERENCES choroba ( id_choroba );
ALTER TABLE historia_chorob
    ADD CONSTRAINT historia_chorob_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia );
ALTER TABLE lekarze
    ADD CONSTRAINT lekarze_specjalizacja_fk FOREIGN KEY ( specjalizacja_id_specjalizacja )
        REFERENCES specjalizacja ( id_specjalizacja );
ALTER TABLE choroba_historia
    ADD CONSTRAINT lista_chorob_fk FOREIGN KEY ( id_ch )
        REFERENCES historia_chorob ( id_historia );
ALTER TABLE magazyn_recepta
    ADD CONSTRAINT magazyn_recepta_magazyn_fk FOREIGN KEY ( id_mag )
        REFERENCES magazyn ( id_magazyn );
ALTER TABLE magazyn_recepta
    ADD CONSTRAINT magazyn_recepta_recepty_fk FOREIGN KEY ( id_mag )
        REFERENCES recepty ( id_recepty );
ALTER TABLE recepty
    ADD CONSTRAINT recepty_lekarze_fk FOREIGN KEY ( lekarze_id_lekarz )
        REFERENCES lekarze ( id_lekarz );
ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_rodzaj_wizyty_fk FOREIGN KEY ( rodzaj_wizyty_id_rodz_wiz )
        REFERENCES rodzaj_wizyty ( id_rodz_wiz );
ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_zabiegi_fk FOREIGN KEY ( zabiegi_id_zabieg )
        REFERENCES zabiegi ( id_zabieg );
ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia );
ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_lekarze_fk FOREIGN KEY ( lekarze_id_lekarz )
        REFERENCES lekarze ( id_lekarz );
ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_rodzaj_zabiegu_fk FOREIGN KEY ( rodzaj_zabiegu_id_rodz_zab )
        REFERENCES rodzaj_zabiegu ( id_rodz_zab );
ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia );
ALTER TABLE zwierzeta
    ADD CONSTRAINT zwierzeta_gatunek_fk FOREIGN KEY ( gatunek_id_gatunku )
        REFERENCES gatunek ( id_gatunku );
ALTER TABLE zwierzeta
    ADD CONSTRAINT zwierzeta_wlasciciele_fk FOREIGN KEY ( wlasciciele_id_wlasciciela )
        REFERENCES wlasciciele ( id_wlasciciela );

