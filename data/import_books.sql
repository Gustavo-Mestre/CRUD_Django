-- Inserindo categorias de exemplo
INSERT INTO books_category (id, name) VALUES 
(1, 'Filosofia'),
(2, 'Psicologia'),
(3, 'Espiritualidade'),
(4, 'Autoajuda'),
(5, 'Literatura Clássica');

-- Inserindo autores de exemplo
INSERT INTO books_author (id, first_name, last_name) VALUES 
(1, 'Viktor', 'Frankl'),
(2, 'Hermann', 'Hesse'),
(3, 'Eckhart', 'Tolle'),
(4, 'Fyodor', 'Dostoevsky'),
(5, 'Lao', 'Tzu'),
(6, 'Ralph', 'Ellison');

-- Inserindo livros reflexivos e profundos
INSERT INTO books_book (id, title, author_id, category_id, published_date) VALUES 
(1, 'Em Busca de Sentido', 1, 4, '1946-01-01'),
(2, 'Sidarta', 2, 3, '1922-01-01'),
(3, 'O Poder do Agora', 3, 3, '1997-01-01'),
(4, 'Crime e Castigo', 4, 5, '1866-01-01'),
(5, 'Tao Te Ching', 5, 1, '-600-01-01'),
(6, 'O Homem Invisível', 6, 5, '1952-01-01');
