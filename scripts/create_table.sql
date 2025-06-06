create table if not exists public.url_mappings  (
	id serial primary key,
	original_url varchar(2048),
	shortened_url varchar(2048)
);
