INSERT INTO funds (brief, name, code) select '840', 'Доллары США', 'USD' where not exists (select 1 from funds where brief = '840');
INSERT INTO funds (brief, name, code) select '810', 'Российские рубли', 'RUR'  where not exists (select 1 from funds where brief = '810');
INSERT INTO funds (brief, name, code) select '978', 'Евро', 'EUR'  where not exists (select 1 from funds where brief = '978');
INSERT INTO funds (brief, name, code) select '156', 'Китайский Юань', 'CNY'  where not exists (select 1 from funds where brief = '156');