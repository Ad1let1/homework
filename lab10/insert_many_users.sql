-- Функция upsert_many_users: вставляет или обновляет записи из массивов username и phone.
-- Если телефон некорректный (не соответствует '^\+?[0-9]+$'), то возвращает эту пару.
DROP FUNCTION IF EXISTS upsert_many_users(text[], text[]);
CREATE OR REPLACE FUNCTION upsert_many_users(usernames text[], phones text[])
RETURNS TABLE(incorrect_username text, incorrect_phone text) AS
$$
DECLARE 
    i integer;
    n integer := array_length(usernames, 1);
BEGIN
    IF n IS NULL OR n = 0 THEN
        RETURN;
    END IF;
    FOR i IN 1..n LOOP
        IF NOT (phones[i] ~ '^\+?[0-9]+$') THEN
            RETURN NEXT (usernames[i], phones[i]);
        ELSE
            INSERT INTO phonebook(username, phone) 
            VALUES (usernames[i], phones[i])
            ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
