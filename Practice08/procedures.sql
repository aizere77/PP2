-- TABLE
DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);


-- UPSERT
CREATE OR REPLACE PROCEDURE upsert_user(
    p_name TEXT,
    p_surname TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(name, surname, phone)
    VALUES (p_name, p_surname, p_phone)
    ON CONFLICT (phone)
    DO UPDATE SET
        name = EXCLUDED.name,
        surname = EXCLUDED.surname;
END;
$$;


-- INSERT MANY
CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    surnames TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql
AS $$
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        INSERT INTO phonebook(name, surname, phone)
        VALUES (names[i], surnames[i], phones[i])
        ON CONFLICT (phone) DO NOTHING;
    END LOOP;
END;
$$;


-- DELETE
CREATE OR REPLACE PROCEDURE delete_user(val TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = val OR surname = val OR phone = val;
END;
$$;